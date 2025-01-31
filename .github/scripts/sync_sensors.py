import os
import json
import requests
import hashlib
import re
from github import Github
# from openai import OpenAI  # Commented out as OpenAI is no longer used

# GitHub Setup
GITHUB_REPO = "iotcommunity-space/sensors"
SENSOR_TOKEN = os.getenv("SENSOR_TOKEN")  # GitHub Token for Repo Access
# AC_TOKEN = os.getenv("AC_TOKEN")  # OpenAI API Key (No longer needed)

# Verify API Keys
if not SENSOR_TOKEN:
    raise ValueError("Missing GitHub API key! Check your GitHub Secrets.")
# if not AC_TOKEN:
#     raise ValueError("Missing OpenAI API key! Check your GitHub Secrets.")  # Not needed

# Initialize GitHub & OpenAI Clients
github = Github(SENSOR_TOKEN)
repo = github.get_repo(GITHUB_REPO)
# client = OpenAI(api_key=AC_TOKEN)  # Commented out

# Source URLs
CODECS_JSON_URL = "https://raw.githubusercontent.com/iotcommunity-space/codec/main/assets/codecs.json"
SENSORS_JSON_URL = "https://raw.githubusercontent.com/iotcommunity-space/sensors/main/assets/sensors.json"

# Paths
SENSORS_JSON_PATH = "assets/sensors.json"
SENSORS_ASSETS_PATH = "assets/sensors"
# CACHE_PATH = "assets/cached_overviews.json"  # No longer needed

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
        if existing_hash != current_hash:
            return True
    return False

# def load_cache():
#     """Load cached OpenAI responses from disk to prevent redundant API calls."""
#     if os.path.exists(CACHE_PATH):
#         with open(CACHE_PATH, "r") as f:
#             return json.load(f)
#     return {}

# def save_cache(cache):
#     """Save cached OpenAI responses to disk."""
#     with open(CACHE_PATH, "w") as f:
#         json.dump(cache, f, indent=2)

def process_sensor(codec, sensors_data, existing_sensors):
    """Process a single sensor and update metadata only if needed."""
    detailed_name = codec.get("name", "").strip()
    if not detailed_name:
        print("⚠️ Sensor entry missing 'name'. Skipping.")
        return
    vendor_name = detailed_name.split(" - ")[0].strip()

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

    # Populate sensor_entry with desired fields
    sensor_entry = {
        "Description": codec.get("description", "No description available."),
        "Communication": codec.get("communication", "LoRaWAN"),  # Default to LoRaWAN if not specified
        "Applications": codec.get("applications", []),  # Expecting a list
        "Environmental Compatibility": codec.get("environmental_compatibility", "Indoor and outdoor use"),
        "Data Formats": codec.get("data_formats", ["JSON", "MQTT"]),  # Default formats
        "Technology": codec.get("technology", "LoRaWAN End node"),
        "Cost": codec.get("cost", "Affordable"),  # Default cost
        "Vendor": vendor_name,
        "imageUrl": codec.get("image", None),
        "slug": sensor_slug  # Add slug to JSON
    }

    current_hash = get_md5_hash(sensor_entry)

    if not needs_update(sensor_folder, current_hash):
        print(f"✅ No changes detected: {detailed_name}")
        return

    print(f"🚀 Processing: {detailed_name}")

    # Generate overview.md without OpenAI
    generate_overview(detailed_name, vendor_name, overview_path, sensor_entry)

    os.makedirs(sensor_folder, exist_ok=True)
    with open(hash_file_path, "w") as f:
        f.write(current_hash)

    if detailed_name not in existing_sensors:
        sensors_data[detailed_name] = sensor_entry
        existing_sensors.add(detailed_name)
    else:
        # Update existing sensor entry
        sensors_data[detailed_name].update(sensor_entry)

def generate_overview(sensor_name, vendor, output_path, sensor_entry):
    """Generate a detailed technical overview without using OpenAI."""
    if os.path.exists(output_path):
        print(f"⚠️ Skipping overview.md creation: Already exists for {sensor_name}")
        return

    # Use the Description as the overview content or provide a placeholder
    overview_content = sensor_entry["Description"]

    # Optionally, you can structure the overview using other fields
    overview_content += f"\n\n**Vendor:** {vendor}\n\n"
    overview_content += f"**Communication:** {sensor_entry['Communication']}\n\n"
    overview_content += f"**Applications:** {', '.join(sensor_entry['Applications']) if sensor_entry['Applications'] else 'N/A'}\n\n"
    overview_content += f"**Environmental Compatibility:** {sensor_entry['Environmental Compatibility']}\n\n"
    overview_content += f"**Data Formats:** {', '.join(sensor_entry['Data Formats'])}\n\n"
    overview_content += f"**Technology:** {sensor_entry['Technology']}\n\n"
    overview_content += f"**Cost:** {sensor_entry['Cost']}\n\n"
    if sensor_entry["imageUrl"]:
        overview_content += f"![Sensor Image]({sensor_entry['imageUrl']})\n"

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(overview_content)

    print(f"✅ Successfully wrote overview.md for {sensor_name} at {output_path}")

def commit_to_github(file_path, commit_message):
    """Commit changes to GitHub."""
    try:
        with open(file_path, "r") as f:
            content = f.read()
        try:
            contents = repo.get_contents(file_path)
            repo.update_file(file_path, commit_message, content, contents.sha)
            print(f"✅ Updated {file_path} in repository.")
        except:
            repo.create_file(file_path, commit_message, content)
            print(f"✅ Created {file_path} in repository.")
    except Exception as e:
        print(f"❌ Failed to commit {file_path} to GitHub: {e}")

# Main Execution
if __name__ == "__main__":
    try:
        print("🔍 Fetching sensors.json data...")
        sensors_response = requests.get(SENSORS_JSON_URL)
        sensors_response.raise_for_status()
        sensors_data = sensors_response.json() or {}
        print(f"Loaded {len(sensors_data)} existing sensors.")

        print("🔍 Fetching codecs.json data...")
        codecs_response = requests.get(CODECS_JSON_URL)
        codecs_response.raise_for_status()
        codecs_data = codecs_response.json()
        print(f"Loaded {len(codecs_data)} codecs.")

        existing_sensors = set(sensors_data.keys())

        # Process all sensors
        print("🛠️ Processing sensors...")
        for codec in codecs_data:
            process_sensor(codec, sensors_data, existing_sensors)

        # Save updated sensors.json
        print("📄 Writing sensors.json...")
        with open(SENSORS_JSON_PATH, "w") as f:
            json.dump(sensors_data, f, indent=2)
        print("✅ sensors.json successfully written.")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        commit_to_github(SENSORS_JSON_PATH, "Updated sensors.json with new verified entries.")
        print("🎯 Completed: sensors.json and overview.md files updated when necessary.")
