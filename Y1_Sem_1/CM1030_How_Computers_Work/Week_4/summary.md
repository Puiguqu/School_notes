# Week 4 - CM1030 How Computers Work - How a computer works - Week 1

## Websites Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/W7qNq/websites)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The Internet refers to the underlying network that connects computers across the world, while the World Wide Web is a way of communicating and sharing information using the Internet. The web consists of pages connected by links, with each webpage being a single document loaded into a browser at a given time. A website is a collection of pages, such as those for Goldsmiths. Modern websites are interactive, utilizing data from multiple sources and constantly updating based on user interaction. They are examples of complex computer science concepts, including web applications. Web applications use various protocols to send emails and participate in video conferencing via applications like Skype. The web is the most popular use of the Internet, but there are other uses, such as email and video conferencing. A webpage is a single document loaded into a browser, while a website is a collection of pages. Websites can be categorized into different types, including webmail applications, social networks, and online courses. The next few videos will guide you through the process of applying your learning on websites. To summarize key concepts, the Internet and World Wide Web are distinct entities, with the internet providing the underlying network and the web being a way to communicate and share information. Modern websites require advanced computer science concepts, including data storage, security, and state management. The structure of a website includes clients (browsers) and servers, which work together to display and update content. Understanding these concepts is crucial for building and maintaining modern websites.

Key formulas or technical details are not mentioned in the text, but it does provide an overview of the fundamental concepts and relationships between different components of the World Wide Web.

---

## Networks and the web Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/mquGg/networks-and-the-web)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The web is a network technology that fundamentally relies on communication over networks. Websites are accessed through organizations' web servers, which hold information used by many people via different clients (computers or software). Communication between clients and servers occurs through packets sent using the Internet Protocol (IP) and Hypertext Transfer Protocol (HTTP). HTTP is a protocol that allows for the transfer of data over IP. To access a website, a client (such as a web browser) sends an HTTP request packet to a server, which includes a URL consisting of "HTTP", domain name, and query string. The query string allows websites to create pages tailored to individual requirements. When a server receives a query, it sends back a web page, which is typically too large for single packets, so it's split into multiple packets. Some elements like pictures are sent separately from text. Modern websites are networked applications that rely on transferring packets across the Internet between clients and servers. The client sends HTTP requests, and the server responds with web pages. The web uses IP to enable communication over the Internet and HTTP as a protocol to transfer data between servers and clients. A query string is used to specify requirements for website content. Web search engines use query strings to create results tailored to individual needs. The web's functionality relies on state, modularity, networks, security, and client-server communication.

---

## Security and the web Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/Ihqg9/security-and-the-web)

Here is a summary of the text in 15 sentences, preserving key information and technical details:

The web relies on sending messages across the internet, making security a major concern. These messages can be intercepted by malicious computers trying to hack websites and extract private data. Websites use encryption, such as HTTPS (Hypertext Transfer Protocol Secure), to secure data transmission. The "S" in HTTPS stands for secure, indicating that all transmitted data is encrypted. When using HTTPS, the URL shows "HTTPS" instead of "HTTP", and most browsers display a padlock symbol. However, not seeing this symbol on a website's URL can be worrisome. Websites also use access control, requiring login credentials to access sensitive information. Strong encryption ensures secure login names and passwords. Despite these measures, website software can still be hacked, highlighting the importance of installing latest software updates. A website's security should include features like two-factor authentication, password protection, and encrypted data transmission. Users should be aware when logging in or out, as well as whether data is being sent securely. Additionally, users should verify the security certificate and ensure it is valid. The web relies on secure connections between clients (web browsers) and servers (websites), with encryption ensuring that sensitive information is protected from interception. By taking these precautions, individuals can protect themselves and their data when using websites for security-sensitive activities.

---

## State and the web Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/Agy5S/state-and-the-web)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

1. Software, including websites, has state, which refers to changing configurations that affect how users interact with it.
2. The page being viewed is an obvious example of website state, as different pages have distinct states.
3. E-commerce sites also track more subtle states, such as remembering which items a user has viewed and displaying them on the page for easy access.
4. Logging in to a site changes the user's ability to interact with it, highlighting the importance of understanding state.
5. A common problem is when a website logs out a user without their knowledge, often due to inactivity.
6. Web servers, where websites are stored, typically have no state and respond uniformly to requests.
7. Despite this, user interactions can create subtle states that change within a single page.
8. One key way websites track state is through the use of cookies, small amounts of data stored on users' computers by their browser software.
9. Cookies allow websites to keep track of user login status and browsing history.
10. While some people worry about the privacy implications of cookies, they are essential for most websites to function properly.
11. A website's notional machine should consider how it is affected by state, such as changes in user interactions and page views.
12. Understanding state can help users work more effectively with websites on a daily basis.
13. The concept of state is also relevant to networks, where data is transmitted between clients and servers.
14. Web applications and APIs (Application Programming Interfaces) rely heavily on understanding state to function correctly.
15. Overall, recognizing the importance of state in website functionality can help users navigate online interactions more effectively.

---

## Clients and servers Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/wOtzb/clients-and-servers)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Websites are modular applications that rely on various components working together. The two primary modules are the client (your computer and web browser) and the server (the website's computer and software running on it). A basic web server consists of one or more web pages, each represented by one or more HTML files. When a request comes in, one page is sent to the client. Modern websites are more complex, with web pages created only when needed in response to specific requests.

Databases are software platforms designed to store data in a structured way that's easy to access for computers. They're efficient for getting data from a database but challenging to add new data. Social media sites store user information, such as name, age, and gender, in databases. The server uses templates with formatting for web pages (e.g., social media profiles) and combines them with data from the database.

The template page contains empty spaces that are filled with data from the database. Webpage formatting is done using HTML and CSS files. Almost everything on a website is a combination of pre-designed templates and dynamically generated content from databases. The interaction between web servers, databases, and browsers demonstrates the modular nature of websites. A server doesn't just store webpages; it creates them using templates and databases.

Understanding these interactions is crucial for becoming a web developer or effectively using websites. Databases make it possible to extend website information without creating new pages. This highlights the importance of modularity in software development, as seen in the complex interactions between web servers, databases, and browsers.

---

## Embedding and APIs Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/MAC32/embedding-and-apis)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

1. The concept of websites is often misunderstood as if they all originate from a single website, but this is not always true.
2. Websites can use embedded functionality and data from third-party sources, such as YouTube or advertising services.
3. Online payments are typically handled through embedding with specialized services like PayPal.
4. An Application Programming Interface (API) is a version of the website designed for computer programs, allowing other servers to access data and create new websites.
5. APIs enable different versions of the same application, available on both websites and mobile apps.
6. Major online applications are often accessed through multiple channels, including websites and mobile apps, with different API versions for each platform.
7. Developers use APIs to provide data to their applications, which can be used to create new experiences on different platforms.
8. Twitter's popularity is partly due to third-party developers creating mobile apps using its API, which were available before the company created its own app.
9. The complexity of a website has increased with the addition of embedded information and APIs, making it harder to determine the sources of data used.
10. Websites now incorporate information from multiple sources, including third-party services and APIs.
11. Understanding how websites combine data from different sources can help identify the origins of information used on a website.
12. Embedding allows websites to reuse functionality and data from other servers, reducing development time and costs.
13. APIs provide a standardized way for applications to access data and communicate with each other.
14. The use of APIs has enabled the creation of multiple versions of the same application, catering to different platforms and user needs.
15. Developers must consider API design and implementation when creating web applications that need to interact with multiple sources and platforms.

---

## Your data Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/IkTbn/your-data)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Websites collect data from various sources on the internet to provide services such as online shopping and social networking. This data collection raises concerns about privacy and security. To address these concerns, websites need to be transparent about how they use user data and implement measures to secure it. Online shopping sites, for example, track user behavior to personalize recommendations and deliver products to their doorstep.

Social networks also collect data without users' awareness, which can lead to targeted advertising. Advertising services can track user behavior across multiple sites, resulting in tailored ads on unrelated websites. This raises concerns about data protection and online privacy. However, the web wouldn't work without data collection, and many websites rely on advertising revenue to fund their operations.

To be more aware of data collection, users can use private mode in their browser or educate themselves about website functionality. Understanding how websites work is crucial for making informed decisions about data sharing. Embedding and APIs enable modern websites to collect data from multiple sources, often without users' knowledge. This highlights the need for transparency and security measures when it comes to user data.

The web relies on a complex network of clients and servers to deliver content and services. Websites use various techniques to embed content and track user behavior, such as cookies and tracking pixels. These technologies enable targeted advertising and personalized experiences but also raise concerns about user privacy. By understanding how websites work and taking steps to protect their data, users can regain control over their online presence.

In conclusion, the web is built on a foundation of data collection, which raises important questions about online privacy and security. As websites continue to evolve, it's essential for users to be aware of these issues and take proactive steps to protect their data.

---

## Summary Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/OeJ4A/summary)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The course provides an overview of computer science fundamentals, including abstraction and state, applications, and networks. Students have learned about how websites work, but also gained general knowledge that applies to all computer systems. The course will move on to more detailed topics, covering data, CPUs, operating systems, networks, and the internet. Additionally, students will engage with interactive simulations, world-class textbooks, and expert tutors who will provide feedback on assignments.

The course is designed to help students understand how computers work and how to use them in a more meaningful way. Students are encouraged to think about the abstractions and notional machines that underlie software and websites. They will learn about states, modules, and protocols used by websites.

The course includes interactive components, such as quizzes, discussions, and peer reviews, as well as free access to textbooks and simulations. The instructor is excited for students to continue their learning journey in computer science and hopes that what they've already learned will enrich their use of computers.

At the end of the course, students can expect to learn about cutting-edge topics like machine learning and data science. By the end of the course, students should have a deeper understanding of how computers work and be able to approach software and websites in a more informed way.

The course is designed to provide a comprehensive introduction to computer science, covering fundamental concepts that apply to all areas of the field. Students will learn about the principles behind websites and software, as well as how to think critically about technology.

Overall, the course aims to make using computers more interesting, satisfying, and fun for students.

---

