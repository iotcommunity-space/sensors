# MILESIGHT - AT101 Technical Overview

The MILESIGHT AT101 is a sophisticated indoor air quality monitor designed to provide comprehensive data about air conditions, ensuring that indoor environments are optimized for health and comfort. Equipped with cutting-edge sensor technology, the AT101 integrates seamlessly into IoT ecosystems through LoRaWAN connectivity, making it ideal for smart buildings and environmental monitoring applications.

## Working Principles

The MILESIGHT AT101 utilizes multiple integrated sensors to measure a range of air quality parameters, including:

- **Temperature and Humidity:** Utilizes precision digital sensing technology to provide accurate readings of ambient temperature and relative humidity.
- **CO2 Levels:** Infrared technology is employed to measure CO2 concentration, ensuring precise monitoring of air quality.
- **Volatile Organic Compounds (VOCs):** Equipped with metal oxide-based sensing technology for detecting various harmful VOCs present in indoor environments.

These sensors collectively contribute to building an accurate profile of air quality, enabling users to take actionable steps to improve indoor conditions.

## Installation Guide

### Hardware Installation
1. **Location Selection:** Choose a well-ventilated area for placement, avoiding close proximity to heat sources, air conditioners, and windows to prevent distorted readings.
   
2. **Mounting:** The AT101 can be wall-mounted using the provided bracket or stationed on a flat surface. Make sure it's positioned at a height between 1.5 to 2 meters for optimal readings. Follow the manufacturer's guide for wall-mount installation steps.

3. **Power Connectivity:** Connect the device to power using the supplied adaptor. Ensure the connection is secure to prevent intermittent power issues.

### Software Configuration
1. **Initial Setup:** Connect the AT101 to your local network by following the initial setup instructions. This typically involves connecting via Bluetooth or USB to configure the device’s network settings.

2. **LoRaWAN Configuration:** Use the MILESIGHT IoT Cloud or dedicated network server to configure the LoRaWAN parameters. Set up parameters such as Device EUI, Application EUI, and App Key for secure network communication.

3. **Calibration:** Provide adequate time for the initial sensor calibration (often around 24 hours) for accurate readings from start-up.

## LoRaWAN Details

The MILESIGHT AT101 supports LoRaWAN connectivity, featuring:

- **Frequency Bands:** Configured to operate in various regions including EU868, US915, AS923, and AU915, among others, adhering to regional compliance requirements.
- **Data Rate:** Supports dynamic data rates based on network conditions to optimize range and power efficiency.
- **Security:** Provides end-to-end AES128 encryption ensuring data integrity and secure transmission.
- **Network Deployment:** Can integrate with existing LoRaWAN networks or set up with private LoRa gateways.

## Power Consumption

The MILESIGHT AT101 is designed with power efficiency in mind, featuring a low-power operation mode:

- **Operating Voltage:** 5V DC using an adapter.
- **Power Usage:** Standby power consumption is low, optimizing the device for continuous operation without significant energy costs.

## Use Cases

The MILESIGHT AT101 is suited for various applications, including:

- **Smart Buildings:** Enhancing HVAC system efficiency by providing real-time air quality data for automated climate control.
- **Schools and Offices:** Monitoring and improving air quality in educational and professional environments to foster better health and productivity.
- **Healthcare Facilities:** Maintaining superior indoor air quality standards in hospitals and clinics to ensure patient and staff safety.

## Limitations

- **Installation Constraints:** Close proximity to abnormal heat sources or draughts can affect accuracy.
- **Environmental Sensitivity:** Extreme conditions outside rated humidity and temperature ranges may impact sensor performance.
- **Coverage Limitations:** Being designed for indoor environments, the device is not suitable for outdoor air quality assessments.

In conclusion, the MILESIGHT AT101 is a robust solution for indoor air quality monitoring, offering seamless integration, advanced sensor capabilities, and reliable LoRaWAN connectivity. Ensuring that this device is installed and configured properly is paramount for achieving optimal performance and data accuracy.