# NETVOX - R718N3 Sensor: Technical Overview 

## Working Principles 

The NETVOX R718N3 is based on LoRaWAN wireless technology, a system that uses low-power wide-area networks (LPWANs) to connect IoT devices and sensors. The R718N3 primarily functions as a tilt sensor, detecting both tilt angle and vibration.

Once activated, it senses the inclination angle and vibration of an object and transmits this data back to IoT gateways via LoRaWAN. Then the gateways convey the sensed data to a central network server, translating the information into usable insights on object state or environment conditions.

## Installation Guide 

1. Open the pastic shell of the device and insert the battery according to the guide present inside.
2. Assemble the shell back together; the device will automatically start up.
3. Hold the 'Confirm' button for 5 seconds to confirm the device's start up.
4. Use the device's 'Set' button to set it to support OTAA or ABP modes in LoRaWAN protocol as per your requirement. The set procedures vary based on the mode.
5. Place the device on the object or within the environment you wish to monitor.

## LoRaWAN Details 

The NETVOX R718N3 is compatible with all standard LoRaWAN gateways. It supports the AU915, EU868, US915, AS923, and KR920 MHz frequency bands. For LoRaWAN 1.0.2, it supports Class A & C, but for LoRaWAN 1.0.3 revisions, it only supports Class A.

Also, it holds two modes: OTAA and ABP. Over-the-Air Activation (OTAA) and Activation By Personalisation (ABP) are the two methods of connecting a device with a LoRaWAN network. The firmware supports both, with different setup procedures for each.

## Power Consumption 

The R718N3 is powered by two standard 1/2 AA 3.6V ER14250 1200mAh batteries. The device is considered low power with a typical battery life of 5 years, assuming a detection frequency of 20 uplinks per day.

Furthermore, the power consumption is prominently contingent on the frequency of usage, the payload of transmitted data, and environmental factors like temperature.

## Use Cases 

Due to its core function as a tilt sensor, the R718N3 finds use in a variety of applications. Common use cases include:

- Monitoring of structures for signs of shifting, buckling, or deformation, which can be crucial for maintaining the integrity of buildings, bridges, and other large structures.
- Asset tracking and vehicle monitoring, wherein any sudden change in position or significant vibration may indicate suspicious activity. 
- Industrial equipment monitoring, allowing for predictive maintenance schedules.
- Monitoring of patient beds in healthcare, alerting staff when a patient leaves or falls out of bed.

## Limitations 

1. The sensor is not rated for extreme temperatures or for use in wet or very humid environments. 
2. Though the sensor has a long battery life under typical usage, battery life may be significantly reduced with heavy usage.
3. The sensor requires LoRaWAN gateways close enough to receive its transmissions, limiting use in remote or isolated locations.
4. The R718N3 detects only changes in tilt and vibration. If more complex object motion or environment conditions need sensing, additional or different types of sensors are necessary.
5. Tilt detection may not be enough for some applications, as the sensor does not provide precise positioning, and occasional false alarms may occur due to vibrations.