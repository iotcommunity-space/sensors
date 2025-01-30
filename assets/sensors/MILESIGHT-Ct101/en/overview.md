## Technical Overview for MILESIGHT - CT101

### Introduction
The MILESIGHT CT101 is a LoRaWAN-enabled PIR (Passive Infrared) sensor designed to detect motion and occupancy with high precision in various environments. It is an essential component of smart building and facility management systems, offering insights into space utilization and enhancing automation capabilities.

### Working Principles
The CT101 employs Passive Infrared (PIR) technology, which detects changes in infrared radiation levels caused by the movement of objects within its field of view. The sensor utilizes a pyroelectric component that senses infrared radiation emitted by warm bodies. When a temperature change is detected due to movement, the sensor triggers an alarm signal, which is transmitted via the LoRaWAN network.

**Key Features:**
- **High sensitivity PIR sensing:** Ensures accurate detection of motion up to a specified range.
- **Configurable detection range and angle:** Adjustable parameters for various installation requirements.

### Installation Guide

1. **Site Selection:**
   - Mount the CT101 at a height between 2 to 3 meters above the ground for optimal coverage.
   - Ensure there are no obstructions such as furniture or partitions that may block the sensor's field of view.

2. **Mounting:**
   - Use the included mounting bracket and screws to affix the sensor to the desired location on surfaces such as walls or ceilings.
   - The sensor can be tilted to adjust the detection area as needed.

3. **Power Setup:**
   - Insert the required batteries (typically AA or lithium batteries) following the polarity instructions marked on the device.
   - Ensure batteries are fully charged to maximize sensor uptime and minimize maintenance intervals.

4. **Connection to LoRaWAN Network:**
   - Ensure the CT101 is within the communication range of a LoRaWAN gateway.
   - Using the provided instructions, register and configure the device's DevEUI, AppEUI, and AppKey on your network server to establish secure LoRaWAN communication.

5. **Calibration and Testing:**
   - Perform initial tests by walking in front of the sensor to ensure it detects movement and communicates the event appropriately.

### LoRaWAN Details

- **Frequency Bands:** Compatible with standard LoRaWAN frequency bands (e.g., EU868, US915), enable the configuration based on regional requirements.
- **Communication Range:** Typically up to several kilometers in open environments, dependent on network setup and environmental factors.
- **Network Security:** Employs standard LoRaWAN security measures, including 128-bit AES encryption for secure data transmission.

### Power Consumption

The CT101 is designed for low power consumption, extending the battery life up to several years depending on usage. The device employs sleep mode when inactive to preserve battery life, awakening only during active motion detection and for scheduled communication events.

### Use Cases

- **Building Automation:** Part of smart energy management systems for automating lighting and HVAC control based on occupancy.
- **Security Systems:** Enhance security by detecting unauthorized movement within monitored areas.
- **Space Utilization Analytics:** Collect data for informing space utilization strategies in commercial and office environments.

### Limitations

- **Detection Range Limitation:** Limited to a specific radius and angle, which may not be suitable for very large spaces or areas with obstructed line of sight.
- **Environmental Constraints:** Performance might be affected in extremely hot environments or areas with high levels of electromagnetic interference.
- **LoRaWAN Dependency:** Requires a robust LoRaWAN network infrastructure for reliable data transmission.

### Conclusion
The MILESIGHT CT101 is an advanced PIR sensor leveraging LoRaWAN technology to provide dependable occupancy and motion detection solutions. It is ideal for integrators seeking energy-efficient and low-maintenance sensor options for large-scale building and security applications. Proper installation and network setup are critical to maximizing the sensor's capabilities and range.