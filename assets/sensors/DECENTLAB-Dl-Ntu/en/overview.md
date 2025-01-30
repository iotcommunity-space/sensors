## Technical Overview for DECENTLAB - DL-NTU

### Introduction
The DECENTLAB DL-NTU is a sophisticated Internet of Things (IoT) sensor specifically designed for the remote monitoring of turbidity in water. It leverages the LoRaWAN protocol for efficient long-range communication, making it ideal for a variety of environmental and industrial applications. This document provides a comprehensive overview of the sensor's working principles, installation procedures, LoRaWAN details, power consumption, potential use cases, and limitations.

### Working Principles

The DL-NTU sensor determines the turbidity of water by employing an optical measurement technique. It uses a light-emitting diode (LED) to project light into the water at a specific angle. A photodetector then measures the amount of light that is scattered by particles suspended in the water. Turbidity is deduced from the intensity of scattered light, which correlates with the concentration of suspended particles.

The sensor is pre-calibrated to provide accurate turbidity measurements in Nephelometric Turbidity Units (NTU) and is designed to compensate for color and large particles by adapting the optical measurement automatically.

### Installation Guide

1. **Site Selection**: Choose a location where the water flow is consistent and the water is representative of the water body or system being monitored. Avoid places where debris or excess algae may accumulate.

2. **Mounting the Sensor**: 
   - Use the mounting hardware provided to securely attach the sensor to a stable structure, such as a pole or a wall, ensuring that the sensor is submerged to the recommended depth.
   - Position the sensor so that it remains submerged in water but is not impacted by strong currents or debris.

3. **Powering the Device**: Insert the batteries into the sensor. The DL-NTU is designed to be low-maintenance and offers a long battery life due to its low power design.

4. **Activation**: Once powered, the device automatically starts and initiates communication with the LoRaWAN network.

5. **Calibration and Verification**: Although the sensor is pre-calibrated, verify readings using a reference turbidity standard if precise measurements are critical. Calibration may be required periodically based on deployment conditions.

### LoRaWAN Details

- **Frequency Plan**: The sensor supports multiple frequency bands complying with LoRaWAN regional specifications such as EU868, US915, AS923, etc.
- **Network Configuration**: 
  - The DL-NTU must be registered with the LoRaWAN network using a unique Device EUI, App EUI, and App Key.
  - Supports Over-The-Air Activation (OTAA) or Activation By Personalization (ABP) for network registration.

- **Communication Range**: Offers long-range communication, generally up to 15 kilometers in rural areas and 2-5 kilometers in urban environments.

- **Data Rate and Duty Cycle**: Operates using adaptive data rates (ADR) to optimize battery usage and network capacity, with typical uplink intervals ranging from minutes to several hours, depending on configuration.

### Power Consumption

The DL-NTU is designed to consume minimal energy:
- **Battery Type**: Utilizes high-quality lithium batteries.
- **Operational Lifetime**: Typical battery life ranges from 5 to 10 years, contingent upon the reporting frequency and environmental conditions.
- **Power Management**: Features intelligent power-saving modes, waking up only to perform measurements and data transmissions.

### Use Cases

- **Environmental Monitoring**: Ideal for monitoring lakes, rivers, and reservoirs to detect changes in water quality.
- **Industrial Applications**: Can be utilized in wastewater management to regulate turbidity levels and reduce environmental discharge impacts.
- **Agricultural Monitoring**: Assists in irrigation water quality assessments, ensuring optimal conditions for crop growth.
- **Drinking Water Utilities**: Monitors raw water turbidity for treatment plant intake assessments or within distribution networks.

### Limitations

- **Interference with Large Debris**: Substantial physical debris can obstruct the sensor, leading to inaccurate readings.
- **Dependency on Solar or Battery Life**: Prolonged deployments in extreme temperatures may affect battery life.
- **Calibration Needs**: Requires occasional calibration to maintain precision, especially in highly variable water conditions.

The DECENTLAB DL-NTU is a versatile tool, offering reliable turbidity measurement capabilities over a long range via LoRaWAN. However, users should consider environmental factors and regular maintenance to ensure optimal performance.