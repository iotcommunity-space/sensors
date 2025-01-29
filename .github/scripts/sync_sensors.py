import os
import json
import requests
from openai import OpenAI
from bs4 import BeautifulSoup
from github import Github

# GitHub Setup
GITHUB_REPO = "iotcommunity-space/sensors"
SENSOR_TOKEN = os.getenv("SENSOR_TOKEN")  # GitHub Secret
AC_TOKEN = os.getenv("AC_TOKEN")  # ChatGPT API Key

# GitHub Headers
HEADERS = {"Authorization": f"token {SENSOR_TOKEN}"}

# Source URLs
CODECS_JSON_URL = "https://raw.githubusercontent.com/iotcommunity-space/codec/refs/heads/main/assets/codecs.json"
SENSORS_JSON_URL = "https://raw.githubusercontent.com/iotcommunity-space/sensors/refs/heads/main/assets/sensors.json"

# Paths
SENSORS_JSON_PATH = "assets/sensors.json"
SENSORS_ASSETS_PATH = "assets/sensors"

# Initialize GitHub
github = Github(SENSOR_TOKEN)
repo = github.get_repo(GITHUB_REPO)

# Load Existing sensors.json
try:
    sensors_data = requests.get(SENSORS_JSON_URL).json()
except:
    sensors_data = {}

# Fetch codecs.json
codecs_data = requests.get(CODECS_JSON_URL).json()

# Ensure Unique Sensors
existing_sensors = set(sensors_data.keys())

# Scraper for Manufacturer Data
def scrape_sensor_details(sensor_name, vendor):
    search_url = f"https://www.google.com/search?q={sensor_name}+{vendor}+datasheet"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract possible description from meta tags
        meta_description = soup.find("meta", attrs={"name": "description"})
        if meta_description:
            return meta_description["content"]
    except:
        return None

# Initialize OpenAI client
client = OpenAI(api_key=AC_TOKEN)

# Process Each Sensor
for codec in codecs_data:
    sensor_name = codec["name"].split(" - ")[-1]
    vendor_name = codec["name"].split(" - ")[0]
    sensor_folder = f"{SENSORS_ASSETS_PATH}/{vendor_name}/{sensor_name}/en"
    overview_md_path = f"{sensor_folder}/overview.md"

    # If manually added, do not modify
    if os.path.exists(sensor_folder):
        print(f"Manual entry detected: {sensor_name} - Skipping modification.")
        continue

    # Fetch Manufacturer Data
    manufacturer_description = scrape_sensor_details(sensor_name, vendor_name) or "No official description found."

    # Prepare Sensor Metadata
    sensor_entry = {
        "Description": codec.get("description", manufacturer_description),
        "Communication": "LoRaWAN",
        "Applications": ["IoT", "Industrial", "Smart Monitoring"],
        "Environmental Compatibility": "Indoor/Outdoor",
        "Data Formats": ["JSON", "MQTT"],
        "Technology": "LoRaWAN End Node",
        "Cost": "Moderate",
        "Vendor": vendor_name,
        "imageUrl": codec.get("image", None),
    }

    # Store in sensors.json if missing
    if sensor_name not in existing_sensors:
        sensors_data[sensor_name] = sensor_entry
        existing_sensors.add(sensor_name)

    # Create Sensor Folder
    os.makedirs(sensor_folder, exist_ok=True)

    # Generate overview.md if missing
    if not os.path.exists(overview_md_path):
        print(f"Generating overview.md for {sensor_name}...")

        # ChatGPT API Request (Updated)
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": "You are a professional technical writer."},
                      {"role": "user", "content": f"Generate an extremely detailed technical overview for the {sensor_name} sensor from {vendor_name}. Include: working principles, installation, LoRaWAN protocol details, power consumption, use cases, challenges, and comparisons."}]
        )

        overview_content = response.choices[0].message.content

        # Write overview.md
        with open(overview_md_path, "w") as md_file:
            md_file.write(overview_content)

# Save Updated sensors.json
with open(SENSORS_JSON_PATH, "w") as f:
    json.dump(sensors_data, f, indent=2)

# Commit Changes
def commit_to_github(file_path, commit_message):
    try:
        contents = repo.get_contents(file_path)
        repo.update_file(file_path, commit_message, open(file_path, "r").read(), contents.sha)
    except:
        repo.create_file(file_path, commit_message, open(file_path, "r").read())

commit_to_github(SENSORS_JSON_PATH, "Updated sensors.json with new verified entries.")

print("Updated sensors.json and generated detailed overview.md files.")
