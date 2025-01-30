### Technical Overview for ZANE - Zdoor (ZANE)

The ZANE - Zdoor (ZANE) is an advanced IoT-enabled door sensor designed to monitor door status in various environments. It utilizes LoRaWAN technology for long-range, low-power consumption data transmission, making it ideal for remote or large-scale deployments where traditional wireless communication methods may be inefficient.

#### Working Principles

The Zdoor sensor operates on the principle of magnetic contact detection. It consists of two main components: the sensor unit and a magnetic contact. When installed, the magnetic field is altered when the door is opened or closed, which is detected by the sensor unit. This change in state is then wirelessly communicated via LoRaWAN to a central hub or gateway for processing, logging, or triggering action.

#### Installation Guide

1. **Pre-Installation Preparation:**
   - Verify that the LoRaWAN gateway is within range.
   - Ensure the mounting surface is clean and dry.
   - Gather required tools: screwdriver, drill (if needed), and mounting adhesive or screws.

2. **Physical Mounting:**
   - Affix the sensor unit to the door frame using screws or industrial adhesive.
   - Align the magnetic contact directly opposite the sensor on the door itself.
   - Ensure a gap no larger than 10mm between the sensor and magnet for accurate detection.

3. **Configuration:**
   - Insert batteries in the sensor unit (batteries come with the device; check orientation).
   - Power on the sensor and use the accompanying app to integrate it with your LoRaWAN network.
   - Set the parameters such as data transmission intervals and sensitivity according to your requirements.

4. **Testing:**
   - Open and close the door to verify the sensor detects the states correctly.
   - Check data reception on the connected network to ensure communication.

#### LoRaWAN Details

- **Frequency Bands:** Compatible with multiple frequency bands including EU868, US915, AS923, depending on regional regulation.
- **Communication Range:** Up to 15 km in rural areas and up to 5 km in urban settings.
- **Data Rate:** Supports variable data rates, optimizing for power or latency as needed (ADR - Adaptive Data Rate).
- **Network Integration:** Easily integrates with existing LoRaWAN network servers typically using OTAA for secure and scalable deployment.

#### Power Consumption

- **Battery Type:** Typically powered by two AA lithium batteries.
- **Operational Current:** Approximately 15uA in idle mode, and up to 120mA during transmission.
- **Battery Life:** Expected to last up to 5 years, depending on transmission frequency, environmental conditions, and settings.

#### Use Cases

- **Smart Cities:** Monitoring public facility access points.
- **Industrial Facilities:** Tracking door status in warehouses to optimize logistics processes.
- **Residential Homes:** Integrating with home automation systems for security and convenience.
- **Agricultural Applications:** Monitoring access to barn doors or storage facilities for improved security and operational insights.

#### Limitations

- **Interference:** Metal structures and dense building materials may affect the communication range and reliability. Proper site survey is recommended before deployment.
- **Installation Constraints:** Requires precise alignment of the sensor and magnet for optimal performance, which may be challenging in certain door designs.
- **Battery Dependency:** While the battery life is long, environments with extreme temperatures may affect battery performance and lifespan.
- **Latency:** With a focus on low power, there might be a delay in data transmission compared to real-time systems—an important consideration for critical safety applications.

The ZANE - Zdoor is a versatile and efficient solution for door state monitoring in various applications, offering long-range connectivity and smart integration possibilities in IoT ecosystems. Understanding its operational nuances and requirements is essential for maximizing its potential and ensuring reliable performance.