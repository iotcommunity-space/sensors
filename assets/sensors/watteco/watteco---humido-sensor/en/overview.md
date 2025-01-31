# WATTECO - Humido Sensor Technical Overview

## Working Principles:

The WATTECO Humido Sensor is an IoT device designed to measure humidity levels in various environments. The sensor operates on the principle of capacitive sensing, whereby changes in humidity affect the capacitance of an electrical component embedded within the sensor. 

A built-in hygroscopic (water-attracting) dielectric material interacts with water vapor in the air, and the amount of water absorbed results in measurable changes in the component's capacitance proportionate to the air's humidity. The sensor converts these capacitance changes into an electrical signal, which is then processed and transmitted to the recipient LoRaWAN.

## Installation Guide:

1. Choose a suitable location for the Humido Sensor, ensuring it won't be directly exposed to condensation, rain, or direct sunlight.
2. Using the mounting bracket provided, secure the sensor on the wall or any flat surface.
3. Connect the sensor to your power source. If using a battery, insert it according to the polarity signs on the SENSOR.
4. Finally, integrate the sensor with your LoRaWAN network by adding the device to your network server, using the provided model, firmware version, and DevEUI.

## LoRaWAN Details:

The WATTECO Humido Sensor utilizes the LoRaWAN (Low Range Wireless Access Network) protocol for communicating with other IoT devices or central systems. It supports LoRaWAN class A and class C with adherence to the LoRaWAN 1.0.3 specification. This sensor is prepared for a wide range of ISM bands, permitting worldwide usage.

## Power Consumption:

While operational, the WATTECO Humido Sensor has an outstanding minimal power consumption rate, making it ideal for long-term installations. It's powered by a 3.6V Thionyl Chloride battery, and depending on the measurement frequency and network conditions, the battery life can typically last for several years.

## Use Cases:

1. **Building automation**: Maintaining optimal humidity levels in office buildings, manufacturing spaces, warehouses, residential homes, and greenhouses.
2. **Health and Safety**: Monitoring humidity in health care facilities or pharmaceutical manufacturing to meet specific health or production needs.
3. **Agriculture**: Monitoring soil humidity for better irrigation control and optimal crop growth.

## Limitations:

Though the WATTECO Humido Sensor provides a wealth of applications, certain limitations should be considered:

1. **Configuration Changes**: Any necessary in-field configuration changes must be performed using Downlink messages via the LoRaWAN network. Direct device interaction isn't feasible once mounted in operation.
2. **Battery Replacement**: The non-rechargeable battery does require replacement over time, which is especially important to consider during initial placement and mounting.
3. **Ranging Limitations**: Like all LoRaWAN devices, the Humido Sensor has a range limit depending on environmental circumstances and the LoRaWAN gateway's location.
4. **Environment**: It's only able to operate efficiently within its specific operating temperature and humidity range.