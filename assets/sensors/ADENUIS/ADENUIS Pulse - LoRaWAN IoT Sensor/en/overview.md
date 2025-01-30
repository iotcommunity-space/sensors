# ADENUIS Pulse - LoRaWAN IoT Sensor Documentation

## 1. Overview

The ADENUIS Pulse is a highly specialized IoT sensor designed for remote monitoring of pulse output devices via the LoRaWAN protocol. This sensor is adept at handling signal inputs from devices such as water, gas, and electricity meters, providing accurate and timely data transmission for utility management and monitoring applications.

## 2. Working Principles

The ADENUIS Pulse sensor operates by detecting the pulse output from metering devices. Each pulse corresponds to a specific quantity of resource consumption (e.g., one liter of water, one cubic meter of gas, or a watt-hour of electricity). The sensor counts these pulses and transmits the accumulated data at pre-set intervals over a LoRaWAN network to a central system for analysis and monitoring.

### Components:

- **Pulse Input Interface:** Accepts signals from pulse-emitting devices.
- **Microcontroller Unit (MCU):** Processes incoming pulses and prepares data for transmission.
- **LoRa Transceiver:** Facilitates long-range, low-power communication over the LoRaWAN network.

## 3. LoRaWAN Details

The ADENUIS Pulse sensor is compatible with the LoRaWAN protocol, which supports bi-directional communication, end-to-end security, mobility, and localization services. This sensor can operate in various LoRaWAN classes, though typically it is used in Class A, which minimizes power consumption by allowing the device to transmit data and then immediately enter a low-power sleep mode until the next scheduled transmission.

### Network Configuration:

- **Frequency Bands:** Configurable to suit different regional LoRaWAN frequency band regulations (e.g., EU863-870, US902-928).
- **Data Rates:** Adaptable, depending on network demands and coverage.
- **Adaptive Data Rate (ADR):** Supported, optimizing data transmission rate and power consumption based on network conditions.

## 4. Installation Guide

### Pre-installation:

- Ensure compatibility of the pulse output from the metering device.
- Verify LoRaWAN network coverage in the installation area.
- Plan the mounting location, ideally minimizing obstacles between the sensor and the nearest gateway.

### Steps to Install:

1. **Mount the Sensor Bracket:** Fix the bracket at the chosen location, ensuring it is stable and secure.
2. **Attach the Sensor:** Secure the ADENUIS Pulse sensor to the bracket and connect the pulse input interface to the meter’s pulse output terminal.
3. **Configure the Device:** Using the configuration tool, set up network parameters, data transmission intervals, and other specific settings.
4. **Test the Installation:** Verify that the sensor is operational by checking for live data transmission to the monitoring system.

## 5. Power Consumption

The ADENUIS Pulse sensor is optimized for low energy usage, drawing power primarily when transmitting data. It is typically powered by a long-life battery, suitable for sustained use:

- **Operational Voltage:** 2.1V to 3.6V
- **Quiescent Current:** Low, to ensure extended battery life.
- **Battery Life:** Up to 10 years, depending on transmission intervals and environmental conditions.

## 6. Use Cases

Common applications include:

- **Utility Metering:** For water, gas, and electricity consumption tracking.
- **Resource Management:** In agriculture or manufacturing, monitoring resource use efficiency.
- **Smart City Infrastructure:** For monitoring street lighting or public amenities.

## 7. Limitations

- **Distance from Gateway:** Effective transmission range depends on environmental factors; obstructions like buildings can reduce range.
- **Pulse Compatibility:** Only compatible with devices that emit a standard pulse output.
- **Environmental Factors:** Extreme temperatures and humidity can affect battery life and sensor operation.

## 8. Conclusion

The ADENUIS Pulse sensor provides a robust and efficient solution for monitoring and managing resource consumption data over LoRaWAN networks. While mindful of its limitations, this sensor can significantly enhance operational efficiency and provide crucial data for smart resource management across various industries.