# AWS-IOT - Custom Aws Iot (AWS-IOT): Technical Overview

## Working Principles

AWS-IoT provides secure, bidirectional communication between internet-connected devices such as embedded micro-controllers, sensors, actuators and Amazon Web Services (AWS) Cloud. It supports HTTP, WebSocket, and MQTT, a lightweight protocol specifically designed to tolerate intermittent connections, minimize the code size on devices, and reduce network bandwidth requirements.

The service is equipped with Device Shadow technology for persistent representation of IoT device state which can be interacted with irrespective of whether the device is online or offline. It also presents a rules engine for continuous processing and routing of messages sent by connected devices based on expression-based rules that take actions aligned with changes in device data.

## Installation guide

To set up AWS IOT:

1. Access AWS Management Console and select IoT Core
2. Register a device in the AWS IoT Core registry
3. Create/associate security resources to a device
4. Enable device to receive, send and process MQTT messages

## LoRaWAN details

AWS IoT does not directly support LoRaWAN protocol. However, it can be integrated with a LoRaWAN network server, essentially becoming an ingress point for LoRaWAN device data. This will enable the utilization of AWS IoT’s powerful functionalities such as the ability to use AWS Lambda to analyze device data immediately after it is sent, or AWS IoT Analytics for further processing and analysis.

## Power Consumption

Being a cloud-based platform, AWS IoT does not consume power in a conventional manner as related to devices or sensors. However, the IoT devices connected to it demand energy, and the power consumption varies per device, their operational state, and their communication frequency.

## Use Cases

1. **Industrial Automation**: AWS-IoT is designed to handle enormous quantities of data from multiple devices, making it suitable for monitoring machinery and equipment in an industrial environment. 

2. **Smart Homes**: Domestic devices can be automated and controlled from anywhere via AWS-IoT.

3. **Agriculture**: Deploying AWS-IoT sensors on agricultural land can help monitor and control farming equipment and conditions.

4. **Telemetry**: It can be used extensively in collecting and analyzing data from remote or inaccessible areas.

## Limitations

1. AWS IoT does not directly support the LoRaWAN protocol.
2. The default setting in AWS IoT allows only 128 active MQTT connections, which could limit the deployment of multiple IoT devices.
3. While AWS IoT allows integration with other AWS services, integration with third-party services or tools may not always be straightforward. 
4. The use of AWS IoT requires a certain level of technical expertise and may not be easily accessible to individuals without a programming or cloud management background. 

Combining reliable, scalable IoT solution functionality with industrial-grade security, AWS IoT is ideal for businesses wanting to connect devices and create IoT applications, while conforming with data handling regulations.