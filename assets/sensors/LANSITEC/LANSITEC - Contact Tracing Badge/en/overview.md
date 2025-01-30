# Technical Overview: LANSITEC Contact Tracing Badge

## Introduction

The LANSITEC Contact Tracing Badge is an innovative IoT device designed for efficiently monitoring human interactions within defined environments. It utilizes LoRaWAN technology to transmit long-range data with low power consumption, catering to various sectors like healthcare, corporate offices, and events for contact tracing during pandemics or for monitoring interactions in workspaces.

## Working Principles

The LANSITEC Contact Tracing Badge operates by continuously scanning the surrounding environment to detect nearby badges. When another badge is within its proximity, the mutual encounter data is logged with details such as time and duration. These interactions are then transmitted via LoRaWAN to a centralized server where data aggregation and analysis occur. Using unique identifiers helps protect user privacy while facilitating effective contact tracing.

## Installation Guide

1. **Unpacking and Inspection:**
   - Ensure the package contains the badge(s), charging cable, and user manual.
   - Check the device for any physical damage before use.

2. **Initial Setup:**
   - Charge the device fully using the provided charging cable.
   - Power on the badge; the LED indicator should illuminate to confirm activation.

3. **Network Configuration:**
   - Install the LANSITEC configuration software on a computer with LoRa connectivity.
   - Use the configuration software or a mobile app to add each badge to your LoRaWAN network by inputting the device's unique identification numbers (DevEUI, AppEUI, AppKey).

4. **Deployment:**
   - Distribute the badges to users ensuring they wear them on their lanyards or clipped securely for optimal performance.
   - Ensure the LoRa gateway is appropriately positioned to cover the operational area, optimizing radio conditions to ensure seamless data transmission.

## LoRaWAN Details

- **Frequency Bands:** Operates typically in ISM radio bands which vary by region (e.g., 868 MHz in Europe, 915 MHz in North America).
- **Data Rates:** Supports adaptive data rates to optimize network efficiency and power consumption, ranging from 0.3 kbps to 50 kbps.
- **Range:** Capable of a communication range of up to 10 kilometers in open areas; multi-kilometer range in urban environments.
- **Security:** Utilizes AES-128 encryption at the network and application layers to ensure data confidentiality and integrity.

## Power Consumption

The LANSITEC Contact Tracing Badge is designed for ultra-low power operation, powered by a rechargeable lithium battery. Under typical operating conditions, the badge can last several days on a single charge, depending on the frequency of interactions and data transmissions. The device also accommodates various power-saving modes, activating transmission and scanning only when necessary to extend battery life.

## Use Cases

- **Healthcare Facilities:** To monitor and trace interactions among healthcare workers and patients, reducing the risk of infection spread.
- **Corporate Offices:** For managing workforce interaction tracking in large corporate spaces, optimizing workspace utilization and safety.
- **Events and Conferences:** Enabling effective attendee tracking to facilitate better contact tracing and security management.

## Limitations

- **Limited Indoor Precision:** While effective in general proximity detection, indoor environments with heavy metal obstacles may affect performance.
- **Dependent on Network Infrastructure:** Requires a properly configured LoRaWAN network with gateways positioned strategically for optimal coverage.
- **Privacy Considerations:** While using unique IDs to protect user identities, implementing robust data protection policies and user consent is critical for compliance with privacy regulations.

Overall, the LANSITEC Contact Tracing Badge provides a reliable and efficient solution for monitoring interactions in various environments, leveraging low-power LoRaWAN technology for extended operation and broad coverage. With proper network setup and data management practices, it becomes a valuable tool for safeguarding health and optimizing operational workflows.