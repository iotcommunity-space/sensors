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


def get_sensor_hash(sensor_data):
    """Generate stable hash for sensor metadata"""
    return hashlib.sha256(json.dumps(sensor_data, sort_keys=True).encode()).hexdigest()


def needs_update(sensor_folder, current_hash):
    """Check if the sensor needs AI processing"""
    hash_file = os.path.join(sensor_folder, "metadata.sha256")

    if not os.path.exists(sensor_folder):  # New sensor
        return True
    if os.path.exists(os.path.join(sensor_folder, "manual.flag")):  # Manual flag means no update
        return False
    if not os.path.exists(hash_file):  # No hash file = process it
        return True

    with open(hash_file, "r") as f:
        return f.read().strip() != current_hash


def scrape_sensor_details(sensor_name, vendor):
    """Scrape manufacturer website for official sensor description"""
    search_url = f"https://www.google.com/search?q={sensor_name}+{vendor}+datasheet"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        meta_description = soup.find("meta", attrs={"name": "description"})
        if meta_description:
            return meta_description["content"]
    except Exception as e:
        print(f"Web scraping failed for {sensor_name}: {e}")
        return None


def generate_detailed_name(codec):
    """Generate a meaningful and detailed sensor name"""
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


def process_sensor(codec, sensors_data, existing_sensors):
    """Process a single sensor and update metadata"""
    detailed_name = generate_detailed_name(codec)
    vendor_name = codec["name"].split(" - ")[0]
    sensor_folder = os.path.join(SENSORS_ASSETS_PATH, vendor_name, detailed_name, "en")
    overview_path = os.path.join(sensor_folder, "overview.md")
    hash_file_path = os.path.join(sensor_folder, "metadata.sha256")

    if os.path.exists(os.path.join(sensor_folder, "manual.flag")):
        print(f"Skipping manual entry: {detailed_name}")
        return

    sensor_entry = {
        "Description": codec.get("description") or scrape_sensor_details(detailed_name, vendor_name),
        "Vendor": vendor_name,
        "TechnicalSpecs": codec.get("specs", {}),
        "imageUrl": codec.get("image", None)
    }

    current_hash = get_sensor_hash(sensor_entry)

    if not needs_update(sensor_folder, current_hash):
        print(f"No changes detected: {detailed_name}")
        return

    print(f"Processing: {detailed_name}")
    generate_overview(detailed_name, vendor_name, overview_path)

    os.makedirs(sensor_folder, exist_ok=True)
    with open(hash_file_path, "w") as f:
        f.write(current_hash)

    if detailed_name not in existing_sensors:
        sensors_data[detailed_name] = sensor_entry
        existing_sensors.add(detailed_name)


def generate_overview(sensor_name, vendor, output_path):
    """Generate a detailed technical overview using GPT-4"""

    # ✅ Ensure the directory exists before writing
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    prompt = f"Write a technical overview for {sensor_name} ({vendor}). Include working principles, installation guide, LoRaWAN details, power consumption, use cases, and limitations."

    response = openai_client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a technical IoT expert writing detailed sensor documentation."},
            {"role": "user", "content": prompt}
        ]
    )

    with open(output_path, "w") as f:
        f.write(response.choices[0].message.content)

    print(f"✅ Successfully wrote overview.md for {sensor_name} at {output_path}")



def commit_to_github(file_path, commit_message):
    """Commit changes to GitHub"""
    try:
        contents = repo.get_contents(file_path)
        repo.update_file(file_path, commit_message, open(file_path, "r").read(), contents.sha)
    except:
        repo.create_file(file_path, commit_message, open(file_path, "r").read())


# Main Execution
if __name__ == "__main__":
    try:
        # Load existing data
        sensors_data = requests.get(SENSORS_JSON_URL).json() or {}
        codecs_data = requests.get(CODECS_JSON_URL).json()

        # Process only the first 20 sensors for testing
        existing_sensors = set(sensors_data.keys())
        for codec in codecs_data[:20]:  # Only first 20 for testing
            process_sensor(codec, sensors_data, existing_sensors)

        # Save updated data
        with open(SENSORS_JSON_PATH, "w") as f:
            json.dump(sensors_data, f, indent=2)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        commit_to_github(SENSORS_JSON_PATH, "Updated sensors.json with new verified entries.")
        print("Updated sensors.json and generated detailed overview.md files where necessary.")
