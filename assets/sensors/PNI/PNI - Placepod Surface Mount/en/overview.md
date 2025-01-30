# Technical Overview for PNI - Placepod Surface Mount

## Introduction

The PNI PlacePod Surface Mount is a sensor designed to provide real-time data for smart parking management systems. The sensor integrates leading-edge vehicle detection capabilities with IoT connectivity, specifically utilizing the LoRaWAN communication protocol, to deliver reliable parking space status information. Its primary function is to detect the presence or absence of a vehicle in a parking spot, which can be crucial for efficient urban parking management.

## Working Principles

The PNI PlacePod Surface Mount operates using a highly sensitive magnetic sensing technology. This allows the sensor to detect disturbances in the Earth's magnetic field caused by a vehicle parked above the sensor. With its proprietary algorithms, the PlacePod provides accurate vehicle detection even in challenging environmental conditions, such as extreme temperatures or high levels of electromagnetic interference.

## Installation Guide

### Pre-installation Considerations

- **Site Selection**: Identify appropriate installation sites that are free from large metallic structural influences other than the vehicles themselves.
- **Environmental Suitability**: Ensure that the area is not subject to flooding or standing water, as the casing is weatherproof but not waterproof in terms of submersion.

### Installation Steps

1. **Prepare the Site**: Clean and dry the surface where the PlacePod is to be installed. Ensure that the position selected is directly within the parking space.

2. **Mounting the Sensor**: The PlacePod Surface Mount is designed for adhesive installation. Use the supplied high-strength adhesive to bond the sensor to the surface.

3. **Calibration**: Once installed, the sensor automatically begins a calibration process that typically lasts a few minutes. During this period, it identifies baseline magnetic field readings for accurate future comparisons.

4. **Verification**: Use the companion mobile or desktop application to verify sensor operation. Check readings to ensure that the sensor accurately detects parked vehicles.

## LoRaWAN Details

The PNI PlacePod supports LoRaWAN connectivity, allowing it to send data over long ranges with low power consumption. Key features include:

- **Network Compatibility**: Compatible with standard LoRaWAN networks, the PlacePod can be integrated into existing network infrastructures.
- **Frequency Bands**: The device supports multiple frequency bands, including EU868, US915, AS923, and AU915, among others, depending on regional specifications.
- **Data Transmission**: Capable of up to 10 years of battery life through periodic data reporting, typically every 5 minutes for real-time updates.
- **Configuration**: The PlacePod can be remotely configured for various parameters such as transmission interval and sensitivity settings.

## Power Consumption

The PlacePod is equipped with a long-life lithium battery optimized for low power consumption and extended service life. Under typical conditions with standard reporting intervals, the battery can last up to 10 years, depending on environmental conditions and the frequency of vehicle detections.

## Use Cases

- **Smart City Parking**: Integrating multiple PlacePods across a city can optimize parking utilization and reduce congestion.
- **Commercial Parking Management**: Retail environments can use PlacePod sensors to monitor parking lot availability and inform customers in real-time.
- **Event Spaces**: Large venues can enhance visitor experience by providing up-to-date parking availability via integrated apps.
- **Campus Management**: Universities can manage parking distribution effectively with real-time data, allowing for efficient space allocation.

## Limitations

While the PNI PlacePod Surface Mount offers a robust solution for smart parking management, certain limitations must be considered:

- **Environmental Limitations**: While designed to withstand various weather conditions, prolonged exposure to extreme temperatures or water may affect performance.
- **Metallic Interference**: Significant nearby metallic structures, other than vehicles, may alter magnetic readings, potentially affecting accuracy.
- **Connectivity Dependence**: The sensor's performance relies heavily on the presence of a stable LoRaWAN network; any interruptions could delay data reporting.
- **Installation Surface**: Adequate surface preparation is crucial for effective adhesive bonding; ineffective bonding can lead to operational failures.
  
Overall, the PNI PlacePod Surface Mount is a sophisticated addition to any IoT-based parking management system, promising reliability, efficiency, and adaptability within its operational parameters.