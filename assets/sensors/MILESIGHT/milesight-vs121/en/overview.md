## Technical Overview of MILESIGHT - VS121

The MILESIGHT VS121 is an advanced indoor people counting sensor designed to provide precise footfall traffic analysis. It integrates seamlessly with various IoT ecosystems using the LoRaWAN protocol, making it ideal for use in retail environments, office buildings, and other public spaces where monitoring occupancy is crucial.

### Working Principles

The VS121 utilizes stereoscopic vision technology, employing dual-camera sensors to accurately count and analyze people entering and exiting a designated area. The device uses advanced image processing technology to distinguish people from other objects, ensuring that the data collected is precise and reliable. This stereoscopic approach allows the sensor to function effectively even in varying lighting conditions and dense traffic environments. It can also be configured to determine directionality of movement, making it versatile for bidirectional counting needs.

### Installation Guide

1. **Location Selection**: Choose a location that provides a clear and unobstructed view of the entrance or passage being monitored. The installation height should generally range from 2.3 to 5 meters to ensure proper coverage and accuracy.
   
2. **Mounting**: The sensor can be mounted on the ceiling or suspended depending on physical constraints and the field of view required. Ensure the cameras face directly downward, with their field of view parallel to the entrance path.

3. **Angle Adjustment**: Depending on the height and specific requirements of the monitoring area, adjust the viewing angle of the cameras to cover the entire width of the monitored area.

4. **Integration and Configuration**: Integrate the device with your LoRaWAN network following the network’s protocol for device registration and configuration. Use the companion software for initial setup to calibrate the sensor according to the specific characteristics of the monitored space.

5. **Power On and Test**: Connect the device to a power source using the standard 12V DC input. Once powered, verify installation correctness and connectivity status, and conduct a test run to ensure the accuracy of people counting.

### LoRaWAN Details

The VS121 uses LoRaWAN technology for wireless communication, providing long-range connectivity with low power consumption. It operates on the EU863-870, US902-928, and other regional frequency bands compliant with the LoRaWAN specification. The sensor communicates using the Class A/C LoRaWAN protocols, enabling efficient battery management and transmission scheduling. This allows the sensor to periodically send data to a central server for analysis and visualization.

### Power Consumption

Designed for energy efficiency, the VS121 uses minimal power to operate its cameras and processing unit. It typically draws less than 3 Watts in standard conditions when powered via DC input. This low power requirement is particularly beneficial for installations in locations where power availability may be limited or where operational costs need to be minimized.

### Use Cases

1. **Retail and Shopping Malls**: Monitor customer flow and dwell time to optimize staffing, security, and inventory management.
   
2. **Corporate Offices**: Analyze occupancy trends to improve space utilization and energy efficiency.

3. **Public Buildings and Airports**: Manage crowd control and ensure compliance with health and safety regulations by monitoring real-time occupancy data.

4. **Smart Buildings**: Integrated into a broader smart building management system to enhance automated environmental controls based on people presence and density.

### Limitations

1. **Indoor Use Only**: The VS121 is designed exclusively for indoor environments and may not perform accurately under outdoor conditions where factors like inclement weather can affect detection capabilities.

2. **Installation Height Constraints**: Needs careful calibration and installation at appropriate heights to deliver accurate counts, limiting flexibility in specific architectural scenarios.

3. **Privacy Concerns**: Though the sensor does not record video, privacy considerations should be taken into account in sensitive environments.

4. **LoRaWAN Network Dependency**: Requires a robust and well-managed LoRaWAN network to ensure real-time data transmission, which may require additional infrastructure in remote or signal-challenged locations.

By understanding these operational principles and constraints, users can maximize the value they derive from integrating the Milesight VS121 into their environment, optimizing both people counting accuracy and IoT ecosystem performance.