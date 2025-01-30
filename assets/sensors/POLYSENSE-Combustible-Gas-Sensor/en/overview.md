# Technical Overview for POLYSENSE - Combustible Gas Sensor

## Introduction

The POLYSENSE Combustible Gas Sensor is a sophisticated device designed for the detection and monitoring of combustible gases in various environments. Integrated with LoRaWAN connectivity, this sensor offers reliable data transmission for IoT applications, ensuring enhanced safety and efficiency in detecting potential gas leakages.

## Working Principles

The POLYSENSE Combustible Gas Sensor operates on the principle of catalytic combustion. When combustible gases come into contact with the sensor, they are oxidized on a heated catalyst surface, resulting in a change in resistance across the sensor element. This change is then converted into an electrical signal that is proportionate to the gas concentration. The sensor is calibrated to recognize specific gas types and concentrations to provide accurate and timely alerts.

## Installation Guide

1. **Location Selection**:
   - Choose a strategic location where gases are most likely to accumulate.
   - Avoid areas with excessive dust, water spray, or vibrations.

2. **Mounting the Sensor**:
   - Secure the sensor at an appropriate height (typically 1 to 3 meters from the floor for heavier-than-air gases).
   - Use the mounting brackets provided to ensure stable positioning.

3. **Power Supply**:
   - Connect the sensor to a suitable power source as per the power specifications.
   - Ensure connections are water-tight in outdoor or exposed environments.

4. **Commissioning**:
   - Power on the device and check for LED indicators that signal normal operation or fault conditions.
   - Calibrate the sensor using known gas concentrations to ensure accuracy.

5. **Communication Configuration**:
   - Set up the LoRaWAN parameters such as DevEUI, AppEUI, and AppKey through the provided interface or software application.

6. **Integration and Testing**:
   - Integrate the sensor with your existing IoT platform for real-time data monitoring.
   - Perform testing in a controlled environment with known gas concentrations to verify performance.

## LoRaWAN Details

- **Frequency Bands**: Supports different ISM frequency bands (e.g., 868 MHz for EU, 915 MHz for US regions).
- **Adaptive Data Rate (ADR)**: Ensures efficient use of bandwidth and power by adjusting the data rate based on signal quality.
- **Class A Device**: The sensor operates primarily in Class A mode, enabling low-power operation with scheduled uplink and unscheduled downlink capabilities.
- **Network Security**: Utilizes AES-128 encryption ensuring secure data over the network.
- **Coverage**: Offers extended range capabilities, typically up to 10 km in rural areas and 3 km in urban settings, depending on the environmental conditions.

## Power Consumption

- **Sleep Mode**: Consumes an ultra-low power of approximately 15µW, ensuring long battery life.
- **Active Mode**: Simply monitors with power consumption in the range of 60-200mW, depending on data transmission frequency and environment conditions.
- **Battery Life**: Depending on the reporting interval and environmental factors, battery life can extend up to several years with optimized settings.

## Use Cases

- **Industrial Safety**: Prevention and early detection of gas leaks in petrochemical plants, refineries, and gas storage facilities.
- **Residential Monitoring**: Continuous monitoring of combustible gas levels within homes to prevent accidents.
- **Smart Cities**: Integration into city-wide safety systems ensuring public safety in densely populated areas.
- **Agricultural Applications**: Monitoring of biogas plants ensuring safe operation and management.

## Limitations

- **Calibration Drift**: Over time, sensors may experience drift necessitating periodic recalibration for accuracy.
- **Environmental Extremes**: Extreme temperatures and humidity levels may affect sensor accuracy and lifespan.
- **Cross-Sensitivity**: May exhibit sensitivity to gases other than the target gasses leading to false positives under certain conditions.
- **Maintenance Needs**: Regular cleaning and maintenance may be required in dusty or dirty environments to ensure long-term reliability.

This sensor provides a robust solution in environments where gas detection and safety are priorities, contributing to health and safety compliance, environmental monitoring, and operational efficiency.