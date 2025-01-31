import os
import json
import requests
import hashlib
import re
import traceback
from github import Github, GithubException
from openai import OpenAI  # Updated import for OpenAI >=1.0.0
import logging

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

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
        existing_hash = f.read().strip()
        return existing_hash != current_hash

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
    detailed_name = codec.get("name")
    if not detailed_name:
        logging.warning("⚠️ Missing 'name' in codec. Skipping entry.")
        return
    vendor_name = detailed_name.split(" - ")[0]

    # Generate slugs for vendor and sensor names
    vendor_slug = generate_slug(vendor_name)
    sensor_slug = generate_slug(detailed_name)

    # Create folder path using slugs
    sensor_folder = os.path.join(SENSORS_ASSETS_PATH, vendor_slug, sensor_slug, "en")
    overview_path = os.path.join(sensor_folder, "overview.md")
    hash_file_path = os.path.join(sensor_folder, "metadata.md5")

    if os.path.exists(os.path.join(sensor_folder, "manual.flag")):
        logging.warning(f"⚠️ Skipping manual entry: {detailed_name}")
        return

    sensor_entry = {
        "Description": codec.get("description", "No description provided."),
        "Communication": codec.get("communication", "Unknown"),
        "Applications": codec.get("applications", []),
        "Environmental Compatibility": codec.get("environmental_compatibility", "Unknown"),
        "Data Formats": codec.get("data_formats", []),
        "Technology": codec.get("technology", "Unknown"),
        "Cost": codec.get("cost", "Unknown"),
        "Vendor": vendor_name,
        "imageUrl": codec.get("image", None),
        "slug": sensor_slug
    }

    current_hash = get_md5_hash(sensor_entry)

    if not needs_update(sensor_folder, current_hash):
        logging.info(f"✅ No changes detected: {detailed_name}")
        return

    logging.info(f"🚀 Processing: {detailed_name}")
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
        key = f"{sensor.get('name', 'unknown')}-{sensor.get('vendor', 'unknown')}"
        if key in cache:
            logging.info(f"⚡ Using cached overview for {sensor.get('name', 'unknown')}")
            continue
        prompt = f"Write a technical overview for {sensor.get('name', 'unknown')} ({sensor.get('vendor', 'unknown')}). Include working principles, installation guide, LoRaWAN details, power consumption, use cases, and limitations."
        batch_prompts.append({"role": "user", "content": prompt})
        batch_keys.append(key)

    if not batch_prompts:
        return  # Nothing to process

    try:
        response = client.chat.completions.create(
            model="gpt-4o mini",
            messages=[{"role": "system", "content": "You are a technical IoT expert writing detailed sensor documentation."}] + batch_prompts
        )

        for i, sensor_response in enumerate(response.choices):
            cache[batch_keys[i]] = sensor_response.message.content
        save_cache(cache)
    except Exception as e:
        logging.error(f"Error during batch_generate_overviews: {e}")
        traceback.print_exc()

def generate_overview(sensor_name, vendor, output_path, cache):
    """Generate a detailed technical overview using GPT-4, but avoid redundant API calls."""
    
    if os.path.exists(output_path):
        logging.warning(f"⚠️ Skipping OpenAI API call: overview.md already exists for {sensor_name}")
        return

    cache_key = f"{sensor_name}-{vendor}"
    if cache_key in cache:
        logging.info(f"⚡ Using cached OpenAI response for {sensor_name}")
        response_text = cache[cache_key]
    else:
        logging.info(f"🚀 Calling OpenAI API for {sensor_name}")
        prompt = f"Write a technical overview for {sensor_name} ({vendor}). Include working principles, installation guide, LoRaWAN details, power consumption, use cases, and limitations."
        try:
            response = client.chat.completions.create(
                model="gpt-4o mini",
                messages=[
                    {"role": "system", "content": "You are a technical IoT expert writing detailed sensor documentation."},
                    {"role": "user", "content": prompt}
                ]
            )
            response_text = response.choices[0].message.content
            cache[cache_key] = response_text
            save_cache(cache)
        except Exception as e:
            logging.error(f"Error during generate_overview for {sensor_name}: {e}")
            traceback.print_exc()
            return

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(response_text)

    logging.info(f"✅ Successfully wrote overview.md for {sensor_name} at {output_path}")

def commit_to_github(file_path, commit_message):
    """Commit changes to GitHub."""
    try:
        contents = repo.get_contents(file_path)
        repo.update_file(file_path, commit_message, open(file_path, "r").read(), contents.sha)
        logging.info(f"✅ Committed changes to {file_path}")
    except GithubException as e:
        if e.status == 404:
            repo.create_file(file_path, commit_message, open(file_path, "r").read())
            logging.info(f"✅ Created and committed new file {file_path}")
        else:
            logging.error(f"❌ GitHub Exception: {e}")
            traceback.print_exc()

# Main Execution
if __name__ == "__main__":
    try:
        sensors_response = requests.get(SENSORS_JSON_URL)
        sensors_response.raise_for_status()
        sensors_data = sensors_response.json() or {}
        logging.info(f"Fetched existing sensors.json with {len(sensors_data)} entries.")
        
        codecs_response = requests.get(CODECS_JSON_URL)
        codecs_response.raise_for_status()
        codecs_data = codecs_response.json()
        logging.info(f"Fetched codecs.json with {len(codecs_data)} entries.")

        existing_sensors = set(sensors_data.keys())
        cache = load_cache()

        # Process all sensors
        for codec in codecs_data.values():
            process_sensor(codec, sensors_data, existing_sensors, cache)

        # Batch process all remaining sensors for overview generation
        batch_generate_overviews(codecs_data.values(), cache)

        with open(SENSORS_JSON_PATH, "w") as f:
            json.dump(sensors_data, f, indent=2)
        logging.info(f"✅ Updated sensors.json with {len(sensors_data)} entries.")

    except Exception as e:
        logging.error(f"❌ Error during main execution: {e}")
        traceback.print_exc()
    finally:
        try:
            commit_to_github(SENSORS_JSON_PATH, "Updated sensors.json with new verified entries.")
            logging.info("🎯 Completed: sensors.json and overview.md files updated when necessary.")
        except Exception as commit_error:
            logging.error(f"❌ Error during commit: {commit_error}")
            traceback.print_exc()
