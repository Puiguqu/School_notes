# The internet Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/9mqJ2/the-internet)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The Internet is a network of networks that connects different networks and allows computers to communicate with each other across these networks. A router connects two networks, forwarding messages from one network to another and translating between network protocols. When sending a message over the Internet, it doesn't just go directly from the sender to the receiver; instead, it's forwarded by lots of routers across many networks before reaching its destination.

Most users connect to local networks in their homes, workplaces, or public spaces like libraries or internet cafes. These networks don't generally communicate directly with each other but are connected via Internet Service Providers (ISPs). ISPs can span whole countries and are often connected to international ISPs called the Internet Backbone.

To send a message over the Internet, a protocol is needed. The Internet Protocol (IP) is used by all computers and routers to communicate, even if they're on different networks or in different countries. This protocol works like an envelope, where the sender's IP address and other information are included to ensure delivery.

When sending an email, the message is put into a virtual envelope called a Packet that includes the recipient's IP address and other information. The packet is then sent to the router, which forwards it to the ISP's protocol packet. This process repeats until the message reaches its destination.

In reality, messages traveling over the Internet often use multiple protocols wrapped up in each other. For example, email uses the send-mail protocol, web pages use the HTTP protocol, and TCP ensures reliable transmission of data. Each of these protocols is wrapped in an IP packet that might be further wrapped in a WiFi packet when sent over WiFi.

Every computer on the Internet has an IP address, which allows routers to know how to reach any other computer on the Internet. However, IP addresses are not user-friendly for humans; instead, URLs (Uniform Resource Locators) make it easy for humans to remember and type in internet addresses. The domain name part of a URL is converted to an IP address using the Domain Name Service (DNS).

When sending emails or accessing websites, messages often travel through email servers or web servers before reaching their destinations. These servers handle large volumes of data and use specific protocols to ensure delivery. Overall, the Internet works because all computers and routers understand the same protocol, allowing them to communicate across different networks and countries.

