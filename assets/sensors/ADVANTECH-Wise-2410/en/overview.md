# Technical Overview of ADVANTECH - WISE-2410

The ADVANTECH WISE-2410 is a versatile and robust wireless condition monitoring sensor designed for industrial applications. It is designed to enhance predictive maintenance strategies by monitoring the condition of rotating machinery through the measurement of vibrations and other key parameters. The WISE-2410 is equipped with wireless communication capabilities using LoRaWAN protocol, making it ideal for deployment in wide-scale industrial environments.

## Working Principles

The WISE-2410 operates by measuring vibration data from machinery in three axes (X, Y, and Z) using an integrated accelerometer. It collects acceleration data and computes spectral and time-domain features, including root mean square (RMS) vibration velocity, acceleration, and displacement. The device also measures temperature to provide additional context for understanding vibration data. This data is then sent wirelessly via LoRaWAN to a central gateway or application, where it can be further analyzed to determine machine health and anticipate potential failures.

## Installation Guide

1. **Pre-Installation Check:**
   - Ensure the desired location for the sensor installation is within the coverage range of the LoRaWAN gateway.
   - Verify that the environmental conditions (temperature, humidity) are within the sensor's operational specifications.

2. **Physical Mounting:**
   - Attach the WISE-2410 securely to the machine surface using appropriate mounting accessories. It should be placed as close to the primary vibration source of the machine as possible to ensure accurate readings.

3. **Configuration:**
   - Use the WISE Studio software or a compatible cloud platform to configure the sensor settings such as sampling rate, transmission intervals, and threshold settings.
   - Set up the LoRaWAN network parameters, including DevEUI, AppEUI, and AppKey, to integrate it with your existing IoT infrastructure.

4. **Power Setup:**
   - Ensure the sensor batteries are adequately charged or replace them with new ones if necessary.
   - Power on the device and ensure it successfully joins the LoRaWAN network.

## LoRaWAN Details

- **Frequency Bands:** The WISE-2410 supports multiple regional frequency bands compliant with LoRaWAN specifications, including EU868, US915, AS923, and others, allowing flexible deployment globally.
- **Network Integration:** The sensor can be easily integrated into existing LoRaWAN networks, offering support for Over-The-Air (OTA) activation and Activation By Personalization (ABP).
- **Data Transmission:** The WISE-2410 transmits data at regular intervals configured during setup, with available settings to optimize transmission frequency based on battery life and data criticality.

## Power Consumption

The WISE-2410 is designed to operate on battery power, with consumption rates optimized for long-term use. Its power consumption is significantly influenced by the transmission frequency, sensor activity, and environmental factors. On typical duty cycles with standard settings, the sensor can operate for several years on its integrated battery, providing a maintenance-free solution for condition monitoring.

## Use Cases

- **Predictive Maintenance:** By monitoring vibration levels and detecting anomalies, the WISE-2410 helps in predicting machine failures, reducing downtime, and extending equipment lifespan.
- **Industrial Automation:** Used in factories and production lines to monitor the health of motors, pumps, fans, and compressors, ensuring efficient and continuous operation.
- **Remote Monitoring:** Ideal for applications where wired solutions are impractical, such as remote or hazardous locations.

## Limitations

- **Data Latency:** As the WISE-2410 uses LoRaWAN, there may be a delay in data transmission compared to real-time wired solutions, which might not suit critical applications requiring immediate alerts.
- **Battery Life Dependence:** The operational life is heavily dependent on the frequency of data transmission and environmental conditions. Frequent transmissions for real-time data can drain the battery faster.
- **Coverage Limitations:** The performance of LoRaWAN is contingent on the availability of network coverage. In regions with limited gateway coverage, data transmission may be unreliable.
- **Environmental Constraints:** While robust, extreme environmental conditions exceeding the specified operational limits may affect sensor performance or lifespan.

In conclusion, the ADVANTECH WISE-2410 is a powerful tool for enhancing industrial equipment maintenance strategies. Its wireless capabilities, coupled with long battery life and detailed vibration analysis, offer a compelling solution for organizations looking to modernize their predictive maintenance efforts.