# DRAGINO - LSN50 (DRAGINO) Detailed Sensor Documentation 

## Overview

The DRAGINO LSN50 is a GPS tracking-based sensor featuring built-in telemetry capabilities. The main aim of this sensor is to facilitate the Internet of Things (IoT) applications to track and locate physical assets in real-time via Global Positioning System (GPS) and deviate sensor-based information via the Long Range Wide Area Network (LoRaWAN).

## Working Principles

### GPS Tracking

The LSN50 operates based on the mainstream GPS chip and LoRaWAN protocol, allowing you to track assets and gather space-related data from the GPS satellites. It then sends this data to a central LoRaWAN gateway, which is directed to a server for analysis and storage.

### Sensor-based Information

The LSN50 is equipped with multiple sensors to gather physical data, including temperature, relative humidity, tilt, and 3-axis accelerometer sensors.

## Installation Guide

To install the LSN50:

1. Have the LoRaWAN network server ready and configured.
2. Mount the sensor in the preferred location with a clear view of the sky for better GPS reception.
3. Register the device on the LoRaWAN network server by providing the Device EUI, Application EUI, and App Key, which are provided in the product manual or packaging.
4. Confirm the device is transmitting data to the server - this step can be verified via the server portal.

## LoRaWAN Details

The LSN50 uses the LoRaWAN Class A protocol, meaning that each end-device schedules communication sessions based on its communication needs with a small downlink window opening at scheduled intervals. This device operates in bands from 862 to 1020 MHz, allowing for a variety of regional implementations.

## Power Consumption

The LSN50 is powered by 8500mAh Li-SOCI2 batteries. It demonstrates ultra-low power consumption, with a battery life of more than 10 years (under optimal setup conditions). Factors such as data transmission frequency, sensor report frequency, and GPS working time can influence power consumption.

## Use Cases

Due to its robust tracking abilities and durable structure, the LSN50 is suitable for a myriad of IoT applications and environments. Example use cases include asset tracking, agricultural resource monitoring, transportation logistics, temperature and humidity monitoring, building and drop detection.

## Limitations

While the LSN50 is flexible for most tracking applications, it has some limitations:

1. GPS signal: The device must have a clear line of sight to the sky for optimal GPS working conditions.
2. Network coverage: The range and quality of data gathered significantly depend on the proximity and quality of the LoRaWAN gateway.
3. Battery life: The device's battery life is influenced by the frequency of data transmission and the load of the sensors, which, if high, will lead to rapid battery depletion.
4. Environment: The sensor modules are developed to operation within a given range of temperature and humidity. Exposing the device to conditions outside these ranges can affect the sensors accuracy.

Despite these limitations, DRAGINO LSN50's capabilities and flexibility make it one of the top choices for IoT-based asset tracking applications.
