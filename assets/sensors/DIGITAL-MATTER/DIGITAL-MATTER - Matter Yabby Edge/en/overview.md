## Technical Overview: DIGITAL-MATTER Yabby Edge

The DIGITAL-MATTER Yabby Edge is a compact, efficient IoT device designed for asset tracking across various environments using LoRaWAN technology. It is known for its high performance in energy-saving geolocation as well as flexibility in deployment.

### Working Principles

The Yabby Edge utilizes a combination of GNSS (Global Navigation Satellite System), Wi-Fi scanning, and Bluetooth Low Energy (BLE) to determine the precise location of assets. It intelligently selects the most energy-efficient method based on the environment and availability of signals. The device leverages LoRaWAN for communication, enabling long-range low-power transmissions.

- **Geolocation**: Utilizes GNSS when outdoor signals are strong and switches to Wi-Fi scanning or BLE indoors or when signals are obscured, reducing power consumption and improving accuracy.
- **LoRaWAN Communication**: Sends data over the network to a cloud application where location and other parameters are logged and analyzed.
  
### Installation Guide

1. **Unboxing and Inspection**
   - Verify the integrity of the packaging and all included components.
   - Ensure the device is free from physical damage and check for the presence of necessary documentation.

2. **Activation**
   - Activate the device by removing the battery isolation tab.
   - The Yabby Edge typically comes with internal batteries pre-installed.

3. **Configuration**
   - Configure the device using the provided software or mobile app.
   - Set the reporting interval and geolocation mode according to your use case.

4. **Deployment**
   - The Yabby Edge can be affixed to assets using screws, cable ties, or industrial adhesives depending on the operational environment.
   - Ensure the device is mounted in a position unobstructed for best signal reception, such as on the top or side of an asset.

5. **Network Registration**
   - Register the device with the chosen LoRaWAN network provider by inputting the device EUI and other necessary details.

6. **Testing**
   - Conduct a field test to ensure successful data transmission to the network and check the reported location accuracy.

### LoRaWAN Details

- **Frequency Bands**: Supports global frequency bands, such as 868 MHz (EU) and 915 MHz (US).
- **Communication Range**: Typically ranges from 2 to 15 kilometers, depending on environmental conditions and network deployment.
- **Data Encryption**: Utilizes AES-128 encryption for secure data transmission.

### Power Consumption

The Yabby Edge is designed for ultra-low power consumption, with the capability to operate for multiple years on a single set of internal batteries, depending on the configuration and reporting interval. Energy-efficient algorithms and adaptive geolocation contribute significantly to battery longevity.

- **Typical Usage**: Battery life can reach up to 3 years with a daily update interval and optimal reception conditions.
- **Battery Type**: Utilizes field-replaceable lithium batteries.

### Use Cases

- **Asset Tracking**: Ideal for tracking pallets, containers, or construction equipment in logistics and supply chain operations.
- **Environmental Monitoring**: Suitable for situational monitoring in smart city applications when combined with compatible sensors.
- **Security**: Can be deployed for security and theft prevention in remote or high-value asset monitoring.

### Limitations

- **Signal Dependency**: Performance can be affected by signal obstructions, such as metallic enclosures or dense urban environments.
- **Battery Replacement**: Although long-lasting, the internal batteries will eventually require replacement or service, which may necessitate halting asset operations temporarily.
- **Non-Real-Time Tracking**: Best suited for periodic tracking rather than real-time location monitoring due to the nature of LoRaWAN duty cycles and power constraints.

The DIGITAL-MATTER Yabby Edge is a robust solution for a variety of asset tracking applications, offering flexibility, extended battery life, and secure communications, with considerations for installation environment and signal availability.