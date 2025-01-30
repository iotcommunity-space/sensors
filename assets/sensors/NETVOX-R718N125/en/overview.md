# NETVOX R718N125 Technical Overview

## Introduction
The NETVOX R718N125 is a LoRaWAN ultrasonic level sensor that is designed for remote level monitoring in various applications. It employs LoRaWAN technology to transmit data over long distances with low power consumption, making it ideal for use in smart agriculture, industrial tanks, waste management, and other IoT applications requiring level measurement.

## Working Principles
The NETVOX R718N125 uses ultrasonic technology to measure the distance from the sensor to the surface of a liquid or solid. The sensor emits ultrasonic pulses, and then calculates the time taken for the pulse to reflect back. This time measurement is directly proportional to the distance to the target surface, allowing the sensor to determine the level of the material being measured.

### Key Features
- **Ultrasonic Level Detection**: Measures distances with high accuracy using ultrasonic sound waves.
- **LoRaWAN Connectivity**: Utilizes LoRaWAN protocol for long-range, low-power wireless communication.
- **Configurable Parameters**: Allows for adjustments in measurement range and data transmission intervals.
- **Low Power Consumption**: Designed for extended battery life, making it suitable for remote deployments.
- **Weatherproof Design**: Suitable for outdoor and harsh environmental conditions.

## Installation Guide
1. **Placement**: Mount the sensor in a stable position directly above the target surface to ensure accurate measurement. Ensure there is a clear path for the ultrasonic signal without obstructions.
2. **Mounting**: The sensor should be securely attached to avoid vibrations which could affect measurements. Use appropriate brackets or supports depending on the installation environment.
3. **Power Supply**: Install batteries according to the device specifications. Ensure that connections are clean and secure.
4. **Configuration**: Use the provided documentation and tools to configure measurement parameters such as detection range and reporting intervals.
5. **Testing**: After installation, perform tests to verify the accuracy and reliability of the level measurements.
6. **Connectivity Check**: Ensure the LoRaWAN network connection is functioning correctly and that the device is communicating with the gateway.

## LoRaWAN Details
- **Frequency Band**: The R718N125 operates in various ISM bands depending on regional regulations, typically in the 868MHz or 915MHz frequency bands.
- **Transmission Power**: Complies with local regulatory requirements, typically up to +22 dBm.
- **Network Join Procedure**: Supports Over-The-Air Activation (OTAA) and Activation by Personalization (ABP).
- **Data Rate**: Adaptive data rate (ADR) settings can be optimized based on network configurations and environmental factors.
- **Encryption**: All communication is secured using AES-128 encryption to protect data transmission over the network.

## Power Consumption
The R718N125 is designed to be power efficient, making it an ideal choice for battery-powered IoT applications. Power consumption varies based on configurations such as the reporting interval, with long intervals leading to reduced power use. Typical battery life extends up to several years under normal operating conditions.

## Use Cases
- **Agriculture**: Monitoring water levels in irrigation systems and reservoirs.
- **Industrial Tanks**: Measuring the level of chemicals, fuels, or liquids in storage tanks.
- **Waste Management**: Detecting fill levels in waste bins to optimize collection routes.
- **Flood Monitoring**: Providing early warnings by monitoring water levels in flood-prone areas.

## Limitations
- **Range Limitations**: The effective measurement range may be limited by environmental factors, such as the presence of foam on liquid surfaces or extreme angles.
- **Obstacles**: Physical obstructions between the sensor and the measured surface can affect accuracy. Careful placement is required.
- **Environmental Conditions**: While designed for outdoor use, extreme weather conditions might affect longevity and accuracy.
- **Deployment Area**: The LoRaWAN network's coverage is necessary for operation, so areas without sufficient network presence may hinder data transmission.

Overall, the NETVOX R718N125 offers reliable level measurement capabilities for a wide range of applications, leveraging the efficient communication offered by the LoRaWAN protocol to provide continuous monitoring with minimal maintenance.