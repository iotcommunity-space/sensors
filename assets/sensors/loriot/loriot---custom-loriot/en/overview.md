## LORIOT - Custom Loriot (LORIOT) Technical Overview

### I. Working Principles

The LORIOT (Long Range Internet Of Things) software is a server-side application designed to manage, control and supervise the Low Range (LoRa) protocol-based IoT infrastructures. The software enables secure bidirectional communication, end-to-end security, mobility, and localization services between sensors and the network server.

#### System Architecture:

The LORIOT server distributes the workload across different functional modules, which are encapsulated as microservices. These ensure a scalable, stable, and robust LoRaWAN environment compatible with thousands of gateways and millions of devices.

#### Device Management:

Device management on the LORIOT platform involves setting up and managing the lifecycle of LoRaWAN sensors and gateways added to the network.

### II. Installation Guide

Custom Loriot can be set up on various hardware platforms. The essential requirements include a Linux operating system, preferably Ubuntu, and the specific gateway details.

Installation involves obtaining the software packet from the LORiOT Server, unpacking it on the system, and then launching the process with specific user credentials. Users must configure the IoT devices and gateways via the LORIOT management interface.

The setup also involves the configuration of end-device with specific parameters mainly- DevEUI, AppEUI, and AppKey for OTAA, or DevEUI, DevAddr, NwkSKey, AppSKey for ABP.

### III. LoRaWAN Details

LORIOT operates on LoRaWAN technology, designed for wide area networks. LORIOT supports LoRaWAN 1.0 and 1.1, including all classes (A, B, C) and regional parameters defined by LoRa-Alliance.

LoRaWAN with LORIOT has a range covering several kilometers, providing connectivity for devices that require very long battery life, and suits applications demanding low-cost mobility and a secure bi-directional communication.

### IV. Power Consumption

Power consumption with LoRaWAN protocol, and hence LORIOT, is considerably low due to its unique modulation technique. This makes it feasible to deploy battery-powered devices, with battery life extending up to several years.

### V. Use Cases

1. **Smart Agriculture**: LORIOT can support applications in the agriculture sector, including monitoring of soil moisture levels, atmospheric conditions, pest detection, etc.

2. **Smart Cities**: In urban environments, LORIOT can power waste management systems, smart parking, environmental monitoring, and public infrastructure management.

3. **Supply Chain**: It can also help optimize supply chain processes through asset tracking, inventory management, and condition monitoring.

4. **Industrial IoT**: For Industrial IoT, LORIOT can help in predictive maintenance of machinery, energy management, and warehouse management.

### VI. Limitations

- LORIOT LoRaWAN doesn't support real-time transmission due to the time it takes for data to travel back-and-forth over long distances.

- Limited payload size of LoRaWAN packets restricts the amount of data to be sent at one time.

- While LORIOT is relatively easy to use, actual deployment may require technical expertise to handle gateway installation, network management, etc.

- Interference may occur in urban or densely populated environments due to the unlicensed Sub-GHz band used by LoRa. 

Summarily, LORIOT offers a robust, scalable solution for managing and controlling LoRaWAN IoT infrastructures, making long-range IoT networks seamless and efficient. Given the versatile applications of LORIOT, its usage can extend across various industries and use-cases, notwithstanding few limitations associated with LoRaWAN technology.