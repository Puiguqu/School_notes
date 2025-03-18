# Network security Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/7Cpck/network-security)

Here is a summary of the text in 15 sentences, preserving key information and technical details:

Networks are vulnerable to numerous security issues, one of which is the potential for packets to be intercepted by malicious computers. To address this issue, network administrators use protocols like HTTPS (Hypertext Transfer Protocol Secure), an encrypted version of HTTP that uses encryption algorithms to protect application-layer packets. When using HTTPS, packet encapsulation occurs, where the encrypted packet is wrapped in transport layer and link layer packets for transmission over the network.

When a router receives the packet, it can extract and use the unencrypted network packets but cannot access the encrypted HTTPS packet. The packet only becomes accessible when it reaches its final destination, where the browser has the correct decryption key to read the contents of the packet.

Network security also involves defending against external attacks that aim to disable or compromise a network without gaining direct access to individual machines. One common attack is a Distributed Denial of Service (DDoS) attack, which involves sending a large volume of network packets to a specific machine or multiple machines on the network, overwhelming them and causing them to become unavailable.

DDoS attacks are often performed using botnets, networks of infected computers that perform the attack without direct human intervention. Since DDoS attacks use valid network traffic, they can be difficult to detect and defend against. Firewalls are commonly used as a defense mechanism, filtering out specific types of packets or blocking IP addresses known to be malicious.

Firewalls can also accidentally block legitimate traffic, causing issues for users. To mitigate this, proxy servers can be implemented, acting as intermediaries between clients and servers or within networks to filter traffic before it reaches its destination. When configured correctly, proxy servers and firewalls provide strong defenses against a wide range of security threats.

However, new security threats are constantly emerging, requiring network administrators to remain vigilant and update their defenses regularly. This is an essential aspect of maintaining network security in the field of computer science. Malware can compromise networks in various ways, including through phishing attacks or exploiting vulnerabilities in software applications.

