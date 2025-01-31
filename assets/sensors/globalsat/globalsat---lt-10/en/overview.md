### GLOBALSAT - Lt 10 Technical Overview

**I. Working Principle**

The GLOBALSAT Lt 10 is a LoRaWAN powered asset tracker designed to keep track of assets, whether stationary or mobile. The device uses Global Navigation Satellite System (GNSS) technology to calculate its geographical location, then transmits this location and other data back to the user's designated network server via LoRaWAN RF technology.

**II. Installation Guide**

1. **Physical Installation**: Attach the GLOBALSAT Lt 10 to the meeting point of the material to be tracked. Its robust enclosure design allows it to withstand harsh external environments. Note, the device should be installed in a place with a clear view of the sky for an optimal GNSS signal.

2. **Network Configuration**: Register the device on your LoRaWAN network server. You'll require the device's unique EUI, which can be found on the device. 

3. **Device Setup**: Configure the device using the GLOBALSAT Lt 10 configuration tool. You may set up parameters like reporting frequencies, LoRaWAN settings, alarms, etc, depending on your specific use case. Save and export your configurations then import them into your device.

**III. LoRaWAN Details**

The GLOBALSAT Lt 10 uses LoRaWAN technology for its network communication. It operates in different frequency bands (US915, AU915, EU868, AS923, and KR920) depending on the geographical location. It supports both ADR and DR (Data Rate) settings, giving users more control over the tradeoff between the device's range and energy usage.

**IV. Power Consumption**

The device operates on non-rechargeable 3.6V/3600mAh Lithium battery which can typically provide up to 5 years of operation, depending on the upload frequency and environmental conditions. The GLOBALSAT Lt 10 also comes with power-saving options which users may exploit to extend battery life.

**V. Use Cases**

The GLOBALSAT Lt 10 can be used in various industries for asset tracking purposes such as:

- Logistics and Supply Chain: Tracking the movement and location of goods
- Agriculture: Monitoring and managing farm machinery  
- Construction: Keeping track of high-value construction equipment
- Public Services: Keeping track of waste containers or other mobile city assets
- Fleet management: Tracking of commercial vehicles

**VI. Limitations**

Despite its various use cases, the GLOBALSAT Lt 10 comes with its limitations:

- It requires a clear view of the sky for optimal GNSS performance. Indoor or dense urban environments can affect accuracy.
- It can only guarantee the Battery Life under certain usage conditions, such as the frequency of data transmission and environmental factors.
- It can only function within the coverage area of a LoRaWAN gateway.
- It can’t deliver real-time tracking due to the nature of LoRaWAN’s duty cycle limitations and fair usage policy.
- Being a non-cellular device, it cannot function in locations without LoRaWAN coverage.

Despite these limitations, the GLOBALSAT Lt 10 is a reliable device for IoT applications within its designed use case. Please ensure to test the device under your specific use conditions to affirm suitability.