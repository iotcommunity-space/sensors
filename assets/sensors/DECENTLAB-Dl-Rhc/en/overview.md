### Technical Overview of DECENTLAB - DL-RHC Sensor

The DECENTLAB DL-RHC is a versatile environmental monitoring device designed to measure air temperature, relative humidity, and carbon dioxide (CO₂) concentration. It leverages LoRaWAN technology for wireless communication, making it ideal for a variety of remote sensing applications. Below is a detailed technical overview of the DL-RHC sensor:

#### Working Principles

The DL-RHC employs a suite of integrated sensors:
- **Temperature and Humidity Sensor**: Utilizes a high-precision digital sensor that provides accurate readings of ambient air temperature and relative humidity.
- **CO₂ Sensor**: Equipped with an NDIR (Non-Dispersive Infrared) sensor, capable of accurate CO₂ concentration measurement.

These sensors are tightly integrated to maintain performance in various environmental conditions. The data collected by the sensors is processed by an onboard microcontroller and transmitted via LoRaWAN.

#### Installation Guide

1. **Site Selection**: Choose an open area with representative environmental conditions. Avoid placing the sensor in direct sunlight or near any source of heat or emissions that could skew the readings.

2. **Mounting**: Secure the sensor in a vertical position using the supplied mounting bracket or a compatible mounting structure. Ensure it is mounted at the recommended height (typically 1.5 to 2 meters above the ground) and that the sensors are not impeded by any obstructions.

3. **Activation**: The DL-RHC comes with a pre-installed battery. To activate the device, follow the manufacturer's instructions, which typically involve pressing a designated button or removing a pull tab from the battery compartment.

4. **Configuration**: Use the DECENTLAB Tool or any compatible device to configure the sensor’s settings, such as data transmission intervals and LoRaWAN parameters.

#### LoRaWAN Details

- **Frequency Bands**: Operates on standard LoRaWAN frequency bands (EU868, US915, etc.), depending on regional regulations.
- **Network Capacity**: Supports Class A LoRaWAN devices, which communicate in scheduled uplink and receive windows for downlinks.
- **Communication Range**: Capable of long-range transmission, typically up to 10 km in rural areas and 3-5 km in urban environments.
- **Data Transmission**: The device can be configured to transmit data at intervals ranging from a few minutes to several hours, depending on the application needs and power conservation requirements.

#### Power Consumption

The DL-RHC is powered by replaceable lithium batteries designed to provide several years of service depending on the update interval:
- **Idle mode**: Extremely low power consumption to maximize battery life.
- **Active mode**: Power consumption increases during measurement and data transmission but remains optimized for extended operation.

#### Use Cases

- **Agricultural Monitoring**: Measure microclimatic conditions to optimize crop yield and manage irrigation.
- **Building Management**: Monitor indoor air quality for CO₂ concentration and ensure a comfortable and healthy environment.
- **Environmental Research**: Deploy in various ecological locations to collect data for climate studies and biodiversity assessments.
- **Industrial Applications**: Monitor conditions in warehouses or greenhouses to ensure optimal storage and growth environments.

#### Limitations

- **Line of Sight Requirement**: The effective communication range can be reduced in areas with dense obstructions to line-of-sight, such as forests or heavily built-up areas.
- **Battery Life**: Intensive data sampling rates can reduce battery life significantly, requiring more frequent maintenance or battery replacement.
- **Temperature & Humidity Ranges**: Extreme temperature and humidity conditions beyond sensor specifications can affect accuracy or sensor lifespan.

Overall, the DECENTLAB DL-RHC is a robust and efficient tool for environmental monitoring applications, particularly where long-range, low-power wireless communication is required. Its seamless integration with LoRaWAN networks enables extensive data collection and analysis in diverse operational scenarios.