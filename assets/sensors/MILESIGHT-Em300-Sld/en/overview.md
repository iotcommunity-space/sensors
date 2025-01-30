### Technical Overview of MILESIGHT - EM300-SLD Sensor

#### Introduction
The MILESIGHT EM300-SLD is a compact, robust, and efficient LoRaWAN sensor designed for real-time monitoring of liquid presence or absence. It is widely used in applications such as detecting water leaks to prevent water damage, monitoring environmental conditions, and supporting facility management with timely alerts.

#### Working Principles
The EM300-SLD employs capacitive sensing technology to detect the presence of water or other conductive liquids on its surface. It operates by emitting an electrical signal from its probe; when a liquid comes in contact with the probe, it alters the capacitive field, indicating the presence of liquid. The sensor then transmits the collected data over a LoRaWAN network to a server for analysis and notification handling.

#### Installation Guide

1. **Site Evaluation**: Identify areas prone to liquid exposure. Common sites include under pipes, near sump pumps, in basements, or around water tanks.

2. **Mounting the Sensor**:
   - Securely mount the sensor using the provided adhesive pad or mounting screws. Ensure the flat sensing probe is positioned in such a way that liquid contact is detected immediately upon a leak.
   - Avoid placing the sensor in highly metallic environments that could dampen signal strength.

3. **Activation**:
   - Open the enclosure and install the battery, ensuring proper orientation as indicated.
   - Use a magnet to trigger the device into pairing mode with the LoRaWAN network.

4. **Configuration**:
   - Use the MILESIGHT IoT configuration app to set sensor parameters like data transmission intervals and thresholds.
   - Configure network settings to join a LoRaWAN gateway by entering the necessary network credentials (Device EUI, App EUI, and App Key).

5. **Testing**:
   - Simulate a liquid contact to verify that the sensor detects and transmits the alert signal correctly.
   - Check connectivity status on your LoRaWAN network dashboard to ensure consistent data reception.

#### LoRaWAN Details
- **Frequency Bands**: EM300-SLD supports multiple frequency bands, including EU868, US915, AS923, among others, depending on the regulatory domain.
- **Class A Device**: The sensor operates in Class A mode, facilitating bi-directional communication with downlink capability immediately after an uplink transmission.
- **Data Encryption**: Utilizes AES-128 algorithm to encrypt data ensuring secure communication over the network.
- **Communication Range**: The EM300-SLD can communicate up to 10 km in open environments and around 1-3 km in urban settings, depending on geographical conditions and obstructions.

#### Power Consumption
- The sensor operates on a replaceable 4000 mAh Li-SOCl2 battery.
- With optimization settings (e.g., transmission interval set to 20 minutes), the battery can last up to 10 years, making it highly energy-efficient for long-term monitoring.
- The device enters a low-power sleep mode when inactive to conserve energy further.

#### Use Cases
- **Leak Detection**: Suitable for alerting facility managers about potential water leaks in commercial buildings, data centers, and residential complexes.
- **Flood Monitoring**: Deployed in flood-prone areas for early warnings.
- **Remote Environmental Monitoring**: Ideal for areas where regular manual inspection is unfeasible, such as remote pipelines and utility rooms.

#### Limitations
- **Limited Sensor Range**: The EM300-SLD is designed for point detection and may require multiple units for extensive coverage.
- **Signal Interference**: Performance may degrade in environments with strong electromagnetic interference or dense metal structures.
- **Static Installation**: Once installed, relocation requires careful re-evaluation to ensure optimal placement and connectivity.
- **Sensitivity to Conductive Liquids**: It is optimized for liquids with a conductive property and may not effectively detect non-conductive liquids.

In summary, the MILESIGHT EM300-SLD is a reliable LoRaWAN device tailored for applications needing prompt liquid detection. Its balance of low power consumption, secure communication, and flexible configuration makes it a valuable tool in modern IoT ecosystems focused on asset and facility protection.