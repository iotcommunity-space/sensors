#!/usr/bin/env python3
import os
import re
import json
import hashlib
import requests
from github import Github

# ==============================
# OPTIONAL: If you want OpenAI integration, un-comment these lines and set AC_TOKEN
# from openai import OpenAI
# ==============================

########################################################
# Configuration
########################################################

GITHUB_REPO = "iotcommunity-space/sensors"
SENSOR_TOKEN = os.getenv("SENSOR_TOKEN")  # GitHub Token for Repo Access
# AC_TOKEN = os.getenv("AC_TOKEN")         # OpenAI API Key, if used

if not SENSOR_TOKEN:
    raise ValueError("Missing GitHub API key! Check your GitHub Secrets.")

# If you want GPT calls, un-comment these checks:
# if not AC_TOKEN:
#     raise ValueError("Missing OpenAI API key! Check your GitHub Secrets.")

# Initialize GitHub
github = Github(SENSOR_TOKEN)
repo = github.get_repo(GITHUB_REPO)

# If using OpenAI, initialize it (uncomment below):
# openai_client = OpenAI(api_key=AC_TOKEN)

# Source URLs
CODECS_JSON_URL = "https://raw.githubusercontent.com/iotcommunity-space/codec/main/assets/codecs.json"

# Paths
SENSORS_JSON_PATH = "assets/sensors.json"
SENSORS_ASSETS_PATH = "assets/sensors"
CACHE_PATH = "assets/cached_overviews.json"  # Cache OpenAI responses if using GPT

########################################################
# Helper Functions
########################################################

def slugify(text: str) -> str:
    """
    Convert a sensor's 'name' to a slug suitable for filenames and JSON keys.
    Example: 'MILESIGHT - Em300 Mcs' -> 'milesight-em300-mcs'
    """
    text = text.lower()
    text = text.replace(" ", "-")
    text = re.sub(r"[^a-z0-9-]+", "", text)
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
        # If the file already exists in the repo, update it
        contents = repo.get_contents(file_path)
        repo.update_file(
            path=file_path,
            message=commit_message,
            content=new_content,
            sha=contents.sha
        )
        print(f"Updated {file_path} in repo.")
    except Exception:
        # Otherwise, create a new file
        repo.create_file(
            path=file_path,
            message=commit_message,
            content=new_content
        )
        print(f"Created {file_path} in repo.")

# --------------------------------------------
# OPTIONAL GPT Functions (Commented Out)
# --------------------------------------------

# def load_cache():
#     if os.path.exists(CACHE_PATH):
#         with open(CACHE_PATH, "r") as f:
#             return json.load(f)
#     return {}

# def save_cache(cache):
#     with open(CACHE_PATH, "w") as f:
#         json.dump(cache, f, indent=2)

# def generate_overview(slug: str, sensor_folder: str, sensor_name: str, vendor: str, cache: dict):
#     """
#     Call GPT to generate an overview.md, skipping if one exists.
#     """
#     overview_path = os.path.join(sensor_folder, "overview.md")
#     if os.path.exists(overview_path):
#         print(f"⚠️ Skipping GPT call for {slug}: overview.md already exists.")
#         return

#     cache_key = f"{slug}"
#     if cache_key in cache:
#         print(f"⚡ Using cached GPT response for {slug}")
#         response_text = cache[cache_key]
#     else:
#         print(f"🚀 Calling OpenAI API for {sensor_name}")
#         prompt = (
#             f"Write a technical overview for {sensor_name} ({vendor}). "
#             "Include working principles, installation guide, LoRaWAN details, power consumption, "
#             "use cases, and limitations."
#         )
#         response = openai_client.chat.completions.create(
#             model="gpt-4o",
#             messages=[
#                 {"role": "system", "content": "You are a technical IoT expert writing detailed sensor documentation."},
#                 {"role": "user", "content": prompt}
#             ]
#         )
#         response_text = response.choices[0].message.content
#         cache[cache_key] = response_text
#         save_cache(cache)

#     with open(overview_path, "w") as f:
#         f.write(response_text)

#     print(f"✅ Created overview.md for {slug}")

########################################################
# Main Logic
########################################################

def main():
    print("Fetching codecs.json ...")
    resp = requests.get(CODECS_JSON_URL)
    resp.raise_for_status()
    codecs_data = resp.json()

    # We'll build a fresh sensors dict
    sensors_data = {}

    # Create the sensors folder if it doesn’t exist
    os.makedirs(SENSORS_ASSETS_PATH, exist_ok=True)

    # If using GPT, load cache (commented out)
    # cache = load_cache()

    for codec in codecs_data:
        raw_name = codec["name"]  # e.g. "MILESIGHT - Em300 Mcs"
        slug = slugify(raw_name)  # e.g. "milesight-em300-mcs"

        sensor_folder = os.path.join(SENSORS_ASSETS_PATH, slug, "en")
        os.makedirs(sensor_folder, exist_ok=True)

        sensor_entry = {
            "name": raw_name,
            "description": codec.get("description", ""),
            "vendor": codec.get("vendor", ""),
            "technology": codec.get("technology", ""),
            "imageUrl": codec.get("image", None),
        }

        # Write a metadata.md5 so we can track changes if desired
        metadata_hash = get_md5_hash(sensor_entry)
        hash_file_path = os.path.join(sensor_folder, "metadata.md5")
        with open(hash_file_path, "w") as f:
            f.write(metadata_hash)

        # Place sensor_entry in sensors_data under slug
        sensors_data[slug] = sensor_entry

        # --------------------------------------------
        # OPTIONAL: Generate GPT-based overview
        # --------------------------------------------
        # generate_overview(slug, sensor_folder, raw_name, sensor_entry["vendor"], cache)

    # Save sensors_data as JSON
    with open(SENSORS_JSON_PATH, "w") as f:
        json.dump(sensors_data, f, indent=2)

    commit_to_github(
        file_path=SENSORS_JSON_PATH,
        commit_message="Rebuilt slug-based sensors.json (OpenAI calls currently disabled)."
    )
    print("✅ Done! Created slug-based sensors.json (no GPT usage).")

if __name__ == "__main__":
    main()
