# Technical Overview for Custom Myriota (MYRIOTA) Sensor

## Introduction

The Custom Myriota sensor is an advanced device designed for reliable and efficient IoT communication, leveraging Myriota's innovative satellite communication technology. It is optimized for remote and challenging environments where traditional network connectivity is unavailable or unreliable. This sensor facilitates low-cost, low-power, and secure global data transfer suitable for a variety of applications.

## Working Principles

The Custom Myriota sensor operates by harnessing Myriota’s direct-to-satellite technology, enabling devices to send small packets of data from anywhere on Earth. This technology is built on a store-and-forward message delivery principle, where data from sensors is stored temporarily and later transmitted to satellites passing overhead. The data is then relayed to ground stations and subsequently to the cloud for access and processing by end-users. Myriota’s technology is specifically designed for uplink communication, optimized for low bitrate and sporadic transmissions to maximize battery life and minimize costs.

## Installation Guide

1. **Site Survey and Preparation:**
   - Conduct a thorough site survey to ensure clear line of sight to the sky for optimal satellite communication.
   - Select a stable location to mount the device, avoiding obstructions like thick vegetation or tall structures.

2. **Mounting the Device:**
   - Use the provided mounting brackets and hardware to securely attach the device to a pole, wall, or another stable structure.
   - Ensure the sensor is oriented correctly (as per device specifications) for optimal connectivity.

3. **Power Connection:**
   - Connect the sensor to its power source. If using solar power, ensure solar panels are exposed to maximum sunlight.

4. **Initial Setup:**
   - Use a compatible configuration tool or software interface to program the sensor with necessary parameters (e.g., data transmission intervals, sensor calibration factors).
   - Verify connectivity by checking the initial transmission and reception of data through the monitoring platform.

5. **Testing and Calibration:**
   - Conduct initial tests to ensure the data is being sent and received as expected.
   - Calibrate the sensor according to the specific application and environmental conditions.

## LoRaWAN Details

While Myriota's technology primarily uses direct-to-satellite communication, integration with LoRaWAN is possible for specific applications requiring LoRa-based sensors. In such cases, the Myriota sensor acts as a gateway, collecting data from local LoRaWAN devices and transmitting it back through the satellite network.

- **Frequency Bands:** Depends on the regional specifications for LoRaWAN integration (EU868, US915, etc.).
- **Network Integration:** The sensor can be set up to support LoRaWAN data acquisition and forward the aggregated data via satellite communication to the cloud.

## Power Consumption

The Custom Myriota sensor is designed for ultra-low power consumption, a critical feature for remote deployments with limited access to power sources:

- **Average Power Consumption:** Typically ranges from 1 to 10 microamperes in idle mode, depending on the configuration and transmission schedule.
- **Transmission Power:** ~100mW during data uplink.
- **Battery Life:** Depending on usage, device configuration, and power source, the battery life can extend over several years.

## Use Cases

- **Remote Environmental Monitoring:** Ideal for monitoring weather stations, water levels in remote rivers, or soil moisture in agricultural fields.
- **Asset Tracking:** Fits asset tracking applications for industries like oil & gas, mining, and logistics where real-time tracking is crucial.
- **Wildlife Monitoring:** Used for tracking migration patterns and behavior of wildlife in remote conservation areas where cellular networks do not reach.
- **Infrastructure Integrity Monitoring:** For the monitoring of critical infrastructure such as pipelines and railways in remote areas, enabling timely maintenance actions.

## Limitations

- **Data Throughput:** Due to the low-bandwidth nature of Myriota’s satellite communication, the sensor is best suited for applications with small data packets and infrequent transmissions.
- **Latency:** The store-and-forward system may introduce latency depending on satellite pass schedules, which may not be suitable for real-time applications.
- **Coverage:** While Myriota provides global coverage, the efficiency of data transmission can vary based on satellite passes, which are not continuous in any given location.
- **Environmental Constraints:** Performance can be affected by extreme environmental conditions such as heavy storms or dense forest canopies obstructing satellite line-of-sight.

By leveraging Myriota’s unique technology, these sensors empower industries and conservation efforts to function in untapped areas, expanding the horizons of IoT connectivity.