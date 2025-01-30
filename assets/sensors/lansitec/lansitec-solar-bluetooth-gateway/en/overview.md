# LANSITEC - Solar Bluetooth Gateway Technical Overview

## Overview
The LANSITEC Solar Bluetooth Gateway is a cutting-edge device designed to extend Bluetooth sensor data over long distances using the LoRaWAN protocol. It leverages solar energy to operate, minimizing maintenance and maximising deployment versatility in remote and off-grid areas. This gateway is ideal for applications requiring low-power, wide-area network (LPWAN) capabilities while collecting data from Bluetooth-enabled devices.

## Working Principles
The Solar Bluetooth Gateway works by gathering data from Bluetooth sensors within its proximity. It then encodes and transmits this data over the LoRaWAN network to a centralized server or cloud platform for further processing and analysis. The gateway’s solar panel supplies power to recharge its internal battery, ensuring continued operation even during periods of low sunlight.

### Key Components:
- **Bluetooth Module**: Scans and connects with nearby Bluetooth sensors to gather data.
- **LoRaWAN Module**: Transmits collected data over long distances using low-power, wide-area networking.
- **Solar Panel and Battery**: Captures solar energy to charge its battery, enabling it to function autonomously.
- **Embedded Processor**: Manages data processing and communication protocols between Bluetooth and LoRaWAN modules.

## Installation Guide
1. **Location Selection**: Choose an installation site with sufficient sunlight exposure for optimal solar charging.
2. **Mounting**: Securely mount the gateway using the provided brackets on a pole or wall, ensuring the solar panel faces the sun.
3. **Configuration**: Initialize the device using the configuration tool provided by LANSITEC, setting LoRaWAN parameters like frequency plan, data rate, and join method (OTAA/ABP).
4. **Bluetooth Pairing**: Enable pairing mode to connect with nearby Bluetooth sensors, ensuring they are within the gateway’s effective range.
5. **Network Integration**: Connect the gateway to a LoRaWAN network server, setting the appropriate network keys and application settings.
6. **Testing**: Perform functional tests to confirm data transmission from Bluetooth sensors through the LoRaWAN network to the designated endpoint.

## LoRaWAN Details
- **Frequency Bands**: Supports global LoRaWAN frequency bands, including EU 868, US 915, AU 915, and others depending on regional compliance.
- **Data Rate**: Configurable data rates from DR0 to DR5, adapting to network conditions and range requirements.
- **Network Join Methods**: Supports both Over-the-Air Activation (OTAA) and Activation By Personalization (ABP).
- **Security**: Utilizes AES-128 encryption for secure data transmission.

## Power Consumption
- **Solar Panel**: Integrated high-efficiency solar panel keeps the internal battery charged.
- **Battery Capacity**: Typically, the gateway includes a rechargeable battery with a lifespan optimized for several days of operation without sunlight.
- **Power Management**: Advanced power management features to conserve energy during periods of inactivity or low data usage.

## Use Cases
- **Agriculture**: Monitoring environmental conditions (e.g., soil moisture, temperature) in remote fields.
- **Smart Cities**: Collecting data from dispersed IoT devices such as air quality monitors.
- **Industrial**: Data aggregation from sensor networks in large facilities for predictive maintenance and safety management.
- **Wildlife Monitoring**: Deploying gateways in natural environments to track tagged animals or environmental variables.

## Limitations
- **Bluetooth Range**: Limited by Bluetooth standards, typically up to 100 meters under ideal conditions, which may affect sensor placement.
- **Solar Dependency**: Performance is dependent on solar exposure; prolonged cloudy conditions may impact efficiency.
- **Network Coverage**: Requires availability of a LoRaWAN network or gateway infrastructure for full functionality.
- **Interference**: Both Bluetooth and LoRaWAN communications can be vulnerable to environmental interference, potentially affecting data transmission reliability.

By understanding these aspects, users can effectively deploy LANSITEC Solar Bluetooth Gateways in various scenarios, optimizing their operations through efficient data collection and transmission.