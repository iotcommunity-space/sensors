**NETVOX - Rb11E Technical Overview**

The NETVOX – Rb11E is an advanced IoT sensor powered by LoRaWAN technology. The device primarily functions to monitor electric current status and detect factors such as overcurrent or undercurrent hazards. This document provides an in-depth understanding of the sensor's functionalities, installation process, power consumption, use cases, and limitations. 

**Working Principles**

The Rb11E operates based on LoRaWAN, a modulation technology for LoRa offering long-range, low-power features ideal for IoT applications. The device consists of an in-built AC current sensor, capable of monitoring the current in the range of 0 to 60 A AC. On detection of any anomalies in the current, such as overcurrent or undercurrent, the device sends an alert to the connected gateway using the LoRaWAN network.

**Installation Guide**

The Rb11E comes with an integrated CT (Current Transformer), and due to this, the installation process is straightforward. The CT is clamped onto the cable needing monitoring, and once attached, a LoRaWan gateway must be within range, and the device needs to be configured to the network.

1. Clamp the CT to the cable for monitoring.
2. Connect the device to a LoRaWAN gateway within range.
3. Configure your Rb11E to connect it to your network and set necessary alert levels.

**LoRaWAN Details**

Rb11E employs Class C LoRaWAN 1.0.2, utilizing the unlicensed radio spectrum in the Industrial, Scientific, and Medical (ISM) band. This helps in long-range transmissions, with up to 10 km in rural areas and 2 km in urban scenarios.

**Power Consumption**

Equipped with a 6500mAH battery, the Rb11E is designed for low power consumption, lasting up to 5 years depending on the use case and transmission frequency. The nominal voltage is 3.6V.

**Use Cases**

The RB11E sensors are valuable in various scenarios such as:

1. Industry: For monitoring machinery and ensuring they are operating within required current ranges.
2. Data centers: For preventing any overcurrent or undercurrent scenarios that might damage expensive equipment.
3. Residential homes: Monitoring of home appliances and early identification of electrical issues.

**Limitations**

Though highly efficient, the Rb11E sensor also has few limitations:

1. The device must be within the LoRaWAN gateway range for effective functioning.
2. The sensor only monitors AC current, making it non-useful for DC current monitoring.
3. The durability and battery life of the sensor highly depend on the usage frequency and environmental conditions.
4. The maximum detection range is 60A AC, limiting its usage in high current industrial application where current exceeds 60A.

Despite these minor limitations, the NETVOX - Rb11E stands out as a reliable, efficient, and user-friendly IoT sensor for monitoring electrical currents. With its long-range capabilities and low power consumption, it is ideally suited for a vast array of applications from industrial to household usage.