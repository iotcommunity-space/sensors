## Technical Overview: BROWAN Water Leak Sensor

### Working Principles
The BROWAN Water Leak Sensor is designed to detect the presence of water and alert users through a LoRaWAN network. The sensor detects water presence through its conductive probes; when water comes into contact with these probes, it completes an electrical circuit. This change in circuit status triggers a signal to be sent via the LoRaWAN network, indicating a water leak event.

### Installation Guide
1. **Location Selection**: Place the sensor in areas where water leaks are potential risks, such as near pipes, dishwashers, sinks, or water heaters.
2. **Mounting**: The sensor can be placed on the floor or mounted on a wall. Ensure the probes are positioned where they can effectively detect water.
3. **Power Activation**: The device typically comes with a pre-installed battery. Ensure the battery is properly seated and the device is powered on. An LED indicator may signal power status upon activation.
4. **Network Configuration**: Follow the device's specific guide for configuring its connection to your LoRaWAN network. Ensure appropriate keys and identifiers (e.g., DevEUI, AppEUI) are correctly configured.
5. **Testing**: Simulate a leak to test sensor responsiveness. Ensure the device successfully sends alerts across the network to the intended application.

### LoRaWAN Details
- **Frequency Bands**: Supports various regional frequency plans (EU868, US915, etc.).
- **Network Class**: Typically operates as a LoRaWAN Class A device, focusing on ultra-low power consumption.
- **Data Transmission**: Sends short data packets detailing the leak status, battery level, and occasionally diagnostic information.
- **Range**: Effective communication ranges from several kilometers in rural areas to hundreds of meters in urban environments, depending on network and environmental conditions.

### Power Consumption
The BROWAN Water Leak Sensor is designed for low power consumption, crucial for battery-operated IoT devices. Operating as a Class A device, the sensor predominantly stays in a deep sleep mode, waking only to send data or upon triggering by water detection. Battery life can extend multiple years under normal operation due to infrequent and low-power communication events.

### Use Cases
- **Residential Monitoring**: Protect homes from potential water damage by placing sensors in bathrooms, kitchens, basements, or near water heaters.
- **Commercial Buildings**: Deploy in high-risk areas to prevent water damage in office buildings, especially in unattended areas such as basements and machine rooms.
- **Industrial Sites**: Monitor areas with high water usage or where equipment is sensitive to water damage, such as server rooms or production lines.
- **Utility Management**: Utility companies can preserve infrastructure by early leak detection in water supply systems.

### Limitations
- **Dependency on Network Coverage**: Performance heavily relies on adequate LoRaWAN network coverage, which may not be available in remote locations.
- **Water Detection Specificity**: The sensor requires direct contact with water, making early detection of slowly accumulating or non-contactable leaks challenging.
- **Potential Interference**: Physical obstructions or interference from dense building materials may affect signal transmission quality.
- **Battery Life**: Though designed for longevity, battery life can be diminished by frequent false triggering or more frequent reporting.

The BROWAN Water Leak Sensor presents a robust solution for proactive leak detection and prevention, leveraging IoT capabilities for effective asset and risk management.