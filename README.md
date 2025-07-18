# IoT Community Sensors Directory

This repository serves as the primary data store for the IoT Community sensors directory and their companion devices, accessible at [iotCommunity.space/sensors](https://iotCommunity.space/sensors).

## Overview

The IoT Community Sensors Directory is a comprehensive database of IoT sensors and companion devices used across various IoT projects and implementations. This repository maintains the data structure and information that powers the directory website.

**🤖 Automated Data Sync**: This repository automatically syncs sensor data from our codec registry daily, ensuring up-to-date information while preserving manual corrections.

## Data Structure

The sensor data is stored in a single `sensors.json` file with the following structure:

```json
{
  "Sensor Name": {
    "Description": "Detailed sensor description",
    "Communication": "Communication protocol used",
    "Applications": ["Application 1", "Application 2"],
    "Environmental Compatibility": "Usage environment details",
    "Data Formats": ["Format 1", "Format 2"],
    "Technology": "Underlying technologies",
    "Cost": "Cost category",
    "Vendor": "Manufacturer name",
    "imageUrl": "URL to sensor image (optional)",
    "slug": "auto-generated-slug"
  }
}
```

### Required Fields

Each sensor entry must include:
- Description
- Communication
- Applications (array)
- Environmental Compatibility
- Data Formats (array)
- Technology
- Cost
- Vendor

The `imageUrl` field is optional but recommended. The `slug` field is auto-generated for URL-friendly references.

## Automated Synchronization

This repository uses GitHub Actions to automatically sync sensor data from our codec registry:

- **Schedule**: Daily at midnight UTC
- **Source**: [IoT Community Codec Registry](https://github.com/iotcommunity-space/codec)
- **Process**: Fetches latest sensor data, generates technical overviews, and updates the directory
- **Protection**: Manual corrections are preserved using protection mechanisms

### Manual Override System

To protect your manual corrections from being overwritten by automation:

#### Method 1: Manual Edit Flag
Add `"_manual_edit": true` to any sensor entry you've manually corrected:

```json
{
  "Your Sensor Name": {
    "Description": "Your corrected description",
    "Communication": "LoRaWAN",
    "Cost": "Your updated cost",
    "_manual_edit": true
  }
}
```

#### Method 2: Manual Flag File
Create a `manual.flag` file in the sensor's assets folder:
```bash
touch assets/sensors/vendor-slug/sensor-slug/en/manual.flag
```

#### Method 3: Manual Overrides File
Create `assets/manual_overrides.json` for centralized overrides:
```json
{
  "Sensor Name": {
    "Description": "Your corrected description",
    "Cost": "Your corrected cost",
    "custom_notes": "Any additional fields"
  }
}
```

## Contributing

### For New Sensors
1. Add sensor data to the [IoT Community Codec Registry](https://github.com/iotcommunity-space/codec)
2. The automation will automatically sync it to this repository within 24 hours
3. Alternatively, manually add to `sensors.json` following the data structure above

### For Corrections to Existing Sensors
1. Fork this repository
2. Create a new branch (`git checkout -b fix-sensor-data`)
3. Modify the `sensors.json` file with your corrections
4. **Important**: Add `"_manual_edit": true` to protect your changes from automation
5. Validate your JSON before submitting
6. Submit a Pull Request

### Example Entry

```json
"LHT65N-VIB -- LoRaWAN Vibration Sensor": {
  "Description": "LoRaWAN protocol for detecting vibration and runtime. Includes temperature & humidity sensors.",
  "Communication": "LoRaWAN",
  "Applications": ["Smart Agriculture", "Industrial Monitoring"],
  "Environmental Compatibility": "Outdoor use, IP-rated",
  "Data Formats": ["JSON", "MQTT"],
  "Technology": "LoRaWAN End node",
  "Cost": "Affordable",
  "Vendor": "Dragino",
  "imageUrl": "https://dragino.com/media/k2/items/cache/3abb66d58aa91d2b7b16f08ee38a95c0_L.jpg",
  "slug": "lht65n-vib-lorawan-vibration-sensor"
}
```

## Repository Structure

```
├── assets/
│   ├── sensors.json              # Main sensor database
│   ├── manual_overrides.json     # Manual corrections (optional)
│   ├── cached_overviews.json     # Cached AI-generated content
│   └── sensors/                  # Individual sensor documentation
│       └── vendor-slug/
│           └── sensor-slug/
│               └── en/
│                   ├── overview.md    # Technical overview
│                   ├── metadata.md5   # Change tracking
│                   └── manual.flag    # Manual protection (optional)
├── .github/
│   ├── workflows/
│   │   └── sync-sensors.yml      # Automation workflow
│   └── scripts/
│       └── sync_sensors.py       # Sync script
└── README.md
```

## Data Validation

We provide a JSON schema for validating sensor entries. All submissions must pass schema validation before being accepted. The automation includes built-in validation to ensure data integrity.

## Automation Details

### GitHub Actions Workflow
- **Trigger**: Daily cron job + manual dispatch
- **Process**: Fetches codec data, generates overviews, updates sensors.json
- **Protection**: Preserves manual corrections and existing overview.md files
- **Logging**: Comprehensive logging for debugging and monitoring

### Environment Variables Required
- `SENSOR_TOKEN`: GitHub token for repository access
- `AC_TOKEN`: API key for generating technical overviews

## Troubleshooting

### My Manual Changes Were Overwritten
1. Check if you added `"_manual_edit": true` to your sensor entry
2. Verify the automation logs in GitHub Actions
3. Create a manual.flag file for complete protection
4. Submit an issue if problems persist

### Sensor Not Updating
1. Verify the sensor exists in the codec registry
2. Check if a manual.flag file exists
3. Review GitHub Actions logs for errors
4. Ensure the sensor name format matches exactly

## License

This repository and its contents are licensed under the MIT License. See [LICENSE](LICENSE) file for details.

## Contact

For questions, suggestions, or support:
- [Join our Discord Community](https://iotCommunity.space/discord)
- [Submit an Issue](https://github.com/iotcommunity-space/sensors/issues)
- Email: support@iotCommunity.space

## Additional Resources

For more information about the IoT Community and our projects, please visit:
- [Project About Page](https://iotCommunity.space/about)
- [Developer Documentation](https://docs.iotCommunity.space)
- [Community Guidelines](https://iotCommunity.space/guidelines)
- [Codec Registry](https://github.com/iotcommunity-space/codec) - Source data for sensor information
