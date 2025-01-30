### Technical Overview for DECENTLAB - DL-PM Sensor

#### Introduction
The DECENTLAB DL-PM sensor is a precise particulate matter (PM) monitoring solution designed for environmental sensing applications. This sensor is part of DECENTLAB's range of products tailored for connectivity with the LoRaWAN network, enabling real-time data transmission for air quality assessment.

#### Working Principles
The DL-PM sensor operates using optical scattering technology to measure particulate matter concentrations. The internal laser light source illuminates particles as they pass through the sensor's detection chamber. When these particles scatter light, the sensor's photodetector captures this scattered light, which is then analyzed to determine the size and concentration of PM10, PM2.5, and PM1.0 particles. The sensor is calibrated to provide accurate and reliable data over a wide range of environmental conditions.

#### Installation Guide
1. **Site Selection:** Choose a location where the air flow is representative of the area being monitored, avoiding direct exposure to wind, water, or obstructions.
   
2. **Mounting:** Secure the DL-PM sensor vertically using the provided mounting bracket. Ensure that the sensor is elevated to avoid interference from ground-based particles or moisture.

3. **Power Connection:** The sensor can be powered using a long-lasting internal battery or connected to an external power source. Ensure connections are secure and protected from environmental exposure.

4. **LoRaWAN Configuration:** 
   - Ensure that a LoRaWAN gateway is within range.
   - Access the sensor via its configuration interface to input the necessary LoRaWAN credentials, including DevEUI, AppEUI, and AppKey.
   - Confirm successful network join via status indicators.

5. **Calibration Check:** Although the sensor is factory-calibrated, perform a field calibration check if the installation environment significantly differs from standard conditions.

#### LoRaWAN Details
- **Frequency Band:** Depending on the region, the DL-PM can operate on relevant ISM frequency bands such as EU868, US915, or AS923.
- **Data Transmission:** Employs standard LoRaWAN Class A protocol for low-power, long-range communication.
- **Payload Format:** Sends data packets containing readings for PM1.0, PM2.5, and PM10 concentrations, along with temperature and humidity metrics if the sensor model supports these measurements.
- **Network Server Compatibility:** Compatible with major LoRaWAN network servers, allowing seamless integration into existing IoT platforms.

#### Power Consumption
The DL-PM sensor is designed for energy efficiency, drawing minimal power to maximize battery life. Typical power consumption:
- **Active Mode:** ~70 mW during measurement.
- **Sleep Mode:** <1 mW to preserve battery during inactive periods.
- **Battery Life:** Depending on the reporting interval, the sensor can operate on a single internal battery pack for up to several years.

#### Use Cases
- **Air Quality Monitoring:** Used in urban environments to provide data for public health tracking.
- **Industrial Applications:** Monitors PM levels within and around industrial sites to ensure compliance with air quality regulations.
- **Research Studies:** Utilized in environmental research projects to gather accurate and long-term data on particulate pollution.

#### Limitations
- **Environmental Factors:** Sensitivity to humidity and extreme temperatures can slightly affect measurement accuracy; additional protection or adjustments may be necessary in harsh environments.
- **Calibration Drift:** Over time, sensor calibration might drift, requiring periodic validation and recalibration to maintain data accuracy.
- **Network Coverage:** Reliant on LoRaWAN network availability; areas with limited gateway coverage could affect data transmission reliability.

The DECENTLAB DL-PM sensor offers a robust solution for those needing efficient and scalable particulate matter monitoring. With its advanced features and connectivity capabilities, it stands as a favored choice for air quality professionals and researchers alike.