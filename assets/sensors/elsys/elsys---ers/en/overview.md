## Technical Overview: ELSYS - Ers (ELSYS) 

### Working Principles

ELSYS Ers is an IoT sensor designed to provide Indoor Environmental and Air Quality Monitoring. The device measures 6 crucial metrics - temperature, humidity, light, motion (PIR), CO2, and sound level.

The sensor integrates various small transducers to gather these essential data. The Pulse Width Modulation (PWM) principle governs these transducers. The IoT sensor sends a signal, and the corresponding variable modifies the signal's length (in microseconds). The device then measures and digitizes these pulse lengths to obtain the respective monitoring metrics.

### Installation Guide

1. Ensure you have a registered LoRaWAN gateway within range of the device.
   
2. To start installation, first, open the cover of the sensor by turning the top half counter-clockwise.
   
3. Install the 3.6V AA batteries that come with the device.
   
4. Close the cover and wait for the device LED to start blinking, indicating a successful initialization process.
   
5. The ELSYS Ers should be mounted on a wall using screws or double-sided tape at 1-1.5 meters from the ground for optimal sensing.
   
6. Use the ERS Dashboard to register the device and start monitoring your environment.

### LoRaWAN Details

The ELSYS Ers sensor leverages the LoRaWAN (Low Range Wide Area Network) protocol to provide long range, low power wireless IoT connectivity. LoRaWAN uses unlicensed radio spectrum in the Industrial, Scientific, and Medical (ISM) bands globally. For Europe, it operates at +14dBm max (25mW), while in the USA, it is +20dBm max (100mW). 

The device features compatibility with LoRaWAN version 1.0.2 and can dynamically adjust the data rate from SF7 to SF12 for optimal power usage and range.

### Power Consumption

ELSYS Ers uses 2xAA 3.6V Lithium batteries that are rated to last for many years depending on the data rate setting. The sensor activates only when it needs to take a measurement, then it goes back to sleep to conserve power. The device's low power consumption allows for battery life up to several years, ensuring long-term uninterrupted monitoring.

### Use Cases

ELSYS Ers finds applications in various fields to ensure optimal environmental conditions:

1. Office and commercial buildings: employers can monitor air quality, temperature, and light levels to maintain optimal conditions for productivity.
   
2. Smart Homes: to monitor and control the home environment like room temperature, humidity, light levels, etc.
   
3. Warehouses: to monitor and maintain optimal storage conditions.
   
4. Hospitals and Healthcare: to ensure the health standards are adhered to and that patients experience favorable conditions.
   
5. Public Buildings and Schools: to establish and maintain healthful school conditions for students and staff.

### Limitations

While ELSYS Ers is an advanced sensor, it has some limitations:

1. The device operates optimally within the temperature range of -20°C to +55°C. Extreme temperatures outside this range may affect its performance.

2. The device relies on LoRaWAN for connectivity, limiting its use in regions where LoRaWAN gateways are not available or have weak signals.

3. Finally, the ELSYS Ers sensor might not provide accurate readings if it is installed higher than the recommended height or has obstructions nearby.
   
Despite these limitations, ELSYS Ers sensor provides valuable data for optimizing indoor environments and air quality.