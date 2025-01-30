# Technical Overview for DIGITAL-MATTER - Matter Yabby Edge

## Product Overview
The DIGITAL-MATTER Yabby Edge is a compact, robust, and versatile IoT sensor designed for asset tracking and environmental monitoring. Utilizing cutting-edge technologies, it leverages GNSS, Wi-Fi AP MAC Address Scanning, and LoRaWAN connectivity to deliver accurate global position and environmental data.

## Working Principles

### GNSS and Wi-Fi Positioning
The Yabby Edge uses a hybrid positioning system that combines GNSS (Global Navigation Satellite System) data and Wi-Fi AP (Access Point) MAC address scanning. This dual system allows the device to calculate positions in both outdoor and indoor environments efficiently. The GNSS engages only when necessary to preserve battery life, while Wi-Fi scanning enhances the accuracy indoors, where GPS signals might be weak or unavailable.

### LoRaWAN Connectivity
LoRaWAN (Long Range Wide Area Network) is the primary communication protocol used by the Yabby Edge. It enables long-range communication over sparse networks, ensuring data can be transmitted over several kilometers. LoRaWAN's ability to support ultra-low power devices makes it ideal for battery-operated sensors like the Yabby Edge.

### Environmental Sensors
The Yabby Edge also includes environmental sensors that measure parameters such as temperature and motion, offering comprehensive monitoring capabilities alongside asset tracking.

## Installation Guide

1. **Preparation**
   - Ensure you have a compatible LoRaWAN network and have the necessary credentials and applications set up for data visualization and management.
   - Verify the Yabby Edge device is charged and functional by checking the indicator lights.

2. **Configuration**
   - Using the compatible configuration tool provided by DIGITAL-MATTER, connect to the device via Bluetooth or a provided interface to set up the necessary operational parameters, including LoRaWAN credentials such as DevEUI, AppEUI, and AppKey.
   - Set specific reporting intervals and geofencing parameters as required for your use case.

3. **Installation**
   - Secure the device to the asset or location to be monitored using the built-in mounting holes or an adhesive, ensuring it is in a position to receive both satellite and Wi-Fi signals.
   - Verify the device is transmitting data by checking status updates from your network server.

4. **Verification**
   - Use the monitoring dashboard to ensure data is being received accurately and in real-time.
   - Conduct tests by moving or interacting with the device to verify operational functionality.

## LoRaWAN Details

- **Frequency Bands:** The Yabby Edge supports multiple frequency bands including EU868, US915, AU915, and others, making it compatible with global LoRaWAN networks.
- **Communication Range:** Up to 15 km in rural areas and about 2-5 km in urban settings.
- **Data Rates:** Uses adaptive data rate (ADR) to dynamically optimize performance and power consumption.

## Power Consumption

- **Battery Life:** Up to several years, depending on configuration and usage patterns—typically 3 to 5 years with moderate reporting frequency and environmental conditions.
- **Power Source:** Includes a built-in replaceable lithium battery optimized for low power consumption, with management features that enhance longevity.

## Use Cases

1. **Asset Tracking:** Ideal for tracking valuable assets across supply chains, such as containers, pallets, and machinery.
2. **Logistics Management:** Optimize fleet management operations with precise location tracking.
3. **Environment Monitoring:** Monitor temperature-sensitive goods in storage or transit.
4. **Indoor and Outdoor Positioning:** Effective for hybrid environments where assets need to be tracked indoors and outdoors, such as in large warehouses or across corporate campuses.

## Limitations

- **Signal Dependency:** Performance may degrade in areas with obstructions or poor network coverage.
- **Battery Replacement:** Despite long battery life, in some cases, battery replacement might be necessary, potentially incurring maintenance costs.
- **GNSS Limitations:** In dense urban or heavily wooded environments, GNSS accuracy can be affected by multipath signals or obstructions.
- **LoRaWAN Infrastructure:** Requires a compatible LoRaWAN network, which may not be available in all areas.

Overall, the DIGITAL-MATTER Yabby Edge is a highly versatile and efficient choice for those needing comprehensive tracking and monitoring solutions in a wide range of environments.