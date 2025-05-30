# TCP and UDP Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/BMqX6/tcp-and-udp)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The internet standard defines two main transport layer protocols: Transmission Control Protocol (TCP) and User Datagram Protocol (UDP). TCP is a reliable protocol that ensures messages get through, while UDP is an unreliable protocol suitable for real-time applications. In the context of mobile payments, TCP establishes a connection between the sender's phone and the recipient's bank to ensure message reliability. The connection is established by sending packets with the "syn" packet to confirm readiness. Once connected, devices can send data, with acknowledgments sent after each packet transmission. To handle large data sets, TCP assigns numbers to packets (e.g., packet 1, packet 2). Acknowledgments always include the packet number for sender verification.

However, if packets get lost or are delayed, TCP's reliance on acknowledgments slows down communication. In contrast, UDP sends packets without acknowledging them and does not resend lost packets. For example, in an online racing game, using TCP would delay gameplay due to frequent acknowledgement requests. Using UDP allows for faster communication, as lost packets can be adjusted during the game.

In summary, TCP prioritizes message reliability over speed, while UDP balances speed with minimal latency. The transport layer ensures that messages reach their destination without considering content, and the application layer handles specific applications' needs, such as ultra-reliable or real-time communication.

