### Technical Overview of MILESIGHT AM107

The MILESIGHT AM107 is a sophisticated indoor environment monitoring sensor designed for use in smart buildings and industrial IoT applications. It measures a wide array of environmental parameters, including temperature, humidity, CO2 concentration, TVOC (Total Volatile Organic Compounds), barometric pressure, and ambient light levels. Here's an in-depth look at its features and operations:

#### Working Principles

The AM107 integrates multiple advanced sensors to monitor various environmental factors. Below are its key components:

- **Temperature and Humidity Sensor:** Utilizes a digital sensor that features capacitive humidity detection and thermal detection components. This sensor provides highly accurate, linear, and precise readings.

- **CO2 Sensor:** Utilizes Non-Dispersive Infrared (NDIR) technology which offers stability and reliability in CO2 measurement, essential for indoor air quality assessment.

- **TVOC Sensor:** Employs metal-oxide gas sensing technology to detect a broad range of VOCs, providing comprehensive indoor air quality data.

- **Barometric Pressure Sensor:** A piezo-resistive sensor that offers accurate atmospheric pressure readings, which are crucial for altitude and weather-related monitoring.

- **Ambient Light Sensor:** Captures light levels using a photodiode that simulates the human eye's response to various lighting conditions.

#### Installation Guide

1. **Site Selection:** Choose an optimal location free from obstruction for accurate reading, ideally in central indoor spaces away from air vents or heaters.

2. **Mounting:** The AM107 can be wall-mounted or placed on a flat surface. Use the provided bracket for wall installation, ensuring the sensor is vertically aligned for precise gravitational and environmental measurements.

3. **Commissioning:** Power the device using the provided batteries. The device features a LCD screen for on-site data visualization and initial setup can be done via Bluetooth with the MILESIGHT Toolbox app.

4. **Network Configuration:** Configure the LoRaWAN settings following the network's parameters. This involves setting the Device EUI, Application EUI, and Application Key in the app for network join process.

#### LoRaWAN Details

- **Frequency Bands:** Supports global ISM bands (EU868/US915/AU915/AS923).
- **Data Rate:** Adapts using Adaptive Data Rate (ADR) based on network structure and transmission conditions.
- **Network Security:** Employs AES-128 encryption for secure data transmission.
- **Communication Range:** Capable of providing long-range connectivity, typically between 2 to 15 kilometers in open areas, and 1 to 3 kilometers in dense urban environments.

#### Power Consumption

The AM107 is powered by 2 x 1.5V AA batteries. With efficient power management, the AM107 can operate for over a year on these batteries under typical use conditions. The exact lifespan is contingent on the frequency of data transmission and environmental conditions.

#### Use Cases

- **Smart Workplaces:** Monitoring and optimizing indoor air quality and lighting for enhanced employee productivity and wellbeing.
- **Educational Facilities:** Ensuring healthy learning environments by maintaining optimal CO2, temperature, and humidity levels.
- **Healthcare Facilities:** Continuous monitoring in sensitive areas such as surgeries or wards, to detect VOCs and maintain sanitary conditions.
- **Industrial Monitoring:** Understanding and controlling indoor climate conditions to ensure compliance with safety and operational standards.

#### Limitations

- **Position Sensitivity:** Placement is crucial as positioning near HVAC outlets or direct sunlight may skew readings.
- **Battery Dependency:** Limited by battery life; frequent data transmission reduces operation time, thus maintenance for battery replacement is required.
- **Network Range Dependency:** Performance may decrease if obstacles obstruct LoRaWAN signal, requiring strategic placement of gateways.

The MILESIGHT AM107 stands as a robust and versatile solution for those needing comprehensive indoor environmental monitoring, with its integration into networks via LoRaWAN providing data scalability across various applications, making it ideal for deploying large-scale, sustainable IoT systems.