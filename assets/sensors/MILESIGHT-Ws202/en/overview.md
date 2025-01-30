# MILESIGHT - WS202 Technical Overview

## Introduction
The MILESIGHT WS202 is a radar-based motion sensor designed for indoor applications. It is part of the MILESIGHT IoT series, leveraging LoRaWAN technology for efficient and long-range wireless communication. The WS202 is primarily used for detecting motion and occupancy, utilizing microwave radar technology to offer reliable performance even in challenging conditions.

## Working Principles
The WS202 operates based on radar wave detection. It emits microwave signals in the 24 GHz ISM band, which then bounce off surrounding objects. The sensor processes the returned signals to detect movement, providing a dynamic range and sensitivity compared to traditional infrared sensors. This radar-based method allows the WS202 to penetrate materials like glass and plywood to detect motion, providing a non-line-of-sight detection capability.

### Key Features:
- **Microwave Detection:** Utilizes the Doppler Effect to detect motion by observing frequency shifts.
- **High Sensitivity:** Capable of noticing subtle movements, improving occupancy and presence detection applications.
- **Non-Intrusive Detection:** Can detect motion through thin walls or glass.

## Installation Guide
### Location and Mounting:
1. **Choose the Right Location:** Mounting height should typically be between 2 to 3 meters for optimal coverage.
2. **Avoid Obstructions:** Ensure there are minimal metal or dense materials blocking the line of sight to improve detection accuracy.
3. **Fixing:** Use screws and wall brackets for a secure mounting. Ensure the sensor is firmly attached to prevent vibrations which can cause false readings.

### Configuration:
1. **Power Up:** Insert the supplied battery or connect to an external power source if applicable. The WS202 typically uses built-in batteries suitable for long-term operation.
2. **Activate the Sensor:** The WS202 has a simple activation mechanism—usually pressing a button or using a magnet activation process.
3. **Configure via Software:** Use the designated MILESIGHT configuration tool or platform to adjust parameters such as sensitivity, detection range, and reporting intervals.

## LoRaWAN Details
### Connectivity:
- **LoRaWAN Protocol:** Utilizes LoRaWAN protocol for wireless communication.
- **Frequency Bands:** Supports EU868, US915, AS923, or CN470, depending on regional requirements.
- **Data Rate:** Adapts to varying data rates, typically between 0.3 kbps to 27 kbps in different operating countries.

### Network Integration:
- **Activation:** Supports both OTAA (Over-The-Air Activation) and ABP (Activation By Personalization).
- **Security:** Encrypted with AES-128 to ensure secure data transmission across the network.

## Power Consumption
The WS202 is designed for low power consumption, ideal for battery-operated use:
- **Typical Power Usage:** In sleep mode, it consumes less than 20 µA.
- **Operating Time:** With typical settings and standard use, the battery can last up to 5 years.
- **Optimization Features:** Adjustable reporting intervals and sensitivity settings allow users to optimize battery life according to specific use cases.

## Use Cases
- **Smart Building Management:** For automating lighting and HVAC systems based on occupancy.
- **Security Monitoring:** Used in offices and residential properties for intrusion detection.
- **Retail Analytics:** Helps in understanding footfall and customer behavior by monitoring movements in designated areas.

## Limitations
- **Material Interference:** Certain dense materials (e.g., metal and concrete) can significantly reduce detection accuracy.
- **Setup Complexity:** Requires careful calibration and configuration to balance detection sensitivity and false alarm reduction.
- **Coverage Limitations:** While non-line-of-sight capabilities are beneficial, detection range is generally limited to 10-15 meters indoors.
- **Environmental Factors:** High-frequency signals may be impacted by heavy rain or snowfall if mounted in areas exposed to such conditions.

## Conclusion
The MILESIGHT WS202 is a versatile radar-based motion sensor suitable for various applications requiring reliable motion detection and efficient connectivity. Its integration with LoRaWAN makes it a powerful addition to any IoT network, providing seamless data transfer and long battery life. However, proper installation and configuration are crucial to overcoming its limitations and achieving optimal performance.