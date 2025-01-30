# Technical Overview for AXIOMA - Water Meter Qalcosonic W1

## Introduction
The AXIOMA Qalcosonic W1 is a cutting-edge ultrasonic water meter designed for accurate monitoring and management of water usage. It utilizes ultrasonic technology to enhance measurement precision, reliability, and efficiency. This water meter integrates seamlessly with IoT infrastructures using LoRaWAN technology for remote data transmission, making it suitable for various applications in smart city projects, residential and commercial water monitoring, and utility management.

## Working Principles

### Ultrasonic Measurement
The Qalcosonic W1 uses ultrasonic transit-time technology. It consists of two ultrasonic transducers positioned at a specific angle on the pipe. The device measures the time taken by ultrasonic waves to travel with and against the flow of water. The difference in these transit times is directly proportional to the flow rate. This non-invasive technique ensures high accuracy and minimal wear and tear, as there are no moving parts involved.

### Digital Signal Processing
Advanced digital signal processing (DSP) algorithms are employed to filter out noise and interference, resulting in stable and precise measurements even under challenging conditions, such as low flow or varying water quality.

## Installation Guide

### Site Preparation
1. **Pipe Preparation**: Ensure the pipe is clean and free of any debris or buildup where the meter is to be installed.
2. **Orientation**: Install the meter in a horizontal position with the display facing upward for optimal readability and performance.

### Installation Steps
1. **Pipe Cutting**: Cut the pipe to accommodate the meter's length and ensure smooth ends for coupling.
2. **Mounting**: Insert the meter in-line with the pipe using appropriate couplings, maintaining the correct flow direction, usually indicated by an arrow on the meter body.
3. **Tightening**: Use suitable tools to securely fasten the mounting, taking care not to over-tighten and damage the meter housing.

### Configuration
1. **Power Supply**: Install batteries as per manufacturer specifications, ensuring correct polarity.
2. **Calibration**: The meter is factory calibrated, but it is recommended to perform a system check to confirm calibration accuracy post-installation.
3. **Network Setup**: Configure the meter to connect to the local LoRaWAN network; this may require registration with the network provider and activation in accordance with local regulations.

## LoRaWAN Details

### Frequency and Bandwidth
- **Frequency Bands**: Supports both EU standard (868 MHz) and US standard (915 MHz) frequency bands, compliant with regional regulations.
- **Bandwidth**: Utilizes a bandwidth of 125 kHz for robust and efficient data transmission over long distances.

### Network Integration
- **Connectivity**: Connects seamlessly to LoRaWAN gateways, facilitating data upload to cloud services.
- **Data Transmission**: Sends periodic usage and status data, configurable in transmission intervals from every few minutes to several hours.

### Security
- Supports AES-128 encryption to ensure secure data transmission.

## Power Consumption
The Qalcosonic W1 is designed for low power consumption, typically powered by replaceable lithium batteries meant to last several years depending on configuration and usage. The use of LoRaWAN further optimizes energy use, as it is inherently a low power wide area network (LPWAN) technology.

## Use Cases
- **Residential Water Metering**: Offers precise household water usage monitoring, helping homeowners manage consumption and detect leaks.
- **Commercial Applications**: Ideal for commercial properties where tenants or departments require separate water billing.
- **Utility Management**: Provides utilities with reliable data for billing, demand forecasting, and supply management.
- **Smart Cities**: Integrates with smart city infrastructure to contribute to efficient water management, monitoring, and conservation initiatives.

## Limitations

1. **Installation Constraints**: Requires adequate pipe length for accurate measurements. Incorrect installation can result in inaccurate readings.
2. **Environmental Conditions**: While robust, extreme temperatures or corrosive water conditions can affect performance.
3. **Battery Life**: Battery lifespan is highly dependent on data transmission frequency and signal strength, which can vary with network coverage.
4. **Signal Interference**: Obstacles like buildings or dense foliage may impact LoRaWAN signal strength, requiring careful placement of gateways.
5. **Calibration**: While factory calibrated, periodic calibration checks are recommended to maintain accuracy, especially in high-demand use cases.

In summary, the Qalcosonic W1 by AXIOMA provides an efficient and reliable solution for contemporary water metering needs. Its advanced ultrasonic measurement capabilities, coupled with IoT connectivity via LoRaWAN, make it a versatile tool for modern water management environments. However, appropriate installation and network considerations are crucial to optimizing its performance and reliability.