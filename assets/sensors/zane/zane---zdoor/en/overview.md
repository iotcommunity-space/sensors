# ZANE-Zdoor Technical Overview

## Product Description:
The ZANE-Zdoor (ZANE) is an advanced IoT door sensor that revolutionizes residential and commercial security by providing real-time intrusion detection and alert. With its elegant design and low-power consumption, this sensor employs LoRaWAN technology, ensuring extended range and strong non-line-of-sight penetration capability.

## Working Principles:

ZANE operates on a simple yet effective principle. It uses two components: the main sensor attached to the door frame and a secondary magnet that mounts on the door. When the door opens or closes, it changes the magnetic field that the primary sensor can detect. This change triggers an alarm that is transmitted via a LoRaWAN connection to the system's central server or your IoT platform.

## Installation Guide:

The installation of ZANE is straightforward and user-friendly:

1. Attach the main unit on the door frame, and the second smaller unit onto the door itself, ensuring that both components align appropriately when the door is shut.
2. Power up the device (there would typically be an ON/OFF switch at one to the main sensor unit).
3. On the device is an identification number or QR code; this will be needed when you try to pair the device on the server.
4. Log into your server console, enter or scan the device's unique identification number. Once the device and server are syncronized, the system is ready for monitoring.

## LoRaWAN Details:

ZANE utilizes LoRaWAN (Long Range Wide Area Network), a protocol designed for low-power devices, creating durable, long-range communication. The LoRaWAN features of ZANE include:

- Network Frequency: Can be customized based on region (433/470/868/915 MHz)
- Modulation: LoRa/FSK 
- Network Connectivity: Bidirectional end-device communication
- Data Encryption: AES128

## Power Consumption:

Outstanding power management is one of the unique features of ZANE. It operates on two AAA batteries, which guarantees over a year's usage (depending on traffic rate and network conditions), thanks to the Low Energy LoRa technology.

## Use Cases:

ZANE finds wide application in:

- Residential and Commercial security: It provides real-time intrusion detection and sends alerts when doors open unexpectedly.
- Hotel rooms: It can be integrated into hotel room security system to detect unauthorized access.
- Asset management: In cases where assets or specific areas are off-limits, Zdoor ensures unauthorized breaches are detected.
  
## Limitations:

1. Distance and Obstruction: While LoRa has an excellent range, dense obstructions and long-distances may reduce its efficiency.
2. Network: ZANE relies heavily on the existence of a LoRaWAN network; It can't communicate in areas with no such network.
3. Battery: Though efficient, ZANE is battery-operated and will cease to function once the battery expires.
4. Non-IoT systems: It doesn’t integrate with non-IoT secuirty systems. 

## Conclusion:

In conclusion, ZANE-Zdoor is a best-of-breed IoT sensor optimized for user-friendliness, low power consumption, and extensive range.
Please note, the functionality may significantly vary with environmental factors and will require professional installation for optimum output.
