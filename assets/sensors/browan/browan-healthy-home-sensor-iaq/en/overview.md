## Technical Overview: BROWAN - Healthy Home Sensor IAQ

The BROWAN Healthy Home Sensor IAQ is designed to provide comprehensive indoor air quality monitoring to ensure a healthy living environment. It measures various environmental parameters such as temperature, humidity, carbon dioxide (CO2), volatile organic compounds (VOCs), and particulate matter (PM2.5). These sensors employ advanced sensing technologies to offer real-time data, facilitating informed decisions for improving indoor air quality.

### Working Principles

The BROWAN Healthy Home Sensor IAQ operates through a combination of different sensing technologies:

1. **Temperature and Humidity Sensor**: Uses a digital capacitive humidity sensor and a thermistor for accurate measurements.
2. **CO2 Sensor**: Employs non-dispersive infrared (NDIR) technology to measure carbon dioxide levels with excellent accuracy.
3. **VOCs Sensor**: Utilizes metal-oxide-semiconductor (MOS) technology to detect VOCs in the air, providing an overall IAQ index.
4. **PM2.5 Sensor**: Uses laser-scattering technology to detect PM2.5 particles, providing real-time particle concentrations.

These sensor data are processed internally and transmitted via LoRaWAN for remote monitoring.

### Installation Guide

1. **Location Selection**: Choose a place indoors that is well-ventilated but away from windows, doors, and direct sunlight to avoid external interference.
2. **Mounting**: The sensor can be mounted on a wall or placed on a flat surface. Ensure it is at a height of 1-2 meters for optimal air sampling.
3. **Powering**: Insert the batteries as per the polarity instructions or connect to an external power source if available.
4. **Configuration**: Use the dedicated app or tool for device configuration, including setting the appropriate LoRa network parameters.

### LoRaWAN Details

- **Frequency Band**: Compatible with multiple frequency bands based on regional requirements (e.g., EU868, US915).
- **Activation**: Supports both Over-the-Air Activation (OTAA) and Activation by Personalization (ABP).
- **Data Rate**: Adaptive data rate (ADR) capabilities optimize network performance and power consumption.
- **Network Integration**: Can be integrated into existing LoRaWAN networks for seamless data transmission to cloud platforms or local servers.

### Power Consumption

The BROWAN Healthy Home Sensor IAQ is designed for low power usage:

- **Battery Type**: Runs on standard AA lithium batteries, providing long battery life due to efficient power management.
- **Average Power Consumption**: Depends on reporting frequency and network conditions but generally optimized for extended use.
- **Sleep Mode**: When not actively transmitting, the sensor enters a low-power state to prolong battery life.

### Use Cases

- **Residential Monitoring**: Ideal for homeowners looking to maintain healthy indoor air quality and comfort.
- **Commercial Buildings**: Used in office spaces and commercial environments to ensure air quality compliance and employee well-being.
- **Schools and Universities**: Monitors classroom environments to promote healthy learning conditions.
- **Healthcare Facilities**: Ensures that hospital and clinic air quality meet stringent health standards.

### Limitations

- **Range**: While LoRaWAN provides a long-range capability, physical barriers and local interference can affect signal quality.
- **Battery Life**: Although optimized for long life, frequent data transmission can reduce battery longevity.
- **Calibration**: Sensors may require occasional calibration to maintain accuracy over long periods.
- **Environmental Extremes**: Not designed for use in extreme temperature or humidity conditions outside typical indoor ranges.

The BROWAN Healthy Home Sensor IAQ is an essential tool for maintaining healthy indoor air through efficient monitoring and reliable data transmission, suitable for a variety of applications while being mindful of its operational constraints.