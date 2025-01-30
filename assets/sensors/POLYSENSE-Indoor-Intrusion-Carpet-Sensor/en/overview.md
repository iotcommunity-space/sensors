# Technical Overview of POLYSENSE - Indoor Intrusion Carpet Sensor

## Introduction
The POLYSENSE Indoor Intrusion Carpet Sensor is an advanced sensing solution designed for indoor security applications. This sensor integrates seamlessly into existing LoRaWAN networks to provide reliable and secure intrusion detection capabilities. It is particularly suited for environments where traditional sensors are impractical or aesthetically intrusive, such as museums, retail spaces, and high-security areas.

## Working Principles
The POLYSENSE Indoor Intrusion Carpet Sensor operates using capacitive or piezoelectric detection principles. When pressure is applied—such as when someone steps on the carpet—it causes a change in the electrical properties of the sensor, which is detected and processed to determine the presence of an intruder. The sensor measures the force exerted on its surface and can differentiate between different levels of pressure, aiding in reducing false alarms.

## Installation Guide
1. **Choosing Location**: Select an area where traffic flow needs monitoring. Ideal placements include entryways, underneath mats, or in high-security zones.
2. **Surface Preparation**: Ensure the flooring is clean and flat to avoid interference with sensor readings.
3. **Sensor Placement**: Roll out the carpet sensor and cut it to the desired shape and size, ensuring full coverage of the targeted area.
4. **Connection**: Connect the sensor to the designated LoRaWAN communication module. Ensure the module is properly secured to avoid disconnections.
5. **Calibration**: Perform initial calibration by stepping on the carpet in various locations to establish baseline readings.
6. **Integration with LoRaWAN**: Set up the LoRaWAN gateway and node configuration to ensure proper communication between the sensor and network.

## LoRaWAN Details
- **Frequency Bands**: The sensor operates on standard LoRaWAN frequencies, which vary by region (e.g., EU868, US915).
- **Data Rate**: Supports adaptive data rate (ADR) for optimizing data transmission based on environmental conditions.
- **Security**: Utilizes LoRaWAN's AES-128 encryption to ensure data integrity and security.
- **Range and Coverage**: Provides extensive coverage with a line-of-sight range of up to 15 km in rural areas and 2–5 km in urban environments.

## Power Consumption
The POLYSENSE Indoor Intrusion Carpet Sensor is engineered for low-power operation, making it suitable for long-term use in battery-powered scenarios. Power consumption typically ranges between 10 to 50 microamperes (µA) during standby and peaks during active transmissions. Battery life can extend up to several years depending on usage and reporting frequency.

## Use Cases
- **Retail Security**: Monitor unauthorized access or traffic patterns in stores.
- **Museum Protection**: Install under valuable exhibits to detect unauthorized presence.
- **Residential Settings**: Enhance home security by detecting intrusions in entryways.
- **Office Surveillance**: Provide discreet intrusion detection in sensitive office areas.

## Limitations
- **Detection Area Sensitivity**: Only covers the area directly above it. Multiple units may be required for larger spaces.
- **False Positives**: Heavy objects placed on the sensor may trigger false alarms, requiring calibration adjustments.
- **Environmental Constraints**: Excessive humidity or rough surfaces can affect performance.
- **Power Dependency**: Although low-powered, reliance on battery life necessitates periodic maintenance checks.

In conclusion, the POLYSENSE Indoor Intrusion Carpet Sensor offers a versatile and discreet solution for intrusion detection with integration ease into LoRaWAN networks. Careful installation and regular maintenance ensure optimal performance and reliability.