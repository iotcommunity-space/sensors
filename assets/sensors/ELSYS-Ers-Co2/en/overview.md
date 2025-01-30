# Technical Overview for ELSYS - ERS CO2 Sensor

## Introduction
The ELSYS ERS CO2 sensor is a compact, multipurpose indoor air quality sensor designed for monitoring carbon dioxide (CO2) levels, temperature, humidity, and motion. Utilizing LoRaWAN communication protocol, the device is suitable for various smart building applications, ensuring seamless integration with IoT systems for real-time air quality and occupancy monitoring.

## Working Principles
The ERS CO2 sensor is built around a combination of sensing technologies:

1. **NDIR (Non-Dispersive Infrared) CO2 Sensor**: The ERS CO2 uses NDIR technology to measure carbon dioxide levels. This method involves infrared light absorption to determine gas concentration, providing accurate and stable readings.

2. **Temperature and Humidity Sensor**: The ERS CO2 incorporates a digital sensor for precise temperature and humidity measurements, allowing for environmental condition monitoring.

3. **PIR Motion Sensor**: A PIR (Passive Infrared) sensor detects motion based on the infrared energy emitted by moving entities, suitable for occupancy detection.

## Installation Guide
1. **Physical Setup**:
   - Choose a suitable location in the room for the sensor. It should be mid-height on the wall to ensure open exposure to the room air and motion field. Avoid installations near windows, vents, or heat sources.
   - Mount the ERS CO2 using the accompanying screws or adhesive tape, ensuring it is securely attached.

2. **Powering the Device**:
   - Insert 2x AA batteries into the compartment, ensuring proper polarity alignment. The sensor features a low power design to maximize battery life.

3. **Activation and Configuration**:
   - Use the Dip-switches located inside the sensor to set the activation parameters such as LoRa channel settings.
   - Configure the desired measurement intervals and thresholds if applicable via the ELSYS application or third-party platforms.

4. **LoRaWAN Network Connection**:
   - Ensure the sensor is within the coverage of a compatible LoRaWAN gateway.
   - Use the unique device EUI (DEUI) for registering the sensor on your network server.
   - Configure network-specific settings like AppEUI and AppKey to establish a secure connection.

## LoRaWAN Details
The ERS CO2 sensor operates on the LoRaWAN protocol, offering capabilities like:

- **Frequency Ranges**: Compatible with EU868, US915, AU915, and other regional frequency plans.
- **Data Rate**: Supports adaptive data rate (ADR) for optimizing communication efficiency.
- **Security**: Uses standard LoRaWAN encryption for secure data transmission.
- **Uplinks**: Regularly transmits sensor data in uplinks which include CO2 levels, temperature, humidity, and motion status.
- **Downlinks**: Allows remote configuration and management via network server communication.

## Power Consumption
The ERS CO2 sensor is specifically designed for low power consumption:
- Average current consumption is below 50 µA during idle states.
- Operating power varies depending on transmission intervals and sensing activity, with a battery life expectancy of 2 to 10 years based on network and usage settings.

## Use Cases
1. **Indoor Air Quality Monitoring**: Ideal for maintaining healthy CO2 levels in office buildings, schools, and homes.
2. **Smart Building Management**: Provides data for HVAC control systems to improve energy efficiency and comfort.
3. **Occupancy Detection**: Facilitates energy savings and security automation by detecting room occupancy through motion sensing.
4. **Environmental Analytics**: Useful in collecting environmental data for analytics and insights in various applications.

## Limitations
- **Coverage Requirements**: Requires adequate LoRaWAN gateway coverage for data transmission, which may limit use in remote locations.
- **Data Transmission Limits**: Abide by local regulations regarding duty cycle and transmission intervals (e.g., EU868 limited duty cycle).
- **Battery Dependence**: While low-power, battery replacement is necessary after extended usage periods based on configuration settings and transmission frequency.
- **Fixed Installation**: Once mounted, the positioning is relatively static, requiring reinstallation for significant relocations.

In conclusion, the ELSYS ERS CO2 is a versatile IoT sensor tailored for enhancing indoor environments through accurate monitoring and data-driven management while relying on seamless LoRaWAN connectivity to ensure reliable and secure data communication.