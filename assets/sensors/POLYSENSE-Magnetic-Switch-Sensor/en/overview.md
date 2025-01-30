# POLYSENSE - Magnetic Switch Sensor

## Technical Overview

The POLYSENSE Magnetic Switch Sensor is a state-of-the-art IoT device designed to detect the opening and closing of doors, windows, or any object where positional awareness is beneficial. This sensor leverages LoRaWAN technology to provide efficient, low-power, and long-range communication, making it ideal for various applications in smart buildings, homes, and industrial environments.

### Working Principles

The POLYSENSE Magnetic Switch Sensor operates based on a magnetic reed switch. The sensor comprises two main components: the magnetic reed switch circuit and the magnetic field source, typically a small magnet. When the magnet is close to the reed switch, the magnetic field causes the switch to close, signaling a "closed" state. Conversely, when the magnet moves away, the field diminishes, causing the switch to open and signaling an "open" state. This change in state is then transmitted wirelessly to a central monitoring system via LoRaWAN.

### Installation Guide

1. **Choose the Location**: Identify the optimal location for installation where the magnetic switch assembly (sensor and magnet) will fully close and open when the object (e.g., door or window) is in its operational states.

2. **Secure the Sensor**: Attach the sensor component to the fixed frame of the deployment surface using screws or adhesive backing. Ensure the sensor is within sufficient range of the target magnet.

3. **Install the Magnet**: Affix the magnet to the movable part of the deployment surface directly opposite the sensor. Alignment is crucial for accurate state detection.

4. **Test the Setup**: Open and close the object to ensure the sensor detects the states accurately. Adjust positioning if necessary.

5. **Configuration**: Use the accompanying software or mobile application to configure the sensor settings, including device ID, operating frequency, data transmission intervals, and any threshold settings.

### LoRaWAN Details

- **Frequency Band**: Operates on standard LoRaWAN frequency bands (EU868, US915, etc.), dependent on the region.
- **Network Join Mode**: Supports OTAA (Over-the-Air Activation) and ABP (Activation by Personalization) for network connectivity.
- **Data Rate**: Adaptable data rates are available (ADR - Adaptive Data Rate), allowing optimization between range and data transmission rate.
- **Transmission Range**: Depending on the environment, the sensor can reliably transmit data over a distance of several kilometers (up to 10 km in rural and 2-5 km in urban settings).

### Power Consumption

- **Power Source**: Typically powered by a replaceable lithium battery.
- **Consumption Rate**: Extremely low power consumption is achieved due to the energy-efficient nature of LoRaWAN and the magnetic reed switch mechanism.
- **Battery Life**: The sensor can operate for several years on a single battery, depending on the frequency of state changes and data transmission settings.

### Use Cases

- **Security Systems**: Monitors entry and exit points for unauthorized access in homes, offices, and secure facilities.
- **Smart Lighting Control**: Integrates with lighting systems to automate light control based on door/window states.
- **Industrial Automation**: Ensures doors/gates in industrial environments are in the required positions before operating machinery.
- **Environmental Monitoring**: Keeps track of ventilation points in greenhouses or animal shelters to regulate environmental conditions.

### Limitations

- **Magnetic Interference**: Proximity to strong magnetic fields from other equipment can cause false or missed readings.
- **Obstruction**: Installation requires unobstructed lines of travel between sensor and magnet for precise operation.
- **Battery Replacement**: While infrequent, users need to monitor and replace batteries periodically to maintain functionality.
- **Signal Blockage**: Dense structures, such as thick concrete walls, may impede LoRaWAN signals, necessitating additional gateways for extended range.

The POLYSENSE Magnetic Switch Sensor is a versatile and reliable option for efficiently monitoring position states in various settings, thanks to its robust design and LoRaWAN connectivity.