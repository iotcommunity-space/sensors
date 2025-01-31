# NETVOX - R718Ubb: A Technical Overview

## Working Principles

The NETVOX - R718Ubb, hereafter referred to as R718Ubb, is a cutting-edge IoT sensor that leverages LoRaWAN (Long Range WAN) technology for advanced wireless communication. Developed by NETVOX, the R718Ubb utilises a built-in accelerometer for detecting vibration patterns and tilt.

When the R718Ubb feels motion due to vibration or changes in angle, it triggers and sends alert messages over a secure LoRaWAN connection. These events are defined in part by the onboard accelerometer’s ability to set a user-defined sampling period. 

## Installation Guide

Installation of the R718Ubb is straightforward:

1. Mount the R718Ubb to the asset via screws or adhesive. It should be securely fastened to the item which motion detection is required.
2. Initiate the sensor by installing the LoRaWAN network (Gateway and Server) if not already installed, followed by the battery.
3. Follow your network server's procedure to add a new device. The R718Ubb comes with a unique set of LoRaWAN credentials: DevEUI, AppEUI/JoinEUI, and AppKey.
4. Test the device to confirm successful installation by initiating motion detection.

## LoRaWAN Details

The R718Ubb relies on the LoRaWAN Protocol stack (Class A) for its communication needs. LoRaWAN, or Long Range Wide Area Network, is designed for low-power devices to communicate with Internet-connected applications over long-range wireless connections. The device supports a wide range of LoRaWAN frequency bands adjusted to the region requirements, including AS923, AU915, EU868, and US915.

## Power Consumption

The R718Ubb features a high-capacity lithium battery with an expected lifetime of more than 5 years under normal operations (25℃, 15-minute report interval, LoRa Tx power at 0dBm). However, power consumption varies depending on the environmental factors, signal strength, data reporting intervals and other operating conditions.

## Use Cases

R718Ubb can be applied in a diverse range of sectors, including:

- Industrial automation: Monitoring of machinery for sudden movements, vibrations or changes in orientation can help in proactive maintenance.
- Construction industry: To monitor and record vibrations or earth movement around sensitive worksites.
- Asset management: For detecting any unauthorised movement or disturbance of valuable assets.

## Limitations

In spite of its innovative features, R718Ubb possesses certain limitations. While the device boasts long range connectivity, its maximum distance may vary significantly based on environmental factors such as physical obstructions or RF noise.

As a motion detection sensor, the device cannot provide exact location tracking or fall detection. Additionally, power usage can be higher in conditions of frequent reporting intervals or poor network coverage, which may shorten battery life.

Even though covered within a protective case, the device cannot fully withstand harsh conditions such as extreme temperatures, moisture, or corrosive environments. Proper installation and regular maintenance are required to ensure the longevity of the device. 

## Conclusion

The NETVOX - R718Ubb represents a strong addition to the IoT sensor community, offering reliable motion detection and communication over versatile and powerful LoRaWAN technology. However, users must be aware of contextual factors impacting power consumption and longevity, as well as install the device in environments compatible with its design.