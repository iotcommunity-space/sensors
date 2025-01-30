## Technical Overview: POLYSENSE - Magnetic Switch Sensor

### Introduction
The POLYSENSE Magnetic Switch Sensor is a device engineered to monitor and report the open or closed status of a door or window. It utilizes LoRaWAN protocol for communication, allowing for remote data transmission over long distances with low power consumption, making it ideal for various IoT applications in smart buildings, security systems, and industrial automation.

### Working Principles
The POLYSENSE Magnetic Switch Sensor operates based on a reed switch mechanism. It consists of a magnetic sensor mounted on a frame and a magnet attached to the movable part (such as a door or window). When the magnetic field between the two components is interrupted (i.e., when the door opens), the reed switch changes its state (from closed to open or vice versa), sending a signal to the embedded IoT module to transmit a status update via LoRaWAN.

### Installation Guide
1. **Positioning**: Identify the location for installing the sensor. The magnetic components should be aligned properly so that they are in close proximity when the door or window is closed.

2. **Mounting**: Secure the magnetic sensor on the fixed frame using screws or adhesive backing depending on the surface material. Attach the magnet on the moving part ensuring alignment with the sensor.

3. **Connection**: The POLYSENSE normally comes preconfigured but ensure the device is powered by its onboard battery. Check connectivity status as indicated by the onboard LED (if available).

4. **Configuration**: Using specified software tools, configure the sensor by connecting it to a LoRaWAN gateway. Input the required parameters such as DevEUI, AppEUI, and AppKey for network authentication.

5. **Testing**: Once installed, verify the functionality by opening and closing the door/window and checking if the state changes are accurately transmitted to the designated receiver or application server.

### LoRaWAN Details
- **Frequency Bands**: Supports multiple frequency bands compliant with regional ISM standards (e.g., EU868, US915, etc.).
- **Communication Range**: The typical outdoor line-of-sight range is up to 10 km, while the indoor range is up to 2 km depending on obstructions and building materials.
- **Data Rate**: Variable data rates supported, from 0.3 kbps to 50 kbps using adaptive data rate (ADR) to optimize network efficiency.
- **Network Architecture**: Operates in a star-of-stars topology where sensors communicate with gateways that forward data to a network server.

### Power Consumption
The POLYSENSE Magnetic Switch Sensor is designed for ultra-low power consumption, utilizing a lithium battery that can provide up to 5 years of operation under typical usage conditions. Energy-efficient components are used to ensure minimal power draw in sleep mode and optimal usage during state change transmissions.

### Use Cases
- **Smart Building Management**: Monitor entry points, automate lighting, and manage HVAC systems based on occupancy.
- **Security Systems**: Detect unauthorized entry or tampering with windows or doors in residential and commercial properties.
- **Industrial Automation**: Monitor loading bays or manage access to restricted areas in factories and warehouses.

### Limitations
- **Magnetic Interference**: Strong external magnetic fields may cause false positives or negatives in signal detection.
- **Range Limitations**: Dense urban environments or thick building materials can significantly reduce the communication range.
- **Battery Life**: Frequent transmissions (e.g., doors with high traffic) can reduce the anticipated battery life.

By understanding the above technical overview, users can effectively deploy and manage the POLYSENSE Magnetic Switch Sensor in their specific environments, maximizing performance while addressing potential limitations.