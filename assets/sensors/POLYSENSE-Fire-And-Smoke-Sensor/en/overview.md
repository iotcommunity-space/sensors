# Technical Overview for POLYSENSE Fire And Smoke Sensor

## 1. Introduction
The POLYSENSE Fire and Smoke Sensor is designed to provide early fire detection with wireless connectivity, making it suitable for remote and inaccessible areas. Utilizing LoRaWAN technology, the sensor offers reliable communication over long distances with excellent power efficiency. 

## 2. Working Principles
### 2.1 Smoke Detection
The POLYSENSE sensor employs optical detection techniques to identify smoke particles in the air. Using a photoelectric chamber, it detects changes in light patterns caused by the presence of smoke particles, which scatter the chamber's light beam and trigger an alert when a threshold is exceeded.

### 2.2 Fire Detection
Designed for fire detection, the sensor also incorporates a heat detection mechanism which triggers an alarm if the ambient temperature exceeds a predefined threshold. This dual-detection mechanism reduces false alarms and enhances the reliability of the device in fire and smoke detection.

## 3. Installation Guide
### 3.1 Pre-installation Checklist
- Ensure the sensor is supported by a local LoRaWAN network.
- Verify the battery is charged or replaced with a new one.
- Confirm device ID and registration with the network server for activation.

### 3.2 Mounting Positions
- Position the sensor at ceiling level for optimal smoke detection, approximately 12 inches away from the corner where the wall meets the ceiling.
- Avoid installing the sensor near ventilation ducts, ceiling fans, or any location where smoke may not reach rapidly.

### 3.3 Activation Procedure
- Register the device with the LoRaWAN network using the device EUI and appropriate keys.
- Perform a smoke test to ensure proper functionality by using test aerosols designed for smoke detectors.
- Confirm the LED indicator functionality to verify power and operational status.

## 4. LoRaWAN Details
### 4.1 Network Configuration
- Operates on standard LoRaWAN frequencies (e.g., EU868/US915), providing a robust range up to several kilometers depending on the environment.
- Supports adaptive data rate (ADR) to optimize communication efficiency and battery usage.

### 4.2 Communication
- Utilizes Class A device specifications for optimal power consumption.
- Sends periodic status updates and triggers immediate alerts when smoke or heat detection exceeds set thresholds.

## 5. Power Consumption
The sensor is designed with energy optimization in mind:
- Powered by replaceable lithium batteries, offering up to 10 years of life under normal conditions.
- Sleep mode is automatically activated during inactivity to conserve energy, with an ultra-low standby current of less than 10 μA.

## 6. Use Cases
- **Residential Buildings**: Ensures fire and smoke detection in apartments and homes with simple installation.
- **Industrial Facilities**: Monitors smoke levels in factories and warehouses where traditional wiring is impractical.
- **Remote Areas**: Provides fire alert in isolated locations such as forests or national parks.
- **Historical Sites**: Protects valuable structures where non-invasive installation is crucial.

## 7. Limitations
- **Environmental Interference**: Smoke detection accuracy might be reduced in dusty or humid environments.
- **Network Dependency**: Requires a reliable LoRaWAN network for real-time alerts, limiting use in areas without network coverage.
- **Physical Barriers**: Dense structures can hinder radio signal penetration, affecting communication range.
- **Battery Temperature Sensitivity**: Extreme temperatures can affect battery performance and lifespan.

The POLYSENSE Fire and Smoke Sensor delivers reliable, long-distance fire detection via LoRaWAN, making it well-suited for a variety of applications. Proper installation and awareness of limitations ensure its optimal performance.