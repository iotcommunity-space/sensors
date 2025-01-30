# Technical Overview: POLYSENSE Combustible Gas Sensor

## Introduction
The POLYSENSE Combustible Gas Sensor is designed for detecting and measuring concentrations of combustible gases such as methane, propane, and butane in various environments. It is a critical component in ensuring safety in industrial, commercial, and residential spaces by alerting users to potentially hazardous gas leaks.

## Working Principles
The POLYSENSE Combustible Gas Sensor leverages catalytic bead sensing technology. This technology involves a catalytic element (or bead) that is heated to oxidize combustible gases present in the atmosphere. The heat released during oxidation changes the resistance of the bead, which is then measured and translated into gas concentration. This method is reliable for detecting a variety of hydrocarbons and is widely used due to its accuracy and responsiveness.

### Key Components:
- **Catalytic Bead**: Reacts with combustible gases.
- **Heater**: Maintains optimal reaction temperature.
- **Resistive Circuit**: Measures resistance change correlating with gas concentration.

## Installation Guide
1. **Site Selection**: Install the sensor in locations where combustible gases are most likely to accumulate, such as near potential leak sources or in poorly ventilated areas.
2. **Mounting**: Use the provided mounting hardware to securely attach the sensor device to a stable surface, ensuring it's free from potential interference or obstructions.
3. **Power Connection**: Connect the sensor to a suitable power source. The power supply should conform to the specified voltage and current requirements to ensure reliable operation.
4. **Calibration**: Calibrate the device according to the manufacturer’s guidelines. Perform periodic recalibrations to maintain accuracy.
5. **Network Configuration**: Connect the sensor to the LoRaWAN network by entering the provided credentials into the network configuration interface.

## LoRaWAN Details
The POLYSENSE sensor integrates seamlessly with LoRaWAN technology for long-range, low-power communication.

- **Frequency Band**: Configurable for regional ISM bands, including US 915 MHz, EU 868 MHz, and others.
- **Communication Range**: Up to 15 km in rural environments and up to 5 km in urban settings.
- **Data Rate**: Supports adaptive data rates (ADR) to optimize sensor communication and battery life.
- **Encryption**: Ensures secure data transmission using AES-128 encryption.

## Power Consumption
The POLYSENSE Combustible Gas Sensor is designed for minimal power consumption to prolong battery life in remote installations.

- **Sleep Mode**: The sensor enters a low-power sleep mode when not actively sampling or transmitting, significantly reducing power usage.
- **Active Mode**: Requires higher power during active sampling and data transmission. Detailed power specifications can be found in the technical datasheet.

## Use Cases
- **Industrial Safety**: Continuous monitoring of gas concentrations in factories and processing plants to prevent explosions and fires.
- **Residential Compliance**: Enhancing safety in homes, particularly in kitchens and basements, where gas leaks can occur.
- **Environmental Monitoring**: Detection of combustible gases in waste management facilities and landfills to promote environmental safety.

## Limitations
- **Cross-Sensitivity**: May exhibit reduced accuracy in environments with high concentrations of non-target gases or pollutants.
- **Maintenance Requirement**: Periodic calibration and maintenance are necessary to ensure long-term accuracy.
- **Environmental Conditions**: Performance may be affected by extreme temperatures, humidity, or corrosive environments—protective housing may be required.

## Conclusion
The POLYSENSE Combustible Gas Sensor is a versatile and reliable tool for detecting and monitoring combustible gas concentrations. With its advanced sensing technology and integration with LoRaWAN, it provides robust safety measures across various applications. However, operators must consider its limitations and ensure regular maintenance and calibration to achieve optimal performance.