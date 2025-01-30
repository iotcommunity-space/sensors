# Technical Overview of Ft Series - Ft101

## Introduction

The Ft Series - Ft101 is an advanced IoT sensor designed for environmental monitoring using LoRaWAN connectivity. It is engineered for a variety of applications such as agriculture, smart cities, industrial automation, and environmental research. The Ft101 sensor allows users to gather critical data remotely with minimal maintenance and energy consumption.

## Working Principles

The Ft101 leverages a variety of sensor technologies incorporated into a single device to monitor environmental parameters like temperature, humidity, air pressure, and VOCs (Volatile Organic Compounds). The sensor data is collected and then transmitted over the LoRaWAN network. The sensor operates using advanced algorithms to ensure accuracy and minimize data loss.

### Key Components:

- **Temperature and Humidity Sensor:** Utilizes digital capacitive sensing element for precise readings.
- **Pressure Sensor:** Incorporates MEMS technology to detect pressure variations.
- **VOC Sensor:** Uses metal-oxide semiconductor technology to assess air quality.

### Communication:

- **LoRaWAN Protocol:** The Ft101 uses LoRaWAN for communication, providing wide-area connectivity with low power consumption. It supports Class A and Class C device profiles, ensuring versatility in data transmission intervals and energy usage.

## Installation Guide

### Pre-Installation Checklist:

1. **Site Survey:** Ensure the installation site provides optimal environmental conditions and LoRaWAN coverage.
2. **Power Supply:** Verify availability for either the integrated battery or a power source for those using external power options.

### Steps:

1. **Mounting:**
   - Secure the Ft101 using mounting brackets provided. Installation height and location depend on the monitored parameter and intended application.

2. **Powering:**
   - Insert the batteries if opting for the integrated power source. If using external power supply, connect using the provided cables and sockets.

3. **Configuration:**
   - Connect the Ft101 to a configuration tool via Bluetooth or USB.
   - Use the companion software to set up LoRaWAN parameters such as Device EUI, Application EUI, and App Key.
   - Test the sensor using the mobile or desktop application before full deployment.

4. **Network Integration:**
   - Ensure that your LoRaWAN Network Server (LNS) is configured to accept data from the sensor.

5. **Validation:**
   - Verify data reception from the Ft101 on a user platform or application to ensure installation success.

## LoRaWAN Details

- **Frequency Bands:** Supports all standard ISM frequency bands required per country such as EU863-870, US902-928, and AS923.
- **Spreading Factors:** Capable of operating in SF7 to SF12 for optimizing trade-offs between range and data rate.
- **Join Methods:** Supports both OTAA (Over-The-Air Activation) and ABP (Activation By Personalization).

## Power Consumption

- **Sleep Mode:** <10 µA
- **Active Mode:** ~100 mA
- **Transmission Mode:** ~28 mA at SF7
  
The power-efficient design allows the Ft101 to deliver long-term operation on a single battery charge under typical conditions. Standard battery life expectancy can be several years depending on the data transmission intervals configured.

## Use Cases

- **Agriculture:** Monitor soil moisture levels and environmental conditions affecting crop growth.
- **Smart Cities:** Provide real-time data for urban climate monitoring.
- **Industrial Automation:** Track environmental conditions in factories to protect sensitive equipment.
- **Environmental Research:** Gather distributed environmental data for scientific studies and assessments.

## Limitations

- **Range:** Effective range is subject to LoRaWAN network coverage and environment factors, such as obstructions and terrain.
- **Data Rate:** Limited by the LoRaWAN standard, which may not be suitable for high-frequency data transmission in certain applications.
- **Environmental Conditions:** The sensor has specific operating temperature and humidity ranges, which must be observed for accurate readings and functionality.

In conclusion, the Ft Series - Ft101 sensor is a robust and versatile solution for IoT applications requiring remote environmental monitoring with a balance of power efficiency and reliable data transmission.