## Technical Overview: POLYSENSE Bidirectional People Counting Sensor End Node

### Introduction
The POLYSENSE Bidirectional People Counting Sensor leverages advanced mirrored reflection technology to accurately measure and collect data on foot traffic across a specified passageway. Designed to integrate seamlessly with smart building IoT systems, this sensor node utilizes LoRaWAN for communication, offering a robust and versatile solution for efficient people counting in a variety of environments.

### Working Principles
The POLYSENSE sensor employs a combination of infrared and mirrored reflection technologies to detect the presence and direction of individuals passing through its coverage area. Utilizing a pair of infrared emitters and detectors arranged at strategic angles with respect to reflective surfaces, it creates a virtual curtain. When a person crosses this curtain, their body interrupts the beams, allowing the sensor to detect and count the passage while determining the direction of movement. The mirrored component enhances detection accuracy by reflecting the infrared light at optimized angles, mitigating blind spots and ensuring precise bidirectional counting.

### Installation Guide
- **Placement**: The sensor should be installed at passageways, entry/exit points, or corridors where people traffic is expected. It is crucial to position the sensor where it can emit parallel detection lines unobstructed.
- **Height and Orientation**: Mount the sensor at a height between 1.2m to 2.0m for optimal coverage. The sensor must be oriented such that the infrared beams cover the complete width of the passageway.
- **Calibration**: Calibration is necessary to account for varying environmental conditions. Use the accompanying software to adjust sensitivity settings and reflective angles for maximal accuracy.
- **Power Supply**: Ensure that the power source is reliable and consistent, whether using battery or wired connections.

### LoRaWAN Details
- **Frequency Band**: The sensor supports multiple global frequency bands, including EU868, US915, AS923, and others, providing compatibility with various regional LoRaWAN networks.
- **Data Rate**: Equipped to utilize LoRaWAN's Adaptative Data Rate (ADR) feature, optimizing communication reliability and battery life.
- **Security**: Implementing AES-128 encryption ensures secure transmission of data packets between the sensor node and the LoRaWAN gateway.
- **Integration**: Compatible with standard LoRaWAN gateways and network servers, allowing for easy integration into existing IoT ecosystems.

### Power Consumption
The sensor is designed with energy efficiency in mind, offering various power modes:
- **Active Mode**: Consumes approximately 50 mA during data collection and transmission processes.
- **Idle Mode**: Power consumption is reduced to under 10 µA in low-power standby, significantly extending battery life, often surpassing 2 years under typical use.

### Use Cases
- **Retail and Malls**: Monitoring customer footfall, optimizing store layouts, staffing, and promotions.
- **Public Buildings**: Tracking occupancy and usage patterns in libraries, museums, and transit hubs.
- **Corporate Offices**: Enhancing space utilization by understanding foot traffic patterns to manage meeting rooms and communal spaces efficiently.
- **Health Facilities**: Ensuring safe and regulated traffic flow in hospitals and clinics.

### Limitations
- **Line-of-Sight**: The sensor requires an unobstructed line-of-sight between the emitters, detectors, and reflective surfaces to function effectively.
- **Environmental Factors**: Extreme lighting conditions or reflective materials in the environment may affect counting accuracy.
- **Installation Constraints**: In highly irregularly shaped or excessively wide passageways, additional sensors might be necessary to ensure full coverage.

In summary, the POLYSENSE Bidirectional People Counting Sensor End Node provides a reliable and energy-efficient solution for monitoring pedestrian traffic across various settings, utilizing the robust LoRaWAN communication protocol and sophisticated mirrored reflection technologies. When installed and calibrated correctly, it offers accurate people counting data, driving informed decision-making in smart environments.