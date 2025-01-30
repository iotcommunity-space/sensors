# Technical Overview: POLYSENSE - Limit Switch Sensor

## Introduction
The POLYSENSE Limit Switch Sensor is a robust IoT device designed for monitoring the positional status of mechanical systems through LoRaWAN connectivity. This sensor is particularly useful for applications requiring precise limit detection, such as in industrial automation, smart building management, or safety systems. The integration of limit switch functions into IoT solutions allows for remote monitoring and control, enhancing operational efficiency.

## Working Principles
The POLYSENSE Limit Switch Sensor operates based on the mechanical principle of a limit switch. It detects the motion of a mechanical component, typically when it reaches a predefined limit position. Upon actuation, the limit switch changes its contact state, which is then converted into a digital signal by the sensor's internal microcontroller. This digital signal is transmitted via LoRaWAN, enabling real-time monitoring of mechanical system status.

**Key Components:**
- **Mechanical Actuator:** Engages with a moving part of the machine or system.
- **Binary Sensor Unit:** Detects the change in position when the actuator is engaged.
- **Microcontroller:** Processes the signal from the sensor unit.
- **LoRaWAN Transceiver:** Sends data to a network server for remote data access.

## Installation Guide

1. **Site Selection:**
   - Identify critical points in the mechanical system where position monitoring is required.
   
2. **Mounting:**
   - Securely mount the sensor near the mechanical limit position using appropriate brackets or adhesives. Ensure the actuator is aligned with the moving component's trajectory.
   - The sensor should be installed in a way that allows for unobstructed movement within the mechanical system.

3. **Connection:**
   - Connect the switch actuator to the mechanical system ensuring proper engagement and disengagement without excess force.
   - Verify secure connection to power supply and check compatibility with system voltages if applicable.

4. **Configuration:**
   - Configure device settings via the POLYSENSE configuration tool or app. This generally involves setting transmission intervals and thresholds.

5. **Testing:**
   - Perform multiple test actuations to ensure reliable engagement and accurate signal transmission before routine operation.

## LoRaWAN Details

- **Frequency Bands:** Typically operates in standard ISM bands (e.g., US915, EU868).
- **Data Transmission:** Utilizes LoRa modulation for long-range, low-power communications.
- **Network Configuration:**
  - Supports both private and public LoRaWAN networks.
  - Requires Device EUI, Application EUI, and App Key for activation.

- **Adaptive Data Rate (ADR):** Optimizes data rate, spreading factors, and energy consumption based on network conditions.
- **Payload:** Sends a basic binary signal indicating the limit switch status (open/closed).

## Power Consumption

- **Power Source:** Typically powered by long-life batteries, offering years of operation under normal usage conditions.
- **Sleep Mode:** Ultra-low power mode when inactive to conserve battery.
- **Active Mode:** Low power consumption during signal transmission due to the efficient LoRaWAN protocol.

## Use Cases

- **Industrial Automation:** Monitor and control machine movement limits to prevent mechanical failures.
- **Building Management:** Detect open/close states of doors, gates, or windows to automate security systems.
- **Safety Systems:** Ensure proper actuation of emergency stops or safety interlocks to maintain safe operational environments.

## Limitations

- **Environmental Conditions:** Sensitivity to dust, moisture, or extreme temperatures may require additional protective enclosures.
- **Mechanical Alignment:** Precise installation is crucial; misalignment can lead to errors in detection.
- **Network Coverage:** Requires access to a LoRaWAN network with sufficient coverage for reliable operation.
- **Data Limitations:** Provides binary state status only; does not offer continuous variable feedback.

The POLYSENSE Limit Switch Sensor, with its integration into IoT systems, provides businesses with the ability to transform mechanical limit monitoring into a smart, connected process. While there are considerations such as environmental conditions and network coverage to account for, its simple operation and significant potential applications make it a valuable component in enhancing automated systems.