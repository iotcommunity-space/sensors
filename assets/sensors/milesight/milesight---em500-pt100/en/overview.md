## MILESIGHT EM500-PT100 Technical Overview

### Working Principles

The MILESIGHT EM500-PT100 is a specifically designed IoT sensor for temperature measurement utilizing the PT100 sensing technology. A PT100 get its name from its positive resistance change of 100 ohms for every degree Celsius rise in temperature. This sensor measures temperature changes by correlating the resistance change of the PT100 sensing element. This therefore provides a precise and repeatable temperature data that can be used across a variety of industrial, commercial and domestic applications and environments.

### Installation Guide

Installation of the EM500-PT100 sensor majorly involves proper positioning of the sensor, attaching the PT100 probe, and connecting to a gateway device.

1. **Positioning the Sensor:** Identify an optimal location for the sensor. This should be at a convenient location which also favors a strong connectivity. Avoid any metal objects or surfaces while positioning the sensor since they can interfere with the device’s wireless signals.
   
2. **Attaching the PT100 Probe:** The PT100 probe can be attached onto the desired target area where temperature measurements are desired. However, care should be taken since the probe is sensitive and fragile.
   
3. **Connecting to the Gateway:** The sensor must be connected to a LoRaWAN gateway to facilitate wireless data transmission. The frequency should be set on both the gateway and the sensor to ensure that they are in the same communication band.

### LoRaWAN Details

The MILESIGHT EM500-PT100 sensor uses LoRaWAN Class A communication protocol. This means that the sensor communicates in an asynchronous manner with the gateway and it's not always listening for downlink messages. It operates on various frequency bands depending on the region (EU868, US915, AU915, AS923, KR920, IN865), which is in concordance with the regional LoRaWAN protocol specification. 

### Power Consumption

Because of its low power consumption capabilities, the EM500-PT100 has a long battery life of up to 10 years.  Its power consumption is rated at 2 μA in sleep mode, 14.5 mA in receive mode, and in transmit mode, it varies (max 130 mA @+20 dBm). Given the frequency of data transmission, these figures may vary under different conditions.

### Use Cases

The EM500-PT100 sensor finds a wide variety of applications in domains including but are not limited to:
1. Industrial temperature monitoring for machinery and equipment.
2. HVAC system temperature monitoring.
3. Environmental temperature monitoring in fields like agriculture, horticulture, etc.
4. Temperature monitoring in data centers.

### Limitations

While the EM500-PT100 has numerous advantages and applications:
1. It is limited by its LoRaWAN communication technology, ranging up to 10 km in rural areas, and up to 2 km in urban areas, depending on the environment and interferences.
2. The sensor may experience signal interferences from metals and other obstacles if not properly positioned.
3. The battery life might be shorter if data is transmitted at a very high frequency, as this increases power consumption.
4. The brittle nature of the PT100 probe also stands as a limitation, extra care should be taken to prevent physical damage.

In conclusion, the EM500-PT100 is a highly useful IoT sensor tool for any temperature-dependent industry, owing to its highly efficient, precise and reliable temperature measurement within an easy plug-and-play design. However, optimal use and longevity depend largely on correct installation and usage practices.