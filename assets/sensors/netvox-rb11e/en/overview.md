# Technical Overview for NETVOX - Rb11E

The NETVOX Rb11E is a versatile IoT sensor designed to detect and communicate changes in environmental conditions. This sensor is part of NETVOX's range of wireless, battery-operated devices that leverage LoRaWAN technology for long-range communication.

## Working Principles

The NETVOX Rb11E operates as a wireless contact sensor, capable of detecting open/close events in a variety of applications. It utilizes a magnetic reed switch, which changes state when the accompanying magnet is removed (open) or brought closer (closed). The sensor transmits data related to these state changes using LoRaWAN, a low-power, wide-area networking protocol. This allows it to communicate events over significant distances, making it suitable for monitoring remote locations.

### Key Features:
- **Magnetic Contact Sensor**: Detects open/close events.
- **LoRaWAN Communication**: Supports long-range data transmission using LoRaWAN Class A protocol.
- **Configurability**: Various parameters including uplink interval and alarm thresholds can be configured.
- **Low Power Operation**: Designed to be power-efficient to support long-term battery use.

## Installation Guide

### Step-by-Step Installation:

1. **Unpack and Inspect**: Begin by carefully unpacking the Rb11E sensor. Ensure that all components, including the sensor and magnet, are intact and undamaged.
   
2. **Positioning**: Identify the correct location for installation. The sensor and magnet should be aligned so that they maintain orientation as specified (parallel) when doors/windows are closed.

3. **Mount the Sensor**:
   - Use the adhesive backing or screws provided to mount the sensor unit on the fixed frame (door/window frame).
   - Attach the magnet on the movable part (door/window) ensuring it is aligned with the sensor when in the closed position.

4. **Configuration**:
   - If required, access the internal DIP switches or software configuration settings to set the desired parameters.
   - Typical configurable settings include data reporting intervals and threshold values. Refer to the user manual for detailed configuration instructions.

5. **Activate the Device**: Insert the battery if not pre-installed. Ensure the device powers up and performs a self-check (usually indicated by an LED).

6. **Network Integration**: Register the device with the desired LoRaWAN network. Input the Device EUI, App Key, and other necessary credentials to integrate the Rb11E with your network server.

7. **Testing**: Open and close the monitored object (e.g., door) to confirm that the sensor is correctly detecting state changes and sending data to the network.

8. **Final Adjustment**: Once verified, ensure that the sensor and network settings are secured and the tamper detection feature (if applicable) is active.

## LoRaWAN Details

- **Protocol**: The Rb11E uses LoRaWAN Class A communication, designed for low power battery-operated devices.
- **Frequency Bands**: Compatible with LoRaWAN frequency bands including EU868, US915, AS923, and others based on regional regulations.
- **Data Rates**: Adaptive Data Rate (ADR) to optimize the data transmission rate and power consumption.
- **Range**: Transmits up to several kilometers depending on environmental factors and network configurations.

## Power Consumption

- **Battery Type**: Typically equipped with a CR123A lithium battery.
- **Battery Life**: Estimated battery life varies depending on reporting intervals and environmental conditions, but can last up to several years with optimal configuration.
- **Sleep Mode**: Utilizes a sleep mode to significantly reduce power consumption between transmission intervals.

## Use Cases

The Rb11E is suitable for a wide range of applications, including but not limited to:
- **Security Systems**: Monitoring door and window states in residential and commercial properties.
- **Industrial Applications**: Supervising the state of equipment enclosures and industrial machinery access points.
- **Building Management**: Integration into smart building systems for facility monitoring.

## Limitations

- **Magnet Alignment**: The sensor's functionality is dependent on maintaining proper alignment with the magnet, which can be a limiting factor in certain installation environments.
- **Obstructions and Interference**: Physical barriers and RF interference could diminish effective communication range and reliability.
- **Battery Dependency**: Operational dependence on battery life necessitates periodic checks, especially in mission-critical applications.

In conclusion, the NETVOX Rb11E is a highly reliable and versatile sensor offering long-range, low-power wireless communication suitable for multiple market segments. Proper installation and configuration are critical to optimizing its performance and battery longevity.