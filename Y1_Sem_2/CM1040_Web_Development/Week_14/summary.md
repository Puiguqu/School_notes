# Week 14 - CM1040 Web Development - Topic 1: HTTP and HTML – The internet and HTTP - Week 1

## Topic 7 Week 2 introduction Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/IVKUl/topic-7-week-2-introduction)

There is no text provided for me to summarize. The text appears to be a transcript of a video lecture on web development, specifically covering the topic of deploying websites onto servers using Unix command line hacking. 

If you provide the actual text, I would be happy to assist with summarizing it in 8 sentences, preserving key information, formulae, links, and technical details.

---

## Basic static website deployment Video• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/zLpIq/basic-static-website-deployment)

This appears to be a transcript of a video lecture on deploying a static website on a web server. The lecturer walks through the process of setting up a web server, installing necessary software, configuring domain names, testing the site, and deploying it.

Here's a summary of the key points covered in the lecture:

1. **Configuring a web server**: The lecturer shows how to set up a basic web server using a Unix-based system such as Ubuntu.
2. **Installing necessary software**: They install Apache, Nginx, or another web server software, and PHP.
3. **Configuring domain names**: The lecturer explains that you need to buy a domain name and then configure it to point to the IP address of your web server.
4. **Transferring files**: They show how to use Filezilla (SFTP) to transfer files from the local machine to the web server.
5. **Testing the site**: The lecturer demonstrates how to test the website using ping, curl, and viewing the access logs on the server side.
6. **HTTPS**: They discuss how to configure HTTPS using a service like Let's Encrypt to generate secure certificates for the website.

The lecture is divided into several sections:

1. **Introduction** (1 minute)
2. **Basic static website deployment** (30 minutes)
3. **Practice Assignment: Basic website deployment** (9 minutes)
4. **Lab: Configuring a web server** (1 hour)

Overall, the lecture provides a comprehensive introduction to deploying a static website on a web server, covering the basics of configuration, testing, and security.

---

## Non-static and scalable website deployment Video• . Duration: 24 minutes 24 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/orpHZ/non-static-and-scalable-website-deployment)

This transcript appears to be a video lecture on web deployment techniques, specifically on how to deploy dynamic websites in a scalable and secure manner.

The lecturer covers various topics such as:

1. Basic web deployment techniques
2. Non-static and scalable website deployment
3. Database considerations for dynamic websites
4. Reverse proxies and load balances for high traffic
5. Containerization for deploying applications
6. Continuous integration and continuous deployment (CI/CD) pipelines
7. Monitoring and security for large-scale systems

The lecturer uses a visual diagram to illustrate the concepts and explains each topic in detail, providing examples and best practices where applicable.

Some key takeaways from this video lecture include:

* The importance of using non-static content for dynamic websites
* How to set up reverse proxies and load balances for high traffic
* The benefits of containerization for deploying applications
* The role of continuous integration and deployment in maintaining a scalable system
* The need for monitoring and security measures when dealing with large-scale systems

Overall, this video lecture provides a comprehensive overview of the techniques and considerations involved in deploying dynamic websites in a scalable and secure manner.

---

## Topic 7 summary Video• . Duration: 45 seconds 45 sec

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/WUdN3/topic-7-summary)

There is no text to summarize. The provided content appears to be a video transcript and additional page content related to web development lifecycle, specifically covering lessons on deployment techniques for non-static and scalable websites.

However, I can provide a general summary of the topics covered:

Web development lifecycle encompasses various stages, including user requirement gathering, participatory design workshops, and late-stage deployments. The course covers techniques for deploying websites onto web servers, reverse proxies, Dockerizations, and other aspects of deployment. Two specific lessons are mentioned: Lesson 14.1, which covers basic web deployment techniques, and Lesson 14.2, which focuses on non-static and scalable website deployment. Additional resources include videos, practice assignments, reading activities, and a self-evaluation checklist.

Key concepts and findings from the text are not explicitly stated, as it appears to be a video transcript rather than a written article or technical document.

---

## Activity – Non-static and scalable website deployment practical Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/mZ8TF/activity-non-static-and-scalable-website-deployment-practical)

Here is a summary of the text in 8 sentences, preserving key information:

To get the Book Server running, extract the `bookserver.zip` file and run `node server.js` in the extracted directory. The server should be accessible at `http://localhost:3000`. Verify that the API data can be accessed directly from the Node Server by visiting `http://localhost:3000/api/books` in Chrome. To configure Nginx to reverse proxy to the Node API Server, install and start Nginx using `sudo apt install nginx` and `sudo service nginx start`. Add a configuration block to the `default` file in `/etc/nginx/sites-enabled/` to proxy requests from `/api/` to `http://localhost:3000/`. With this setup, three services can be accessed: `http://localhost` (static files), `http://localhost:3000/api/books` (raw books directly from the Node Server), and `http://localhost/api/books` (raw books via Nginx). The challenge now is to upload and operationalize a Book Client website that talks to the API on `http://localhost/api/books`.

---

## Activity – Website maintenance Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/nf8iX/activity-website-maintenance)

Here is a summary of the text in 8 sentences, preserving key information:

To determine the frequency for each task in website maintenance, consider using your understanding of web development processes. Tasks should be performed regularly to ensure website updates are current and secure. Content management tasks include updating static content (daily/weekly), removing outdated content (monthly/quarterly), and repairing and updating broken links (weekly). Browser compatibility testing should be done daily on all major browsers and devices, with a focus on less-popular and latest browser versions. Code optimisation involves streamlining HTML, CSS, and JavaScript for efficiency (monthly/quarterly) and removing redundant code and comments. Website performance should be regularly checked and optimized as needed to ensure accessibility and security measures are in place. Deployment practices include using CI/CD pipelines for automated testing and deployment (weekly), implementing blue-green and canary deployment strategies (monthly/quarterly), and monitoring uptime and receiving alerts for any downtime (daily). User feedback and analytics should be collected and reviewed regularly to improve website traffic, CTAs, and user pathways.

---

## Lesson 14.2: self-evaluation checklist Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/ly8ah/lesson-14-2-self-evaluation-checklist)

Here is a summary of the text in 8 sentences:

To regularly assess understanding, reflect on learning journey, identify areas for improvement, and develop a plan. Use this checklist to evaluate knowledge against learning outcomes and revisit relevant materials if needed. The process of deploying a website involves setting up a server and configuring it to serve content. Availability and scalability are crucial in website deployment. Configuring a server to handle requests using reverse proxies is also important. Key tasks involved in maintaining a website include content updates, security checks, and performance optimisation. Testing website compatibility across different browsers and devices is significant. The provided self-evaluation checklist can be used to assess understanding of topics covered in this lesson.

---

