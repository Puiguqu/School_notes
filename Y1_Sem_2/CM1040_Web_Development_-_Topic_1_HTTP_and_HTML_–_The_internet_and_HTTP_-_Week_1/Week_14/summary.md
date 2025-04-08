# Week 14 - CM1040 Web Development - Topic 1: HTTP and HTML – The internet and HTTP - Week 1

## Topic 7 Week 2 introduction Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/IVKUl/topic-7-week-2-introduction)

There is no text provided for me to summarize. The given text appears to be a video transcript with information about an upcoming lecture on deploying websites into different server setups, including Unix command line hacking and web server configuration. 

However, I can provide a summary of the key concepts and findings in 8 sentences:

This week's topic is Week 2 for Topic 7, focusing on web development lifecycle and deploying websites onto servers. The instructor will be using Unix command line skills to share expertise with students. They aim to cover web server configuration techniques and deployable website setups at scale. Students can expect to learn about static and non-static website deployment methods through video lectures and practice assignments. A lab exercise, "Configuring a web server," is also available for hands-on experience. The instructor hopes that students will enjoy the process of learning about deploying websites and gain knowledge on scalable deployment techniques. Key concepts include Unix command line skills and web server configuration. The material covered in this week's lesson should be valuable to those working on websites and looking to improve their web development lifecycle understanding.

---

## Basic static website deployment Video• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/zLpIq/basic-static-website-deployment)

This is a video transcript of a tutorial on basic web deployment techniques, specifically deploying a static website on a web server.

The tutorial covers the following topics:

1. Deploying a static website on a web server
2. Configuring domain names for the website
3. Testing the website with ping and curl commands
4. Using HTTPs certificates to secure the website

The tutorial includes live demonstrations of each step, using a virtual machine as an example.

Here is a summary of the key points covered in the tutorial:

* To deploy a static website on a web server, you need to:
	+ Install a web server software (e.g. Nginx)
	+ Create a virtual host configuration file
	+ Upload your website files to the web server using Filezilla or SFTP
	+ Configure the domain name for the website
* To configure a domain name for the website, you need to:
	+ Buy a domain name from a registrar (e.g. GoDaddy)
	+ Point the domain name at an IP address (in this case, the virtual machine's IP address)
	+ Set up DNS records for the domain name
* To test the website with ping and curl commands, you need to:
	+ Use the `ping` command to check if the website is reachable from a remote location
	+ Use the `curl` command to send an HTTP request to the website and verify that it responds correctly
* To use HTTPs certificates to secure the website, you need to:
	+ Generate a self-signed certificate (or obtain one from a trusted certificate authority)
	+ Configure the web server to use the HTTPs certificate

The tutorial concludes by emphasizing the importance of testing and verifying that the website is working correctly after deployment.

Overall, this tutorial provides a comprehensive introduction to deploying a static website on a web server, including configuration, testing, and security considerations.

---

## Non-static and scalable website deployment Video• . Duration: 24 minutes 24 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/orpHZ/non-static-and-scalable-website-deployment)

This is a transcript of a video on deploying dynamic websites, specifically focusing on non-static and scalable deployment techniques.

The video covers the following topics:

1. Basic web deployment techniques
2. Non-static and scalable website deployment
3. Continuous integration and continuous deployment
4. Containerization and orchestration
5. Monitoring and security

The video discusses various tools and technologies used in deploying dynamic websites, including:

* Reverse proxies
* Load balancers
* Docker containers
* Kubernetes (not explicitly mentioned, but implied by the container orchestration discussion)
* Prometheus for monitoring
* GitHub for continuous integration and deployment

The video also touches on the importance of security, monitoring, and maintenance when deploying complex systems.

Throughout the video, the author provides examples and explanations to help viewers understand the concepts and technologies involved in deploying dynamic websites.

Some key takeaways from the video include:

* The importance of using non-static and scalable deployment techniques for dynamic websites
* The benefits of containerization and orchestration for managing and updating containers
* The role of continuous integration and continuous deployment in ensuring code quality and efficiency
* The need for monitoring and security measures to ensure the stability and integrity of the deployed system

Overall, this video provides a comprehensive overview of deploying dynamic websites, covering both technical details and best practices.

---

## Topic 7 summary Video• . Duration: 45 seconds 45 sec

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/WUdN3/topic-7-summary)

There is no text to summarize. The provided text appears to be a video transcript and additional page content for an online course or tutorial, but it does not contain any specific information or data that can be summarized into 8 sentences.

However, I can provide a summary of the topics mentioned in the text:

The text discusses two main stages of the web development lifecycle: early stages (user requirement gathering, participatory design workshops) and late stages (deploying websites onto web servers, reverse proxies, and Dockerizations).

The course covers lesson 14.1 on basic web deployment techniques, 14.2 on non-static and scalable website deployment, which includes a video, practice assignment, reading activity, and self-evaluation checklist.

Additionally, the text mentions other topics related to website deployment and maintenance, including a practice assignment for website maintenance planning and a reading lesson for non-static and scalable website deployment practical work.

If you provide the actual text or content you'd like me to summarize, I'll be happy to assist you.

---

## Activity – Non-static and scalable website deployment practical Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/mZ8TF/activity-non-static-and-scalable-website-deployment-practical)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

To run the Bookserver Node.js application, download the bookserver.zip file, unzip it, navigate to the bookserver directory, and run node server.js. This should start the server on http://localhost:3000. Next, configure Nginx as a reverse proxy server by installing it with sudo apt install nginx, starting the service with sudo service nginx start, and editing the default config file to include the following code snippet:

```javascript
location /api/ {
  proxy_pass http://localhost:3000/;
  proxy_http_version 1.1;
  proxy_set_header Upgrade $http_upgrade;
  proxy_set_header Connection 'upgrade';
  proxy_set_header Host $host;
  proxy_cache_bypass $http_upgrade;
}
```

After saving the changes, try accessing http://localhost/api/books in Chrome to verify that the raw JSON data is displayed correctly. If you encounter a "502 Bad Gateway" error, it means that the node server is not running and needs to be restarted. With the bookserver up and running, you can now upload your book client website to the website folder and serve it on http://localhost. The client website should communicate with the API on http://localhost/api/books. To complete this lesson, verify that the book client website works correctly and mark it as completed in the provided completion checklist.

---

## Activity – Website maintenance Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/nf8iX/activity-website-maintenance)

Here is a summary of the text in 8 sentences, preserving key information:

To maintain a website, tasks should be performed at various frequencies. Content management tasks, such as updating static content and fixing broken links, should be done regularly (e.g., daily, weekly). Code optimisation, accessibility, and security measures should also be reviewed and updated frequently, including checking for outdated content, plugins, and browser compatibility. For scalability, load balancing, and caching strategies can be implemented with regular monitoring and backups to ensure database performance and uptime.

Automated testing and deployment using CI/CD pipelines can help streamline website updates, while blue-green and canary deployment strategies can minimize downtime. Regular security audits and vulnerability assessments should be performed to ensure strong access control and secure authentication. User feedback and analytics can help improve CTAs and user pathways, leading to better website performance.

It is essential to set up monitoring and logging systems to automate regular backups and test recovery plans. A comprehensive approach to website maintenance involves implementing these strategies to ensure a smooth and efficient online experience.

---

## Lesson 14.2: self-evaluation checklist Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/ly8ah/lesson-14-2-self-evaluation-checklist)

Here is a summary of the text in 8 sentences:

The provided text appears to be a self-evaluation checklist for a course on web deployment techniques. The exercise aims to help students reflect on their learning journey, identify areas for improvement, and develop a plan for growth. Students are expected to regularly assess their understanding against the learning outcomes. The checklist covers key concepts such as deploying a website, configuring a server, maintaining a website, and testing website compatibility. Students who feel uncertain about these concepts should revisit relevant lecture videos, readings, and activities to consolidate their knowledge. The text mentions specific topics covered in lessons 14.1 and 14.2, including basic web deployment techniques, non-static and scalable website deployment, and website maintenance. Students are also expected to complete practice assignments, reading activities, and a self-evaluation checklist as part of their progress through the course. Overall, the exercise aims to help students develop a plan for improvement and deepen their knowledge and skills in web deployment techniques.

---

