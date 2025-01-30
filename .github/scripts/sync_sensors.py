import os
import json
import requests
import hashlib
import re
import shutil
from openai import OpenAI
from github import Github

# GitHub Setup
GITHUB_REPO = "iotcommunity-space/sensors"
SENSOR_TOKEN = os.getenv("SENSOR_TOKEN")  # GitHub Token for Repo Access
AC_TOKEN = os.getenv("AC_TOKEN")          # OpenAI API Key

# Verify API Keys
if not SENSOR_TOKEN:
    raise ValueError("Missing GitHub API key! Check your GitHub Secrets.")
if not AC_TOKEN:
    raise ValueError("Missing OpenAI API key! Check your GitHub Secrets.")

# Initialize GitHub & OpenAI Clients
github = Github(SENSOR_TOKEN)
repo = github.get_repo(GITHUB_REPO)
openai_client = OpenAI(api_key=AC_TOKEN)

# Source URLs
CODECS_JSON_URL = (
    "https://raw.githubusercontent.com/iotcommunity-space/codec/main/assets/codecs.json"
)
SENSORS_JSON_URL = (
    "https://raw.githubusercontent.com/iotcommunity-space/sensors/main/assets/sensors.json"
)

# Paths
SENSORS_JSON_PATH = "assets/sensors.json"
SENSORS_ASSETS_PATH = "assets/sensors"
CACHE_PATH = "assets/cached_overviews.json"  # Cache OpenAI responses

# -----------------------------
# Utility & Slug Functions
# -----------------------------
def generate_slug(name):
    """Generate a URL-friendly slug from a string."""
    slug = re.sub(r"[^\w\s-]", "", name.lower())  # remove special characters
    slug = re.sub(r"[\s-]+", "-", slug)           # collapse multiple spaces/hyphens
    return slug.strip("-")

def get_md5_hash(sensor_data):
    """Generate an MD5 hash for sensor metadata to track changes efficiently."""
    return hashlib.md5(json.dumps(sensor_data, sort_keys=True).encode()).hexdigest()

def needs_update(sensor_folder, current_hash):
    """Check if sensor metadata changed or if folder is new -> needs update."""
    hash_file = os.path.join(sensor_folder, "metadata.md5")

    if not os.path.exists(sensor_folder):  # new sensor folder
        return True
    if os.path.exists(os.path.join(sensor_folder, "manual.flag")):  # skip if flagged
        return False
    if not os.path.exists(hash_file):      # no md5 file => definitely needs update
        return True

    with open(hash_file, "r") as f:
        old_hash = f.read().strip()
        return (old_hash != current_hash)

def load_cache():
    """Load cached OpenAI responses."""
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH, "r") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    """Save cached OpenAI responses."""
    with open(CACHE_PATH, "w") as f:
        json.dump(cache, f, indent=2)

# -----------------------------
# Core Processing Functions
# -----------------------------
def process_sensor(codec, sensors_data, existing_sensors, cache):
    """
    Process a single sensor (from codecs_data).
    1) Generate vendor + sensor slug.
    2) Write overview if needed.
    3) Update sensors.json with slug + other fields.
    """
    detailed_name = codec["name"]            # e.g. "Advantech - Wise 2410X"
    vendor_name = detailed_name.split(" - ")[0] if " - " in detailed_name else detailed_name
    vendor_slug = generate_slug(vendor_name) # folder-friendly vendor
    sensor_slug = generate_slug(detailed_name)

    # Final folder path: assets/sensors/<vendor_slug>/<sensor_slug>/en/
    sensor_folder = os.path.join(SENSORS_ASSETS_PATH, vendor_slug, sensor_slug, "en")
    overview_path = os.path.join(sensor_folder, "overview.md")
    hash_file_path = os.path.join(sensor_folder, "metadata.md5")

    # If user wants to skip auto-generation for this sensor
    if os.path.exists(os.path.join(sensor_folder, "manual.flag")):
        print(f"⚠️  Skipping manual entry: {detailed_name}")
        return

    sensor_entry = {
        "Description": codec.get("description"),
        "Vendor": vendor_name,
        "TechnicalSpecs": codec.get("specs", {}),
        "imageUrl": codec.get("image", None),
        "slug": sensor_slug,       # for front-end lookups
        "vendorSlug": vendor_slug  # optional, if you want to store vendor slug as well
    }

    current_hash = get_md5_hash(sensor_entry)

    # Decide if we need to update
    if not needs_update(sensor_folder, current_hash):
        print(f"✅ No changes detected: {detailed_name}")
        return

    print(f"🚀 Processing: {detailed_name}")
    generate_overview(detailed_name, vendor_name, overview_path, cache)

    # Write the new md5
    os.makedirs(sensor_folder, exist_ok=True)
    with open(hash_file_path, "w") as f:
        f.write(current_hash)

    # Update sensors_data if it's new
    if detailed_name not in existing_sensors:
        sensors_data[detailed_name] = sensor_entry
        existing_sensors.add(detailed_name)

def generate_overview(sensor_name, vendor_name, output_path, cache):
    """Generate or reuse an overview.md via GPT-4o, caching results in local JSON."""
    if os.path.exists(output_path):
        print(f"⚠️  Skipping API call: overview.md already exists for {sensor_name}")
        return

    cache_key = f"{sensor_name}-{vendor_name}"
    if cache_key in cache:
        print(f"⚡ Using cached overview for {sensor_name}")
        response_text = cache[cache_key]
    else:
        print(f"🚀 Calling OpenAI API for {sensor_name}")
        prompt = (
            f"Write a technical overview for '{sensor_name}' by {vendor_name}. "
            "Include working principles, installation guide, LoRaWAN details, "
            "power consumption, use cases, and limitations."
        )
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a technical IoT expert writing detailed sensor documentation."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        response_text = response.choices[0].message.content
        cache[cache_key] = response_text
        save_cache(cache)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(response_text)

    print(f"✅ Wrote overview.md for {sensor_name} at {output_path}")

def batch_generate_overviews(sensor_list, cache):
    """
    Optional optimization: call OpenAI once for many sensors.
    If sensors already exist in 'cache', skip them.
    """
    batch_prompts = []
    batch_keys = []

    for sensor in sensor_list:
        name = sensor["name"]
        vendor = sensor["vendor"]
        cache_key = f"{name}-{vendor}"
        if cache_key in cache:
            continue
        prompt = (
            f"Write a technical overview for {name} by {vendor}. "
            "Include working principles, installation guide, LoRaWAN details, "
            "power consumption, use cases, and limitations."
        )
        batch_prompts.append({"role": "user", "content": prompt})
        batch_keys.append(cache_key)

    if not batch_prompts:
        return

    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a technical IoT expert writing detailed sensor documentation."
            }
        ] + batch_prompts
    )

    for i, sensor_response in enumerate(response.choices):
        cache[batch_keys[i]] = sensor_response.message.content
        save_cache(cache)

def cleanup_old_folders(sensors_data):
    """
    Remove folders that do NOT match <vendorSlug>/<sensorSlug>.
    We'll compare each known vendorSlug -> sensorSlug from sensors_data
    to what's actually on disk.
    """
    # Build a set of valid paths, ignoring 'en' subfolder
    valid_paths = set()
    for full_name, info in sensors_data.items():
        vendor_slug = info.get("vendorSlug") or generate_slug(info["Vendor"])
        sensor_slug = info["slug"]
        folder_path = os.path.join(SENSORS_ASSETS_PATH, vendor_slug, sensor_slug)
        valid_paths.add(folder_path)

    # Iterate through vendor directories
    for vendor_dir in os.listdir(SENSORS_ASSETS_PATH):
        vendor_path = os.path.join(SENSORS_ASSETS_PATH, vendor_dir)
        if not os.path.isdir(vendor_path):
            continue

        # For each sensor subfolder
        for sensor_dir in os.listdir(vendor_path):
            sensor_folder_path = os.path.join(vendor_path, sensor_dir)
            if not os.path.isdir(sensor_folder_path):
                continue

            # If this <vendor_dir>/<sensor_dir> is not in valid_paths, remove it
            if sensor_folder_path not in valid_paths:
                print(f"🗑️ Removing unused/duplicate folder: {sensor_folder_path}")
                shutil.rmtree(sensor_folder_path)

def commit_to_github(file_path, commit_message):
    """Commit changes to GitHub. If file doesn't exist, create it."""
    try:
        contents = repo.get_contents(file_path)
        repo.update_file(
            file_path,
            commit_message,
            open(file_path, "r").read(),
            contents.sha
        )
    except:  # if not found, create
        repo.create_file(
            file_path,
            commit_message,
            open(file_path, "r").read()
        )

# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":
    try:
        # Load existing sensors & new codecs
        sensors_data = requests.get(SENSORS_JSON_URL).json() or {}
        codecs_data = requests.get(CODECS_JSON_URL).json() or []

        existing_sensors = set(sensors_data.keys())
        cache = load_cache()

        # Process new or updated sensors
        for codec in codecs_data:
            process_sensor(codec, sensors_data, existing_sensors, cache)

        # Optionally, do batch overview generation
        # (If you want to reduce separate OpenAI calls.)
        # batch_generate_overviews(codecs_data, cache)

        # Clean up old folder duplicates
        cleanup_old_folders(sensors_data)

        # Write updated sensors_data
        with open(SENSORS_JSON_PATH, "w") as f:
            json.dump(sensors_data, f, indent=2)

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        # Commit changes to sensors.json
        commit_to_github(SENSORS_JSON_PATH, "Updated sensors.json with new verified entries.")
        print("🎯 Completed: sensors.json & overview.md updated as needed.")
