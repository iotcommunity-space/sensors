### Technical Overview of LANSITEC - Wifi Indoor Bluetooth Gateway

The LANSITEC Wifi Indoor Bluetooth Gateway offers a robust solution for indoor environments, facilitating seamless data collection and transmission from Bluetooth-enabled sensors to a centralized LoRaWAN network. This device is engineered to bridge the gap between wireless sensor networks and IoT platforms by leveraging Wi-Fi connectivity for data relay.

#### Working Principles

The LANSITEC Wifi Indoor Bluetooth Gateway operates by continuously scanning for Bluetooth signals within its vicinity. It captures sensor data such as temperature, humidity, or asset movements from Bluetooth Low Energy (BLE) devices. Once the data is captured, it's processed and transmitted via Wi-Fi to a predefined IoT server. This process allows real-time monitoring and remote management of the sensors’ environment. The gateway is designed to operate in indoor environments, ensuring a strong and stable connection within the coverage area.

#### Installation Guide

1. **Site Selection**: Choose a location within the range of target Bluetooth devices and has reliable Wi-Fi access.
2. **Mounting**: Install the gateway using the provided mounting kit. Ensure it is elevated, away from obstructions, and in a central position relative to monitored sensors.
3. **Power Connection**: Connect the gateway to a power source using the supplied AC adapter.
4. **Configuration**:
   - Connect to the gateway via its default Wi-Fi access point.
   - Access the configuration interface using a web browser.
   - Input network credentials to connect the gateway to the local Wi-Fi network.
   - Configure MQTT or HTTP server settings for data forwarding.
5. **Testing**: Verify connectivity with the IoT server and ensure that data from at least one Bluetooth sensor is being received and transmitted correctly.

#### LoRaWAN Details

Although the primary function of this gateway is to relay data via Wi-Fi, it supports integration into LoRaWAN networks as part of a hybrid setup. This can be useful for extending IoT applications that require both short-range Bluetooth and long-range LoRaWAN connectivity. The device is typically used in configurations where Bluetooth data needs to be bridged over Wi-Fi and managed alongside LoRaWAN devices in a single IoT platform.

#### Power Consumption

The LANSITEC Wifi Indoor Bluetooth Gateway is designed to be energy-efficient, making it suitable for continuous operation. It consumes approximately 2-5 watts per hour, depending on the volume of Bluetooth traffic and network activity. The power usage is optimized via a sleep mode for periods of inactivity, further reducing energy consumption.

#### Use Cases

- **Healthcare Facilities**: Monitoring patient movements or environmental conditions in hospitals.
- **Smart Offices**: Tracking assets or office occupancy levels.
- **Retail Environments**: Monitoring customer foot traffic and engagement.
- **Warehouses**: Tracking inventory movements and environmental conditions.
- **Educational Institutions**: Ensuring optimal conditions and tracking asset usage in classrooms.

#### Limitations

- **Range**: The effective Bluetooth range is typically around 30 to 50 meters indoors, which might require multiple gateways for larger environments.
- **Wi-Fi Dependency**: The system's reliance on Wi-Fi means that network downtime can disrupt data transmission.
- **Environment Sensitivity**: Physical obstructions or dense environments may interfere with both Bluetooth and Wi-Fi signal propagation.
- **Data Throughput**: While suitable for handling typical sensor data, higher data rates could lead to delayed transmissions due to bandwidth limitations.

In summary, the LANSITEC Wifi Indoor Bluetooth Gateway is a versatile and efficient solution for integrating Bluetooth sensor data into IoT networks. Its design makes it particularly suitable for applications needing swift deployment and significant coverage within indoor environments, with considerations for network infrastructure and sensor density influencing effective deployment.