## Technical Overview: MILESIGHT - EM500-PT100

### Introduction
The MILESIGHT EM500-PT100 is a LoRaWAN-enabled temperature sensor designed for precise temperature monitoring in challenging environments. Utilizing a PT100 probe, it extends the capabilities of IoT into industrial and environmental applications where precise temperature measurement is critical.

### Working Principles
The EM500-PT100 operates based on the resistance-temperature relationship inherent to PT100 sensors. As temperature changes, the resistance of the platinum RTD sensor changes linearly, allowing the EM500 to compute accurate temperature values. These readings are then transmitted wirelessly via the LoRaWAN protocol to a central monitoring system, enabling remote temperature monitoring and data logging.

### Installation Guide
1. **Preparation**: Ensure you have all components of the EM500-PT100 package, including the PT100 probe and sensor body. Verify that the installation site allows for optimal LoRaWAN signal transmission.
   
2. **Mounting**: 
   - Select an appropriate location where the PT100 probe will have uninterrupted contact with the surface or medium being measured.
   - Use the provided mounting brackets to secure the sensor body. Ensure that it is tightly fixed to avoid any displacement.

3. **Connecting the Probe**: 
   - Attach the PT100 probe to its designated port on the sensor body, ensuring secure connections to maintain accurate readings.
   
4. **Power On**: 
   - The EM500-PT100 is equipped with replaceable batteries. Insert the batteries following the indicated polarity directions.
   - The device will automatically power on once the battery compartment is closed.
   
5. **Network Configuration**: 
   - Use a LoRaWAN gateway to incorporate the sensor into your network. Input the sensor’s unique Device EUI, Application EUI, and App Key into the network server.
   - Ensure the sensor is within range of the LoRaWAN gateway for successful data transmission.

### LoRaWAN Details
The EM500-PT100 communicates over the LoRaWAN protocol, known for its low-power, long-range capabilities. Specific attributes include:
- **LoRaWAN Class**: Class A
- **Frequency Bands**: Compatible with EU868, US915, and other regional frequencies
- **Data Rate**: Supported LoRa data rates from DR0 to DR5 (depending on regional settings)
- **Transmission Interval**: Configurable, typically ranging from every few minutes to hours depending on application requirements

### Power Consumption
The EM500-PT100 utilizes a low-power design suitable for battery operation. The device typically uses a 19,000 mAh battery, which can last for several years under standard operating conditions, assuming an update interval of once per hour. Power consumption varies based on transmission frequency, distance from the gateway, and environmental conditions.

### Use Cases
- **Industrial Monitoring**: Precise monitoring of production processes where temperature stability is crucial, e.g., chemical processing.
- **Environmental Monitoring**: Deployment in remote areas to monitor climate or environmental conditions, such as in soil or groundwater temperature assessment.
- **Cold Chain Management**: Ensuring temperature-sensitive goods remain within safe temperature ranges during storage and transport.

### Limitations
- **Network Dependency**: Requires a compatible LoRaWAN network gateway within range for communication.
- **Installation Environment**: Extreme installation environments may require additional protective enclosures for the sensor body to avoid damage.
- **Update Limitations**: Real-time monitoring is constrained by the transmission interval set within the device configuration, which might not be suitable for applications requiring continuous real-time data.
- **Battery Replacement**: While designed for low power use, eventual battery replacement is necessary and involves accessing the sensor’s internal compartment.

### Conclusion
The MILESIGHT EM500-PT100 offers robust and precise temperature monitoring capabilities in a compact, energy-efficient package ideal for a range of industrially demanding applications. With LoRaWAN connectivity facilitating data collection over vast distances, it is a quintessential tool for modern IoT deployments seeking to integrate environmental data for enhanced operational efficiency.