# Technical Overview for NETVOX - R718Ubb

The NETVOX R718Ubb is a wireless ultrasonic distance measurement sensor designed to operate on LoRaWAN networks. This device is primarily used for applications such as level measurement, including measuring water levels in tanks, bins, or containers, or for monitoring distances in various environments. Below is a detailed technical overview covering its working principles, installation, LoRaWAN details, power consumption, use cases, and limitations.

## Working Principles

The NETVOX R718Ubb uses ultrasonic sound waves to measure the distance to an object. Here's how it operates:

- **Ultrasonic Transmission and Reception**: The sensor emits an ultrasonic wave, which travels through the air and hits the target object. The wave reflects back to the sensor.
- **Time of Flight (ToF) Calculation**: By measuring the time it takes for the ultrasonic wave to return, the sensor calculates the distance to the object using the speed of sound.
- **Conversion to Distance**: The time taken for the journey is divided by two (since the wave travels to the object and back) and multiplied by the speed of sound to produce the distance measurement.

## Installation Guide

### Tools and Materials Needed:
- Drill (if mounting on a hard surface)
- Screws and mounting brackets (if necessary)
- LoRaWAN Gateway within range

### Steps:
1. **Choose Location**: Select a location that provides an unobstructed path to the target object. Ensure the environment remains within the operational temperature range of the sensor.
   
2. **Mounting**: Use screws and brackets to mount the sensor on a flat, stable surface. Ensure the sensor is pointing directly towards the surface or object you wish to measure.

3. **Power On**: Insert the provided batteries into the sensor. The R718Ubb is powered by two 3.6V lithium batteries.

4. **Connectivity**: Ensure the device is within the range of a compatible LoRaWAN Gateway. Begin the pairing process by following NETVOX instructions provided for LoRaWAN network integration.

5. **Configuration**: Access the device settings to configure measurement intervals and reporting frequency, according to the specific requirements of your application.

## LoRaWAN Details

- **Frequency Bands**: Operates on the standard LoRaWAN frequency bands such as EU868, US915, AS923, AU915, and others based on regional regulations.
- **Network Class**: The sensor is a Class A device, which uses the most energy-efficient mode of communication, suitable for applications with infrequent communication.
- **OTAA/ABP**: Supports both Over-the-Air Activation (OTAA) and Activation by Personalization (ABP) for network joining.
- **Data Rate**: Supports multiple data rates (ADR – Adaptive Data Rate) to ensure optimal communication efficiency and range.

## Power Consumption

The NETVOX R718Ubb is designed to be power-efficient:

- **Battery Type**: Uses two 3.6V lithium batteries.
- **Battery Life**: Up to several years of battery life, depending on the frequency of data transmission and environmental conditions.
- **Consumption**: Energy consumption is minimized by the implementation of sleep modes when the sensor is inactive.

## Use Cases

- **Water Level Monitoring**: Ideal for measuring the depth of water in tanks or reservoirs.
- **Waste Management**: Used to determine the fill level of bins or containers.
- **Industrial Automation**: Distance measurement for monitoring moving machinery or stock levels.
- **Agricultural Applications**: Monitoring liquid levels in feed or fertilizer tanks.

## Limitations

- **Environmental Conditions**: Performance can be affected by extreme temperatures, high humidity, and precipitation.
- **Obstacles in Path**: The presence of obstacles or debris can deflect ultrasonic waves, leading to inaccurate readings.
- **Range Limitations**: The effectiveness decreases with increased distance and may not be suitable for extremely large measurements.
- **Blind Zone**: There is a minimum distance below which the sensor cannot detect objects accurately (usually within a few centimeters).

## Conclusion

The NETVOX R718Ubb is a reliable and versatile sensor for a range of applications where ultrasonic distance measurement is required. By leveraging LoRaWAN technology, it provides long-range communication while maintaining low power consumption. Users should consider the environmental and operational limitations to ensure optimal performance in the intended use case.