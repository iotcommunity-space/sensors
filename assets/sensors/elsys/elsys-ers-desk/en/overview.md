### Technical Overview of ELSYS - ERS Desk

#### Working Principles

ELSYS - ERS Desk is an advanced IoT sensor specifically designed to monitor desk occupancy in real-time. It uses passive infrared (PIR) sensing technology to detect human presence by identifying heat emitted from a body as it moves in the sensor's field of view. The ERS Desk sensor operates over the LoRaWAN protocol, enabling long-range, low-power communication, making it ideal for office environments and buildings where centralized monitoring is essential.

#### Installation Guide

1. **Site Preparation**:
   - Choose a central location under or above the desk to ensure optimum visibility and efficiency.
   - Avoid locations near heating vents or direct sunlight to prevent false detections.

2. **Mounting**:
   - Attach the sensor using the provided adhesive pads or screws.
   - Ensure the sensor's detection range covers the desired area beneath or above the desk.

3. **Configuration**:
   - Power on the sensor using the internal batteries.
   - Use the ELSYS app or a compatible LoRaWAN network server to configure the device settings, including sensitivity, reporting interval, and network credentials.

4. **Connection to LoRaWAN**:
   - The sensor will automatically connect if the LoRaWAN network coverage is available.
   - Verify the connection via the network management interface to ensure data transmission.

#### LoRaWAN Details

- **Frequency Bands**: Supports multiple frequency bands including EU868, US915, AS923, etc., contingent upon regional regulations.
- **Data Rates**: Utilizes adaptive data rate (ADR) to optimize communication based on the signal quality, enhancing both battery life and network capacity.
- **Encryption**: Data transmission is secured using AES-128 encryption to ensure privacy and integrity.
- **Network Integration**: Compatible with standard LoRaWAN gateways and network servers, allowing seamless integration into existing IoT ecosystems.
  
#### Power Consumption

- **Battery**: Operates on replaceable AA lithium batteries designed for extended use, offering a typical lifespan of 10 years under optimal conditions.
- **Power Modes**: Includes sleep mode to minimize energy consumption when not actively detecting presence.
- **Efficiency**: Reports and communicates data only upon occupancy detection or at predefined intervals to conserve power.

#### Use Cases

- **Office Space Management**: Optimizes the use of workspace by providing real-time data on desk occupancy, helping facility managers allocate resources efficiently.
- **Smart Building Integration**: Can be integrated into smart building systems for automated control of lighting, HVAC, and other systems based on occupancy data.
- **Remote Work Monitoring**: Assists organizations in tracking and analyzing workspace utilization trends, aiding in remote work policy formulation.

#### Limitations

- **Field of View Constraints**: Limited to detecting movement within its specific range, which may not cover the entire desk area if improperly positioned.
- **Interference Factors**: Presence detection can be affected by environmental conditions such as unusual temperature variations or obstructions between the sensor and target area.
- **Network Dependency**: Requires a stable LoRaWAN network for consistent data reporting, which could be a limitation in areas with poor coverage.
- **Update Frequency**: Predetermined reporting intervals might not capture rapid changes if not suitably configured, potentially leading to delays in real-time occupancy updates.

Overall, the ELSYS - ERS Desk sensor is a robust solution for monitoring desk occupancy, with ease of installation and integration into LoRaWAN networks. However, careful consideration of placement and network conditions is key to maximizing its performance and accuracy.