# ELLENEX - Ptf2 L - Technical Overview

## Working Principles

The ELLENEX - Ptf2 L is a smart IoT-based sensor that functions on the principles of differential pressure measurement to determine the level of liquid or slurry in a vented container. The device uses MEMS-based pressure transducer technology to detect changes in pressure, which is converted into a corresponding level of liquid. The data gathered by the device is transmitted over a LoRaWAN connection, allowing for efficient and remote data collection.

## Installation Guide

Installation of the ELLENEX - Ptf2 L involves several distinct steps. The device should be mounted at the bottom or side of the container in such a manner that it measures the pressure of the liquid column directly above it.

1. Ensure the target container where the sensor will be installed is clean and safe for the installation process.
2. Mount the Ptf2 L sensor at the accurate position, considering the height from which you want to measure the liquid’s level.
3. Connect the sensor with the LoRaWAN gateway, ensuring the gateway is within the effective range of the sensor.
4. Configure the sensor parameters and connect it to the IoT platform for data monitoring and analysis.

## LoRaWAN Details

The ELLENEX - Ptf2 L uses a LoRaWAN (Long Range Wide Area Network) to allow for low-power, long-range communication between the sensor and the collection point. The sensor operates in the ISM band, which is licence-free and globally accepted. It supports various Data Rates (DR) from DR0 (SF12, 125kHz) to DR5 (SF7, 125kHz) which makes it suitable for different ranges and data size transmissions.

## Power Consumption

The ELLENEX - Ptf2 L sensor has been designed for low power consumption, an essential aspect for any IoT device. The sensor operates on a power range between 2.0 V and 3.6 V and features a power-saving mode for periods of inactivity. The average power consumption of the device is very low, contributing to a longer battery life up to 10 years (depending on the specific usage and data transmission intervals).

## Use Cases

The ELLENEX - Ptf2 L sensor is highly versatile, finding application in a host of diverse sectors. It can be used for monitoring the level of liquid in tanks in water management or industrial processes. Other uses include wastewater treatment monitoring, fuel level tracking in the logistics industry, and agricultural irrigation management.

## Limitations

While the ELLENEX - Ptf2 L sensor is highly flexible, it does have certain limitations. The device functions optimally up to a max pressure of 34.5 kPa and it is not applicable for liquids with extremely high viscosity. It requires a LoRaWAN gateway within range for data transmission, which can sometimes be a limitation in remote locations. Additionally, while the sensor is resistant to most chemicals, certain aggressive chemicals may damage it. Always refer to the chemical compatibility chart provided in the product's data sheet.
The response time and accuracy might also be affected based on the specific density and temperature of the liquid being measured.