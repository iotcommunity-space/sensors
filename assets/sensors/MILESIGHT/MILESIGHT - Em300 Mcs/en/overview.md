### Technical Overview for MILESIGHT - EM300-MCS

#### Introduction

The MILESIGHT EM300-MCS is a compact and robust LoRaWAN-based magnetic contact switch sensor. It's designed for applications requiring the detection of door or window status (open/closed). By incorporating the LoRaWAN connectivity standard, the EM300-MCS is ideal for smart building automation, security monitoring, and other IoT applications where long-range communication is critical.

#### Working Principles

The EM300-MCS operates on the principle of magnetic field detection. It comprises two main components: a magnetic sensor unit and a magnet. When the magnet is moved away from the sensor unit (indicating an open status), the change in magnetic field triggers the sensor to send an alert. Conversely, when the magnet is brought back within proximity (indicating a closed status), another alert is sent to indicate the closure. This mechanism allows remote monitoring of entry and exit points.

#### Installation Guide

1. **Preparation:**
   - Ensure coverage by checking for LoRaWAN network availability in the installation area.
   - Gather necessary tools, including a drill and screws for mounting the sensor and magnet.

2. **Mounting the Sensor:**
   - Position the sensor unit on the stationary frame of the door or window.
   - Use screws or adhesive to secure the sensor firmly. Ensure the surface is clean and dry for optimal adhesion if using adhesives.

3. **Mounting the Magnet:**
   - Align the magnet with the sensor on the door or window itself.
   - Maintain a gap of approximately 15 mm or less between the sensor and magnet in the closed position.

4. **Configuration:**
   - Configure the sensor using the provided MILESIGHT configuration tool or mobile app to join your LoRaWAN network. Input the necessary network credentials, including the device’s unique identifier (EUI).

5. **Testing:**
   - Test the installation by opening and closing the door/window and confirming that the sensor sends appropriate alerts to the LoRaWAN network.

#### LoRaWAN Details

- **Frequency Bands:** The EM300-MCS operates in various frequency bands, compliant with local regulations, including EU868, US915, AS923, among others.
- **Communication:** Utilizes Class A LoRaWAN communication for event-triggered alerts, ensuring low power consumption and efficiency.
- **Range:** Offers a communication range of up to several kilometers in open spaces, depending on environmental conditions and gateway placement.

#### Power Consumption

- **Battery Life:** Powered by a replaceable 4000 mAh battery, the sensor boasts a battery life of up to 5 years under typical conditions, depending on the frequency of status changes and reporting intervals.
- **Efficiency:** Sleep mode is engaged during inactivity periods, significantly reducing power usage and prolonging battery life.

#### Use Cases

1. **Security Monitoring:** Ideal for detecting unauthorized entry by monitoring door and window statuses in residential or commercial buildings.
2. **Building Automation:** Integrates with smart building systems to automate lighting, heating, or cooling based on door/window status.
3. **Warehouse Management:** Tracks access to storage areas, ensuring security and operational efficiency.
4. **Healthcare Facilities:** Monitors patient room doors for safety and management of controlled access areas.

#### Limitations

- **Range Restrictions:** Effective range is dependent on environmental factors and may be reduced in dense urban areas or buildings with thick walls.
- **Magnetic Dependency:** The sensor’s effectiveness is reliant on the correct alignment and proximity of the magnet, which may be challenging on uneven surfaces or with misaligned installations.
- **Battery Replacement:** Though designed for long life, battery replacement will be necessary after several years, dependent on usage patterns.

In summary, the MILESIGHT EM300-MCS is a versatile and efficient solution for wireless location status monitoring via LoRaWAN, suitable for a wide range of applications but requiring careful installation and maintenance to maximize its benefits.