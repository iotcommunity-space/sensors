# TEKTELIC Breeze Indoor Air Quality Co2 Sensor - Technical Overview

## Introduction
The TEKTELIC Breeze is an advanced Indoor Air Quality (IAQ) sensor specifically designed to monitor and report Carbon Dioxide (CO2) levels, along with other environmental parameters. This sensor employs LoRaWAN technology, which is ideal for low power, wide area networks (LPWANs). The device is compact, energy-efficient, and suitable for a variety of indoor environments.

## Working Principles

The TEKTELIC Breeze utilizes Non-Dispersive Infrared (NDIR) technology for CO2 measurement. The NDIR principle is based on the absorption of infrared light by CO2 molecules within the sensor's gas chamber. As the concentration of CO2 increases, it absorbs more infrared light, allowing the sensor to determine and report CO2 levels accurately.

Additionally, the sensor integrates other components to measure environmental parameters such as temperature, humidity, and Volatile Organic Compounds (VOCs), providing a comprehensive overview of indoor air quality.

**Key Specifications:**

- **CO2 Sensor Type**: NDIR
- **CO2 Measurement Range**: Typically 0 - 5000 ppm
- **Temperature Range**: Usually -10°C to +55°C
- **Humidity Range**: Generally 0 – 100% RH

## Installation Guide

### Pre-Installation Requirements
- Ensure LoRaWAN network coverage is available in the installation area.
- Acquire a network connection for data visualization or integration.

### Installation Steps

1. **Location Selection**: 
   - Mount the device at a height of 1.2 to 1.8 meters above the floor.
   - Avoid installing in close proximity to doors, windows, or any potential sources of direct airflow or chemicals.

2. **Mounting the Sensor**:
   - Use the provided screws and anchors to securely affix the sensor to a wall.
   - Ensure the sensor is mounted with clear access to ambient air without obstructions.

3. **Powering the Device**:
   - Connect the device to a power source if required, based on model (battery-powered or externally powered options may exist).

4. **Device Configuration**:
   - Power on the device and wait for the initialization sequence to complete.
   - Use TEKTELIC’s configuration software or app to set desired operational parameters and establish a connection to the LoRaWAN network.

## LoRaWAN Details

- **Network Compatibility**: Supports standard LoRaWAN specifications, typically up to version 1.0.4.
- **Frequency Bands**: Operates on commonly used ISM bands (e.g., EU868, US915) depending on regional regulations.
- **Data Rate and Payload**: Adaptive data rate (ADR) is supported to optimize the communication efficiency based on signal quality.
- **Range**: Typically, a range of up to 5 km in urban areas and 15 km in rural areas under optimal conditions.

## Power Consumption

- **Power Source**: Battery-powered versions use long-lasting lithium batteries. Externally powered options may be available.
- **Battery Life**: Depending on transmission intervals and environmental conditions, the sensor can achieve battery life ranging from 2 to 5 years.
- **Power Management**: Features low-power operation modes to conserve energy and extend battery life.

## Use Cases

The TEKTELIC Breeze is well-suited for various applications, including:

- **Commercial Buildings**: Monitoring and optimizing air quality for healthier indoor environments.
- **Educational Institutions**: Ensuring sufficient ventilation in classrooms to enhance student performance and well-being.
- **Healthcare Facilities**: Maintaining optimal air quality in hospitals and clinics to reduce airborne transmission of pathogens.
- **Industrial Settings**: Monitoring workspace air quality to comply with occupational safety regulations.

## Limitations

- **Network Dependency**: Relies on the availability of a LoRaWAN network, which might not be prevalent in certain remote areas.
- **Installation Constraints**: Requires careful placement to ensure accurate readings and avoid interference.
- **Environmental Factors**: High humidity and temperature extremes can potentially impact sensor performance and longevity.
- **Measurement Lag**: As with many CO2 sensors, rapid changes in CO2 levels might not be instantaneously detected due to diffusion time.

## Conclusion

The TEKTELIC Breeze Indoor Air Quality CO2 Sensor is a reliable, efficient tool for monitoring indoor air quality, leveraging LoRaWAN technology for extensive area coverage with minimal power consumption. Its ease of installation and broad application range make it a versatile addition to intelligent building systems and air quality management solutions.