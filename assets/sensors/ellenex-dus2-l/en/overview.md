## Technical Overview of ELLENEX - Dus2 L

The ELLENEX Dus2 L is a compact, remote monitoring sensor specifically designed for measuring differential pressure in liquid media with high accuracy and reliability. Engineered for industrial applications, this sensor leverages LoRaWAN technology to transmit data over long distances with minimal power consumption, catering to the needs of modern IoT infrastructures in various sectors.

### Working Principles

The ELLENEX Dus2 L operates based on the principle of pressure differential measurement. The sensor features a pair of pressure ports that capture the high and low pressures from the system. These values are then processed by an integrated microcontroller that calculates the differential pressure. The resulting data is transmitted using the LoRaWAN protocol, enabling long-range, low-power communication with IoT gateways.

### Installation Guide

1. **Site Assessment**: Choose an appropriate installation site where the differential pressure needs monitoring, ensuring it is within the recommended operating conditions in terms of temperature and media compatibility.
   
2. **Mounting**: Secure the sensor housing on a stable surface using the provided brackets. Ensure the sensor is oriented correctly, with consideration to the flow direction as indicated by the manufacturer.

3. **Connection**: 
   - Connect the pressure ports to the relevant points in your system using compatible tubing or connectors. 
   - Ensure connections are leak-proof to avoid erroneous measurements.

4. **Power Setup**: The sensor is battery operated. Install the battery as per the supplied instructions, ensuring proper polarity.

5. **Configuration**: Use the ELLENEX configuration software or mobile app to set up the sensor parameters, including measurement intervals and alert thresholds.

6. **LoRaWAN Network Registration**: Register the device on your LoRaWAN network by entering the device's unique identifier and the configured AppEUI. Follow with the activation process by receiving the necessary keys from your LoRaWAN network server.

7. **Testing**: After installation, test the sensor to validate its readings and ensure data is being received correctly at the designated server.

### LoRaWAN Details

- **Frequency Bands**: Operates on standard LoRaWAN frequency bands, which must be selected according to regional regulations (e.g., EU868, US915).
- **Data Rate**: Adjustable data rates are supported from DR0 to DR5, adapting to network conditions to optimize range and data throughput.
- **Network Security**: Employs AES-128 encryption at the network, application, and device level to ensure secure data transmission.

### Power Consumption

The Dus2 L is designed for low power consumption, making it optimal for battery-operated applications:
- **Average Power Consumption**: Less than 100 μA during idle mode.
- **Transmission Power Consumption**: Peaks during data transmission but is optimized through variable transmission intervals and adaptive data rates.
- **Battery Life**: Typically exceeding 5 years under standard operational conditions, thanks to energy-efficient design and adaptive operational modes.

### Use Cases

- **Water and Wastewater Management**: Monitoring pressure differences across filtration systems or pump stations.
- **HVAC Systems**: Measuring differential pressure across filters to determine maintenance needs.
- **Industrial Process Control**: Monitoring of fluids in chemical manufacturing and processing industries.
- **Smart Agriculture**: Managing irrigation systems to ensure optimal water usage by monitoring pipe pressures.

### Limitations

- **Media Compatibility**: Must be limited to compatible liquids as specified to avoid sensor damage or malfunction.
- **Temperature Extremes**: The sensor operates best within its specified temperature range. Extreme temperatures might affect accuracy and longevity.
- **Signal Interference**: In dense urban environments or areas prone to electromagnetic interference, LoRaWAN signal quality may be affected.
- **Range Limitations**: Although LoRaWAN provides long-range communication, actual achievable distance may vary based on environmental factors and antenna placement.

The ELLENEX Dus2 L is a versatile and reliable differential pressure sensor, integral to IoT-enabled monitoring solutions, that promises minimal maintenance, long battery life, and seamless integration with smart networks. Proper installation and calibration ensure optimal performance, while adherence to operational limitations will extend its functional lifespan.