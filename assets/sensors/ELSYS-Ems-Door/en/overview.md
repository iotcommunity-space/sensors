## Technical Overview: ELSYS - Ems Door

**Product Overview:**
The ELSYS Ems Door Sensor is a compact and reliable device designed for detecting the state of a door (open or closed) using LoRaWAN technology. It is ideal for various applications, including security systems, facility management, and smart building automation. Its robust performance and low power consumption make it a suitable choice for long-term applications.

### Working Principles
The ELSYS Ems Door sensor employs a magnetic reed switch to detect the open or closed status of a door. When the door changes state, the magnetic field interrupts or completes the circuit within the reed switch, which is then registered by the sensor unit. This information is transmitted over a LoRaWAN network to a central server or gateway, where it can be analyzed or processed for automated workflows.

### Installation Guide
1. **Unpack the Device:** Ensure all components, including the sensor body and magnet, are available.
2. **Choose a Mounting Location:** 
   - Place the sensor on the stationary part of the door frame.
   - Attach the magnet to the moving part (the door itself), aligning it with the sensor. 
3. **Mount the Sensor:**
   - Clean the surfaces where the sensor and magnet will be attached.
   - Use the adhesive tape provided or screw the components in place for a more robust installation.
4. **Configure the Device:**
   - Use the DIP switches or the NFC interface for local configuration.
   - Optionally, use the ELSYS Configuration app to set parameters such as reporting intervals and activation settings.
5. **Activate the Sensor:**
   - Insert the batteries and ensure the sensor powers up.
   - Establish connectivity with the LoRaWAN network as per your network operator’s instructions.

### LoRaWAN Details
- **Frequency Bands:** Typically supports multiple sub-GHz frequencies (e.g., 868 MHz for Europe, 915 MHz for North America) depending on regional regulations.
- **Device Class:** Class A device with bi-directional communication support.
- **Join Method:** Supports over-the-air activation (OTAA) and activation by personalization (ABP).
- **Data Transmission:** The device sends data payloads consisting of the door’s state and optionally, battery level indicators.
- **Network Server Integration:** Compatible with major LoRaWAN network servers for seamless integration.

### Power Consumption
- **Primary Power Source:** Runs on disposable or rechargeable lithium batteries.
- **Battery Life:** Optimized for low power consumption, enabling operation for several years under typical reporting conditions (usually about 10 years on a single CR123A battery).
- **Duty Cycle and Reporting:** Configurable reporting intervals can significantly extend or reduce battery life based on usage needs.

### Use Cases
- **Security Systems:** Monitor access points in residential, commercial, and industrial settings, providing alerts for unauthorized or unexpected entries.
- **Facility Management:** Integrate with building management systems to automate heating, lighting and security systems based on door status.
- **Smart Home Automation:** Connect with home automation platforms to trigger events such as disarming alarms or notifying residents when doors are opened.
- **Logistics and Warehousing:** Track door openings in storage facilities to optimize operations and ensure security.

### Limitations
- **Range:** The performance is dependent on the LoRaWAN coverage quality; structures such as steel and concrete can affect signal propagation.
- **Environmental Constraints:** While designed for general use, extreme weather or exposure to moisture may impact reliability and lifespan.
- **Configuration Complexity:** Initial setup requires a basic understanding of LoRaWAN configuration and NFC or app usage.
- **Battery Dependency:** Long-term battery performance can vary based on environmental conditions and reporting frequency.

The ELSYS Ems Door sensor is engineered for a wide variety of applications with its robust design and reliable performance but requires adequate planning regarding installation and configuration to fully leverage its capabilities.