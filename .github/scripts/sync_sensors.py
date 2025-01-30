#!/usr/bin/env python3
import os
import re
import json
import hashlib
import requests
from openai import OpenAI
from github import Github

########################################################
# Configuration
########################################################

GITHUB_REPO = "iotcommunity-space/sensors"
SENSOR_TOKEN = os.getenv("SENSOR_TOKEN")  # GitHub Token for Repo Access
AC_TOKEN = os.getenv("AC_TOKEN")         # OpenAI API Key

if not SENSOR_TOKEN:
    raise ValueError("Missing GitHub API key! Check your GitHub Secrets.")
if not AC_TOKEN:
    raise ValueError("Missing OpenAI API key! Check your GitHub Secrets.")

# Initialize GitHub and OpenAI
github = Github(SENSOR_TOKEN)
repo = github.get_repo(GITHUB_REPO)
openai_client = OpenAI(api_key=AC_TOKEN)

# Source URLs
CODECS_JSON_URL = "https://raw.githubusercontent.com/iotcommunity-space/codec/main/assets/codecs.json"

# Paths
SENSORS_JSON_PATH = "assets/sensors.json"
SENSORS_ASSETS_PATH = "assets/sensors"
CACHE_PATH = "assets/cached_overviews.json"  # Cache for GPT responses

########################################################
# Helper Functions
########################################################

def folder_name(text: str) -> str:
    """
    Transform the sensor name into a folder-friendly string:
    - Preserve uppercase letters
    - Remove characters except letters, digits, spaces, and dashes
    - Replace runs of whitespace with a single dash
    - Merge multiple dashes into one
    - Trim leading/trailing dashes
    
    e.g. "MILESIGHT - Em300 Mcs" -> "MILESIGHT-Em300-Mcs"
    """
    # Keep letters, digits, spaces, and dashes
    text = re.sub(r"[^A-Za-z0-9\s-]+", "", text)
    # Replace runs of whitespace with a single dash
    text = re.sub(r"\s+", "-", text)
    # Merge multiple dashes into one
    text = re.sub(r"-+", "-", text)
    return text.strip("-")

def get_md5_hash(sensor_data: dict) -> str:
    """
    Generate an MD5 hash for sensor metadata to track changes efficiently.
    """
    return hashlib.md5(json.dumps(sensor_data, sort_keys=True).encode()).hexdigest()

def commit_to_github(file_path: str, commit_message: str):
    """
    Commit changes to GitHub. Creates or updates the file in the repository.
    """
    with open(file_path, "r") as f:
        new_content = f.read()

    try:
        contents = repo.get_contents(file_path)
        repo.update_file(
            path=file_path,
            message=commit_message,
            content=new_content,
            sha=contents.sha
        )
        print(f"Updated {file_path} in repo.")
    except Exception:
        repo.create_file(
            path=file_path,
            message=commit_message,
            content=new_content
        )
        print(f"Created {file_path} in repo.")

def load_cache():
    """
    Load cached OpenAI responses from disk to prevent redundant API calls.
    """
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH, "r") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    """
    Save cached OpenAI responses to disk.
    """
    with open(CACHE_PATH, "w") as f:
        json.dump(cache, f, indent=2)

def generate_overview(folder_str: str, sensor_folder: str, sensor_name: str, vendor: str, cache: dict):
    """
    Call GPT to generate an overview.md, skipping if one exists already.
    """
    overview_path = os.path.join(sensor_folder, "overview.md")
    if os.path.exists(overview_path):
        print(f"⚠️ Skipping GPT call for {folder_str}: overview.md already exists.")
        return

    cache_key = folder_str
    if cache_key in cache:
        print(f"⚡ Using cached GPT response for {folder_str}")
        response_text = cache[cache_key]
    else:
        print(f"🚀 Calling OpenAI API for {sensor_name}")
        prompt = (
            f"Write a technical overview for {sensor_name} ({vendor}). "
            "Include working principles, installation guide, LoRaWAN details, power consumption, "
            "use cases, and limitations."
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

    with open(overview_path, "w") as f:
        f.write(response_text)

    print(f"✅ Created overview.md for {folder_str}")

########################################################
# Main Logic
########################################################

def main():
    print("Fetching codecs.json ...")
    resp = requests.get(CODECS_JSON_URL)
    resp.raise_for_status()
    codecs_data = resp.json()

    # We'll collect sensor info in a big dict
    sensors_data = {}

    # Make sure our sensors root folder exists
    os.makedirs(SENSORS_ASSETS_PATH, exist_ok=True)

    # GPT caching
    cache = load_cache()

    for codec in codecs_data:
        raw_name = codec.get("name", "Unnamed Sensor")
        folder_str = folder_name(raw_name)  # e.g. "MILESIGHT-Em300-Mcs"

        # Build folder path: assets/sensors/<FolderStr>/en/
        sensor_folder = os.path.join(SENSORS_ASSETS_PATH, folder_str, "en")
        os.makedirs(sensor_folder, exist_ok=True)

        # Build the sensor data object with your specified fields:
        sensor_entry = {
            "Name": raw_name,
            "Description": codec.get("description", ""),
            "Communication": codec.get("Communication", ""),
            "Applications": codec.get("Applications", []),
            "Environmental Compatibility": codec.get("Environmental Compatibility", ""),
            "Data Formats": codec.get("Data Formats", []),
            "Technology": codec.get("technology", ""),
            "Cost": codec.get("Cost", ""),
            "Vendor": codec.get("vendor", ""),
            "imageUrl": codec.get("image", None),
        }

        # Write metadata.md5
        metadata_hash = get_md5_hash(sensor_entry)
        hash_file_path = os.path.join(sensor_folder, "metadata.md5")
        with open(hash_file_path, "w") as f:
            f.write(metadata_hash)

        # Insert into big sensors_data under folder_str
        sensors_data[folder_str] = sensor_entry

        # Generate or skip GPT-based overview
        generate_overview(folder_str, sensor_folder, raw_name, sensor_entry["Vendor"], cache)

    # Save the final sensors.json
    with open(SENSORS_JSON_PATH, "w") as f:
        json.dump(sensors_data, f, indent=2)

    # Commit to GitHub
    commit_to_github(
        file_path=SENSORS_JSON_PATH,
        commit_message="Rebuilt sensors.json with friendly folder names, extra fields, and GPT overviews"
    )
    print("✅ Done! Created sensors.json and overview.md for sensors with your letter-casing and fields.")

if __name__ == "__main__":
    main()
