# Technical Overview for ZANE - Zdoor

## Overview
The ZANE - Zdoor is a sophisticated IoT-enabled door sensor designed for seamless integration into smart buildings and security systems. Utilizing LoRaWAN technology, Zdoor offers extended range capabilities, low power consumption, and reliable data transmission suitable for various applications, from residential to commercial environments.

## Working Principles
The Zdoor operates by detecting changes in the state of a door (open or closed) using a magnetic sensor paired with a magnet. The sensor is installed on the frame, while the magnet is attached to the door itself. As the door opens or closes, the change in the magnetic field triggers the sensor, which then communicates the status to a central system via LoRaWAN. This communication is event-driven, ensuring data is only transmitted when a change in state occurs, thus conserving energy.

## Installation Guide
1. **Unboxing:** Carefully unpack the Zdoor sensor kit. It includes the sensor unit, magnet, mounting hardware, and installation guide.
   
2. **Preparation:** Identify the door and frame area where the sensor and magnet will be positioned. The magnet should be aligned directly opposite the sensor when the door is closed.

3. **Mount the Sensor:** Use the screws or adhesive strips provided to securely mount the sensor unit onto the door frame. Ensure it is level and aligned with the magnet.

4. **Mount the Magnet:** Attach the magnet to the door itself, ensuring it's directly aligned with the sensor when the door is in the closed position to maintain optimal magnetic field interaction.

5. **Power On:** Insert the provided battery or connect a power source if required by the model. Ensure the sensor is properly powered and activate it as per the manual instructions.

6. **Pairing and Calibration:** Initiate the pairing process with your LoRaWAN gateway. Follow the device-specific instructions to ensure successful registration on the network. Test the calibration by opening and closing the door to verify the sensor's response.

## LoRaWAN Details
- **Frequency Bands:** Zdoor supports multiple frequency bands including EU868, US915, and AS923 to accommodate regional laws and regulations.
- **Data Rate:** Operates under adaptive data rate (ADR) management to optimize performance and battery life.
- **Security:** Integrated with AES-128 encryption to ensure data security during transmission.
- **Range:** Zdoor can communicate over distances up to 15 kilometers in rural settings and 2-5 kilometers in urban environments, dependent on gateway placement and environmental factors.

## Power Consumption
Zdoor boasts exceptionally low power consumption, designed to last several years on a single battery charge. The design features ultra-low power usage during idle states and energy-efficient communication protocols, focused on extending battery life without compromising data transmission reliability.

## Use Cases
- **Security Systems:** Integration into home and office security setups to provide real-time alerts on unauthorized access.
- **Facility Management:** Monitoring doors in commercial complexes for access control and maintenance management.
- **Smart Homes:** Enhance automation with smart locks and other connected devices.
- **Inventory Control:** Use in warehouses to monitor bay doors and secure assets.

## Limitations
- **Installation Environment:** Magnetic interference from nearby metals or electronic devices can affect sensor performance.
- **Signal Obstacles:** Building materials like steel and concrete can affect LoRaWAN range, potentially necessitating the use of repeaters.
- **Battery Life:** Continuous operation in a high-frequency data transmission mode may lead to reduced battery life.
- **Network Coverage:** Reliance on LoRaWAN coverage may limit functionality in areas with limited network infrastructure.

In conclusion, the ZANE - Zdoor is a reliable, energy-efficient solution for modern door monitoring needs, offering adaptability across multiple sectors while providing secure, long-range wireless communication capabilities.