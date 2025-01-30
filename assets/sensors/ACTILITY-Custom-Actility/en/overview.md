# Technical Overview: ACTILITY - Custom Actility

## Introduction

ACTILITY - Custom Actility devices are highly versatile sensors designed for integration within IoT (Internet of Things) ecosystems. Leveraging LoRaWAN (Long Range Wide Area Network) technology, these devices are ideal for applications requiring remote monitoring and data transmission over wide areas. This document provides an in-depth technical overview of their working principles, installation procedures, LoRaWAN capabilities, power consumption profiles, potential use cases, and limitations.

## Working Principles

The Custom Actility sensors operate by detecting environmental parameters such as temperature, humidity, pressure, and more, depending on the model. These parameters are measured using highly sensitive and calibrated sensing elements, producing analog or digital signals. The sensor signals are then processed through an onboard microcontroller, which formats the data for transmission.

Data transmission utilizes LoRaWAN, a low-power, wide-area networking protocol designed for IoT devices. LoRaWAN enables long-range communication, making it suitable for applications where infrastructure might be sparse or challenging.

### Core Components

- **Sensor Module**: Measures the specific parameters.
- **Microcontroller Unit (MCU)**: Processes sensor data and controls communication.
- **LoRa Transceiver**: Handles wireless communication over the LoRaWAN network.
- **Power Supply**: Typically battery-operated for low power consumption.

## Installation Guide

1. **Site Assessment**: Identify optimal sensor placement to ensure reliable data collection and transmission. Consider environmental factors and potential obstructions.
   
2. **Mounting**: Securely mount the ACTILITY sensor using provided fixtures. Ensure the sensor is positioned to have minimal physical interference and exposure to the elements, depending on its intended application.
   
3. **Powering**: Insert batteries or connect the sensor to a suitable power source. Ensure compatibility with the specified voltage and current requirements.
   
4. **Configuration**: Use the proprietary Actility configuration tool to set up the sensor parameters and network settings. This typically involves connecting the sensor to a computer via USB or wirelessly via a setup application.
   
5. **Connection to Network**: Register and activate the device on the LoRaWAN network. This requires inputting the device's specific identifiers such as the DevEUI, AppEUI, and AppKey into the network server.

6. **Calibration**: If necessary, calibrate the sensors according to the manufacturer’s specifications to ensure accurate readings.

7. **Testing**: Verify the system's operational status by performing a test run to check data transmission and signal strength.

## LoRaWAN Details

- **Frequency Bands**: Typically operates in ISM bands (e.g., EU863-870, US902-928, etc.), subject to regional regulations.
- **Class Types**: Supports Class A and Class C device classes for bidirectional communication, optimizing for power savings (Class A) and minimal latency (Class C).
- **Data Encryption**: Utilizes AES-128 encryption ensuring secure transmission of data across the network.
- **Range**: Capable of communicating up to 15 kilometers in rural areas and 2-5 kilometers in dense urban environments.
- **Scalability**: Supports thousands of devices within a single network gateway, facilitating extensive IoT deployments.

## Power Consumption

ACTILITY sensors are designed for low-power operation, exploiting the LoRaWAN protocol's low bandwidth and low power characteristics:

- **Energy-saving Mode**: Engages during periods of inactivity, significantly reducing power draw.
- **Battery Life**: Depending on usage, battery life can extend from months to several years. Typical estimations are calculated based on transmission intervals and environmental factors affecting battery efficiency.
- **Power Alert Feature**: Built-in alerts notify users when battery levels are low, ensuring maintenance can be scheduled proactively.

## Use Cases

- **Environmental Monitoring**: Gather data on weather, atmospheric pollutants, and more, useful in agricultural and environmental research settings.
- **Smart Cities**: Manage and monitor city utilities, including water levels and waste management systems remotely.
- **Industrial IoT**: Oversee equipment health and performance in factories by transmitting sensor data from machine components.
- **Asset Tracking**: Monitor valuable assets across expansive areas with minimal infrastructure requirements.
- **Smart Buildings**: Optimize energy use and occupancy comfort through automated HVAC controls and space utilization metrics.

## Limitations

- **Network Dependency**: Requires a compatible LoRaWAN network, which may not cover all regions without deploying additional infrastructure.
- **Data Rate**: Suited for applications with low to moderate data rates. High-frequency and high-volume data collection could be constrained by bandwidth limits.
- **Latency**: While suitable for most monitoring applications, LoRaWAN may introduce latency unsuitable for real-time critical applications.
- **Environmental Factors**: The performance of wireless communication can be degraded by dense building materials, interference, or extreme weather conditions.
- **Battery Dependency**: Despite long battery life, environments with extreme temperatures might impact battery efficiency and longevity.

## Conclusion

ACTILITY's Custom Actility sensors represent a robust solution for deploying connected IoT systems across diverse locations. Their integration into LoRaWAN networks allows for long-distance, secure, low-power communications, highly suitable for environmental monitoring, industrial applications, and beyond. However, it is important to consider network availability, data rate requirements, and environmental conditions to maximize their effectiveness and longevity.