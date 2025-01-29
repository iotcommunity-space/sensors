import os
import json
import requests
import hashlib
from openai import OpenAI
from bs4 import BeautifulSoup
from github import Github

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
openai_client = OpenAI(api_key=AC_TOKEN)

# Source URLs
CODECS_JSON_URL = "https://raw.githubusercontent.com/iotcommunity-space/codec/main/assets/codecs.json"
SENSORS_JSON_URL = "https://raw.githubusercontent.com/iotcommunity-space/sensors/main/assets/sensors.json"

# Paths
SENSORS_JSON_PATH = "assets/sensors.json"
SENSORS_ASSETS_PATH = "assets/sensors"
CACHE_PATH = "assets/cache.json"  # Store API responses to avoid redundant requests


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


def scrape_sensor_details(sensor_name, vendor):
    """Scrape manufacturer website for official sensor description to reduce API usage."""
    search_url = f"https://www.google.com/search?q={sensor_name}+{vendor}+datasheet"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        meta_description = soup.find("meta", attrs={"name": "description"})
        if meta_description:
            return meta_description["content"]
    except Exception as e:
        print(f"⚠️ Web scraping failed for {sensor_name}: {e}")
        return None


def generate_detailed_name(codec):
    """Generate a meaningful and detailed sensor name."""
    vendor = codec["name"].split(" - ")[0]
    model = codec["name"].split(" - ")[-1]

    category_keywords = {
        "LHT": "LoRaWAN Temperature & Humidity Sensor",
        "Dus": "Industrial Pressure Sensor",
        "Fms": "Smart Flow Meter",
        "Pds": "Differential Pressure Sensor",
        "Plc": "Wireless Level Sensor",
        "WQS": "Water Quality Monitoring Sensor",
        "LWL": "Water Leak Detector"
    }

    category = next((v for k, v in category_keywords.items() if k in model), "LoRaWAN IoT Sensor")
    return f"{vendor} {model} - {category}"


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
    detailed_name = generate_detailed_name(codec)
    vendor_name = codec["name"].split(" - ")[0]
    sensor_folder = os.path.join(SENSORS_ASSETS_PATH, vendor_name, detailed_name, "en")
    overview_path = os.path.join(sensor_folder, "overview.md")
    hash_file_path = os.path.join(sensor_folder, "metadata.md5")

    if os.path.exists(os.path.join(sensor_folder, "manual.flag")):
        print(f"⚠️ Skipping manual entry: {detailed_name}")
        return

    sensor_entry = {
        "Description": codec.get("description") or scrape_sensor_details(detailed_name, vendor_name),
        "Vendor": vendor_name,
        "TechnicalSpecs": codec.get("specs", {}),
        "imageUrl": codec.get("image", None)
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


def generate_overview(sensor_name, vendor, output_path, cache):
    """Generate a detailed technical overview using GPT-4, but avoid redundant API calls."""
    
    # ✅ Skip API request if overview.md already exists
    if os.path.exists(output_path):
        print(f"⚠️ Skipping OpenAI API call: overview.md already exists for {sensor_name}")
        return

    # ✅ Check cache before making an API call
    cache_key = f"{sensor_name}-{vendor}"
    if cache_key in cache:
        print(f"⚠️ Using cached OpenAI response for {sensor_name}")
        response_text = cache[cache_key]
    else:
        prompt = f"Write a technical overview for {sensor_name} ({vendor}). Include working principles, installation guide, LoRaWAN details, power consumption, use cases, and limitations."

        response = openai_client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a technical IoT expert writing detailed sensor documentation."},
                {"role": "user", "content": prompt}
            ]
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

        for codec in codecs_data[:20]:  # Process first 20 for testing
            process_sensor(codec, sensors_data, existing_sensors, cache)

        with open(SENSORS_JSON_PATH, "w") as f:
            json.dump(sensors_data, f, indent=2)

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        commit_to_github(SENSORS_JSON_PATH, "Updated sensors.json with new verified entries.")
        print("🎯 Completed: sensors.json and overview.md files updated when necessary.")
