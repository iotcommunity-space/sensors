## Technical Overview of MILESIGHT AM104

### Introduction
The MILESIGHT AM104 is a compact and versatile indoor environment monitoring sensor tailored for IoT applications. It measures various indoor environmental parameters, including temperature, humidity, CO2 concentration, TVOC levels, and barometric pressure. Designed for use in smart buildings and offices, the AM104 integrates these measurements into an efficient, compact form factor, communicating data wirelessly via LoRaWAN technology.

### Working Principles

The AM104 leverages several integrated sensors to measure indoor environment parameters:

- **Temperature and Humidity Sensor**: Uses a high-precision capacitive and digital sensor to provide accurate readings of temperature and relative humidity.
- **CO2 Sensor**: Utilizes a non-dispersive infrared (NDIR) sensor, providing reliable real-time measurements of carbon dioxide concentrations.
- **TVOC Sensor**: Employs a metal-oxide sensor to detect a wide range of harmful volatile organic compounds, aiding in indoor air quality assessment.
- **Barometric Pressure Sensor**: Uses a piezoresistive or capacitive sensor for accurate atmospheric pressure readings.

The AM104 processes data from these sensors and periodically transmits the information over the LoRaWAN network for remote monitoring and analysis.

### Installation Guide

1. **Unpacking and Inspection**:
   - Carefully unbox the AM104 and ensure all components are present, including the sensor itself and mounting accessories.

2. **Placement**:
   - Choose an optimal location for the sensor, ensuring it's away from direct sunlight, heating vents, or drafty areas to avoid skewed environmental readings.
   - Recommended height for mounting is around 1.5 to 2 meters above the ground to ensure optimal results.

3. **Mounting**:
   - Use the provided mounting bracket or adhesive tape (if supplied) to securely attach the sensor to the desired surface.
   - Ensure the sensor is stable and not prone to vibrations or movements.

4. **Powering the Device**:
   - The AM104 is powered by replaceable lithium batteries. Open the battery compartment and insert the batteries ensuring correct polarity.

5. **Configuration**:
   - Use the MILESIGHT IoT Cloud or a compatible LoRaWAN gateway to register the device. Input the device’s unique identifier (EUI).
   - Configure the device to the desired data transmission interval and other specific settings through the associated platform.

### LoRaWAN Details

- **Frequency Bands**: Typically supports EU868, US915, AS923, and other regional frequencies subject to local regulations.
- **Device Class**: Class A device, supporting bi-directional communication where uplink times are initiated by the user and downlinks occur in response.
- **Security**: Utilizes AES-128 encryption to ensure secure data transmission.
- **Range**: LoRaWAN technology allows long-distance communication, with a typical urban range of 2–5 km and suburban range up to 15 km.

### Power Consumption

The AM104 is designed for low power consumption, optimizing battery life for extended operation. Power consumption depends on configuration settings such as data transmission intervals:

- **Sleep Mode**: Minimum power consumption when the sensor is inactive.
- **Active Mode**: Consumes higher power during data acquisition and transmission periods.
- **Battery Life**: Typically lasts several years, depending on reporting frequency and environmental conditions.

### Use Cases

- **Indoor Air Quality Monitoring**: Ideal for offices, classrooms, and residential buildings to maintain healthy air quality levels.
- **Smart Building Integration**: Complements HVAC systems by providing crucial environmental data for climate control and energy-saving optimizations.
- **CO2 and TVOC Monitoring**: Ensures compliance with indoor air quality standards, vital in industrial settings or areas prone to air pollution.
- **Weather Station Components**: Can be part of comprehensive indoor environmental monitoring systems.

### Limitations

- **Data Transmission Rate**: Limited by LoRaWAN's bandwidth, may not support high-frequency data requirements.
- **Indoor Range Limitations**: While LoRaWAN provides long-distance coverage, dense building materials can significantly attenuate signals.
- **Battery Life Dependency**: Battery life greatly depends on transmission frequency and environmental conditions, necessitating periodic maintenance.

In summary, the MILESIGHT AM104 is a sophisticated indoor environment monitoring sensor that, while presenting limitations intrinsic to its design and technology, offers a reliable solution for modern smart building applications. The combination of its multi-sensing capabilities, low power consumption, and seamless LoRaWAN integration make it a valuable tool in the IoT ecosystem.