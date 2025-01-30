### Technical Overview: ORBIWISE - Custom Orbiwise

**Introduction**

The ORBIWISE - Custom Orbiwise is a sophisticated Internet of Things (IoT) device designed for efficient and robust connectivity in Smart City, Agriculture, Industrial, and Environmental Monitoring applications. By leveraging LoRaWAN technology, the device enables long-range data transmission with low power consumption, making it ideal for scenarios requiring sparse maintenance and prolonged battery life.

---

### Working Principles

**LoRaWAN Technology**

ORBIWISE utilizes the LoRaWAN protocol, a Low Power Wide Area Network (LPWAN) specification intended for wireless battery-operated devices in regional, national, or global networks. Its star-of-stars architecture involves gateways relaying messages between end-devices and a central network server.

**How ORBIWISE Operates**

1. **End Devices/Nodes:** These devices collect sensor data and transmit it over long distances using LoRa radio frequencies.
2. **Gateways:** These serve as bridges, forwarding messages between nodes and network servers. With its high receiver sensitivity, ORBIWISE can communicate over several kilometers or miles.
3. **Network Server:** This controls data routing and deduplication and manages adaptive data rate features.

**Installation Guide**

1. **Site Survey and Planning:**
   - Evaluate the area for optimal placement concerning signal strength and line of sight.
   - Determine the density of devices to ensure minimal interference and maximum coverage.

2. **Physical Installation:**
   - Mount the nodes in areas with minimal physical obstructions for better signal transmission.
   - Ensure gateways are installed at strategic locations, preferably elevated, to maximize range.

3. **Configuration:**
   - Use the provided configuration tool to set up node parameters, including DevEUI, AppKey, and AppEUI.
   - Integrate with the LoRaWAN network server through supplied configuration scripts.

4. **Testing:**
   - Conduct tests to ensure reliable data transmission from nodes to the network server.
   - Optimize settings based on initial tests for data rate, frequency, and duty cycle.

---

### LoRaWAN Details

**Frequency Bands:** ORBIWISE supports multiple regional frequency bands, including EU868, US915, AS923, AU915, and others, aligning with local regulations.

**Data Rates:** Utilizes a range of data rates from 0.3 kbps to 50 kbps, adjustable based on distance, payload size, and required data throughput.

**Security:** Implements end-to-end AES-128 encryption to secure the communication between end-devices and servers.

---

### Power Consumption

ORBIWISE is engineered for ultralow power consumption:

- **Sleep Mode:** Typically around 1.5 to 2 µA, preserving battery life when inactive.
- **Active Mode:** Consumption varies based on data transmission rates but usually remains under 50 mA.
- **Duty Cycle Management:** Ensures minimal power usage by optimizing the number of transmissions. Adaptive Data Rate (ADR) adjusts power output according to connection quality.

**Battery Life:** Depending on usage patterns, ORBIWISE can operate for up to 5-10 years on standard batteries, assuming intermittent transmission conditions tailored to the application.

---

### Use Cases

1. **Smart City Applications**: Remote monitoring of water levels, waste management, parking systems, and traffic controls.
2. **Agriculture Monitoring**: Soil moisture sensors, weather station data logging, livestock tracking.
3. **Industrial Facilities**: Pipeline monitoring, predictive maintenance of machinery, asset tracking.
4. **Environmental Monitoring**: Air quality sensors, forest fire detection, and humidity tracking.

---

### Limitations

- **Range**: Line-of-sight limitations may reduce the effective communication range, especially in urban or forested areas.
- **Bandwidth**: Limited data bandwidth best suits applications with low data throughput requirements.
- **Latency**: Not suitable for applications requiring real-time data due to inherent latencies in LPWAN systems.
- **Regulatory Constraints**: Different regions have specific compliance requirements; ensure correct configuration to adhere to local regulations.

---

**Conclusion**

ORBIWISE - Custom Orbiwise presents a reliable and efficient solution for IoT connectivity needs, leveraging the strengths of LoRaWAN for comprehensive remote data acquisition with minimal power usage. Its optimal performance in non-real-time applications makes it a vital component in expanding IoT networks across various industries, though considerations regarding range, bandwidth, and regulatory compliance must be taken into account during deployment.