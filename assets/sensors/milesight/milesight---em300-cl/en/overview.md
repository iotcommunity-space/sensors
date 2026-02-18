# Technical Overview: MILESIGHT - EM300-CL

## Introduction

The MILESIGHT EM300-CL is a compact, wireless sensor designed specifically for detecting liquid levels and leaks in environments like data centers, warehouses, or telecommunication facilities. It utilizes advanced LoRaWAN technology to provide long-range wireless communication with low power consumption, making it ideal for IoT applications where consistent and reliable data communication is critical.

## Working Principles

The EM300-CL operates by detecting the presence of liquid using capacitive sensing. This non-contact method involves monitoring changes in capacitance caused by the presence of liquid near the sensor's electrodes. The sensor translates these capacitance changes into electrical signals that can be wirelessly transmitted through LoRaWAN networks. This allows for precise and immediate alerts in the event of a water level change or leak detection.

## Installation Guide

### Pre-installation Steps

1. **Unpacking**: Carefully unpack the sensor and check for any physical damage.
   
2. **Inspecting Components**: Ensure all components including mounting hardware and sensor cable are included.

### Installation

1. **Location Selection**: Choose an area where leaks or water level changes are most likely to occur. Avoid locations with excessive electrical noise.

2. **Mounting**: Use the included mounting hardware to secure the sensor in place. Ensure that it is placed horizontally on a flat, stable surface.

3. **Connection**: For optimal performance, ensure proper connection between the sensor’s probe and main device. Follow any wiring instructions if applicable.

4. **Configuration**: Configure the sensor via NFC or USB interface using the relevant MILESIGHT software tools to ensure accurate data reporting.

5. **Network Setup**: Pair the sensor with your LoRaWAN network by entering its unique keys and identifiers into your network server software.

### Calibration

Perform sensor calibration according to the manufacturer’s instructions to ensure accurate liquid level measurements.

## LoRaWAN Details

- **Frequency Bands**: The EM300-CL supports various frequency bands, including EU868, US915, and others depending on region-specific regulations.
- **Class**: Operates as a Class A or Class C device, providing bi-directional communication.
- **Output Power**: Adjustable transmission power levels to optimize battery life and range.
- **Data Rate**: Adaptive data rate (ADR) to maintain efficient communication regardless of network conditions.

## Power Consumption

The EM300-CL is designed for low power consumption, maximizing the operational lifespan on battery power:

- **Standby Mode**: Consumes minimal power when inactive, ensuring long battery life.
- **Active Mode**: Significantly more efficient compared to traditional wireless technologies, with power usage adapted based on data transmission frequency.

Typical battery life ranges from 2 to 5 years depending on the frequency of reported events and environmental condition impacts.

## Use Cases

1. **Data Centers**: Monitor for server water cooling leaks, safeguarding against equipment failures.
2. **Warehouses**: Ensure early detection of pipe leaks, preventing property and goods damage.
3. **Telecommunication Facilities**: Monitor moisture levels to protect critical networking hardware.
4. **Smart Building Monitoring**: Integrate into a comprehensive building management system for proactive facility maintenance.

## Limitations

- **Interference**: The sensor might be susceptible to electromagnetic interference in highly industrial environments.
- **Calibration Sensitivity**: Requires careful calibration, especially in environments with varied humidity levels.
- **Coverage**: Effective range depends on environmental obstructions, which may affect LoRaWAN signal penetration.
- **Battery Life Variability**: The operational period on a single battery can vary significantly depending on data reporting intervals and environmental conditions.

The MILESIGHT EM300-CL is a robust choice for remote leak detection and liquid monitoring. Its use of LoRaWAN technology ensures wide coverage and low operational costs, though users should be mindful of its calibration needs and potential environmental limitations.