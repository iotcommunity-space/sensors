# POLYSENSE - Current Transformer Terminal Technical Overview

## Introduction

The POLYSENSE Current Transformer Terminal is an advanced IoT device designed for monitoring electrical current in various applications. The terminal utilizes LoRaWAN communication to provide real-time data remotely, ensuring efficient operation and monitoring across multiple environments. This document provides a detailed technical overview, including working principles, installation guidance, LoRaWAN integration, power consumption, potential use cases, and limitations.

## Working Principles

The POLYSENSE Current Transformer Terminal operates by utilizing a current transformer sensor, which is clamped around a conductor carrying the electrical current. This sensor measures the alternating current (AC) passing through the conductor by inducing a proportional current in its secondary winding. The device converts this induced current into a usable signal that can be interpreted and transmitted as meaningful data.

Key components of the terminal include:

- **Current Transformer Sensor**: This sensor detects the electromotive force from the primary conductor without direct electrical connections.
- **Signal Conditioning**: The terminal features built-in modules for amplifying and converting the raw signal into a digital format.
- **Microcontroller Unit**: Processes the signal and prepares it for packet transmission.
- **LoRaWAN Module**: Facilitates long-range, low-power data communication suitable for IoT networks.

## Installation Guide

1. **Safety Precautions**: Ensure that the installation area complies with electrical safety standards. Turn off relevant circuits to prevent electrical hazards during installation.

2. **Preparing the Conductor**: Identify the conductor to be monitored. Ensure that the outer insulation is intact and accessible for sensor placement.

3. **Mounting the Sensor**: Open the current transformer sensor and securely clamp it around the conductor. Ensure the sensor enclosure is closed after mounting.

4. **Device Configuration**: Connect the device to a configuration tool via USB or use the designated mobile application. Set parameters such as measurement range, frequency, and communication settings.

5. **Establishing Connectivity**: Initiate a connection to a LoRaWAN network. Input the Device EUI, App EUI, and App Key provided by your network service provider.

6. **Verification**: Perform a test measurement to confirm that the data is being accurately captured and transmitted to the LoRaWAN network.

## LoRaWAN Details

The POLYSENSE Current Transformer Terminal utilizes LoRaWAN technology, offering robust communication features:

- **Frequency Bands**: Supports multiple frequency bands (e.g., EU868, US915) according to regional regulations.
- **Data Rate**: Uses an adaptive data rate mechanism to optimize energy usage and signal range.
- **Network Range**: Offers a transmission range of up to 15 km in rural areas and 5 km in urban environments.
- **Device Classes**: Compatible with LoRaWAN Class A (low power) and optional Class C (for more frequent data updates).

## Power Consumption

- **Operating Voltage**: Typically requires a DC voltage of 3.3V or 5V, derived from either an internal battery or an external power source.
- **Battery Life**: Designed for low power consumption, enabling battery life ranging from several months to over a year, depending on the reporting frequency and network conditions.
- **Sleep Modes**: Multiple power-saving modes are available, including deep sleep, reducing consumption significantly when monitoring or communication isn't actively needed.

## Use Cases

The POLYSENSE Current Transformer Terminal is versatile and can be employed in numerous scenarios:

- **Industrial Automation**: Monitoring electrical consumption and efficiency of machinery.
- **Energy Management**: Real-time tracking of power usage in commercial buildings.
- **Renewable Energy Systems**: Monitoring production and consumption in solar and wind installations.
- **Smart Grids**: Enhancing grid reliability by detecting anomalies in current flow.

## Limitations

- **Environmental Conditions**: The terminal is sensitive to extreme temperatures and moisture levels, which may require additional enclosure protection.
- **Measurement Range**: Limited by the physical size and specifications of the current transformer; may not support high-current industrial applications without appropriate model selection.
- **Latency**: Data transmission is subject to network conditions, potentially introducing latency in real-time reporting scenarios.
- **Interference**: Susceptible to electromagnetic interference, potentially affecting accuracy in certain setups without proper shielding.

## Conclusion

The POLYSENSE Current Transformer Terminal offers a high degree of functionality for energy monitoring applications, benefiting from its integration with LoRaWAN technology. Its advanced features and easy installation make it an essential tool for optimizing and managing electrical systems, though users should be mindful of its operational limitations and ensure it's deployed in appropriate conditions.