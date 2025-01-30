## Technical Overview for ADENUIS - Dry Contacts Sensor

The ADENUIS - Dry Contacts sensor is a versatile LoRaWAN device designed to interface with external systems, machinery, or environments that utilize dry contact closures. It serves as a bridge to capture the state changes of these contacts and transmit the data wirelessly for monitoring and control applications.

### Working Principles

The ADENUIS sensor operates by monitoring the open or closed state of dry contacts. These contacts do not supply voltage or current, making them suitable for interacting with various industrial and commercial equipment. When a connected device activates or deactivates a switch, the ADENUIS detects the change in status without impacting the contact’s inherent electrical properties. The sensor then encodes this state change into a data packet and transmits it via the LoRaWAN network to back-end systems for processing and analysis.

### Installation Guide

1. **Location and Positioning:**
   - Ensure the ADENUIS sensor is placed within an optimal range of your LoRaWAN gateway to maintain a strong wireless signal.
   - Mount the sensor on a stable surface near the equipment whose dry contacts are being monitored.

2. **Wiring the Dry Contacts:**
   - Identify the contacts you need to monitor on the external device.
   - Connect these contacts to the corresponding input terminals on the ADENUIS sensor using appropriate wiring standards (typically minimal gauge, insulated copper wire).

3. **Power Connection:**
   - ADENUIS may be powered by an internal battery or an external power source, depending on the model.
   - Ensure the power source is connected as per manufacturer instructions to avoid improper operation or sensor damage.

4. **Configuration:**
   - Program the sensor via the manufacturer's specified interface (typically a smartphone app or a web platform) to suit your specific use case, including setting up the LoRaWAN parameters.
   - Verify that the sensor is correctly paired with your LoRaWAN network by checking connectivity through the associated gateway.

### LoRaWAN Details

- **Frequency Band:** Compatible with multiple frequency bands, including EU868, US915, AS923, ensuring global usability.
- **Data Rate:** Supports configurations in compliance with the LoRaWAN standard, optimizing between range and data rate.
- **Network Security:** Ensures data integrity and privacy using AES-128 encryption, standard in LoRaWAN networks.
- **Activation Method:** Supports both Activation by Personalization (ABP) and Over-the-Air Activation (OTAA) for network integration.

### Power Consumption

- The ADENUIS sensor is designed to be power-efficient, featuring low-power modes that significantly extend battery life.
- Typical power consumption is low during idle states and when transmitting data, supported by a duty-cycle approach to minimize energy usage.

### Use Cases

- **Industrial Automation:** Monitoring the status of machines, conveyor belts, and automated gates for operational efficiency and maintenance alerts.
- **Building Management Systems:** Integration with fire alarm panels, security systems, or HVAC controls for centralized status monitoring.
- **Utility and Energy Management:** Tracking switch states in power grids or substations to enhance real-time remote diagnostics and management.

### Limitations

- **Range Dependencies:** The effective range is highly dependent on environmental conditions and obstacles between the sensor and the LoRaWAN gateway.
- **Dry Contacts Only:** Limited to applications where dry contact closures are present; not suitable for direct connections to active voltage or current signals.
- **Network Reliability:** Operational effectiveness depends on the reliability and coverage of the LoRaWAN network infrastructure within the use area.

The ADENUIS - Dry Contacts sensor offers a robust solution for converting physical switch states into actionable data over a LoRaWAN network, facilitating diverse connectivity use cases in both remote and urban environments.