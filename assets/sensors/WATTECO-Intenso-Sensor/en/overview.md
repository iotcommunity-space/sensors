# Technical Overview of WATTECO Intenso Sensor

The WATTECO Intenso Sensor is a versatile and robust device designed for efficient energy monitoring in both residential and industrial settings. It utilizes LoRaWAN technology for communication, ensuring long-range and low-power data transmission capabilities. This document provides a comprehensive overview of the sensor's working principles, installation guide, communication details, power consumption, potential use cases, and limitations.

## Working Principles

The Intenso Sensor primarily measures electrical parameters such as voltage, current, and power consumption. It operates by interfacing with existing electrical systems through non-intrusive current transformers (CTs) that clamp around electrical conductors. These are connected to the sensor unit which processes the analog signals into digital form, which are then transmitted via LoRaWAN.

### Key Features
- **Current and voltage sensing**: Measures AC current and voltage across multiple channels.
- **Real-time data processing**: Converts analog signals to digital data for real-time monitoring.
- **Wireless Communication**: Utilizes LoRaWAN for efficient data transmission over long distances.

## Installation Guide

### Pre-Installation Checks
1. **Compatibility:** Ensure compatibility with the target electrical system's voltage and current ratings.
2. **Safety**: Verify compliance with safety standards and procedures to prevent electrical hazards.

### Installation Steps
1. **Power Off:** Before installation, ensure the electrical system is powered off.
2. **Mounting:** Securely mount the Intenso Sensor close to the electrical panel using screws or adhesive mounting solutions provided in the package.
3. **CT Clamping:** Attach the current transformers around the conductors of the circuits to be monitored, ensuring a snug and secure fit.
4. **Connecting the Sensor:** Connect the CTs to the sensor unit using the provided input terminals.
5. **Power On and Commissioning:** Power on the system and configure the sensor via the designated setup interface or mobile application, linking it to the LoRaWAN network.

## LoRaWAN Details

The Intenso Sensor supports LoRaWAN Class A protocol, allowing it to join LPWAN networks for optimized resource usage.

### Network Requirements
- **Frequency Bands**: Operates on standard LoRaWAN frequencies such as EU868, US915, or AS923, depending on regional regulations.
- **Data Rate**: Supports adaptive data rate (ADR) to optimize data transmission in varying network conditions.

### Configuration
- **Join Process**: Can be configured via OTAA (Over-The-Air Activation) or ABP (Activation By Personalization).
- **Data Encryption**: Ensures secure data transmission with end-to-end AES-128 encryption.

## Power Consumption

The Intenso Sensor is designed for low power consumption to maximize battery life. It employs an energy-efficient microcontroller and operates primarily in sleep mode, waking up only to capture and transmit data.

### Battery Life
- **Estimated Life**: Up to 10 years based on typical use scenarios with data transmission intervals set to 15 minutes.
- **Battery Type**: Powered by replaceable lithium batteries, typically a 3.6V AA or similar.

## Use Cases

The Intenso Sensor is ideal for multiple applications, including:
- **Residential energy monitoring**: Enable homeowners to observe real-time energy consumption trends and identify opportunities for energy savings.
- **Industrial energy management**: Monitor critical equipment and process energy consumption to optimize operational efficiency.
- **Preventive maintenance**: Detect abnormal electrical patterns indicative of equipment failure.
- **Smart grid applications**: Integrate with broader smart grid initiatives to enhance overall energy distribution and management.

## Limitations

While the Intenso Sensor provides significant advantages, there are limitations to be considered:
- **Interference**: Performance can be affected by electromagnetic interference from nearby devices or appliances.
- **Range Limitations of LoRaWAN**: While LoRaWAN provides long-range coverage, obstacles such as buildings or natural features can impact signal penetration and data transmission reliability.
- **Installation Complexity**: Improper installation or configuration may result in inaccurate readings or suboptimal performance.
- **Data Resolution**: Depending on setup, the granularity of recorded data might not suffice for very high-resolution power analysis.

For optimal performance, adherence to proper installation guidelines and consideration of the potential environmental factors affecting LoRaWAN transmission are essential.