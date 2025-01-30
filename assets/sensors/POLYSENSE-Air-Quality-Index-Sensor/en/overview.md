# Technical Overview: POLYSENSE - Air Quality Index Sensor

## Overview

The POLYSENSE Air Quality Index (AQI) Sensor is designed to provide real-time monitoring of air quality parameters such as particulate matter (PM1.0, PM2.5, PM10), volatile organic compounds (VOCs), carbon dioxide (CO2), temperature, and humidity. The sensor utilizes advanced detection technologies to deliver accurate measurements suitable for both urban and rural environments.

## Working Principles

### Sensing Mechanism

The POLYSENSE AQI Sensor employs laser scattering to measure particulate matter concentration. An internal laser source projects light onto airborne particles, and the scattered light is detected and analyzed to determine the particle size and count. For gases like VOCs and CO2, the sensor uses non-dispersive infrared (NDIR) technology, which measures the absorption of infrared light to quantify gas concentrations.

### Calibration and Processing

The sensor is factory-calibrated for precision; however, it is recommended to perform periodic on-site calibrations based on environment changes. Data from the sensor are processed using embedded algorithms to derive an accurate Air Quality Index (AQI), which represents overall air quality levels.

## Installation Guide

1. **Placement**: Install the sensor at a height of 1.5 to 3 meters above ground level in an open area away from obstructions like walls or trees to ensure accurate airflow.
2. **Mounting**: Use the provided mounting brackets to secure the sensor. Ensure it is firmly attached to prevent vibration that could affect measurements.
3. **Orientation**: Position the sensor with its inlet facing the predominant wind direction to capture representative air samples.
4. **Connections**: Connect the sensor to a suitable power source and data network, as per the guidelines provided in the technical manual.
5. **Weather Protection**: The sensor is IP67-rated, offering protection against dust and water ingress; however, avoid placing it in areas with potential submersion.

## LoRaWAN Details

The POLYSENSE AQI Sensor is equipped with LoRaWAN connectivity, offering long-range, low-power wireless communication. This capability is beneficial for remote monitoring applications.  

- **Frequency Bands**: Supports standard LoRaWAN frequency bands (e.g., EU868, US915, AS923).
- **Data Transmission**: Configurable data transmission intervals, typically ranging from 5 minutes to 24 hours, depending on application needs.
- **Network Compatibility**: Compatible with various LoRaWAN network servers for seamless integration.
- **Security**: Utilizes AES-128 encryption for secure data transmission over the network.

## Power Consumption

The sensor is designed with low-power consumption in mind, essential for battery-operated or solar applications:

- **Nominal Power Usage**: Varies depending on the sensing and transmission frequency, typically under 1 watt in optimal conditions.
- **Battery Life**: When used with a battery, the sensor can operate for several years without replacement, assuming typical settings and environment conditions.
- **Power Supply Options**: Operable via direct AC supply, solar panels, or rechargeable batteries.

## Use Cases

- **Urban Air Quality Monitoring**: Ideal for city councils and environmental agencies monitoring pollution and compliance with air quality standards.
- **Industrial Environment**: Useful in monitoring emissions in factories and plants to ensure workplace safety and regulatory compliance.
- **Smart City Applications**: Integration with other IoT devices for comprehensive environmental and infrastructure monitoring.
- **Public Health and Education**: Facilitates research by providing vital data for epidemiological studies related to air pollution effects.

## Limitations

- **Environmental Factors**: Extreme weather or harsh environmental conditions can affect sensor accuracy and longevity.
- **Interference**: Presence of strong electro-magnetic fields may interfere with data transmission, requiring proper site planning and network setup.
- **Calibration Needs**: While factory-calibrated, periodic recalibration may be necessary to maintain sensor accuracy, especially in rapidly changing environments.
- **Range Constraints**: Although LoRaWAN provides extensive coverage, actual range may vary based on topography and urban structures.

In conclusion, the POLYSENSE Air Quality Index Sensor is a robust, versatile tool for comprehensive air quality monitoring. When properly installed and maintained, it provides valuable data for environmental management and public health initiatives.