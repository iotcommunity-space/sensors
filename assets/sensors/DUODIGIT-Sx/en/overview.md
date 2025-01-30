# Technical Overview for DUODIGIT - Sx

## Overview
The DUODIGIT - Sx is an advanced IoT sensor module designed for accurate and efficient ingestion and transmission of digital signals for a variety of industrial and commercial applications. It leverages the LoRaWAN network for secure, long-range communication, making it suitable for environments where traditional network infrastructure may be unavailable or impractical.

## Working Principles
The DUODIGIT - Sx functions as a digital input acquisition device, specifically engineered to capture and transmit binary signals (such as on/off states) from external digital sources, like switches or relays. It supports multiple input channels and is configured to detect transitions and state changes. The module employs a microcontroller to process input signals and transmit data via the LoRaWAN protocol, ensuring robust communication even over long distances.

Key features include:
- Multiple digital input channels, supporting a wide range of input configurations.
- Adjustable input debounce times to filter out false triggering due to signal noise.
- Configurable transmission intervals to optimize data throughput and power consumption.

## Installation Guide
### Tools Required:
- Screwdriver
- Wire stripper
- Mounting hardware (if required)

### Installation Steps:
1. **Select a Location**: Choose a location ensuring adequate LoRaWAN coverage and proximity to the digital signal sources. Make sure the environment is within the operating temperature range of the device.

2. **Mounting**: Secure the device using the appropriate mounting hardware. Ensure that the unit is installed vertically to comply with the manufacturer's guidelines.

3. **Wiring**:
   - Strip the wires from the digital signal sources.
   - Connect these wires to the corresponding input terminals on the DUODIGIT - Sx. Ensure all connections are secure to prevent signal loss.

4. **Powering the Device**: Insert the appropriate batteries or connect the device to an external power source if applicable. Check the LED indicators to confirm power and functional status.

5. **Configuration**:
   - Connect to the DUODIGIT - Sx via a PC or a smartphone using the manufacturer's software application or web interface.
   - Configure the input channels, debounce settings, and data transmission intervals as per your requirements.

6. **Network Setup**: 
   - Ensure that the DUODIGIT - Sx is registered with your LoRaWAN network provider.
   - Set up network parameters including DevEUI, AppEUI, and AppKey for secure communication.

## LoRaWAN Details
The device operates on the LoRaWAN protocol, utilizing low-frequency bandwidth for reliable communication over long distances, typically up to 15 km in rural areas and 5 km in urban environments. It uses adaptive data rates to optimize battery life and improve network capacity.
- **Frequency Bands**: Available configurations for EU868, US915, AS923, and other regional ISM bands.
- **Security**: End-to-end AES-128 encryption for secure data transfer.
- **Join Modes**: Supports both Over-the-Air Activation (OTAA) and Activation by Personalization (ABP).

## Power Consumption
The DUODIGIT - Sx is designed for low power consumption, making it ideal for battery-operated scenarios. Key power consumption details include:
- **Idle Mode**: Approximately 15 µA
- **Active Mode**: Varies between 10-50 mA based on transmission power and operation times.
- **Battery Life**: With a standard lithium battery pack, the device can operate up to 5 years, depending on data reporting frequency and environmental conditions.

## Use Cases
1. **Industrial Automation**: Monitoring the state of machinery by capturing switch statuses and sending alerts on state changes.
2. **Utility Metering**: Interface with meters to record pulse counts for water, gas, or electricity consumption.
3. **Smart Buildings**: Automate control systems by integrating with building management systems for real-time state monitoring.
4. **Agriculture**: Monitor irrigation systems to ensure optimal water distribution by detecting valve positions.

## Limitations
- **Environmental Conditions**: Limited operational efficiency in extreme weather conditions beyond specified temperature ranges.
- **Network Coverage**: Performance is reliant on LoRaWAN network availability, and actual range can vary based on environmental obstructions.
- **Data Throughput**: Limited by LoRaWAN's low bandwidth, making the sensor unsuitable for real-time high-frequency data applications.
- **Configuration Complexity**: Requires technical knowledge for initial setup and configuration, potentially resulting in a steep learning curve for non-technical users.

In conclusion, the DUODIGIT - Sx stands out as a versatile and robust solution for digital input monitoring, particularly in remote and infrastructure-limited environments. Careful consideration of its use cases and limitations will enable users to deploy it effectively and derive maximum value from its capabilities.