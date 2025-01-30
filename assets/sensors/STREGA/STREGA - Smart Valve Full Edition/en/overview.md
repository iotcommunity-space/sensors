# STREGA - Smart Valve Full Edition (STREGA)

## Technical Overview

The STREGA Smart Valve Full Edition is an innovative Internet of Things (IoT) device designed to offer precise and remote management of fluid control systems. Ideal for use in agricultural, industrial, and smart building applications, the STREGA Smart Valve leverages LoRaWAN connectivity to enable long-range communication for remote valve operation in water, gas, or other fluid distribution networks.

### Working Principles

The STREGA Smart Valve operates on electromechanical principles. It consists of a motorized actuator that, when triggered, rotates a valve either to open or close positions. Commands are sent via LoRaWAN, utilizing low-power wide-area network (LPWAN) technology to provide connectivity over long distances with low energy requirements. The core components enabling its functionality include:

- **Motorized Actuator:** Converts electrical signals into mechanical movement to control the valve position.
- **Controller Unit:** Interprets incoming signals and switches the motor on/off to open or close the valve.
- **LoRaWAN Module:** Provides long-range wireless communication capabilities.
- **Power Management System:** Ensures efficient power usage from the embedded battery supply.

### Installation Guide

Installation of the STREGA Smart Valve is straightforward, requiring only basic plumbing and technical skills. Here is a step-by-step guide:

1. **Site Assessment:** Ensure that the installation site has adequate LoRaWAN network coverage and determine the appropriate valve size for the required flow rate.
2. **Valve Integration:**
   - Disconnect the existing manual valve, if present.
   - Mount the STREGA Smart Valve onto the pipeline, ensuring that the flow direction matches the markings on the valve body.
   - Secure the connections using appropriate fittings or flanges to prevent leakage.
3. **Configuring LoRaWAN:**
   - Create a device profile on your preferred LoRaWAN Network Server (LNS).
   - Configure the device's unique identification (DevEUI, AppEUI, AppKey) and register it with the LNS.
4. **Power Up:**
   - Insert batteries into the valve's power compartment and ensure they are securely in place.
   - Power on the device using the designated button or automatic wake-up procedure.
5. **Testing:**
   - Send test commands to the valve via the LoRaWAN network to confirm successful operation and communication.

### LoRaWAN Details

The STREGA Smart Valve Full Edition utilizes LoRaWAN for its communication, characterized by:

- **Frequency Bands:** Compatible with various ISM bands (e.g., EU868, US915) depending on regional regulations.
- **Communication Range:** Up to 15 kilometers in rural areas and 5 kilometers in urban environments.
- **Data Rate:** Adjustable data rates ranging from 0.3 kbps to 50 kbps, optimizing for distance and power consumption.

### Power Consumption

The STREGA Smart Valve is engineered for energy efficiency. It operates primarily in a low-power state, conserving energy while idle, and requires minimal power when executing valve operations. Typical power consumption parameters include:

- **Sleep Mode:** ~15 μA
- **Active Mode (Valve Operation):** ~200 mA
- **Battery Life:** Dependent on usage patterns, generally exceeding two years on standard AA lithium batteries.

### Use Cases

- **Agriculture:** Automated irrigation ensuring optimal water usage with remote control and scheduling.
- **Smart Buildings:** Efficient water management systems integrated with building management solutions.
- **Industrial Automation:** Remote fluid control in processing plants, reducing the need for manual intervention.
- **Disaster Management:** Quick shut-off capabilities for preventing water damage during flooding.

### Limitations

Despite its advanced features, the STREGA Smart Valve Full Edition has some limitations that users should consider:

- **Network Dependency:** Requires adequate LoRaWAN network coverage for reliable operation.
- **Valve Size Constraint:** Limited to specific sizes that may not integrate with all existing infrastructure.
- **Battery Life Variation:** Battery life can vary significantly based on usage frequency and environmental conditions such as temperature.

In conclusion, the STREGA Smart Valve Full Edition combines robust engineering with IoT connectivity to enhance fluid control in various settings. While it offers substantial advantages in remote management and energy efficiency, users should consider network coverage and compatibility with existing systems during implementation.