## Technical Overview for ELLENEX - Dus2 L

### Product Overview
The ELLENEX Dus2 L is a compact, efficient, and reliable IoT sensor solution designed specifically for monitoring water and wastewater flow. It is equipped with an ultrasonic sensor that precisely measures liquid level, providing key data for water management systems. The sensor communicates via the LoRaWAN protocol, making it ideal for LoRa-based network deployments. 

### Working Principles
The Dus2 L employs ultrasonic technology to measure the distance to a target surface. It emits short ultrasonic pulses and measures the time it takes for the echo to return. By converting the time measurement into distance, the sensor determines the liquid level with high accuracy. The device accounts for variables such as temperature to ensure precise readings under various environmental conditions.

### Installation Guide
1. **Site Selection**:
   - Choose an appropriate location where the sensor can have a clear line of sight to the liquid surface without obstructions.
   - Ensure that the sensor is positioned at a stable mounting point.

2. **Mounting**:
   - Affix the sensor securely using brackets or mounting kits designed for the model.
   - Maintain a distance of at least 30cm above the maximum liquid level to ensure accurate readings.

3. **Orientation**:
   - Position the sensor such that the ultrasonic beam is perpendicular to the liquid surface.
   - Avoid angles or setups that might introduce reflections or false readings.

4. **Powering**:
   - Activate the device by inserting the batteries following the polarity instructions. Confirm the integrity of the battery compartment seal to avoid leakages.
   - Verify the battery indicator for sufficient charge (if applicable).

5. **Configuration**:
   - Use the companion application or device interface to configure the LoRaWAN parameters, including frequency, data rate, and network credentials.
   - Calibrate the sensor, if necessary, using the application's calibration settings, inputting known distance measurements.

### LoRaWAN Details
- **Frequency Band**: Dus2 L supports multiple frequency bands depending on regional regulations (e.g., EU868, US915).
- **Data Rate**: Supports adaptive data rate to optimize battery life and network performance.
- **Network Compatibility**: The device is compatible with standard LoRaWAN network infrastructures and can be connected to various gateways and network servers.
- **Security**: Utilizes LoRaWAN security protocols, including encryption of data packets via AES-128 encryption.

### Power Consumption
- The Dus2 L is designed for low power consumption, optimized through its use of the LoRaWAN protocol and adaptive data rate.
- **Sleep Mode Current**: <10 µA.
- **Active Mode Current**: Dependent on transmission power and frequency, typically maxing out around 30 mA during data transmission.
- **Battery Life**: Depending on transmission interval and environmental conditions, the integrated battery can last up to 5 years.

### Use Cases
- **Water Level Monitoring**: Ideal for reservoirs, tanks, and environmental water sources.
- **Wastewater Management**: Effective in monitoring the flow and levels in wastewater treatment facilities.
- **Flood Monitoring**: Applied in flood-prone areas for continuous water level monitoring to issue alerts.
- **Agricultural Irrigation**: Used in agricultural settings to monitor irrigation ditches and ponds.

### Limitations
- **Obstruction Sensitivity**: Objects or debris can interfere with ultrasonic signals, potentially leading to inaccurate measurements.
- **Environmental Conditions**: Extreme temperatures or high humidity might affect sensor accuracy and battery life. Protective enclosures are recommended in harsh environments.
- **Transmission Range**: While LoRa technology provides extended range, obstacles like buildings or dense foliage can attenuate signal strength.
- **Data Latency**: Due to LoRaWAN's nature, real-time monitoring applications might encounter data transmission delays.

### Final Remarks
The ELLENEX Dus2 L is a versatile and robust solution for liquid level measurement in diverse IoT applications. Proper installation and maintenance ensure reliable performance while leveraging the benefits of LoRaWAN connectivity for efficient data management.