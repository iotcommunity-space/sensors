### DRAGINO - Sw3L (DRAGINO) Overview

#### Working Principles

The DRAGINO - Sw3L sensor works on the principle of LoRa (Long Range) WAN wireless data transmission technology which enables long-range transmissions (up to 10,000 meters) while consuming relatively low power. The sensor is equipped with digital inputs for dry contact detection. When a connected external sensor or device triggers an input, the DRAGINO - Sw3L converts and sends this information as a data packet over the LoRaWAN network to an assigned gateway.

#### Installation Guide
1. Attach the DRAGINO - Sw3L to the device from where you want to acquire data.
2. Connect the external sensor/device to the DRAGINO - Sw3L via digital input.
3. Power on the sensor. The DRAGINO - Sw3L will automatically search for available LoRaWAN networks and connect to the strongest one available. Either by using Over-The-Air Activation (OTAA) or Activation By Personalization (ABP) methods.
4. The sensor is now ready to transmit acquired data to your selected gateway.

#### LoRaWAN details
DRAGINO - Sw3L uses the global LoRaWAN frequency standard and supports many frequency bands like AS923, AU915, EU868, US915, CN470, and KR630. The data rate ranges from DR0-D7 depending on the LoRaWAN regional parameter. The sensor also incorporates advanced features such as adaptive data rate (ADR) and over-the-air updates.

#### Power Consumption
Powered by a AA-size battery, the DRAGINO - Sw3L is designed for low power consumption. In normal operation, the power consumption is about 15 mA at 3V. When in sleep mode, the power consumption falls below 20µA, prolonging battery life considerably.

#### Use Cases
1. Industrial automation/control: Connection to various switches or industrial machines to record and transmit data on operation status.
2. Agriculture: Connected to water level sensors in irrigation systems to monitor and control water levels.
3. Home automation: As a part of smart home systems to monitor and control various equipment and systems in the home.

#### Limitations
While DRAGINO - Sw3L offers many benefits, it's not without limitations. Some include:
- The sensor itself doesn't have IP67 protection, so it's not advised to expose it directly to harsh environmental conditions without proper protective casing.
- The maximum transmission range might be affected by physical barriers and environmental conditions affecting signal strength.
- Despite low energy consumption, the battery needs to be replaced when depleted.
- There is the need for a LoRaWAN network gateway connection, an external factor that might affect DRAGINO - Sw3L functionality.