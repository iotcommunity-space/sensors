## Technical Overview for POLYSENSE - Bidirectional People Counting Sensor End Node

### Introduction
The POLYSENSE Bidirectional People Counting Sensor is a sophisticated IoT solution designed for accurately counting foot traffic in both directions using advanced mirrored reflection technology. This sensor is particularly adept for deployment in environments such as retail stores, museums, libraries, and other areas where understanding people flow is crucial.

### Working Principles
The POLYSENSE sensor uses mirrored reflection technology paired with a series of infrared (IR) beams to detect the movement of individuals. When a person passes through the sensing range, the infrared beam is disrupted, allowing the sensor to detect entry and exit directions. The mirrored setup enhances detection accuracy by covering a wider area and reducing false counts due to shadows or minor obstructions. The sensor processes these interruptions to accurately distinguish and count bidirectional traffic.

Key components include:
- **Infrared Emitter and Detector**: Emit and capture infrared light to detect movement.
- **Mirrored Surface**: Enhances beam coverage and accuracy.
- **Microprocessor**: Processes data to distinguish between entries and exits.
- **LoRaWAN Module**: Facilitates long-range data transmission to central data systems or gateways.

### Installation Guide
1. **Placement**: Install the sensor at entry points such as doors or hallways. Place it at a height of approximately 1.5-2 meters above the ground to ensure optimal detection.
2. **Alignment**: Ensure the mirrored surface is correctly aligned for maximum reflectivity and coverage. Misalignment can lead to inaccuracies.
3. **Power Connection**: Connect the unit to its power source following provided specifications, considering both battery and optional AC power configurations.
4. **LoRaWAN Configuration**: Program the sensor with network details to connect to your LoRaWAN gateway. Ensure network credentials, such as DevEUI, AppEUI, and AppKey, are correctly set.
5. **Calibration**: Initiate a calibration sequence to verify detection accuracy and adjust sensitivity settings as required.

### LoRaWAN Details
The POLYSENSE sensor leverages LoRaWAN for efficient, low-power, wide-area network communication. It supports:
- **Frequency Bands**: Depending on regional regulations (e.g., EU868, US915).
- **Adaptive Data Rate (ADR)**: Allows optimization of data rates and transmission power for efficient network performance.
- **Security**: Implements AES-128 encryption to secure data transmission.

### Power Consumption
The POLYSENSE sensor is designed with energy efficiency in mind:
- **Battery Operation**: Comes with a long-life battery capable of supporting several months of operation, based on transmission frequency and environmental factors.
- **Optional AC Adapter**: For permanent installations where battery maintenance is impractical.
- **Sleep Mode**: Automatically reduces power consumption during inactivity periods.

### Use Cases
- **Retail Stores**: Analyze customer foot traffic to optimize staff deployment and evaluate store layout efficiency.
- **Museums/Exhibitions**: Monitor visitor numbers to ensure safety regulations are met.
- **Public Buildings**: Manage access and egress data for security and operational insights.
- **Transportation Hubs**: Gauge passenger flow through stations and terminals.

### Limitations
- **Environmental Influences**: Sensor performance can be affected by extreme lighting conditions or reflective surfaces not aligned correctly with the sensor field.
- **Height Restrictions**: Mounting outside the specified range can lead to inaccurate readings due to insufficient beam coverage.
- **Crowded Conditions**: In situations of very high-density traffic, some individuals may not be counted if they pass too closely together.
- **Network Dependency**: Requires a well-maintained LoRaWAN infrastructure to ensure reliable data transmission.

### Conclusion
The POLYSENSE Bidirectional People Counting Sensor provides a robust solution for accurately measuring foot traffic in diverse environments. Its seamless integration with LoRaWAN networks and low-power operation ensure it is ideal for modern IoT ecosystems, providing valuable insights for optimizing operational efficiency while highlighting the importance of strategic installation and network management.