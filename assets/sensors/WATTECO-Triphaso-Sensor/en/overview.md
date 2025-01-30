# WATTECO - Triphaso Sensor Technical Overview

## Introduction
The WATTECO Triphaso Sensor is a robust, wireless IoT device designed to provide real-time monitoring of electrical parameters in three-phase systems. Leveraging the LoRaWAN protocol, it facilitates long-range, low-power communication to enable energy management, fault detection, and predictive maintenance.

## Working Principles
The Triphaso Sensor operates by measuring electrical parameters, such as voltage (V), current (I), power (P), and energy (kWh), from each of the three phases of an electrical installation. It utilizes Hall effect or Rogowski coils for non-intrusive current measurement and potential transformers for voltage measurement.

The device processes the analog signals through an onboard microcontroller to compute power-related metrics. These parameters are then transmitted wirelessly via LoRaWAN to a central dashboard for visualization and analysis.

## Installation Guide
1. **Safety Precautions**: Ensure all electrical installations are safely powered down before connecting the device.
2. **Mounting**: Secure the sensor in proximity to the electrical panel or distribution board using DIN rail or a screw mount.
3. **Connection**:
   - Attach the current sensors (clip-on or flexible Rogowski coils) to the respective phase conductors.
   - Connect voltage taps using the provided leads. Ensure phase alignment of voltage and current inputs.
4. **Powering**:
   - For direct mains power, ensure connections are secure and rated for the voltage and current levels in use.
   - Alternatively, use an external power supply if specified.
5. **Configuration**:
   - Use the WATTECO configuration tool or application to set up device parameters such as LoRaWAN credentials (DevEUI, AppEUI, AppKey), transmission intervals, and measurement calibration.

## LoRaWAN Details
The Triphaso Sensor is designed to operate on the LoRaWAN network, compatible with both public and private deployments:
- **Frequency Bands**: Supports different ISM bands (e.g., EU868, US915, AS923) according to regional requirements.
- **Activation Method**: Typically supports both OTAA (Over-The-Air Activation) and ABP (Activation By Personalization).
- **Data Transmission**: Configurable uplink intervals, adaptive data rates, and confirmed/unconfirmed messages to optimize battery life and network performance.
- **Security**: Triple-layered encryption for data integrity and confidentiality.

## Power Consumption
The Triphaso Sensor is energy-efficient, designed for both battery operation and external power sources:
- **Battery Operation**: Utilizes a long-life battery optimized for years of operation, with consumption depending on the frequency of data transmission (< 1 mW in deep sleep mode).
- **External Power**: When powered by an external supply, the device fully utilizes low-power features while enabling more frequent data updates.

## Use Cases
- **Energy Management**: Monitor and control energy consumption in industrial and commercial facilities.
- **Fault Detection**: Early warning systems for detecting electrical faults, imbalance, or phase loss in distribution systems.
- **Predictive Maintenance**: Identify equipment inefficiencies or overloading conditions to schedule maintenance and prevent downtime.
- **Remote Monitoring**: Ideal for asset monitoring in remote or challenging environments without hardwired connectivity.

## Limitations
- **Range Limitations**: LoRaWAN performance is subject to environmental factors, such as obstructions and interference, which may affect communication range.
- **Data Update Rate**: Due to LoRaWAN's low data rate, there is a trade-off between data granularity and power consumption.
- **Installation Complexity**: Requires qualified personnel to ensure safe and correct installation and configuration.
- **Accuracy**: Measurement precision may be influenced by installation quality and sensor alignment.

The WATTECO Triphaso Sensor offers a comprehensive solution for effective three-phase electrical monitoring, promising to enhance operational efficiency while maintaining low-power requirements. However, users must consider range and data rate constraints when planning deployments to ensure optimal performance.