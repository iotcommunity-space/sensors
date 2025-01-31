**Technical Overview for DRAGino - LDS02 (Dragino)**

**Working Principles**

LDS02 is a LoRaWAN leaf wetness sensor developed by Dragino Technology. The sensor works based on the principle of resistive leaf wetness detection. It detects the presence of water droplets on its surface via electrical resistance measurements across a grid surface. When a resistive grid on the leaf-like surface of the sensor gets wet, the current between the grid wires changes to give a measured value for leaf wetness.

**Installation Guide**

1. Place the leaf surface of the LDS02 sensor facing up underneath the plant canopy, parallel to the ground before connecting to the controller.

2. First, connect one end of the 5.5 mm DC plug to the "PWR & I/O" interface on the device.

3. Connect the other end with power interface and I/O interface.

4. Connect the device with the LoRaWAN network by following the network onboarding guide.

**LoRaWAN Details**

LDS02 is compatible with the LoRaWAN protocol, which means it can be used in any LoRaWAN compliant network. It supports different LoRaWan frequency bands which makes it versatile for deployments in different regions. The frequency bands supported include AS923, CN470, EU433, EU868, IN865, KR920, US915, AU915, and RU864.

**Power Consumption**

The LDS02 sensor is powered by a 12V DC power source. In standby mode, the device consumes about 50uA. During transmission, the device's power consumption can peak up to 140mA. 

**Use Cases**

Agricultural context: The LDS02 is particularly relevant in agricultural setups. Farmers can use them to prevent diseases that spread in wet conditions, trigger watering in an irrigation system or determine the best time to apply fungicides.

Research: It is used in research to study micro climates and understand how leaf wetness influences diseases and fungus spread. 

**Limitations**

1. Reading Accuracy: Although the LDS02 provides effective readings, its measurements are qualitative rather than quantitative due to its resistive measurement method. 

2. Requires Line-of-sight: As with standard LoRaWAN devices, the LDS02 requires line-of-sight to communicate with the network gateway, this may limit its deployment in certain environments.

3. Fixed Functionality: The sensor is only designed for detecting leaf moisture. It won't provide readings for other environmental conditions like temperature or humidity.

4. Outdoor Conditions: LDS02 is designed to be weather-proof, but extreme weather conditions may affect the device’s lifespan or operations. Proper precautions should be considered when deploying the device in such environments.