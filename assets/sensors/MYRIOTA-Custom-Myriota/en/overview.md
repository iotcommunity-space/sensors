## Technical Overview of MYRIOTA - Custom Myriota

The MYRIOTA Custom Myriota solution is a satellite-based communication device designed to serve IoT applications in remote and underserved areas. It leverages the Myriota satellite network to ensure reliable, low-power data transmission from IoT sensors globally.

### Working Principles

Myriota operates on a simple but efficient data transmission model. Sensors collect data, which is then sent to a Myriota module. This module transmits the data directly to Myriota's Low Earth Orbit (LEO) satellites. The satellites relay this information to ground stations, which then forward the data to the end user's server via a cloud platform. This model allows for seamless and scalable IoT data communications over widespread geographic areas without reliance on conventional cellular networks.

### Installation Guide

1. **Site Assessment**:
   - Conduct a preliminary survey to ensure clear line-of-sight with the sky for satellite communication. Avoid substantial obstructions like buildings or dense foliage.

2. **Device Mounting**:
   - Securely mount the Myriota module at the designated location. Ensure that the antenna is oriented upwards and unobstructed.
   - Use weather-proof enclosures if exposed to harsh environmental conditions.

3. **Connecting Sensors**:
   - Integrate the necessary sensors with the Myriota module using compatible interfaces. Follow specific sensor wiring guidelines to ensure accurate readings and reliable communication.
   
4. **Power Supply**:
   - Connect an appropriate power source based on the module's voltage and current rating requirements. Solar panels with battery storage are recommended for remote applications to ensure energy autonomy.

5. **Configuration**:
   - Use the Myriota's configuration tools to set up data transmission intervals, data logging parameters, and satellite communication protocols. Test connectivity by sending a few sample datasets.

6. **Monitoring**:
   - Register the device on Myriota's cloud platform for data access and performance monitoring.

### LoRaWAN Details

While Myriota primarily uses its satellite communications network, integrating with LoRaWAN is possible for localized data aggregation before satellite transmission. This is ideal in applications where multiple IoT devices within proximity need to forward data to a single Myriota module. The module must support LoRaWAN interfaces and protocols, typically requiring additional setup at the initial configuration stage to ensure seamless interaction between LoRa and satellite uplinks.

### Power Consumption

Myriota devices are designed to be highly power-efficient, operating on low-average demand, typically in the range of micro to milliwatts during data collection and idle states. Power consumption peaks during satellite transmission, although these periods are brief due to the efficient uplink protocol. Devices typically use AA batteries or a combination of solar panels and rechargeable batteries suitable for extended field deployments.

### Use Cases

- **Agricultural Monitoring**: Remote data tracking for soil moisture, weather conditions, and livestock movements.
- **Environmental Monitoring**: Data collection from sensors deployed in oceans, forests, or conservation areas where typical network connectivity is unavailable.
- **Asset Tracking**: Managing logistics for fleets or equipment in remote operations such as mining and oil fields.
- **Infrastructure Monitoring**: Monitoring critical infrastructure like pipelines, dams, or remote facilities.

### Limitations

- **Real-Time Data Transmission**: Due to reliance on satellite overpasses, there may be slight delays in real-time data availability, which can vary based on geographic location and number of satellites.
- **Data Payload Limitations**: The low-bandwidth nature of satellite communications limits the size of data packets that can be transmitted in a single transmission.
- **Environmental Interference**: Strong atmospheric disturbances or extreme weather conditions can occasionally affect data transmission quality.
- **Initial Cost**: The deployment cost for setting up systems on the Myriota platform can be higher compared to standard terrestrial IoT networks, although offset by lower operational costs in the long run for remote areas.

Understanding these components allows for optimal deployment and integration of Myriota solutions in diverse IoT applications, ensuring robust and cost-effective remote data communication.