# ADENUIS - Temperature (ADENUIS) Documentation

## Technical Overview

ADENUIS - Temperature (ADENUIS) is a highly efficient, low-cost sensor designed to track and monitor temperature in various settings. These devices use thermistors to accurately measure the ambient temperature displaying accurate results irrespective of humidity and air pressure fluctuation. They are ideally suited for applications such as climate control, enological applications, and intelligent agriculture.

---

## Working Principles

ADENUIS works on the principle of temperature-dependent resistance. Its core component is a thermistor whose resistance changes with temperature. The microcontroller in the sensor measures this resistance and, via the device's in-built algorithm, converts this resistance into a temperature reading. This temperature reading is then transmitted using lower power wide area networking technology (LoRaWAN).

---

## Installation Guide

Installation of the ADENUIS temperature sensor is straightforward:

1. Connect the device to the power source and turn it on.
2. Use the configuration interface to set up the LoRaWAN network details and calibrate the temperature sensor.
3. Test the device to ensure it is correctly measuring and transmitting temperature data.
4. Mount the device in your desired location using the provided mounting hardware, ensuring that the device will be in a position to accurately measure the temperature.

---

## LoRaWAN Details

The ADENUIS temperature sensor utilises LoRaWAN technology for data transmission. LoRaWAN (Low Range Wide Area Network) is a communication protocol that uses low power WAN technology for machine-to-machine interactions and IoT applications. It can cover vast geographical areas with low power consumption, ensuring the sensor can operate under different environmental conditions with minimal power usage.

---

## Power Consumption

The ADENUIS Temperature sensor is optimized for low power consumption. It operates using a 3.6V AA lithium battery and has a power consumption of just 10mA in active mode and less than 200uA in sleep mode. Depending on the frequency of measurements and data transmission intervals, this allows for autonomous operation for several years on just one battery.

---

## Use Cases

The ADENUIS temperature sensor can be used for a variety of applications, including:

1. Real-time temperature monitoring in industrial settings.
2. Climate control in homes and offices.
3. Monitoring temperature in agriculture and horticulture.
4. Predicting and monitoring weather patterns for meteorological research.
5. Ensuring proper temperature control for storage facilities (like cold storage, food preservation, etc.)

---

## Limitations

While the ADENUIS temperature sensor is highly efficient and accurate, it does have a few limitations:

1. The sensor requires placement in a location where accurate temperature can be measured. If installed near heat sources or in direct sunlight, it may provide inaccurate readings.
2. It operates in the temperature range from -40°C to +85°C. Above or below this range, the sensor will not provide accurate readings.
3. The sensor's accuracy may decrease over time, and it will require regular calibration to ensure accurate readings.
4. While LoRaWAN technology enables transmission over large areas, physical obstacles or electromagnetic interference can disrupt the signal.
5. The lifespan and performance of the device are dependent on battery life and can be negatively impacted by extremely cold or hot environments or by frequent transmission intervals.

---

This document provides a basic understanding of the ADENUIS temperature sensor, its use cases, and limitations. For more detailed or technical queries, please refer to the manufacturer's detailed guidelines or contact the technical support teams for assistance.