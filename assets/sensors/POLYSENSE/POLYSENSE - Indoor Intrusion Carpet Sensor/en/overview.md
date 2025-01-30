## Technical Overview: POLYSENSE - Indoor Intrusion Carpet Sensor

The POLYSENSE Indoor Intrusion Carpet Sensor is a sophisticated device designed for real-time monitoring of unauthorized access in indoor environments. It provides discreet security by embedding sensors within carpeted flooring, making it ideal for residential, commercial, or secure facility applications.

### Working Principles

The POLYSENSE carpet sensor operates using pressure-sensitive technology. When a person steps on the carpet, the sensor detects changes in capacitance caused by the pressure and triggers an alarm or notification. The sensor integrates advanced signal processing to distinguish between human footsteps and other forms of pressure, such as furniture movement or pets, minimizing false positives. 

### Installation Guide

1. **Pre-Installation Assessment**: Conduct a thorough site survey to identify potential placement areas for optimal coverage and effectiveness without interference from heavy fixture locations.

2. **Hardware Setup**: 
   - Unroll the POLYSENSE carpet and position it in the designated area.
   - Ensure the fiber-optic detection network, embedded within the carpet, is properly aligned and free from physical damage or kinks.

3. **Connectivity Setup**:
   - Attach the accompanying connectivity module to the carpet sensor. The module interfaces with power and communication lines to a centralized monitoring system.
   - Pair the connectivity module with the local LoRaWAN gateway using the setup application on your computer or mobile device. Ensure that device identifiers and security credentials (DevEUI, AppEUI, AppKey) are accurate for secure network access.

4. **Testing and Calibration**:
   - After installation, conduct testing by walking over the carpet in different paths and speeds. Fine-tune sensitivity settings from the accompanying software interface to avoid false alarms.

5. **Integration**: 
   - Integrate the POLYSENSE system with existing security infrastructure, such as alarms and surveillance systems, using standard IoT protocols.

### LoRaWAN Details

- **Frequency Band**: Operates in the standard LoRaWAN frequency bands supported in the region (e.g., EU868, US915).
- **Network Range**: Capable of transmitting data over several kilometers in open space. Indoor performance depends on building structure and materials but typically covers several floors.
- **Data Transmission**: Utilizes Class A LoRaWAN devices standard, ensuring low power consumption and efficient network usage by transmitting data only upon detection events or scheduled intervals.

### Power Consumption

The POLYSENSE sensor is designed to be energy efficient, relying on a low-power architecture:
- **Battery Life**: Typically powered by long-lasting batteries with a lifespan of up to 2 years on a single charge, depending on usage and reporting frequency.
- **Power Options**: Offers additional power options such as a rechargeable battery pack or direct power through an AC adapter, allowing for flexibility in various installations.

### Use Cases

1. **Commercial Buildings**: Enhances security by monitoring unauthorized access to sensitive areas like offices or conference rooms after hours.
2. **Residential Security**: Provides peace of mind by detecting intruders within homes, especially in common entry areas or staircases.
3. **Retail Spaces**: Reduces theft by monitoring unauthorized movements or entry into staff-only areas.
4. **Industrial Facilities**: Monitors access in warehouses or production lines, ensuring safety and security compliance.

### Limitations

- **Environmental Conditions**: The POLYSENSE sensor is primarily designed for indoor use and may not perform optimally in high-humidity environments or those with extreme temperature variations.
- **False Positives**: Although sophisticated in distinguishing false alarms, it may still trigger from heavy machinery or objects falling onto the carpet.
- **Interference from Metallic Surfaces**: Placement near metal-based infrastructure can lead to interference issues affecting sensor performance.
- **Signal Penetration**: Challenges in LoRaWAN signal penetration through dense concrete structures may require additional gateways or repeaters for effective network coverage.

In summary, the POLYSENSE Indoor Intrusion Carpet Sensor provides a high level of indoor security through discreet floor-embedded sensing technology. With proper installation and calibration, it serves as an effective tool for preventing unauthorized access, though it requires optimal environmental conditions for best performance.