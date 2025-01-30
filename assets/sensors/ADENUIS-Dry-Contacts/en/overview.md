# ADENUIS - Dry Contacts Technical Overview

## Introduction
The ADENUIS Dry Contacts sensor is designed to integrate with existing infrastructure to detect and transmit signals from devices with dry contact outputs. This sensor is suitable for various IoT applications where monitoring contact states is critical. Utilizing LoRaWAN technology, it enables long-range communication, making it ideal for deployment in environments with limited connectivity options.

## Working Principles
The ADENUIS Dry Contacts sensor operates by monitoring the closure and opening of dry contacts (non-powered contacts like switches and relays) and converting these events into data signals. It utilizes a microcontroller to detect changes in the contact states and trigger data transmission over a LoRaWAN network. The sensor can be configured to report status changes immediately or at scheduled intervals, depending on the application needs.

## Installation Guide
1. **Site Assessment**: Before installation, assess the environment to determine the optimal placement for signal strength and coverage.
2. **Mounting**: Secure the sensor unit near the device you wish to monitor. Ensure that it is within range of the LoRaWAN gateway.
3. **Wiring**: Connect the wires from the dry contacts of the device directly to the input terminals on the ADENUIS sensor. Ensure a secure connection to avoid false readings.
4. **Configuration**: Use the manufacturer’s configuration tool to set up the device parameters, such as data reporting intervals and thresholds.
5. **Testing**: Once installed, perform a series of tests by manually opening and closing the dry contacts to verify proper transmission and receipt of signals.
6. **Commissioning**: Finalize installation by adding the sensor's device ID and credentials to your LoRaWAN network server to enable communication.

## LoRaWAN Details
- **Frequency Bands**: Supports various frequency plans including EU868, US915, and others as per local regulations.
- **Data Rate**: Utilizes adaptive data rate (ADR) to optimize payload size and transmission power.
- **Class**: Operates as a Class A device, enabling low power consumption and scheduled downlink capabilities.
- **Network Protocol**: Complies with the LoRaWAN specification 1.0.3 or later, ensuring compatibility with most LoRaWAN gateways and network servers.
- **Encryption**: Data encryption is maintained using AES-128 to safeguard data integrity and privacy.

## Power Consumption
The ADENUIS sensor is designed for ultra-low power consumption, making it suitable for battery-powered operations.
- **Standby Mode**: Consumes minimal power, allowing a battery life of several years, depending on network conditions and reporting frequency.
- **Active Transmission**: Power spikes during data transmission; however, due to the short duration of transmissions, overall impact on battery life is minimal.

## Use Cases
- **Industrial Automation**: Monitoring machinery status for operational efficiency and predictive maintenance.
- **Building Management**: Detecting door or window status to improve security and energy management.
- **Utility Monitoring**: Supervising equipment like pumps and valves in water or gas distribution networks.
- **Agriculture**: Managing and controlling irrigation systems and equipment status in remote locations.

## Limitations
- **Network Dependency**: Performance is heavily dependent on coverage and quality of the LoRaWAN network, which can be limited in highly urbanized or extremely remote areas.
- **Latency**: Due to the nature of LoRaWAN, there may be latency in data delivery, which can affect real-time monitoring applications.
- **Sensor Range**: Physical limitations may restrict sensor placement, requiring strategic installation planning to ensure connectivity.
- **Contact Type**: Only compatible with devices that have dry contact outputs; cannot be used with powered contact signals without additional interfaces.

## Conclusion
The ADENUIS Dry Contacts sensor is a versatile, low-power solution for remotely monitoring open/close events, seamlessly integrating with LoRaWAN networks for enhanced connectivity. It is crucial to assess the network environment and application requirements prior to deployment to mitigate potential limitations and to maximize performance and reliability.