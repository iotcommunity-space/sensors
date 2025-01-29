# ADVANTECH Wise 2410 - LoRaWAN IoT Sensor Technical Overview

## Introduction
The ADVANTECH Wise 2410 is a LoRaWAN-enabled IoT sensor designed to monitor tension in cables and wires. Leveraging the cutting-edge Long Range Wide Area Network (LoRaWAN) technology, the Wise 2410 is ideal for applications in structural health monitoring of bridges, elevators, cranes, and other cable-based structures. This document provides a comprehensive overview of the working principles, installation guidelines, technical specifications, power consumption, use cases, and limitations of the Wise 2410 sensor.

## Working Principles
The Wise 2410 sensor operates by detecting changes in the magnetic field caused by the strain in metal cables. The sensor uses a Hall effect-based methodology to accurately measure the tension in any ferrous (iron-based) cable. As tension in the cable increases, subtle changes in the magnetic field around it are detected and measured by the sensor. These measurements are then processed and transmitted over the LoRaWAN network to a central monitoring system for analysis.

## Installation Guide
### Requirements
- LoRaWAN Gateway within range
- Installation clamps or harness
- Standard toolset (wrenches, screwdriver)

### Steps
1. **Site Preparation**: Identify the exact location on the cable where tension needs to be monitored. Ensure the installation spot is clean and accessible.
2. **Mounting the Sensor**: Attach the sensor securely onto the cable using the provided clamps or a suitable harness. Ensure the sensor is firmly fixed and that the Hall effect probe is aligned parallel to the cable.
3. **Configuring the Sensor**: Power on the device and configure it using either NFC (Near Field Communication) or a connected mobile device. The primary parameters to set include network ID, data reporting intervals, and threshold values for alerts.
4. **Connecting to LoRaWAN**: Establish a connection between the sensor and the nearest LoRaWAN gateway. This involves entering the device’s unique ID into the LoRaWAN network server.
5. **Testing and Verification**: Check the data transmission to the central system to ensure consistent and reliable reporting.

## LoRaWAN Details
- **Frequency**: Varies by region (e.g., EU868 MHz, US915 MHz)
- **Range**: 2-5 km urban, up to 15 km rural areas
- **Battery Life**: Typically 3-5 years, depending on transmission interval
- **Data Rate**: Adjustable, typically between 0.3 kbps and 50 kbps

## Power Consumption
The Wise 2410 is designed for low power consumption with a battery life of up to 5 years. It uses a Lithium battery and the consumption heavily depends on the data transmission interval, payload size, and network conditions. In a typical setup with an hourly data transmission, the sensor consumes approximately 2.5 µA in a sleep mode and about 120 mA during transmission.

## Use Cases
- **Structural Health Monitoring**: Monitoring tension in support cables of bridges, architectural structures, and large tents.
- **Elevator Cable Safety**: Ensuring that elevator cables maintain acceptable tension levels, contributing to safety and maintenance.
- **Heavy Machinery**: Monitoring tension in cables used in cranes, hoists, and other lifting equipment.

## Limitations
- **Magnetic Interference**: The sensor can be affected by external magnetic fields, which may cause inaccurate readings.
- **Material Compatibility**: Only suitable for use with ferrous cables.
- **Environmental Constraints**: Performance can degrade under extreme environmental conditions such as temperatures below -20°C or above 50°C, and in highly corrosive or saline environments.

## Conclusion
The ADVANTECH Wise 2410 LoRaWAN IoT Sensor is an advanced, reliable solution for cable tension monitoring in myriad applications where safety and maintenance are critical. By following the detailed installation guide and considering its specific limitations, users can effectively implement this technology to enhance monitoring and predictive maintenance capabilities.