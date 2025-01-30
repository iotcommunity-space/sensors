# Technical Overview: TTN Smart Sensor (Saninudge)

## Introduction

The TTN Smart Sensor by Saninudge is a cutting-edge IoT device designed to monitor hygiene compliance in healthcare settings. Utilizing the robust LoRaWAN network, this sensor ensures reliable, long-range data transmission with minimal power consumption. It primarily functions by detecting movement and usage patterns to help facilities maintain optimal sanitary conditions.

## Working Principles

The Saninudge TTN Smart Sensor operates based on several components:

1. **Motion Detection**: The sensor employs Passive Infrared (PIR) technology to detect motion in its vicinity. This allows it to monitor the usage frequency and patterns of hand sanitation stations or restroom facilities.

2. **Wireless Communication**: It utilizes LoRaWAN for data transmission. The sensor periodically uploads detected activity data to a centralized platform for analysis. This long-range, low-power wide-area network (LPWAN) technology ensures robust connectivity over several kilometers, ideal for expansive healthcare facilities.

3. **Data Analysis and Reporting**: The transmitted data is processed on a cloud platform where it can be visualized through dashboards for hygiene compliance audits and further analyzed for optimization of sanitation practices.

## Installation Guide

1. **Site Survey**: Conduct a site survey to ascertain optimal locations for the sensors, ensuring coverage of all critical hygiene zones.

2. **Mounting the Sensor**:
   - **Placement**: Ideal locations include above hand sanitizer dispensers, near restroom doors, or in strategic locations within a ward or department.
   - **Orientation**: Align the sensor at an angle that captures the desired field effectively, usually 1.5 to 2 meters above the ground.

3. **Power Up**: Insert the batteries into the device. The sensor incorporates low-power modes and efficient sleep cycles to maximize battery life.

4. **Network Configuration**:
   - Register the sensor on a LoRaWAN network server using the Device EUI, App Key, and Join EUI.
   - Configure the device settings via the network server for packet management and data intervals.

5. **Testing**: Validate the installation by checking connectivity and data transmission through the network server. Ensure real-time data capture is occurring as expected.

## LoRaWAN Details

- **Frequency Bands**: Operates within the standard ISM bands, around 868 MHz (EU) and 915 MHz (US).
- **Network Class**: Typically configured in Class A for minimal power consumption.
- **Data Rate**: Employs Adaptive Data Rate (ADR) to optimize the communication link based on distance to the gateway and other environmental factors.
- **Security**: Implements AES-128 encryption for all network communications ensuring data integrity and privacy.

## Power Consumption

The Saninudge TTN Smart Sensor is designed for efficiency:
- **Battery Life**: Typically exceeds two years under normal usage conditions, due to its low power draw from efficient specs and sleep cycles.
- **Power Source**: Operates on replaceable AA or AAA batteries.

## Use Cases

- **Hospitals and Clinics**: Monitors hygiene compliance to prevent infections.
- **Elderly Care Facilities**: Ensures sanitation protocols are adhered to for vulnerable populations.
- **Public Restrooms**: Provides insights into facility usage patterns to aid maintenance scheduling.
- **Food Processing Plants**: Maintains hygiene standards to comply with health regulations.

## Limitations

- **Range Dependency**: LoRaWAN coverage needs to be reliable; objects, structures, and environmental conditions may affect range and signal strength.
- **PIR Limitations**: Motion detection might be less effective in areas with high traffic or frequent environmental changes (e.g., air conditioning drafts).
- **Data Latency**: Due to the duty cycle restrictions inherent to LoRaWAN, there may be a latency in data transmission and reception.

The TTN Smart Sensor by Saninudge offers an innovative solution for maintaining hygiene standards in various industries, combining effective motion sensing, robust data communication via LoRaWAN, and efficient power usage to deliver actionable insights for improved health and safety.