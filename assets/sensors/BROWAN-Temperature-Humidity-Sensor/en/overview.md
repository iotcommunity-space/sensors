# BROWAN - Temperature Humidity Sensor

## Technical Overview

### Introduction
The BROWAN Temperature Humidity Sensor is designed for monitoring environmental conditions such as temperature and relative humidity. It is well-suited for a wide range of applications including smart agriculture, HVAC systems, and indoor environmental monitoring, leveraging the LoRaWAN protocol for wireless transmission of data.

### Working Principles
The sensor employs capacitive humidity sensing technology alongside a precision thermistor for temperature measurement. The capacitive sensor measures the humidity based on changes in capacitance as the humidity level changes, while the thermistor measures temperature changes by detecting changes in resistance. These measured environmental parameters are processed by an onboard microcontroller, which encodes and transmits the data over a LoRaWAN network.

### Installation Guide

1. **Site Selection**: Choose a location with adequate LoRaWAN coverage and within the environmental conditions specified by the sensor's operating range. Avoid placing the sensor in direct sunlight or areas prone to water accumulation.

2. **Mounting**: Use the included mounting hardware to secure the sensor on a wall or post. Ensure that the sensor is mounted at a height suitable for representative environmental measurements.

3. **Power Configuration**: Install batteries as per the specifications (usually 2 x AA or similar). Ensure batteries are installed with the correct polarity to avoid damage.

4. **Activation**: Refer to the device's activation guide to either manually or automatically join a predefined LoRaWAN network. Activation may involve setting device EUI, application EUI, and application key if needed.

5. **Calibration**: Although factory-calibrated, in certain precision-demanding applications, you may perform a calibration check using a reference instrument.

6. **Network Configuration**: Configure the sensor on the LoRaWAN network server to enable data reception, monitoring, and alerting. This may involve setting the correct data transmission rate and interval.

### LoRaWAN Details

- **Frequency Bands**: Supports multiple frequency bands based on regional regulations (e.g., EU868, US915).
- **Activation Methods**: Supports both Over-the-Air Activation (OTAA) and Activation by Personalization (ABP).
- **Data Rate**: Utilizes adaptive data rate (ADR) for optimized power consumption and network capacity.
- **Security**: Implements end-to-end encryption using device-specific keys to ensure data privacy and integrity.

### Power Consumption

The BROWAN Temperature Humidity Sensor is designed for low power consumption, making it ideal for battery-powered applications. In sleep mode, the sensor minimizes power usage to extend battery life. Operating on a typical transmission interval (e.g., every 15 minutes), the sensor's battery can last between 1 to 2 years, depending on the environment and data transmission settings.

### Use Cases

- **Smart Agriculture**: Monitor field conditions to optimize irrigation and ensure optimal crop health.
- **HVAC and Building Management**: Provide insights into climate control within buildings to enhance energy efficiency and occupant comfort.
- **Cold Chain Monitoring**: Ensure that temperature-sensitive goods are stored and transported under the right conditions.
- **Indoor Air Quality Monitoring**: Track the indoor environment quality in residential or commercial buildings to maintain healthy indoor atmospheres.

### Limitations

- **Signal Penetration**: Enclosed metallic environments or significant physical obstructions can impede LoRaWAN signal transmission.
- **Response Time**: Changes in environmental conditions might not be reported instantly due to configured data transmission intervals.
- **Battery Life**: Frequent data transmissions or extremely low-temperature conditions can reduce battery life.
- **Accuracy**: While adequate for many applications, the sensor may not meet the high precision requirements needed for scientific research.
- **Calibration Drift**: Over time and in harsh environments, sensor calibration might drift, necessitating periodic checks against a reference standard.

Conclusively, the BROWAN Temperature Humidity Sensor provides a robust and scalable solution for environmental monitoring, particularly in IoT applications relying on the LoRaWAN network for connectivity. Its operational efficiency, ease of installation, and versatility underline its utility across diverse application domains, notwithstanding its inherent limitations.