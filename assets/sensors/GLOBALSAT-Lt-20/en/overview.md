# Technical Overview for GLOBALSAT - LT-20 LoRaWAN Tracker

## Introduction
The GLOBALSAT LT-20 is a robust GPS tracking device designed for various applications, featuring long-range wireless communication capabilities via the LoRaWAN protocol. Ideal for asset tracking and monitoring applications, the LT-20 merges cutting-edge GPS technology with the efficiency and low power consumption of LoRaWAN networks.

## Working Principles
The GLOBALSAT LT-20 operates by determining its location through a GNSS (Global Navigation Satellite System) module. This module receives satellite signals to triangulate the exact geographic position. The device then transmits this data using LoRaWAN, a Low Power Wide Area Networking protocol optimized for wireless battery-operated things in regional, national, or global networks. This process allows location data to be sent to remote servers for further processing and analytics.

## Installation Guide

### Package Contents
- LT-20 device
- Installation manual

### Installation Steps
1. **Charge the Device**: Ensure that the internal battery is fully charged using the provided charging method. The LT-20 may have a USB charging option.
2. **Activate the Device**: Power on the LT-20 by pressing and holding the designated power button until the device indicates successful activation via LED or a similar mechanism.
3. **Configuration**: Using the GLOBALSAT configuration tool or web interface, configure the device's LoRaWAN settings (e.g., frequency plans, data rate, and dual-layer encryption keys: Network Session Key (NwkSKey) and Application Session Key (AppSKey)).
   - Set the device to the correct regional frequency plan.
   - Ensure that it joins the correct LoRaWAN network by inputting necessary IDs (e.g., Device EUI and AppEUI).
4. **Secure Placement**: Place the LT-20 on the asset to be tracked. It should be mounted in a location with good visibility to the sky for GPS reception.
5. **Test Operation**: Validate device operation by checking connectivity to the network server and ensuring position data is correctly transmitted to your IoT platform.

## LoRaWAN Details

- **Frequency Bands**: The LT-20 is designed to operate in various licensed ISM frequency bands such as EU868, US915, AS923, AU915, etc. Its flexibility enables it to be used globally with minimal adjustments.
- **Network Performance**: Supports ADR (Adaptive Data Rate) for optimized performance and battery life, with data rates ranging from 0.3 kbps to 50 kbps.
- **Security**: Uses end-to-end encryption to secure data packets during transmission, ensuring the integrity and confidentiality of location data.

## Power Consumption

The LT-20 is powered by a rechargeable lithium battery optimized for extended use. The power consumption breakdown includes:
- GNSS Operation: Moderate energy use when actively acquiring satellite signals.
- LoRaWAN Transmission: Low energy use, designed to support long battery life through periodic data transmission.
- Standby Mode: Ultra-low power consumption when the device is idle, extending battery life significantly.

## Use Cases

- **Asset Tracking**: Ideal for tracking high-value assets in logistics and supply chains.
- **Fleet Management**: Effective in managing and monitoring vehicle fleets in real-time.
- **Agriculture and Environmental Monitoring**: Suitable for tracking livestock and ensuring geofenced operations in outdoor and agricultural setups.
- **Safety and Security**: Used for personal safety applications to track individuals in remote and hazardous locations.

## Limitations

- **Line-of-Sight Limitations**: The GPS reception may be impaired in dense urban environments, indoors, or areas with heavy foliage, reducing positional accuracy.
- **LoRaWAN Range Dependency**: Effective communication range can vary based on environmental factors, network infrastructure, and geographic location.
- **Battery Limitations**: While optimized for low consumption, the lifespan between charges can reduce significantly with frequent data transmission and poor GPS signal conditions.
- **Non-Real-Time Data**: Due to the nature of LoRaWAN, the LT-20 is not suitable for applications requiring real-time data streaming.

The GLOBALSAT LT-20 combines reliable tracking capabilities with the efficiency of LoRaWAN, making it a valuable tool for a wide range of IoT tracking applications. Ensuring optimal installation and configuration will maximize its performance and longevity.