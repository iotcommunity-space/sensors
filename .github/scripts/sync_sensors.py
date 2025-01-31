import os
import json
import requests
import hashlib
import re
from bs4 import BeautifulSoup
from github import Github
from openai import OpenAI  # Updated import for OpenAI >=1.0.0

# GitHub Setup
GITHUB_REPO = "iotcommunity-space/sensors"
SENSOR_TOKEN = os.getenv("SENSOR_TOKEN")  # GitHub Token for Repo Access
AC_TOKEN = os.getenv("AC_TOKEN")  # OpenAI API Key

# Verify API Keys
if not SENSOR_TOKEN:
    raise ValueError("Missing GitHub API key! Check your GitHub Secrets.")
if not AC_TOKEN:
    raise ValueError("Missing OpenAI API key! Check your GitHub Secrets.")

# Initialize GitHub & OpenAI Clients
github = Github(SENSOR_TOKEN)
repo = github.get_repo(GITHUB_REPO)
client = OpenAI(api_key=AC_TOKEN)  # Updated OpenAI client initialization

# Source URLs
CODECS_JSON_URL = "https://raw.githubusercontent.com/iotcommunity-space/codec/main/assets/codecs.json"
SENSORS_JSON_URL = "https://raw.githubusercontent.com/iotcommunity-space/sensors/main/assets/sensors.json"

# Paths
SENSORS_JSON_PATH = "assets/sensors.json"
SENSORS_ASSETS_PATH = "assets/sensors"
CACHE_PATH = "assets/cached_overviews.json"  # Cache OpenAI responses

def generate_slug(text):
    """Generate a slug from text by converting to lowercase, replacing spaces with '-', and removing special characters."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)  # Remove special characters
    text = re.sub(r'\s+', '-', text)  # Replace spaces with '-'
    return text

def get_md5_hash(sensor_data):
    """Generate an MD5 hash for sensor metadata to track changes efficiently."""
    return hashlib.md5(json.dumps(sensor_data, sort_keys=True).encode()).hexdigest()

def needs_update(sensor_folder, current_hash):
    """Check if the sensor metadata has changed and needs an update."""
    hash_file = os.path.join(sensor_folder, "metadata.md5")

    if not os.path.exists(sensor_folder):  # New sensor
        return True
    if os.path.exists(os.path.join(sensor_folder, "manual.flag")):  # Manual flag means no update
        return False
    if not os.path.exists(hash_file):  # No hash file = needs update
        return True

    with open(hash_file, "r") as f:
        return f.read().strip() != current_hash

def load_cache():
    """Load cached OpenAI responses from disk to prevent redundant API calls."""
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH, "r") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    """Save cached OpenAI responses to disk."""
    with open(CACHE_PATH, "w") as f:
        json.dump(cache, f, indent=2)

def process_sensor(codec, sensors_data, existing_sensors, cache):
    """Process a single sensor and update metadata only if needed."""
    detailed_name = codec["name"]
    vendor_name = codec["name"].split(" - ")[0]

    # Generate slugs for vendor and sensor names
    vendor_slug = generate_slug(vendor_name)
    sensor_slug = generate_slug(detailed_name)

    # Create folder path using slugs
    sensor_folder = os.path.join(SENSORS_ASSETS_PATH, vendor_slug, sensor_slug, "en")
    overview_path = os.path.join(sensor_folder, "overview.md")
    hash_file_path = os.path.join(sensor_folder, "metadata.md5")

    if os.path.exists(os.path.join(sensor_folder, "manual.flag")):
        print(f"⚠️ Skipping manual entry: {detailed_name}")
        return

    sensor_entry = {
        "Description": codec.get("description"),
        "Vendor": vendor_name,
        "TechnicalSpecs": codec.get("specs", {}),
        "imageUrl": codec.get("image", None),
        "slug": sensor_slug  # Add slug to JSON
    }

    current_hash = get_md5_hash(sensor_entry)

    if not needs_update(sensor_folder, current_hash):
        print(f"✅ No changes detected: {detailed_name}")
        return

    print(f"🚀 Processing: {detailed_name}")
    generate_overview(detailed_name, vendor_name, overview_path, cache)

    os.makedirs(sensor_folder, exist_ok=True)
    with open(hash_file_path, "w") as f:
        f.write(current_hash)

    if detailed_name not in existing_sensors:
        sensors_data[detailed_name] = sensor_entry
        existing_sensors.add(detailed_name)

def batch_generate_overviews(sensor_list, cache):
    """Generate multiple overviews in a single OpenAI API call to reduce costs."""
    batch_prompts = []
    batch_keys = []

    for sensor in sensor_list:
        key = f"{sensor['name']}-{sensor['vendor']}"
        if key in cache:
            print(f"⚡ Using cached overview for {sensor['name']}")
            continue
        prompt = f"Write a technical overview for {sensor['name']} ({sensor['vendor']}). Include working principles, installation guide, LoRaWAN details, power consumption, use cases, and limitations."
        batch_prompts.append({"role": "user", "content": prompt})
        batch_keys.append(key)

    if not batch_prompts:
        return  # Nothing to process

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a technical IoT expert writing detailed sensor documentation."}] + batch_prompts
    )

    for i, sensor_response in enumerate(response.choices):
        cache[batch_keys[i]] = sensor_response.message.content
        save_cache(cache)

def generate_overview(sensor_name, vendor, output_path, cache):
    """Generate a detailed technical overview using GPT-4, but avoid redundant API calls."""
    
    if os.path.exists(output_path):
        print(f"⚠️ Skipping OpenAI API call: overview.md already exists for {sensor_name}")
        return

    cache_key = f"{sensor_name}-{vendor}"
    if cache_key in cache:
        print(f"⚡ Using cached OpenAI response for {sensor_name}")
        response_text = cache[cache_key]
    else:
        print(f"🚀 Calling OpenAI API for {sensor_name}")
        prompt = f"Write a technical overview for {sensor_name} ({vendor}). Include working principles, installation guide, LoRaWAN details, power consumption, use cases, and limitations."
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a technical IoT expert writing detailed sensor documentation."},
                      {"role": "user", "content": prompt}]
        )
        response_text = response.choices[0].message.content
        cache[cache_key] = response_text
        save_cache(cache)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(response_text)

    print(f"✅ Successfully wrote overview.md for {sensor_name} at {output_path}")

def commit_to_github(file_path, commit_message):
    """Commit changes to GitHub."""
    try:
        contents = repo.get_contents(file_path)
        repo.update_file(file_path, commit_message, open(file_path, "r").read(), contents.sha)
    except:
        repo.create_file(file_path, commit_message, open(file_path, "r").read())

# Main Execution
if __name__ == "__main__":
    try:
        sensors_data = requests.get(SENSORS_JSON_URL).json() or {}
        codecs_data = requests.get(CODECS_JSON_URL).json()
        existing_sensors = set(sensors_data.keys())
        cache = load_cache()

        # Process all sensors (not just 20)
        for codec in codecs_data:
            process_sensor(codec, sensors_data, existing_sensors, cache)

        # Batch process all remaining sensors for overview generation
        batch_generate_overviews(codecs_data, cache)

        with open(SENSORS_JSON_PATH, "w") as f:
            json.dump(sensors_data, f, indent=2)

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        commit_to_github(SENSORS_JSON_PATH, "Updated sensors.json with new verified entries.")
        print("🎯 Completed: sensors.json and overview.md files updated when necessary.")
