## Technical Overview for HTTPS - Custom Https (HTTPS)

### Working Principles
Custom HTTPS (Hypertext Transfer Protocol Secure), a communications protocol, ensures secure communication over network systems secured via TLS/SSL encryption. It uses port 443 by default, allowing secure transactions by encrypting the entire communication with SSL. Authentication, data integrity, and confidentiality are ensured with this protocol.

Unlike HTTP, it uses a Public Key Infrastructure (PKI) with X.509 digital certificates to authenticate the server. This ensures that data exchanged between servers and IoT devices that use HTTPS is encrypted and thus secure from interception or alteration.

### Installation Guide
1. **Buy a Certificate from a Certified Authority:** Start by purchasing an SSL certificate from a reliable and certified source, ensuring it comes with an RSA of 2048-bit key.
 
2. **Install the Certificate on the Server:**  This process varies depending on the server. You need access to your server's certificate storage or use an automated tool such as Let's Encrypt for automatic installation. 

3. **Configure your Server to Use the Certificate:**  Configure your web server to use the installed SSL certificate. This step relies on your server type and version's specific guidelines. 

4. **Redirect HTTP to HTTPS:** Configure the server to direct all HTTP requests to HTTPS to ensure that all connections are securely encrypted.

### LoRaWAN Details
Custom HTTPS doesn't preclude integration with LoRaWAN (Long Range Wide Area Network), a media access control (MAC) protocol for wide area networks. You can ensure secure network servers and application servers communication with LoRaWAN devices using HTTPS by encrypting the payload and metadata. However, it is important to note that LoRaWAN servers have their own distinct separate security protocols.

### Power Consumption
Network protocols, including HTTPS, have a varying effect on power consumption. HTTPS requires more computing power than HTTP as encryption and decryption processes are involved. This can lead to greater power usage for devices that require constant communication with the server. However, in today's technological landscape, the increase is usually negligible, given the power efficiency improvements in modern IoT sensors and devices. 

### Use Cases
Custom HTTPS can be used in IoT environments where data integrity and privacy are critical, such as healthcare, banking and finance, smart homes, industrial IoT, and several other domains that handle sensitive user data.

### Limitations
1. **Performance:** HTTPS involves complex procedures like encryption and decryption, which consume a significant amount of system resources, potentially affecting performance. 

2. **Cost:** Getting an SSL certificate from a trusted certificate authority usually comes with a cost, which might be a limitation for small-scale implementations.

3. **Invalid Certificates:** If an SSL certificate doesn't match the domain name or if it's expired, users will be notified and they might choose to leave instead of proceeding, directly impacting the application. 

4. **Compatibility:** Older versions of some IoT devices and operating systems might not fully support HTTPS, leading to compatibility issues. 

In conclusion, while HTTPS brings robust security measures, it's crucial to account for the potentially increased power consumption and performance overheads. Make sure to carefully evaluate these aspects before incorporating HTTPS into your IoT strategy.
