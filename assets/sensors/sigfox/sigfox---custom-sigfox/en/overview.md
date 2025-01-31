Title: Overview and Technical Documentation on Custom Sigfox (SIGFOX)

## Introduction

Custom Sigfox—referred to as Sigfox—is a proprietary global communications service based on a low-power, wide-area network (LPWAN) architecture. It provides Internet of Things (IoT) devices with an efficient, power-minimising way of transmitting small amounts of data over long distances. Sigfox operates globally, but leverages spectrum band ubiquity under unlicensed Industrial, Scientific, and Medical (ISM) bands for the majority of its communications (e.g., 868MHZ in Europe and 902MHZ in US).

## Working Principles

Sigfox utilizes Ultra-Narrow Band (UNB) radio technology to communicate between devices and base stations. UNB is characterized by its very narrow band spread spectrum method. This narrow approach consumes less power and can travel further distances than conventional modulating techniques. The network operates on a star-based topology where all the end devices connect directly to many gateways. Each message undergoes multiple redundant transmissions which eliminates data loss due to obstacles.

## Installation Guide

A SIGFOX-ready device uses the SIGFOX network to communicate with the application server hosting the IoT service. 

1. If you don’t already have a SIGFOX account, you need to create it from the SIGFOX Backend portal.
2. To activate your device, follow the “activate” tab and the site will guide you to register a new device on the network.
3. After activating the device, it should be positioned in a location with a clear and sufficient Sigfox network coverage.
4. Finally, you’ll need to pair your device with the cloud backend. Connect to the Sigfox portal and input the device ID along with the associated PAC number.

## LoRaWAN vs. Sigfox

LoRaWAN is another leading LPWAN technology but unlike Sigfox, it is based on open standard protocol and focuses on device, network, and application server keys to build an end-to-end security scheme. In comparison, Sigfox offers a simple network architecture requiring minimal infrastructure, but it does not provide bidirectional communication like LoRaWAN does.

## Power Consumption

Sigfox devices are designed to be low power. They offer a sleep mode which can prolong the battery life up to several years, ideal for devices that require infrequent updates. Additionally, power usage is minimized due to the short and periodic transmission technique used by Sigfox, known as "keep-alive".

## Use Cases

Sigfox is suitable for applications that require infrequent data transmission over large distances. These could include, but are not limited to: environmental sensing, utility meter reading, agricultural automation, wearable healthcare monitors, smart parking sensors and asset tracking.

## Limitations

While Sigfox provides several advantages, it has some constraints. Its data rate is low with a maximum of 100 bytes/message, limiting its use case to smaller data payloads. Sigfox limits the number of uplink (device to cloud) messages to 140 messages per day and only four downlink (cloud to device) messages per day. This could be a limitation for applications requiring constant or high-frequency data communication.

Nonetheless, Sigfox's low cost, simplicity, and minimal energy consumption make it a viable choice for many IoT applications that do not require high data rates, real-time communication, or high frequency of messages.