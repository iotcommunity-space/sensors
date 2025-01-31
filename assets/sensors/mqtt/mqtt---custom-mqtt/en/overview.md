Technical Overview for MQTT - Custom MQTT (MQTT)

1. Working Principles:
The Message Queuing Telemetry Transport (MQTT) protocol is a light-weight, open-source messaging protocol that allows devices to send messages to each other in an organized, swift and resourceful manner. The MQTT protocol works on top of TCP/IP and provides a means for devices to communicate over a network using a publish/subscribe model. This means devices (clients) can publish messages to a broker, and that broker can then distribute those messages to any clients that have subscribed to that topic.

2. Installation Guide:
To install MQTT, we first need to install a broker. Eclipse Mosquitto is a popular open source MQTT broker that's easy to set up and support MQTT protocol versions 3.1 and 3.1.1. After the broker is set up, MQTT clients can then be installed and configured to publish and/or subscribe to topics. 

3. LoRaWAN Details:
MQTT can be utilized in LoRaWAN (Low Range Wide Area Network) networks where it serves as the medium for forwarding messages from LoRa gateways to LoRa network servers and vice versa. LoRaWAN uses a unidirectional or bidirectional communication flow, allowing IoT devices to efficiently communicate over long ranges with minimal power consumption. However, direct MQTT connection to LoRaWAN devices might not be possible due to its high resource requirements, specifically the TCP stack, which is unavailable in most LoRaWAN devices.

4. Power Consumption:
MQTT is a light-weight protocol and was especially designed for resource-constrained devices and low bandwidth, high latency networks. It's a highly efficient protocol with minimal data overhead resulting in lower power consumption in comparison to other protocols.

5. Use Cases:
MQTT finds use in various applications like home automation (controlling lights, temperature), industrial control systems, location tracking, oil & gas industry, healthcare, energy monitoring, and control.

6. Limitations:
Though MQTT is advantageous for many IoT uses cases, it has limitations too. It's not ideal for real-time communication due to the latency of the broker and network. MQTT also requires a constant connection with the broker, which is impractical for some battery-operated devices. Currently, it supports minimal security measures, with username/password authentication and un-encrypted messaging often criticized for being easily hackable.