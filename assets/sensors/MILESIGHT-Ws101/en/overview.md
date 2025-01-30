# Technical Overview for MILESIGHT - WS101

The Milesight WS101 is a compact and versatile LoRaWAN-based smart switch designed to enable remote control and automation in various IoT applications. This document provides a detailed technical overview, including its working principles, installation guide, LoRaWAN details, power consumption specifications, potential use cases, and limitations.

## Working Principles

The WS101 operates as a wireless smart switch that communicates through LoRaWAN technology to control and automate electrical devices. It integrates a low-power microcontroller with a LoRa radio module to send and receive signals. The WS101 can be programmed to switch devices on or off either manually, via the physical button, or remotely through a LoRaWAN network. The device features capabilities for scheduled and event-based automation, enhancing energy efficiency and user convenience.

### Key Features:
- **Remote Control**: Operates devices from a distance using LoRaWAN.
- **Manual Override**: Allows local device control through a physical push button.
- **Scheduled Operations**: Automate operations based on predefined schedules.
- **Energy Efficiency**: Design prioritizes minimal power usage in idle and active states.
  
## Installation Guide

### Pre-Installation Requirements:
- Ensure a compatible LoRaWAN gateway is configured within the vicinity.
- Verify the network coverage and signal strength at the intended installation site.
- Identify the device to be controlled via the WS101.

### Installation Steps:
1. **Power the Device**: Connect the WS101 to a suitable power source using the provided wiring guides.
2. **Pair with LoRaWAN Network**:
   - Activate the device by pressing and holding the button until it enters pairing mode.
   - Use the LoRaWAN Network Server interface to add the device using its unique IDs (DevEUI, AppEUI, and AppKey).
   - Confirm the device's successful network join, indicated by LED signals or dashboard confirmation on the network server.
3. **Physical Mounting**: Secure the WS101 near the controlled device, ensuring the temperature and environmental conditions align with its operating range.
4. **Functionality Test**: Verify operational status by issuing test commands via the network server and evaluating physical button responses.

## LoRaWAN Details

- **Frequency Bands**: Supports sub-GHz ISM bands (typically 868 MHz for EU and 915 MHz for US regions).
- **Network Protocol**: Compliant with LoRaWAN version 1.0.3/1.1.
- **Communication Range**: Up to 15 km in rural areas and 3-5 km in urban environments.
- **Security**: Achieves robust security via AES-128 encryption.
- **Data Rate**: Adaptive data rate (ADR) allows optimal performance based on network conditions.

## Power Consumption

The WS101 is designed for low power consumption, making it suitable for battery-operated setups:

- **Idle State**: < 10 µA.
- **Transmission State**: Approximately 45 mA during brief signal bursts.
- **Battery Life**: Typically over 2 years under standard operating conditions with support for battery or external power supply options.

## Use Cases

- **Smart Home Automation**: Control lighting, fans, or small appliances remotely.
- **Industrial Applications**: Automation of machinery or environmental controls to enhance efficiency.
- **Energy Management**: Scheduled switching of non-essential devices for improved energy savings.

## Limitations

- **Signal Range Dependency**: Performance is dependent on LoRaWAN gateway proximity and environmental obstacles.
- **Data Rate Limitations**: Limited by LoRaWAN duty cycle regulations and bandwidth.
- **Load Capacity**: Suitable for controlling devices with moderate power requirements; not ideal for high-power machinery.
- **Network Dependency**: Requires a functional LoRaWAN network to enable remote functionalities.

In summary, the MILESIGHT WS101 serves as an efficient, low-power solution for various remote control applications using LoRaWAN technology. While it is adaptable to numerous environments, it does have requirements pertaining to network infrastructure and load capacities that should be considered during deployment.