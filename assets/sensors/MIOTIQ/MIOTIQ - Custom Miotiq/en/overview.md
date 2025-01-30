# MIOTIQ - Custom Miotiq (MIOTIQ) Technical Overview

---

## Introduction

MIOTIQ is a customizable Internet of Things (IoT) sensor platform designed to integrate seamlessly into diverse environments, leveraging the LoRaWAN protocol for robust and long-range connectivity. It is acclaimed for its versatility in data collection across industrial, agricultural, and smart city applications. This document outlines its working principles, installation guidelines, LoRaWAN specifics, power consumption, potential use cases, and limitations.

---

## Working Principles

MIOTIQ operates on the LoRaWAN protocol, which enables low-power, wide-area networking for battery-operated devices. It is equipped with a suite of customizable sensors (e.g., temperature, humidity, pressure, and gas detectors) allowing it to cater to specific use cases. The device collects environmental data and transmits it over LoRaWAN to a central gateway, which forwards the data to the cloud for analysis and visualization.

### Key Features:

- **Customizable Sensor Modules**: Users can tailor sensor suites according to specific application needs.
- **LoRaWAN Connectivity**: Provides extensive range and network redundancy.
- **Configurable Transmission Interval**: Balances data granularity with battery longevity.
- **Data Encryption**: Ensures secure transmission with AES-128 encryption.

---

## Installation Guide

1. **Pre-Installation Requirements**:
   - Identify the sensor modules required for your application.
   - Ensure LoRaWAN gateway coverage in the deployment area.
   - Prepare mounting tools appropriate for the installation environment.

2. **Physical Mounting**:
   - Position the sensor based on application requirements (e.g., at a certain height for environmental monitoring).
   - Securely attach the device to the chosen surface using mounting brackets or industrial adhesive.

3. **Configuration**:
   - Utilize the MIOTIQ configuration software to set up device parameters such as data transmission intervals and specific sensor calibrations.
   - Pair the device with the LoRaWAN gateway following the on-screen instructions.

4. **Network Integration**:
   - Register the device's unique identifier (EUI) with the LoRaWAN network server.
   - Configure necessary network settings such as Device Address, App EUI, App Key for secure communication.

5. **Testing**:
   - Ensure the sensor is correctly communicating with the network by checking for data receipt on the server.
   - Validate sensor readings for accuracy.

---

## LoRaWAN Details

- **Frequency Bands**: Supports 863-870 MHz (EU) and 902-928 MHz (US) frequency bands.
- **Over-the-Air Activation (OTAA)**: Offers secure device activation method for added security.
- **Adaptive Data Rate (ADR)**: Optimizes data transmission rates and battery life according to network conditions.
- **Class A and Class C Support**: Facilitates both bi-directional communication classes for various applications.

---

## Power Consumption

MIOTIQ is designed with energy efficiency in mind, enabling prolonged operation on standard batteries. The following are power consumption characteristics:

- **Sleep Mode**: Approximately 5-10 µA, maximizing battery life during inactivity.
- **Transmission Mode**: Roughly 50-150 mA, dependent on transmission power level and frequency.
- **Battery Life**: Operational up to 5 years with standard lithium batteries under optimal conditions with a transmission interval of every 60 minutes.

---

## Use Cases

- **Smart Agriculture**: Monitor soil moisture, temperature, and crop conditions in real-time to optimize watering schedules and crop yield.
- **Industrial Monitoring**: Track equipment status, temperature, and pressure in industrial settings to preemptively address maintenance needs.
- **Environmental Monitoring**: Provide air quality data in urban environments to inform public health decisions and policy-making initiatives.

---

## Limitations

- **Range Variability**: While LoRaWAN is designed for long-distance communication, actual range is influenced by environmental obstacles such as buildings and foliage.
- **Data Rate Constraints**: Suitable for small data packets due to LoRaWAN's low data rate, which may not be ideal for applications requiring high bandwidth.
- **Battery Dependency**: Prolonged data transmission frequencies can significantly drain battery life, requiring careful interval management.
- **Interference**: Being a spectrum-shared technology, it may suffer interference from other devices operating in the same frequency band.

---

In summary, MIOTIQ is a versatile and robust platform for various IoT applications, combining reliable long-range communication with adaptable sensor configurations. Its efficient power management and secure data handling make it a valuable asset across different sectors, albeit with considerations regarding its transmission rate and range limitations.