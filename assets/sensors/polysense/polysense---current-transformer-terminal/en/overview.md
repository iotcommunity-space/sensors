## POLYSENSE - Current Transformer Terminal (POLYSENSE) Technical Overview

### Working Principles
The POLYSENSE Current Transformer Terminal (CTT) is engineered with electro-magnetic induction principles. In a typical setup, the primary current is transformed and presented as a secondary current in the circuit. This secondary current is then converted into a proportional voltage using resistors. Afterward, the analog-to-digital converter (ADC) translates the voltage into a digital signal for accurate current measurement. This transformation facilitates the current monitoring process in high power circuits, exposing data to analytics network where it can be leveraged for making insightful business decisions.

### Installation Guide
The POLYSENSE CTT is designed for a simple installation process. You need to clamp it around the wire whose current you wish to monitor. After clamping, connect the sensor to your device via the I2C interface provided, taking care to ensure the correct polarity is respected. For measurement accuracy, be sure to keep some clearance from adjacent wires, especially those carrying high current loads.

### LoRaWAN details
The POLYSENSE CTT is equipped with LoRaWAN technology, enabling long-range, low-power wireless communication. LoRaWAN's elegant star topology allows for seamless communication between devices. The sensor communicates with authorized LoRaWAN gateways when transmitting data. The data packet size may vary depending on the amount of upstream (sensor to network) or downstream (network to sensor) communication required.

### Power Consumption
Despite its sophisticated capability, the POLYSENSE CTT is highly power-efficient. The inductive sampling process does not load the primary circuit; therefore, the device has minimal power drain. Standard operation typically sees consumption well below 1W, making it an ideal choice for scenarios that demand long-term, uninterrupted deployment.

### Use Cases
The POLYSENSE CTT is a versatile device that can be employed in various scenarios.

1. Energy Management: It can provide real-time power consumption data leading to improved energy efficiency.
2. Machine Monitoring: Industries can ensure their high-power machinery operates within specified current limits.
3. Preventive Maintenance: By early detection of overcurrent conditions, damaging situations can be anticipated and mitigated.
4. Grid Monitoring: Helps power providers accurately forecast demand and securely manage their reserves.

### Limitations
While the POLYSENSE CTT is designed for optimal performance, certain constraints should be considered:

1. Magnetic Field Interference: The effectiveness can be hampered if the sensor is installed near devices that produce strong magnetic fields.
2. ADC Limit: There is an upper limit to the measurable current, which is constrained by the ADC's full scale.
3. Clamping Limit: The maximum diameter of a wire that can be clamped by the sensor is limited.
4. Wireless Signal Interference: The LoRaWAN technology may face interference from other wireless technologies, impacting information transmission.
5. Correct Polarity: The sensor should be connected with correct polarity, or it may function inaccurately or cause potential damage.
6. Environmental Factors: Harsh environmental factors such as extreme temperatures or humidity can affect the sensor's performance and lifespan.