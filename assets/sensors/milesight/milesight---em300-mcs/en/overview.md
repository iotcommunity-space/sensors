# MILESIGHT: EM300-MCS Documentation

## 1. Technical Overview 

The MILESIGHT - EM300-MCS (EM300) is a high-performance IoT sensor using Magnetic Contact Switch technology, specifically optimized for monitoring the open/closed status of any movable objects like doors, windows, cabinets, safes, etc. 

## 2. Working Principle

The EM300 utilizes a magnetically-activated switch mechanism. When the contact is separated due to the opening of a door, window, etc., the reed within the switch opens and cuts off the electrical circuit. This change in the status is registered by the primary microcontroller unit. The system then sends a notification or alarm over the LoRaWAN network.

## 3. LoRaWAN Compliance

EM300's low-power, long-range communication is underpinned by LoRaWAN technology. It supports LoRaWAN protocol Class A, enabling robust wireless data communication over long distances up to 15km in line of sight and 2km in urban settings. The LoRaWAN also provides bidirectional data communication. 

## 4. Power Consumption

The EM300 is designed for long-term, low power consumption operation. Powered by a 1900mAh ER14505 AA lithium battery, the device can sustain operational lifespan up to 10 years under optimal conditions.

## 5. Installation Guide

1. Open the cover to access the battery holder and install the battery correctly.
2. Secure the main part of the sensor on the frame of the door/window, then place the magnetic part on the movable door/window, ensuring that they align correctly.
3. Configure the device with the Milesight IoT app before mounting, setting up your LoRaWAN network, alarm settings, and more.
4. Mount the device as per the given instruction manual, ensuring the device has good network coverage.

Please consult the user manual for a more detailed guide.

## 6. Use Cases

The EM300 provides a number of use cases across different domains:

1. **Home/Office Security:** Monitor the open/close status of doors, windows, or safes.
2. **Environment Monitoring:** View the status of windows and doors in a room, for better energy conservation and air conditioning control.
3. **Industrial Automations:** Monitor status of machine doors or house hold appliances for safety and regulatory compliance.

## 7. Limitations

- The device's maximum range can be significantly reduced by physical obstacles and dense urban settings.
- Misalignment between the sensor and the moving object can cause false readings.
- Battery life might be compromised by extreme environmental conditions and a heavy-duty cycle.
- EM300 should be installed within the coverage area of a LoRaWAN gateway to ensure reliable data transmission.

It is crucial to consider these potential limitations while developing solutions using EM300.

To conclude, the EM300-MCS serves as a reliable and efficient method of monitoring the open/close status of objects, despite a few limitations. It is, nevertheless, a highly useful application in smart homes, security setups, and industrial automation.