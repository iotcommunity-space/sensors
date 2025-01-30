# ELSYS Ems Door Sensor Technical Overview

## Introduction

The ELSYS Ems Door Sensor is a compact, efficient, and reliable solution designed for monitoring the status of doors and windows. Utilizing LoRaWAN technology, the Ems Door Sensor offers long-range communication with minimal power consumption, making it ideal for smart building automation and security applications.

## Working Principles

The Ems Door Sensor operates using a magnetic reed switch to detect the open or closed status of doors or windows. When the door or window changes state, the sensor communicates this event via LoRaWAN to a network server. The device leverages periodic status reports and event-based triggers to ensure continuous monitoring and alert users of any unauthorized access or environmental changes.

### Key Features:
- **Magnetic Reed Switch**: Detects state change based on magnetic proximity.
- **LoRaWAN Connectivity**: Provides long-range, low-power wireless communication.
- **Periodic Reporting**: Configurable intervals for routine status updates.
- **Event Triggers**: Immediate transmission upon state change events.

## Installation Guide

### Components Included:
- ELSYS Ems Door Sensor
- Magnetic counterpart
- Mounting adhesive or screws

**Installation Steps**:
1. **Placement Planning**: Choose an appropriate location on the door/window frame. The sensor should be installed where the movement and alignment can best accommodate the magnetic switch.
   
2. **Mounting the Sensor**: 
   - Clean the installation area to ensure firm adhesion.
   - Use the provided adhesive to secure the main sensor unit onto the door (or stationary frame).
   - Alternatively, screws can be used for more permanent installations.

3. **Positioning the Magnet**: Attach the magnetic counterpart directly across from the sensor on the moving part (e.g., door leaf), ensuring that they align when closed.

4. **Testing**: Open and close the door to test if the sensor reliably detects state changes. The LED indicator can be used to confirm correct operations initially.

5. **Network Configuration**:
   - Power on the device (usually with pre-installed batteries).
   - Follow the LoRaWAN network configuration settings as provided by the network operator.
   - Validate that the device is correctly registered and transmitting data to the server as expected.

## LoRaWAN Details

- **Frequency Bands**: Compatible with global ISM bands (e.g., EU868, US915).
- **Activation Mode**: Supports both OTAA (Over-the-Air Activation) and ABP (Activation by Personalization) methods.
- **Data Rate**: Utilizes adaptive data rate (ADR) for optimal performance.
- **Security**: Features AES-128 encryption to ensure secure data transmission.

## Power Consumption

- **Battery Life**: Typically up to 10 years depending on configuration and usage (e.g., transmission frequency and environmental conditions).
- **Battery Type**: Lithium-thionyl chloride (Li-SOCl2) 3.6V AA size.
- **Power-saving Modes**: The sensor operates in a low-power state when idle, which significantly conserves battery life.

## Use Cases

1. **Security & Access Control**: Monitor sensitive entryways to detect unauthorized access and trigger security protocols.
2. **Smart Building Management**: Integrate with automated HVAC systems to improve energy efficiency by detecting open windows or doors.
3. **Property Management**: Receive alerts about doors or windows left open in managed properties, reducing the risk of property damage and energy loss.

## Limitations

1. **Environmental Sensitivity**: Performance may vary in extreme environmental conditions like high humidity or extreme temperatures which could affect battery life and transmission integrity.
2. **Signal Interference**: Physical obstructions or interference from other electronic devices can affect LoRaWAN signal quality and range.
3. **Line-of-Sight Requirement**: The magnetic switch needs precise alignment, which might be challenging on irregular or oversized door/window frames.

In conclusion, the ELSYS Ems Door Sensor is a powerful tool for remote door/window monitoring by providing a seamless integration with modern IoT platforms through advanced LoRaWAN connectivity. Its energy-efficient design and long-range capabilities make it ideally suited for a variety of smart-building applications, while users must consider environmental factors and physical installation challenges for optimal performance.