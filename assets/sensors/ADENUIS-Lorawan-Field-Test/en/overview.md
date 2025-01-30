# ADENUIS - LoRaWAN Field Test

## Technical Overview

The ADENUIS LoRaWAN Field Test device is designed to provide an efficient way to perform field testing of LoRaWAN networks. This device enables users to measure network performance, ensuring optimal placement and configuration of LoRaWAN gateways and sensors.

### Working Principles

The ADENUIS relies on LoRaWAN technology, which utilizes Chirp Spread Spectrum (CSS) modulation to achieve long-range communication with low power consumption. The field test device acts as a simulated node, sending data packets to evaluate network metrics such as signal strength, data rate, and packet loss.

Key Components:
- **LoRaWAN Transceiver**: Handles the transmission and reception of signals adhering to LoRaWAN specifications.
- **Microcontroller**: Controls device operation, data logging, and user interface.
- **GPS Module**: Provides geolocation data to correlate network performance with geographical location.
- **OLED Display**: Displays real-time testing results and device status.
- **Battery Unit**: Powers the device with a long-lasting rechargeable battery.

### Installation Guide

1. **Unbox the Device**: Ensure all components, including the LoRaWAN Field Test unit, charging cables, and user manual, are present.

2. **Charge the Battery**: Connect the device to a power source using the provided cable until fully charged, as indicated by the battery status icon on the OLED display.

3. **Turn on the Device**: Press and hold the power button until the display lights up and initializes the system.

4. **Configure Network Settings**:
   - Use the arrow keys to navigate through the menu.
   - Enter LoRaWAN parameters such as Device EUI, Application EUI, and Application Key.
   - Select the desired frequency band and data rate according to the region of operation regulations.

5. **Start Testing**: Select the testing mode and press 'Start' to begin sending packets. The device will display real-time metrics.

6. **Analyze Results**: Results can be viewed on the display or exported via USB connection for detailed analysis.

### LoRaWAN Details

- **Frequency Bands**: Supports all global LoRaWAN frequency bands, such as EU868, US915, AS923, etc.
- **Adaptive Data Rate (ADR)**: Automatically adjusts data rates for optimal network performance.
- **Security**: Utilizes standard LoRaWAN encryption for secure communication.
- **Range**: Capable of supporting communication over several kilometers, depending on environmental conditions and regional regulations.

### Power Consumption

The ADENUIS LoRaWAN Field Test device is engineered for low power consumption, allowing extended field testing without frequent recharging.

- **Sleep Mode**: Conserves energy during idle periods by entering a low-power sleep state.
- **Active Mode**: Consumes approximately 50 mA in a typical transmission scenario, adjusted as per the selected data rate and power settings.

### Use Cases

- **Network Signal Mapping**: Provides detailed signal coverage maps for network deployment.
- **Gateway Placement**: Aids in determining the optimal locations for LoRaWAN gateways.
- **Performance Monitoring**: Conducts regular network diagnostics to ensure efficient operation.
- **Environmental Studies**: Supports studies by analyzing network capabilities in different terrains and conditions.

### Limitations

- **Obstructions**: Signal strength can be significantly affected by physical barriers like buildings and dense foliage.
- **Interference**: Performance may degrade in environments with high RF interference.
- **Data Rate Limitations**: Limited by regional regulations, which can affect throughput and latency.
- **Battery Life**: While optimized, battery life may vary with intensive usage and frequent data transmissions.

The ADENUIS LoRaWAN Field Test device provides a comprehensive tool for evaluating and ensuring the efficiency of LoRaWAN networks, though operators must account for environmental and regulatory constraints during deployment.