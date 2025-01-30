## Technical Overview of BROWAN - Door and Window Sensor

### Introduction
The BROWAN Door and Window Sensor is a compact, battery-operated device designed for monitoring the open/close status of doors or windows. Utilizing LoRaWAN technology, it offers long-range wireless communication, making it suitable for smart buildings, security systems, and IoT applications requiring consistent monitoring of entry points.

### Working Principles
The BROWAN sensor operates by detecting the presence or absence of a magnetic field. It consists of two main components: a sensor unit and a magnet. When the door or window is closed, the magnet aligns with the sensor, creating a closed-loop circuit. When opened, the magnet moves away from the sensor, breaking the circuit and triggering a status change. This change is transmitted over a LoRaWAN network to a central hub or cloud platform for processing or alert generation.

### Installation Guide
1. **Components:** The package includes one sensor unit and one magnet.
2. **Placement:** The sensor unit should be mounted on the static frame (door/window frame), while the magnet is placed on the moving part (door/window).
   - The optimal distance between the sensor and the magnet should not exceed 10mm to ensure reliable operation.
3. **Mounting:** Use the adhesive strips or screws provided in the package to secure both components.
4. **Activation:** Insert the batteries into the sensor unit. An LED indicator will flash to signify power-up.
5. **Registration:** Follow the provided instructions to register the device on your LoRaWAN network. This typically involves scanning a QR code using a network application for automatic configuration.
6. **Testing:** Open and close the door/window to ensure the sensor responds correctly and transmits data.

### LoRaWAN Details
- **Frequency Bands:** Compatible with global LoRaWAN frequency bands (e.g., EU868, US915).
- **Data Rate:** Supports adaptive data rate (ADR) for optimizing the data transmission rate and battery life.
- **Class Type:** Class A device, which is the most energy-efficient class for end devices, transmitting data only upon detecting status changes.
- **Network Server Compatibility:** Works with major LoRaWAN network servers like TTN (The Things Network), Loriot, ChirpStack, etc.

### Power Consumption
- **Battery Type:** Typically powered by a CR2450 or similar coin cell battery.
- **Battery Life:** Estimated at over two years, depending on the frequency of door/window use and the configured transmission interval.
- **Power-saving Features:** Implements power-saving algorithms to minimize energy consumption when the device is idle or when the network is not immediately available.

### Use Cases
- **Home Security:** Alerts homeowners when a door or window is opened, providing real-time security updates.
- **Access Control Systems:** Used in office buildings to monitor entry points and ensure compliance with access policies.
- **Industrial Facilities:** Monitors unauthorized access to restricted areas, ensuring operational security.
- **Smart Buildings:** Integrates into building management systems for automated climate control by detecting open windows, optimizing energy consumption.

### Limitations
- **Range Dependency:** LoRaWAN range can be affected by physical obstructions and is typically optimal in open spaces; performance may vary indoors with thick walls.
- **Battery Dependency:** The sensor requires regular battery replacements, which could be a limitation in applications where maintenance access is challenging.
- **Operation Range:** The sensor and magnet must be precisely aligned and within a specific distance to function correctly. Improper installation may lead to malfunctions.
- **Network Dependency:** Requires a compatible LoRaWAN infrastructure, which may not be available in all regions or environments.

### Conclusion
The BROWAN Door and Window Sensor is a reliable and versatile solution for a wide range of security and smart monitoring applications. With its ease of installation, low power consumption, and robust LoRaWAN connectivity, it is well-suited for modern IoT ecosystems. However, potential users must consider its limitations, particularly in terms of installation precision, network availability, and battery management.