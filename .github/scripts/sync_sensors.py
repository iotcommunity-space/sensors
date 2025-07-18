import os
import json
import requests
import hashlib
import re
import traceback
from github import Github, GithubException
from openai import OpenAI
import logging

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# GitHub Setup
GITHUB_REPO = "iotcommunity-space/sensors"
SENSOR_TOKEN = os.getenv("SENSOR_TOKEN")
AC_TOKEN = os.getenv("AC_TOKEN")

# Verify API Keys
if not SENSOR_TOKEN:
    raise ValueError("Missing GitHub API key! Check your GitHub Secrets.")
if not AC_TOKEN:
    raise ValueError("Missing OpenAI API key! Check your GitHub Secrets.")

# Initialize GitHub & OpenAI Clients
github = Github(SENSOR_TOKEN)
repo = github.get_repo(GITHUB_REPO)
client = OpenAI(api_key=AC_TOKEN)

# Source URLs
CODECS_JSON_URL = "https://raw.githubusercontent.com/iotcommunity-space/codec/main/assets/codecs.json"
SENSORS_JSON_URL = "https://raw.githubusercontent.com/iotcommunity-space/sensors/main/assets/sensors.json"

# Paths
SENSORS_JSON_PATH = "assets/sensors.json"
SENSORS_ASSETS_PATH = "assets/sensors"
CACHE_PATH = "assets/cached_overviews.json"
MANUAL_OVERRIDES_PATH = "assets/manual_overrides.json"  # New: Manual overrides file

def generate_slug(text):
    """Generate a slug from text by converting to lowercase, replacing spaces with '-', and removing special characters."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    return text

def get_md5_hash(sensor_data):
    """Generate an MD5 hash for sensor metadata to track changes efficiently."""
    return hashlib.md5(json.dumps(sensor_data, sort_keys=True).encode()).hexdigest()

def load_manual_overrides():
    """Load manual overrides from disk to preserve user corrections."""
    if os.path.exists(MANUAL_OVERRIDES_PATH):
        with open(MANUAL_OVERRIDES_PATH, "r") as f:
            return json.load(f)
    return {}

def save_manual_overrides(overrides):
    """Save manual overrides to disk."""
    with open(MANUAL_OVERRIDES_PATH, "w") as f:
        json.dump(overrides, f, indent=2)

def apply_manual_overrides(sensor_name, sensor_entry, manual_overrides):
    """Apply manual overrides to sensor entry if they exist."""
    if sensor_name in manual_overrides:
        logging.info(f"🔧 Applying manual overrides for {sensor_name}")
        # Merge manual overrides with generated data
        for key, value in manual_overrides[sensor_name].items():
            if key != "_metadata":  # Skip metadata
                sensor_entry[key] = value
        return True
    return False

def is_manually_protected(sensor_name, sensor_folder):
    """Check if sensor is protected from automatic updates."""
    manual_flag_path = os.path.join(sensor_folder, "manual.flag")
    return os.path.exists(manual_flag_path)

def needs_update(sensor_folder, current_hash):
    """Check if the sensor metadata has changed and needs an update."""
    hash_file = os.path.join(sensor_folder, "metadata.md5")

    if not os.path.exists(sensor_folder):
        return True
    if is_manually_protected(None, sensor_folder):
        return False
    if not os.path.exists(hash_file):
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

def preserve_existing_data(existing_sensors_data, sensor_name, new_sensor_entry):
    """Preserve existing sensor data and only update if significantly different."""
    if sensor_name not in existing_sensors_data:
        return new_sensor_entry
    
    existing_entry = existing_sensors_data[sensor_name]
    
    # Check if this might be manually edited
    # You can add more sophisticated logic here to detect manual edits
    if "_manual_edit" in existing_entry:
        logging.info(f"🔒 Preserving manually edited data for {sensor_name}")
        return existing_entry
    
    # Preserve certain fields that might have been manually corrected
    preserved_fields = ["imageUrl", "Cost", "custom_notes", "manual_description"]
    
    for field in preserved_fields:
        if field in existing_entry and field not in new_sensor_entry:
            new_sensor_entry[field] = existing_entry[field]
        elif field in existing_entry and existing_entry[field] != new_sensor_entry.get(field):
            # If the field exists in both but differs, keep the existing one
            # This assumes manual corrections are intentional
            logging.info(f"🔧 Preserving existing value for {field} in {sensor_name}")
            new_sensor_entry[field] = existing_entry[field]
    
    return new_sensor_entry

def process_sensor(codec, sensors_data, existing_sensors, cache, manual_overrides, existing_sensors_data):
    """Process a single sensor and update metadata only if needed."""
    detailed_name = codec.get("name")
    if not detailed_name:
        logging.warning("⚠️ Missing 'name' in codec. Skipping entry.")
        return
    
    vendor_name = detailed_name.split(" - ")[0]
    vendor_slug = generate_slug(vendor_name)
    sensor_slug = generate_slug(detailed_name)
    sensor_folder = os.path.join(SENSORS_ASSETS_PATH, vendor_slug, sensor_slug, "en")
    
    # Check if manually protected
    if is_manually_protected(detailed_name, sensor_folder):
        logging.info(f"🔒 Skipping manually protected sensor: {detailed_name}")
        return

    overview_path = os.path.join(sensor_folder, "overview.md")
    hash_file_path = os.path.join(sensor_folder, "metadata.md5")

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

    # Apply manual overrides if they exist
    has_manual_override = apply_manual_overrides(detailed_name, sensor_entry, manual_overrides)
    
    # Preserve existing data (especially manual corrections)
    sensor_entry = preserve_existing_data(existing_sensors_data, detailed_name, sensor_entry)

    current_hash = get_md5_hash(sensor_entry)

    if not needs_update(sensor_folder, current_hash) and not has_manual_override:
        logging.info(f"✅ No changes detected: {detailed_name}")
        if detailed_name not in existing_sensors:
            sensors_data[detailed_name] = sensor_entry
            existing_sensors.add(detailed_name)
        return

    logging.info(f"🚀 Processing: {detailed_name}")
    
    # Only generate overview if it doesn't exist or if forced
    if not os.path.exists(overview_path) or has_manual_override:
        generate_overview(detailed_name, vendor_name, overview_path, cache)

    os.makedirs(sensor_folder, exist_ok=True)
    with open(hash_file_path, "w") as f:
        f.write(current_hash)

    sensors_data[detailed_name] = sensor_entry
    existing_sensors.add(detailed_name)

def generate_overview(sensor_name, vendor, output_path, cache):
    """Generate a detailed technical overview using GPT-4, but avoid redundant API calls."""
    
    # Don't overwrite existing overview.md files unless forced
    if os.path.exists(output_path):
        logging.info(f"📄 Preserving existing overview.md for {sensor_name}")
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
                model="gpt-4o",
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
    """Commit changes to GitHub using GitHub Actions bot credentials."""
    try:
        contents = repo.get_contents(file_path)
        repo.update_file(
            file_path,
            commit_message,
            open(file_path, "r").read(),
            contents.sha,
            author={"name": "github-actions[bot]", "email": "github-actions[bot]@users.noreply.github.com"}
        )
        logging.info(f"✅ Committed changes to {file_path} as github-actions[bot]")
    except GithubException as e:
        if e.status == 404:
            repo.create_file(
                file_path,
                commit_message,
                open(file_path, "r").read(),
                author={"name": "github-actions[bot]", "email": "github-actions[bot]@users.noreply.github.com"}
            )
            logging.info(f"✅ Created and committed new file {file_path} as github-actions[bot]")
        else:
            logging.error(f"❌ GitHub Exception: {e}")
            traceback.print_exc()

# Main Execution
if __name__ == "__main__":
    try:
        # Load existing sensors.json
        sensors_response = requests.get(SENSORS_JSON_URL)
        sensors_response.raise_for_status()
        existing_sensors_data = sensors_response.json() or {}
        sensors_data = existing_sensors_data.copy()  # Work with a copy
        logging.info(f"Fetched existing sensors.json with {len(sensors_data)} entries.")
        
        # Load codecs.json
        codecs_response = requests.get(CODECS_JSON_URL)
        codecs_response.raise_for_status()
        codecs_data = codecs_response.json()
        logging.info(f"Fetched codecs.json with {len(codecs_data)} entries.")

        existing_sensors = set(sensors_data.keys())
        cache = load_cache()
        manual_overrides = load_manual_overrides()

        # Process all sensors
        for codec in codecs_data:
            process_sensor(codec, sensors_data, existing_sensors, cache, manual_overrides, existing_sensors_data)

        # Write updated sensors.json
        with open(SENSORS_JSON_PATH, "w") as f:
            json.dump(sensors_data, f, indent=2)
        logging.info(f"✅ Updated sensors.json with {len(sensors_data)} entries.")

        # Commit manual overrides if they were created/updated
        if manual_overrides:
            save_manual_overrides(manual_overrides)

    except Exception as e:
        logging.error(f"❌ Error during main execution: {e}")
        traceback.print_exc()
    finally:
        try:
            commit_to_github(SENSORS_JSON_PATH, "Updated sensors.json with new verified entries (preserving manual corrections)")
            logging.info("🎯 Completed: sensors.json and overview.md files updated when necessary.")
        except Exception as commit_error:
            logging.error(f"❌ Error during commit: {commit_error}")
            traceback.print_exc()
