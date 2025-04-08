# Internet application protocols Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/m1WzG/internet-application-protocols)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The link network and transport layers focus on packet delivery between two ends, while the application layer deals with data content and usage. Email is a client-server application that uses protocols such as Simple Mail Transfer Protocol (SMTP) for communication between servers. When sending an email, it first goes to the sender's email server, which then sends it to the recipient's email server, where it is downloaded by the recipient. The domain name of the email server is part of the email address, consisting of the identifier and name before the "@" symbol, and the domain name after. Email involves multiple protocols, including POP, IMAP, and Exchange, depending on the client used to fetch and store emails.

The World Wide Web is a classic client-server protocol that uses HTTP (or HTTPS) for communication between clients and servers. When a client requests a web page, it sends an HTTP request with a URL (Universal Resource Locator), which includes the IP address of the server. However, DNS (Domain Name System) protocols are used to convert domain names into IP addresses. The DNS protocol is essential for most Internet communication and involves a single request and reply.

Voice over IP (Internet telephony) is another application that uses peer-to-peer protocols, such as Skype, which sends voice data directly between clients without using a server. However, even in peer-to-peer voice over IP, a server is still needed to connect users. The DNS protocol plays a crucial role in identifying the IP address of a domain name.

The HTTP and World Wide Web are the most commonly used application layer protocols, with HTTPS being the secure version. Email, voice over IP, and web applications all rely on the DNS protocol to convert domain names into IP addresses before establishing communication with servers.

In conclusion, understanding the different layers of Internet communication is crucial for grasping how various applications work. The link network and transport layers focus on packet delivery, while the application layer deals with data content and usage. Email, voice over IP, and web applications all use specific protocols to communicate with servers, relying heavily on DNS protocols to identify IP addresses.

Key concepts:

* Link network and transport layers
* Application layer protocols (SMTP, HTTP, HTTPS)
* Client-server architecture of email
* Peer-to-peer protocols in voice over IP
* Domain Name System (DNS) protocol
* Universal Resource Locator (URL)

Key formulas and technical details:

* URL structure: <protocol>://<domain name>/<path>
* DNS protocol: requests and replies for domain name to IP address conversion
* HTTP request format: GET/<path>?<query parameters>

Note that some of the specific protocols mentioned in the text, such as SMTP, POP, IMAP, and Exchange, are not included in this summary due to space constraints.

