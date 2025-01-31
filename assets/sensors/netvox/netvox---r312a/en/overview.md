### NETVOX - R312A Technical Documentation

#### 1. Overview
The Netvox R312A is a cutting-edge wireless IoT sensor that employs the LoRaWAN protocol and is specifically designed to monitor the presence or absence of liquid in tanks, sumps, and containers.

#### 2. Working Principle
The working principle of the NETVOX R312A is relatively straightforward. The device contains a sensing element that interfaces with the fluid. When the liquid level crosses the detection point, the sensor responds accordingly, generating a signal indicating the presence or absence of liquid. This signal is then transmitted wirelessly over a LoRaWAN network to the receiving endpoint.

#### 3. Installation Guide
1. Open the silicone protection layer at the bottom of the device.
2. Position the device in a proper place where you want to monitor the liquid level.
3. Close the silicone bottom layer after the installation.
4. Long-press the button on the device for 5 seconds until a LED light starts to flash, which indicates the device is in network-joining mode.
5. Use your LoRaWAN server's interface to register the sensor by entering the NETVOX sensor’s DevEUI.
6. Once the sensor is registered, it will start to send data to your server through the LoRaWAN network.

#### 4. LoRaWAN Details
The R312A operates in the EU433 and CN470-510 frequency band for China and the EU863-870, US902-928, AU915-928 and AS923 band for other global regions, regulated by the LoRaWAN protocol. The device supports adaptive data rate (ADR) and LoRaWAN confirmed and unconfirmed messages.

#### 5. Power Consumption
The power of the NETVOX R312A is supplied by a 19000mAH ER34615 battery. The battery life is expected to last over 10 years (depending on the frequency of data transmission).

#### 6. Use cases
The NETVOX R312A sensor finds utility in a plethora of sectors. It is commonly used in industrial areas to monitor liquid levels in tanks, containers, and sumps. Additionally, it can be employed in environmental monitoring systems, smart agriculture for irrigation system control, in residential premises to monitor water or fuel tanks, and more.

#### 7. Limitations
While the NETVOX R312A sensor has a robust feature set, there are a few limitations to consider. Distinctly, the sensor is not suitable for detecting the precise volume of liquid. It simply detects the absence or presence of fluid at a given level. Hence, it may not be appropriate for applications that require exact measurement of liquid volume or weight.

Furthermore, the sensor's battery is not rechargeable. Therefore, once the battery gets depleted, it needs to be replaced.

In certain environments, the wireless range may be less than the maximum possible distance due to obstructions or RF interference. However, this is a limitation of all LoRaWAN devices, not exclusive to the R312A.