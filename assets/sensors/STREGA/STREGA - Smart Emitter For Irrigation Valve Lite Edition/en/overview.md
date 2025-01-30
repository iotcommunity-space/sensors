## Technical Overview of STREGA - Smart Emitter For Irrigation Valve Lite Edition

### Introduction

The STREGA Smart Emitter for Irrigation Valve Lite Edition is an innovative device designed to optimize water usage by remotely controlling irrigation systems using the LoRaWAN communication protocol. This device is especially suitable for agricultural and landscape irrigation, allowing for precise water distribution and efficient management from a distance.

### Working Principles

The STREGA Smart Emitter operates by integrating a low-power microcontroller with LoRaWAN capability, which communicates with a central gateway connected to a network server. It controls irrigation valves using solenoid actuators that open or close based on commands received via the LoRaWAN network. The emitter can be programmed with predefined schedules or can respond to real-time control commands, making it adaptable for various irrigation needs.

#### Key Features:

- **Remote Control**: Operate from anywhere with LoRaWAN connectivity.
- **Scheduling Flexibility**: Supports programming for automatic operation based on days, times, or weather conditions.
- **Low-Power Technology**: Prolongs battery life while maintaining consistent operation.
- **Compatibility**: Works with most standard irrigation systems.

### Installation Guide

1. **Pre-Installation Setup**:
   - Ensure you have a compatible LoRaWAN gateway and a reliable network server connection.
   - Verify compatibility of the irrigation system with the STREGA emitter.

2. **Physical Installation**:
   - Mount the STREGA emitter near the existing irrigation valve.
   - Connect the device to the solenoid valve using appropriate connectors and cables, ensuring waterproof seals to prevent damage.
   - Secure the emitter to a stable surface to avoid movement or disconnections.

3. **Electrical Setup**:
   - Insert batteries into the emitter if not powered by an external power supply.
   - Ensure proper connection to the solenoid for operational integrity.

4. **Configuration**:
   - Access the device settings through the network server or a compatible mobile app.
   - Configure the LoRaWAN settings such as Device EUI, Application Key, and Network Session Key.
   - Set desired irrigation schedules or establish triggers based on environmental sensors if integrated.

5. **Testing**:
   - Perform a test operation to ensure the emitter communicates effectively with the gateway and that the valve operates as intended.

### LoRaWAN Details

- **Frequency Bands**: Compatible with several global frequencies including EU868, US915, providing flexibility for international deployment.
- **Data Rate**: Operates in various data rates and spreading factors, ensuring robust communication over long distances.
- **Range**: Depending on environmental conditions, it can cover distances from 2 km in urban settings to 15 km in rural areas.
- **Security**: End-to-end encryption using AES-128 ensures data protection and integrity.

### Power Consumption

The STREGA Smart Emitter is designed for low power consumption to maximize battery life. Typically powered by long-life batteries, it operates in ultra-low power modes when not actively sending or receiving data. Power consumption details are as follows:

- **Sleep Mode**: < 10 µA
- **Active Mode**: 50 mA (during transmission)
- **Battery Life**: Up to several years depending on the frequency of operation and transmission rates.

### Use Cases

- **Agricultural Irrigation**: Efficient control of large-scale irrigation systems across vast tracts of land.
- **Landscape Management**: Automated watering of public parks, golf courses, and private landscapes.
- **Greenhouse Automation**: Precise humidity and watering control for optimal plant growth.
- **Smart City Applications**: Integrated into smart water management systems for urban irrigation.

### Limitations

- **Network Dependency**: Requires a LoRaWAN network gateway; connectivity issues can hamper operations.
- **Environmental Restrictions**: While robust, extreme weather conditions may affect communication or physical components.
- **Scalability**: While suitable for many applications, extremely large-scale operations may require multiple devices and gateways.
- **Battery Replacement**: Although rare due to low power consumption, battery replacement will eventually be necessary.
- **Professional Installation Recommended**: Optimal operation may require technical expertise for installation and configuration.

### Conclusion

The STREGA Smart Emitter for Irrigation Valve Lite Edition is a highly efficient, low-power device designed for flexible and remote irrigation management. With its robust LoRaWAN capabilities and ease of installation, it is an ideal solution for a variety of automated irrigation needs. Despite its limitations, it offers numerous advantages in terms of water saving and operational efficiency.