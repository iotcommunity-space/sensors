## Technical Overview of ELSYS - Elt Lite

The ELSYS Elt Lite is a compact and versatile sensor designed for IoT applications, utilizing LoRaWAN technology for efficient long-range data transmission. It is primarily used for environmental monitoring, supporting a broad range of applications thanks to its multiple sensor capabilities.

### Working Principles

The Elt Lite functions by leveraging LoRaWAN (Long Range Wide Area Network) technology, which allows it to transmit sensor data over considerable distances with minimal power consumption. It is equipped with sensors that can measure temperature and relative humidity. The sensor operates on the ISM band, typically around 868 MHz in Europe and 915 MHz in North America, allowing it to communicate over long distances with minimal interference.

#### Key Sensors
- **Temperature Sensor**: Measures ambient temperature with high precision.
- **Humidity Sensor**: Gauges the relative humidity in the environment.

These sensors periodically record measurements and send the data to a LoRaWAN gateway. From there, the data can be directed to cloud platforms or databases where it can be processed, visualized, and analyzed.

### Installation Guide

1. **Site Evaluation**: Choose an optimal location free from obstructions, with good line-of-sight to a LoRaWAN gateway.

2. **Mounting**: Use screws or adhesive backing to mount the Elt Lite in your desired location. Ensure that the sensor is secure and shielded from direct exposure to elements such as rain or continuous direct sunlight unless housed in appropriate weatherproof enclosures.

3. **Power Supply**: The Elt Lite is powered by 2 x AA 3.6V batteries. Ensure the batteries are installed correctly to enable operation.

4. **Activation and Setup**: 
    - Connect to the device using the NFC interface and accompanying configuration app (available for iOS and Android).
    - Configure the device parameters like sensor data reporting intervals and transmission settings.

5. **Integration with LoRaWAN Network**:
    - Register the device’s DevEUI and AppKey with your LoRaWAN network server.
    - Ensure that the device joins the network successfully by verifying data transmission on the server dashboard.

### LoRaWAN Details

- **Frequency Band**: 868 MHz (Europe) / 915 MHz (North America)
- **Data Rate**: Adjustable depending on the network conditions and requirements (typically uses Adaptive Data Rate - ADR)
- **Transmission Range**: Typically up to 15 km in rural areas and up to 5 km in urban settings
- **Network Integration**: Compatible with any standard LoRaWAN network provider

### Power Consumption

The Elt Lite is designed for low power operation, making it suitable for battery-powered applications. It typically provides a battery life of up to 10 years under optimal conditions, assuming an hourly data transmission interval. Power consumption varies with transmission frequency and data rates which can be adjusted to meet specific application needs.

### Use Cases

- **Environmental Monitoring**: Ideal for monitoring indoor climate conditions in smart building applications.
- **Agriculture**: Useful for greenhouse monitoring to ensure optimal growing conditions.
- **Cold Chain Management**: Ensures proper environmental conditions during the storage and transport of temperature-sensitive goods.
- **Industrial Monitoring**: Helps maintain compliance with environmental regulations in various industrial settings.

### Limitations

- **Network Dependency**: Requires a functional LoRaWAN network. Performance can degrade if the network has poor coverage or excessive latency.
- **Environmental Exposure**: The device must be sheltered from harsh environmental conditions to prevent damage, affecting its suitability for some outdoor applications without additional protective measures.
- **Sensor Limitations**: As a basic model, the Elt Lite lacks advanced features like motion or CO2 detection, present in more sophisticated Elt models.

In summary, ELSYS Elt Lite is a practical choice for basic environmental monitoring needs in both indoor and controlled outdoor settings, capitalizing on the connectivity and efficiency of LoRaWAN technology.