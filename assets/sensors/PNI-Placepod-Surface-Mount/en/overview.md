# PNI - PlacePod Surface Mount Technical Overview

The PNI PlacePod Surface Mount is an advanced vehicle detection sensor designed to be installed in parking spaces for real-time monitoring and management of parking areas. Utilizing LoRaWAN communication technology, the device enables smart city applications by providing accurate data on parking availability.

## Working Principles

The PlacePod Surface Mount sensor utilizes magneto-inductive technology and a geo-magnetic sensor coupled with advanced algorithms. It detects disturbances in the Earth's magnetic field caused by the presence of a vehicle above the sensor. Its sophisticated signal processing enables reliable vehicle detection even in harsh environmental conditions.

### Key Features:
- **Magneto-Inductive Sensing**: Offers precise vehicle detection with low false positive rates.
- **Geo-Magnetic Sensor**: Provides stability and reliability in data collection.
- **Real-Time Data Transmission**: Sends data via LoRaWAN to a centralized management system.

## Installation Guide

### Pre-Installation Requirements:
1. **Site Survey**: Ensure the parking area is suitable for sensor installation, considering signal strength and environmental factors.
2. **Tools Needed**: Drill, screws for surface mounting, LoRaWAN network gateway setup.

### Installation Steps:
1. **Positioning**: Identify the center of the parking space where the sensor will be mounted.
2. **Mounting**: Secure the sensor onto the surface using the provided screws. Ensure it is level and firmly attached.
3. **Calibration**: Once installed, calibrate the sensor in situ to account for local magnetic fields and environmental conditions.
4. **Connectivity Check**: Verify that the sensor is communicating effectively with the LoRaWAN gateway.

## LoRaWAN Details

The PlacePod Surface Mount uses LoRaWAN to transmit data to the cloud. This ensures long-range communication with low power consumption, crucial for IoT deployments in wide areas.

### Communication Parameters:
- **Frequency Bands**: Typically 915 MHz for North America, 868 MHz for Europe. Ensure compatibility with local regulations.
- **Data Rate**: Adapts based on the network setup (e.g., ADR - Adaptive Data Rate).
- **Security**: Utilizes AES encryption to secure data transmission.

## Power Consumption

The PlacePod Surface Mount is designed for energy efficiency, integral to its deployment in battery-powered environments.

- **Battery Life**: Typically exceeds 5 years, depending on transmission frequency and environmental conditions.
- **Low Power Deployment**: Regular sleep modes between detections reduce energy use.

## Use Cases

The PlacePod Surface Mount sensor is versatile in applications such as:

1. **Smart Parking Solutions**:
   - Real-time data enables smart parking guidance systems.
   - Facilitates dynamic pricing and reservation systems.

2. **Traffic Management**:
   - Provides data analytics for traffic flow and congestion management.
   - Helps with urban planning and development projects.

3. **Retail Parking Zones**:
   - Enhances customer experience by showing available parking.
   - Integrates with loyalty programs for frequent visitors.

## Limitations

While the PNI PlacePod Surface Mount offers significant advantages, there are some limitations to consider:

- **Installation Environment**: Performance might be affected by extreme magnetic disturbances or improperly conducted installation sites.
- **Signal Interference**: Dense urban environments may affect LoRaWAN signal performance.
- **Physical Obstacles**: Non-vehicular metallic objects temporarily placed over the sensor may lead to false detection.

In summary, the PNI PlacePod Surface Mount is a robust and effective solution for smart parking and traffic management. Its utilization of magneto-inductive technology and LoRaWAN ensures reliable operation, making it a valuable component in modern IoT urban infrastructure solutions. Proper installation and network setup are essential to maximize its capabilities.