## ELSYS - ERS Desk Technical Overview

The ELSYS - ERS Desk is a highly sophisticated IoT sensor created to monitor and track an array of different environmental parameters in an indoor setting. Fundamentally, the device operates by analyzing and recording the presence or absence of individuals sitting at desks to help optimize office space utilization. 

### Working Principles:
The ERS Desk sensor employs advanced infrared technology to detect occupancy. By measuring the thermal radiation emitted by objects in its field of view, it is capable of identifying whether a desk or workspace is currently in use. Complimenting this functionality, it also collects data regarding temperature and humidity, providing a comprehensive overview of an office environment. 

### Installation Guide:
Mounting and installing the ERS Desk sensor is straightforward:

1. Firstly, ensure you have an optimal site selected for the sensor - it should have a clear view of the desk to be monitored.
2. Fasten the sensor either to the ceiling or high on a wall directing towards the desk.
3. Once installed, the sensor then needs to be linked to the desired LoRaWAN network, this requires the Network Server address, Network Session Key and Data Rate to be input into the device.

### LoRaWAN Details:
As a LoRaWAN device, the ERS Desk sensor can transmit its data using long-range, low-power wireless technology. LoRaWAN offers several different data rates; however, typically the device will communicate at a rate of SF12 (i.e., at the longest range but slowest speed). The configuration of these settings will fundamentally depend on the particularities of the installation site and the user's requirements.

### Power Consumption:
The ERS Desk sensor is a low-power IoT device. It utilises a 3.6V AA lithium battery, and the power consumption mainly depends on the configuration. Factors such as data reporting frequency and transmission data rate play a decisive role in the battery life. In normal conditions, the device can last up to 10 years under an update interval of 5 minutes.

### Use Cases:
The ERS Desk Sensor has several potential use cases, including:
- Office space optimization: By recording data on when and how office desks are utilised, the sensor allows for a more efficient allocation of resources.
- Environmental monitoring: The sensor's ability to track temperature and humidity levels can be utilized to ensure comfortable and safe working conditions. 

### Limitations:
While the ERS Desk Sensor is powerful, it does have several limitations:
- First, the device must have a clear 'line-of-sight' to the area being monitored - any obstacle could interfere with its detecting ability.
- Second, while the sensor provides valuable data, it requires a comprehensive IoT infrastructure to function effectively, including a LoRaWAN presence and compatible data analysis software. 

By understanding its strengths and limitations, the ELSYS - ERS Desk sensor can be a critical tool in the optimization of office spaces, helping businesses utilise their resources more efficiently and create more comfortable working environments.