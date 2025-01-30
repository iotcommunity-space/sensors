### Technical Overview - DECENTLAB DL-GMM

#### Introduction

The DECENTLAB DL-GMM is an advanced IoT sensor designed to measure the concentration of gases such as carbon dioxide (CO2) over a LoRaWAN network. It offers precise environmental monitoring for applications in agriculture, industrial environments, and smart cities.

#### Working Principles

The DL-GMM employs non-dispersive infrared (NDIR) technology to detect and measure gas concentrations. The sensor consists of an infrared source, a sample chamber, and an infrared detector. When the target gas is present in the sample chamber, it absorbs specific wavelengths of light from the infrared source. The detector measures the reduction in the intensity of these wavelengths, which is directly proportional to the gas concentration.

#### Installation Guide

1. **Location Selection**: Choose a location that reflects the area of interest for gas monitoring, avoiding obstruction or containment that might skew readings.

2. **Mounting**: Use the included brackets and hardware to securely mount the device at the appropriate height and orientation, following the environmental protection guidelines (IP65-rated protection).

3. **Power Connection**: Install the included batteries for power. Ensure correct polarity as indicated.

4. **Activation**: Press the activation button located within the battery compartment. This initiates the signal transmission setup.

5. **Network Configuration**: Configure the sensor for your LoRaWAN network using the accompanying DL-GMM configuration tool or via Over-the-Air Activation (OTAA).

6. **Calibration**: Perform sensor calibration in a controlled environment using zero and span calibration gases for accuracy.

#### LoRaWAN Details

- **Frequency Bands**: Supports multiple ISM bands (EU863-870, US902-928, etc.) depending on regional regulations.
- **Device Activation**: Both OTAA and ABP (Activation by Personalization) supported.
- **Data Rate**: Adaptive Data Rate (ADR) mechanism is employed to optimize data transmission frequency and power consumption.
- **Security**: AES-128 encryption ensures secure payload transmissions.

#### Power Consumption

- **Standby Mode**: Ultra-low power consumption, allowing for a prolonged sensor life of up to 10 years on a single battery set under standard reporting conditions.
- **Operating Mode**: Power usage increases during active measurement and data transmission cycles. Detailed consumption is subject to sensor frequency and data payload sizes.

#### Use Cases

- **Agriculture**: Monitor greenhouse gas levels for optimized plant growth.
- **Industrial**: Assess CO2 concentration in manufacturing facilities to ensure worker safety and environmental compliance.
- **Smart Cities**: Track urban air quality metrics for planning and environmental health analysis.
- **Enclosed Spaces**: Control and regulate ventilation systems based on real-time gas concentration data.

#### Limitations

- **Range Limitations**: Effective transmission is contingent upon achieving and maintaining line-of-sight or minimal obstructions between the sensor and LoRaWAN gateway.
- **Cross-Sensitivity**: Sensor accuracy can be affected by the presence of other gases unless specific measures or corrections are applied.
- **Temperature and Humidity Range**: Operates optimally within designated environmental conditions; extremes may impact sensor performance.
- **Network Dependency**: Requires a well-maintained LoRaWAN network for reliable data transmission.

The DECENTLAB DL-GMM is a robust solution for environmental monitoring applications, providing reliable data via a highly efficient communication protocol. Proper installation, calibration, and regular maintenance will ensure optimal performance and longevity of the device.