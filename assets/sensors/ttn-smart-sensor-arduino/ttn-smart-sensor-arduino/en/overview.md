Product Name: TTN Smart Sensor (Arduino)

Technical Overview:

The TTN Smart Sensor, designed with Arduino technology, is an Internet of Things (IoT) device purposed to collect and transmit data in a broad spectrum of applications including environmental monitoring, structural health surveillance, agricultural monitoring, energy management, etc. 

Working Principles:
The TTN Smart Sensor operates by collecting specific data such as temperature or humidity from its environment using the embedded sensor. The sensor interfaces with an Arduino microcontroller, where the raw data is processed. Post-processing, the data is sent to TTN (The Things Network) gateway via LoRaWAN (Long Range Wide Area Network) protocol. The information is then made accessible for end-users in a comprehendible format via cloud service or application. 

Installation Guide:
1. Connect the TTN Smart Sensor to the host Arduino board using the appropriate headers or connectors.
2. Download and install the specific Arduino IDE on your computer.
3. Implement the sensor's library files within the IDE.
4. Upload a suitable sketch onto the Arduino board. 
5. Register your device on The Things Network and retrieve the required keys.
6. Paste your keys into your Arduino sketch.
7. Finally, connect your device to a power supply to start sending data to TTN.

LoRaWAN Details:
The TTN Smart Sensor utilizes LoRaWAN network - an open-source wireless data communication protocol. LoRaWAN optimizes coverage by application of low-power wide area network technology for communication between sensor and TTN gateway, making it perfect for IoT devices where power and network efficiency is crucial.

Power Consumption:
The TTN Smart Sensor (Arduino) promotes low power consumption. Its power usage varies as per the operation state. During sleep mode, it consumes approximate 1.2μA, while in active mode, the consumption can hike up to 120mA based on load and function.

Use Cases:
There are abundant use cases for TTN Smart Sensor:
1. In agriculture, for soil moisture and temperature monitoring to regulate irrigation.
2. In cities, for air quality and noise levels monitoring to assess environmental conditions.
3. In industries, for machine health monitoring to predict maintenances.
4. In homes, for energy usage monitoring to save electricity.

Limitations:
Though there's tremendous potential for TTN Smart Sensors, some limitations do exist.
1. LoRaWAN network's data rate is low, limiting the sensor's use where high-speed data transfer is required.
2. Sensor accuracy complaint has been reported in some applications.
3. Coverage might be limited to urban areas due to the need for gateway proximity.
4. The signal may also be affected by physical obstructions.
5. Assumes basic familiarity with Arduino environment and programming, which can be challenging for non-technical users.