## Technical Overview of Am Series - Am104 Sensor

The Am Series - Am104 is a multi-sensor device designed to capture and transmit environmental data using LoRaWAN technology. It is an advanced sensor solution ideal for various applications, offering reliable and long-range wireless connectivity, low power consumption, and seamless integration capabilities.

### Working Principles

The Am104 sensor utilizes a combination of sensors to monitor environmental conditions such as temperature, humidity, ambient light, and motion. These sensors employ the following working principles:

- **Temperature Sensor**: Typically uses a thermistor or a digital thermometer to accurately measure ambient temperature levels.
- **Humidity Sensor**: Often based on a capacitive measurement principle, where changes in capacitance correlate to changes in humidity.
- **Ambient Light Sensor**: Utilizes photodiodes to measure the intensity of visible light in the environment.
- **Motion Sensor**: Generally adopts Passive Infrared (PIR) technology to detect motion by sensing changes in infrared radiation.

These sensor readings are collected, processed, and then transmitted via the LoRaWAN protocol to a designated network server.

### Installation Guide

1. **Location Selection**:
   - Choose an appropriate installation site that is representative of the area you wish to monitor.
   - Ensure that no obstructions block the sensor’s access to the environment.

2. **Mounting the Sensor**:
   - Attach the sensor to a stable surface using screws, adhesive, or mounting brackets provided. 
   - Ensure the sensor has a clear field of view for effective motion detection.

3. **Powering the Device**:
   - Install the batteries according to the polarity markings. The device is typically powered by AA batteries or a built-in rechargeable battery, depending on the model variant.

4. **Configuration**:
   - Use the configuration application to set up the sensor parameters, such as reporting intervals and thresholds.
   - Connect the sensor to the LoRaWAN network by configuring the device keys and other network credentials.

5. **Testing**:
   - Verify the sensor data transmission by checking the data on the network server for accuracy and completeness.

### LoRaWAN Details

The Am104 supports LoRaWAN, a Low Power Wide Area Network (LPWAN) protocol, which offers:

- **Frequency Bands**: Typically operates in the ISM bands, such as 868 MHz (EU) or 915 MHz (US), facilitating widespread geographical compatibility.
- **Adaptive Data Rate (ADR)**: Adjusts the data rate for optimal performance and battery life by adapting to the network's coverage conditions.
- **End Node Class**: Classified as a Class A device, which opens and closes communication windows to minimize power consumption.
- **Security**: Utilizes AES-128 encryption to ensure secure data transmission.

### Power Consumption

The Am104 sensor is designed to be energy efficient, consuming minimal power due to its low-duty cycle and configurable reporting intervals. This efficiency enables extended battery life, potentially lasting several years based on usage conditions and reporting frequency.

### Use Cases

- **Smart Buildings**: Monitor environmental conditions in offices or residential spaces for HVAC optimization and energy savings.
- **Agricultural Applications**: Track greenhouse conditions to optimize crop production and reduce waste.
- **Warehousing**: Assess ambient conditions to ensure proper storage conditions for sensitive goods.
- **Occupancy Monitoring**: Detect presence or motion in security applications or smart lighting systems.

### Limitations

- **Detection Range**: PIR motion detection is limited to line-of-sight and certain distances, reducing efficacy in complex layouts.
- **Data Transmission Interference**: LoRaWAN communication may be affected by obstructions, signal attenuation, or network congestion.
- **Response Time**: Some sensors may have a slight delay in response to environmental changes, based on configuration settings.
- **Battery Dependency**: Replacement or recharging is necessary, as sensor operation is dependent on battery life, which may vary based on data transmission frequency.

In summary, the Am104 is a versatile sensor device leveraging the power of LoRaWAN to provide comprehensive environmental monitoring with low power consumption, suitable for a wide array of applications but with specific limitations to consider during deployment.