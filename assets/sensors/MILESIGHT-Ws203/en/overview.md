### Technical Overview: MILESIGHT - WS203 (LoRaWAN PIR & Light Sensor)

#### Working Principles
The MILESIGHT WS203 is a versatile LoRaWAN-compatible sensor specifically designed for detecting motion (Passive Infrared Sensor, PIR) and measuring light levels. The sensor utilizes PIR technology to detect changes in infrared radiation, emitted by objects in its field of view. This allows it to effectively sense motion. Additionally, the WS203 is equipped with a photodiode that measures light intensity, providing illuminance data that is useful for various applications, such as automatic lighting control.

#### Installation Guide
1. **Location Selection**: Choose a location within the maximum communication range of the LoRaWAN gateway. Consider areas with optimal line-of-sight and minimal physical obstructions to ensure effective data transmission.

2. **Mounting the Sensor**: 
   - Mount the sensor at a height of 2 to 3 meters for optimal motion detection.
   - Securely attach the device using the provided screws or adhesive tape, depending on whether a temporary or permanent installation is desired.

3. **Orientation**: Ensure the sensor is oriented towards the area of interest to maximize coverage for both movement and light detection.

4. **Powering the Device**: The WS203 comes with a built-in lithium battery. Ensure that the battery is securely in place before sealing the sensor.

5. **Configuration**: Configure the sensor using the MILESIGHT IoT Cloud platform or relevant software. Set parameters such as data transmission frequency, threshold levels for motion detection, and light intensity sensitivity.

6. **Testing**: Perform a walk-test and light level check to ensure sensor accuracy and proper functionality. Adjust settings as necessary based on initial test results.

#### LoRaWAN Details
- **Frequency Bands**: Supports various regional frequency bands (EU868, US915, AU915, etc.), ensuring compliance with local regulations.
- **Communication Range**: Typically up to 15 km in rural areas and 2-5 km in urban areas, subject to environmental conditions and obstacles.
- **Class Type**: Class A or Class C depending on configuration, enabling bidirectional communication with a focus on low power consumption.
- **Data Rates**: Supports adaptive data rates to enhance range and energy efficiency.

#### Power Consumption
The WS203 is highly energy-efficient, benefiting from LoRaWAN's low-power wide-area network technology. It typically consumes:
- **Idle Mode**: Very low current, extending battery life.
- **Active Mode (Motion Detected/Light Measurement)**: Slightly increased power draw, but optimized through configurable reporting intervals to balance responsiveness and battery longevity.
- **Battery Life**: Depending on configuration and usage, the battery can last several years (up to 10 years at one message per hour).

#### Use Cases
1. **Smart Lighting**: Automatically control lighting based on real-time occupancy and ambient light levels, contributing to energy savings.
2. **Security Systems**: Function as part of an intelligent security setup to detect unauthorized presence in critical areas.
3. **Facility Management**: Collect data to optimize space usage and operational efficiency in offices and public buildings.
4. **Environmental Monitoring**: Provide light intensity data as part of broader environmental sensor networks.

#### Limitations
- **Range Dependence**: The effective communication range varies based on topology and physical obstructions; optimal placement near gateways is crucial.
- **Motion Detection Area**: Limited to the direct line-of-sight; reduced sensitivity beyond recommended installation height and coverage area.
- **Light Sensitivity**: While generally reliable, very low-light conditions and extreme light variants may impact the accuracy of illuminance measurements.
- **Battery Limitation**: Although designed for long-term operation, battery replacement or recharge is necessary when deployed in high-communication-frequency setups.

By understanding these factors, users can effectively deploy the MILESIGHT WS203 sensor to enhance automated systems across various domains.