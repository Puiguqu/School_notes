# Week 15 - CM1030 How Computers Work - How a computer works - Week 1

## Introduction to the web Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/yKoDc/introduction-to-the-web)

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

## Internet application protocols Video• . Duration: 6 minutes 6 min

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

---

## Web servers Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/u24dk/web-servers)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The web and HTTP protocol are used to send information between clients and servers. Clients send requests to servers, which then send web pages back using HTML file formats. Early days of the web involved simple URLs that referred to actual files in a file system. However, most websites now use more complex methods to create web pages.

Web pages are often created on the fly by combining a template with data from a database. A template provides the basic layout and formatting, while detailed information is stored in a database. Databases are designed for storing numbers and small amounts of data, so large amounts like videos are typically stored as separate files called assets.

In a database-driven website, a script (e.g., PHP) creates an HTML file by fetching data from a database and combining it with an HTML template. The URL refers to the script and its arguments, which control how the script works. Modern websites use routing engines to interpret URLs and generate web pages, rather than relying on file systems.

The router uses the URL to determine which part of the server program to use, and combines data from a database and a templating engine to create the web page. The templating engine is often separate from the router. This approach allows for greater flexibility and scalability in modern websites.

---

## Client side interaction Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/2xVMr/client-side-interaction)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Modern websites are not just collections of information that we read passively; they require interaction. The oldest form of interaction on the web is links, which send requests to servers to generate new webpages. However, there aren't enough links for modern websites, especially for dynamic content like videos. Implementing interactions as links would be too slow and inefficient. Instead, client-side interaction is used, where all functionality is implemented in a user's web browser using the JavaScript language. This allows for faster and more responsive interactions.

One example of client-side interaction is templating, which sends templates directly to the client and data separately from the template. The client then combines the two to create the webpage, reducing the amount of data sent by the server. This approach makes the process more efficient and responsive. Another advantage is that the output doesn't have to be HTML, and the client can display it in a different way.

This understanding of client-side and server-side processing is crucial for web development. Client-side interaction allows for flexibility and scalability, making it suitable for mobile apps and other non-web applications as well. The distinction between client-side and server-side processing will be important to learn throughout one's computer science degree.

---

## Clusters and clouds Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/IxgrK/clusters-and-clouds)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A modern web server is often implemented as a cluster, consisting of multiple computers working together to serve a single website. Each computer in the cluster can have different functions, such as routing or database management, sharing tasks with other computers. Virtual servers are software-based servers that can run on a single computer, allowing multiple websites to be hosted on a single machine. There are two ways to implement virtual servers: virtual machines and containers.

Virtual machines implement the machine language of another computer in software, creating an independent computer with its own operating system and application software. Containers share the same operating system kernel as other containers but act like different computers with different application software. Virtual machines can be more efficient than containers if they use the same machine language.

Most websites are now hosted on Cloud services such as Amazon Web Services or Google Cloud, which use clusters and virtual servers to serve multiple websites. These cloud servers consist of huge clusters of computers, each website having one or more virtual servers implemented on a cluster. The web is an essential part of our lives, and its implementation efficiency is crucial.

Complex architectures for web servers are needed to support the high demand for online services. This lecture has only scratched the surface of how modern websites work, but future lessons will delve deeper into this topic. Key concepts include clusters, virtual servers, containers, and cloud computing.

---

## LAMP and MEAN Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/E4yIV/lamp-and-mean)

There is no text to summarize. The provided input appears to be a course structure or lesson outline for an online course, listing topics, video durations, reading times, practice assignments, and discussion prompts. 

However, if you provide the actual text related to the topic "The World Wide Web" ( Lesson 15.2 ), I can help summarize it in 6 sentences, preserving key information, formulae, technical details, and important concepts.

---

## Motivating problem Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/supplement/p3VSN/motivating-problem)

Motivating problem: How does Coursera work? How does the information get to you? What happens on your computer and what happens in Coursera's computers? Make notes on your thoughts in response to these questions. Lesson 15.0 Introduction Video: Video Introduction to the web . Duration: 1 minute 1 min Reading: Reading Motivating problem . Duration: 15 minutes 15 min Discussion Prompt: Your web page ....

---

## The internet Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/supplement/BtE6H/the-internet)

Brookshear, J.G. and D. Brylow Computer science: an overview . (Harlow: Pearson Education, 2019) 13th edition (Global Edition). Chapter 4 Networking and the internet Section 4.2. This reading is available in the Online Library via the VLeBooks collection. Lesson 15.0 Introduction Lesson 15.1 The internet Practice Assignment: How does email work? . Duration: 30 minutes 30 min Video: Video Internet application protocols . Duration: 6 minutes 6 min Reading: Reading The internet ....

---

## The world wide web Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/supplement/IpIhQ/the-world-wide-web)

I don't see any provided text for me to summarize. The text appears to be a description of an online learning resource, including a video, reading, practice assignment, and discussion prompt, related to computer science and networking. If you provide the actual text, I can help summarize it in 15 sentences, preserving key information, formulae, and technical details.

---

