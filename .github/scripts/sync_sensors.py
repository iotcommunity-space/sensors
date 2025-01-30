#!/usr/bin/env python3
import os
import re
import shutil

# Where your old sensor folders live
OLD_SENSORS_PATH = "assets/sensors"

def slugify(text: str) -> str:
    """
    Convert something like 'ABEEWAY - Compact Tracker' -> 'abeeway-compact-tracker'.
    """
    text = text.lower().replace(" ", "-")
    text = re.sub(r"[^a-z0-9-]+", "", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")

def main():
    """
    Walk the old sensor structure, look for 'VendorName/VendorName - Sensor/en/overview.md'.
    Then move them to 'assets/sensors/<slug>/en/overview.md'.
    """
    # 1) Scan your vendor folders
    for vendor_dir in os.listdir(OLD_SENSORS_PATH):
        # e.g. 'ABEEWAY'
        vendor_path = os.path.join(OLD_SENSORS_PATH, vendor_dir)
        if not os.path.isdir(vendor_path):
            continue

        # 2) Inside each vendor, we might have subfolders like 'ABEEWAY - Compact Tracker'
        for sensor_dir in os.listdir(vendor_path):
            old_sensor_path = os.path.join(vendor_path, sensor_dir)
            if not os.path.isdir(old_sensor_path):
                continue

            # We only care if there's an 'en' folder
            en_path = os.path.join(old_sensor_path, "en")
            if not os.path.isdir(en_path):
                continue

            # 3) Slugify the sensor folder name
            # e.g. 'ABEEWAY - Compact Tracker' -> 'abeeway-compact-tracker'
            slug = slugify(sensor_dir)

            # 4) Build the new slug-based path
            new_slug_folder = os.path.join(OLD_SENSORS_PATH, slug, "en")
            os.makedirs(new_slug_folder, exist_ok=True)

            # 5) Move overview.md + metadata.md5 if present
            old_overview = os.path.join(en_path, "overview.md")
            old_metadata = os.path.join(en_path, "metadata.md5")

            new_overview = os.path.join(new_slug_folder, "overview.md")
            new_metadata = os.path.join(new_slug_folder, "metadata.md5")

            # If overview.md exists and not already moved
            if os.path.exists(old_overview):
                print(f"Moving {old_overview} -> {new_overview}")
                shutil.move(old_overview, new_overview)

            # If metadata.md5 exists
            if os.path.exists(old_metadata):
                print(f"Moving {old_metadata} -> {new_metadata}")
                shutil.move(old_metadata, new_metadata)

            # (Optional) If you want to remove the old sensor_dir after moving files, do so:
            # But first make sure it's empty
            try:
                os.removedirs(en_path)  # remove 'en' and parent if empty
            except OSError:
                pass  # if not empty, skip

def cleanup_empty_folders(folder_path):
    """
    Recursively remove empty folders if you'd like.
    """
    # If folder empty, remove
    # or else recursively check
    for root, dirs, files in os.walk(folder_path, topdown=False):
        if not dirs and not files:
            os.rmdir(root)

if __name__ == "__main__":
    main()
    # If you want to remove empty leftover vendor folders:
    # cleanup_empty_folders(OLD_SENSORS_PATH)
