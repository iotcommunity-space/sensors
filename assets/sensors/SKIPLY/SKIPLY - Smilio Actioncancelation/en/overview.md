# Technical Overview for SKIPLY - Smilio Action Cancelation

## Overview

SKIPLY's Smilio Action Cancellation is a comprehensive sensor system designed for real-time feedback collection and process optimization using Internet of Things (IoT) technology. It leverages LoRaWAN communication for efficient data transfer over long distances. This document covers the working principles, installation guidelines, LoRaWAN details, power consumption, potential use cases, and system limitations.

## Working Principles

Smilio sensors are versatile devices designed to capture user interactions efficiently and discreetly. The action cancellation feature specializes in negating or retracting previous inputs, allowing users to correct entries. The device communicates through a combination of switch actuation and haptic feedback that ensures user acknowledgment. The data captured by the sensors are transmitted via LoRaWAN to cloud-based or local servers for analysis and action.

### Key Features:
- **Multi-button Interface**: Allows multiple user inputs and cancellations.
- **Haptic Feedback**: Confirms user actions to avoid erroneous entries.
- **LED Indicators**: Provide visual confirmations of successfully recorded or canceled actions.
- **Durability**: Built to last in various environments, from indoors to harsh outdoor conditions.

## Installation Guide

### Tools Required:
- Screwdriver for mounting
- PC or smartphone for configuration
- LoRaWAN Gateway (if not previously installed)

### Steps:
1. **Site Survey**: Conduct a site survey to determine the optimal placement, ensuring good LoRaWAN signal strength.
2. **Mounting**: Secure the sensor using screws or adhesive mounts available as per the installation surface (wall, kiosk, etc.).
3. **Power Initialization**: Insert the batteries (commonly AA or AAA) and ensure they are seated correctly for immediate activation.
4. **Configuration**:
   - Use the accompanying mobile app or PC software to configure network settings.
   - Ensure the device is registered on a LoRaWAN network server, inputting necessary keys (AppEUI, DevEUI, AppKey).
5. **Testing**: Conduct a functionality check by pressing the buttons and verifying if data is reaching the backend.

## LoRaWAN Details

- **Frequency Bands**: Operates in standard ISM bands which vary by region (e.g., EU868, US915).
- **Data Rate**: Compatible with LoRaWAN Adaptive Data Rate (ADR) for optimizing performance and battery life.
- **Coverage**: Supports long-range connectivity, effective over several kilometers in open spaces.
- **Network Join**: Uses Over-the-Air Activation (OTAA) or Activation By Personalization (ABP) for device authentication.

## Power Consumption

- **Battery Type**: Typically powered by two or three standard AA or AAA batteries.
- **Battery Life**: Depending on usage and network conditions, battery life can extend up to 5 years.
- **Energy Efficiency**: The device minimizes power use during inactive periods and optimizes transmission based on ADR settings.

## Use Cases

1. **Customer Feedback**: Retail environments can utilize the Smilio for immediate customer feedback, adjusting services based on real-time data.
2. **Industrial Automation**: Smilio sensors can monitor and confirm process adjustments, providing instantaneous feedback for quality control.
3. **Public Transport**: Deployed in stations to gather quick passenger inputs regarding service satisfaction or cancellations.
4. **Healthcare Facilities**: Enables feedback collection from patients on services received, with options to amend responses if necessary.

## Limitations

- **Signal Obstruction**: Heavy urban environments may interfere with LoRaWAN signals, resulting in connectivity issues.
- **Response Time**: Real-time feedback is dependent on network latency, which may vary.
- **Battery Dependency**: The performance is subject to battery health; frequent checks or proactive replacements are advised.
- **Input Limitation**: The number of buttons limits the type of feedback that can be collected without customization.

---

This overview provides essential information for deploying and operating Smilio Action Cancellation sensors. For more comprehensive guidance, refer to the sensor's detailed operating manual.