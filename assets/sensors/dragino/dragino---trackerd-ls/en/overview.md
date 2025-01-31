# DRAGINO - Tracker Ls Sensor Technical Overview

## Working Principles

The DRAGINO Tracker LS, a LoRaWAN GPS tracking system, is based on the Lora protocol and Global Navigation Satellite System (GNSS). It incorporates a built-in GPS receiver, ensuring an optimal balance between power consumption and GPS positioning accuracy. 

The Tracker LS communicates over the LoRaWAN protocol, which allows it to transmit data over long distances with minimal power usage. This is achieved using LoRa modulation within the sub-GHz bands with low data rate transmissions, rendering the signal's transmission over much longer distances possible.

The device's working principle is straightforward: the built-in GNSS module traces the current location, and the data is then transmitted to the LoRaWAN network server over the LoRaWAN protocol in either confirmed or unconfirmed mode.

## Installation Guide

The Tracker LS comes with a pre-installed battery and LoRa antennae. What you need to do is register the device on a network server using either Over-the-Air (OTAs) activation by setting the App Key and the Device EUI, or ABP activation, where you set the Device Address, Network Session Key and APP Session Key. The mounting of the device is easily done using the accompanying mount brackets.

## LoRaWAN Details

LoRaWAN (Long Range Wide Area Network) is a protocol designed for wireless battery-operated devices in a regional, national or global network. The Tracker LS utilizes this protocol for communication, supporting Class A and Class C devices. It operates in various frequencies including AS923, AU915, EU868, and US915 to ensure global coverage.

## Power Consumption

Power efficiency is of utmost priority in many IoT applications and DRAGINO Tracker LS is no exception. Its power consumption is optimized during the operation of the GNSS system and radio transmissions. Its power specifications are: 3.7V, 10,000mAh battery with a nominal current of 130uA. The device supports operation from a power range of 4.2V - 3.4V, enabling long-term, unsupervised operations.

## Use Cases

A robust, long-range sensor like the Tracker LS can be employed in numerous IoT applications. These include, but are not limited to, asset tracking, wildlife tracking, logistics and supply chain management, Smart City operations, agricultural monitoring, and many more applications where remote tracking is required.

## Limitations

While the Dragino Tracker LS is an impeccable piece of technology, it is not without its limitations.

1. Network reliance: The Tracker LS relies on a LoRaWAN network to transmit data, which may not be available in all regions.

2. Signal obstacles: Signal may be affected by physical obstructions and urban signal noise impacting the quality of transmissions.

3. Battery Limitations: The Tracker LS needs its battery replaced after it's depleted. Repeated conditions of high power consumption will require more frequent battery changes.

4. Weather Limitations: Though typically configured to withstand harsh environments, severe weather conditions could potentially impact its functioning.
   
Understanding these limitations can better inform prospective users and manage their expectations effectively. It is crucial to consider these factors when deciding if the DRAGINO Tracker LS is the right solution for a specific application.