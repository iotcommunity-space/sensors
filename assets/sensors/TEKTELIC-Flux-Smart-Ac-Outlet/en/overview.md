# TEKTELIC - Flux Smart AC Outlet

## Technical Overview

The TEKTELIC Flux Smart AC Outlet is a versatile, IoT-enabled device designed to provide remote monitoring and control of electrical appliances. Utilizing LoRaWAN technology, this smart outlet offers robust wireless communication capabilities for a variety of smart building and energy management applications.

### Working Principles

The Flux Smart AC Outlet functions as both a power outlet and an IoT-enabled sensor. It features:

- **Power Measurement**: The device can measure real-time power consumption, providing detailed insights into energy usage.
- **Remote Control**: With onboard relays, users can switch connected devices on or off remotely via a mobile app or management platform.
- **Data Transmission**: Communicates data over the LoRaWAN network, which is known for its long-range and low-power characteristics, ideal for IoT applications.

### Installation Guide

1. **Site Assessment**: Ensure that the installation location is within the coverage area of a compatible LoRaWAN gateway.
2. **Mounting**: The outlet should be securely mounted onto the wall socket, ensuring a snug fit for stable operation.
3. **Connecting to Power**: Insert the device into the desired AC outlet, ensuring proper alignment with the socket pins.
4. **Pairing with LoRaWAN Network**:
   - Provision the outlet by adding its unique device credentials to the network server.
   - Configure activation mode (ABP or OTAA) as per network requirements.
   - Check connectivity using the associated app or platform to ensure the device communicates successfully with the gateway.
5. **Monitoring and Control Setup**: Use the mobile app or web interface provided by the network service provider to monitor power usage and control the outlet remotely.

### LoRaWAN Details

- **Frequency Bands**: The device operates on standard LoRaWAN frequency bands (e.g., EU868, US915), which vary by region.
- **Communication Range**: Typically, a range of up to 15 km in rural areas and up to 5 km in urban settings, depending on gateway placement and environmental factors.
- **Network Topology**: Supports both public and private LoRaWAN networks, enabling flexible deployment scenarios.
- **Data Rates**: Utilizes adaptive data rate (ADR) to optimize data transmission and battery life.

### Power Consumption

The Flux Smart AC Outlet is designed with energy efficiency in mind, ensuring minimal power draw when not actively controlling a load. The standby power consumption is very low, making it suitable for continuous operation. Precise specifications for power consumption while switching loads will depend on connected devices and usage patterns.

### Use Cases

- **Energy Management**: Collect detailed power consumption data for specific appliances or circuits to optimize energy use and reduce costs.
- **Smart Home Automation**: Integrate with home automation systems to schedule device operations or respond to environmental triggers.
- **Commercial Buildings**: Deploy across office spaces to monitor usage patterns and identify areas for energy savings.
- **Industrial Applications**: Monitor and control equipment remotely to improve efficiency and reduce downtime.

### Limitations

- **Network Dependence**: Requires a functional and appropriately configured LoRaWAN network for data transmission and control.
- **Load Capacity**: Limited by its maximum current and voltage ratings, which must be considered to avoid overloading.
- **Latency**: LoRaWAN’s low data rate and long-range focus may result in higher latency compared to other wireless communication technologies.
- **Environmental Factors**: Signal quality and range can be affected by building materials and interference from other electronic devices.

The TEKTELIC Flux Smart AC Outlet provides a comprehensive solution for energy monitoring and remote control, ideal for enhancing efficiency and convenience in both residential and commercial settings. However, users must consider network capabilities and specific requirements of their use case to maximize the benefits of this technology.