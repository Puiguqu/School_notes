# Week 7 - CM3010 Databases and Advanced Data Techniques - Topic 1: Working with Data - part 1 - Week 1

## 01_Introduction_to_using_relational_databases_Video_1_min

# Introduction to using relational databases
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/WiDB3/introduction-to-using-relational-databases

The primary focus of the course shifts from database structure and reliability to the practical methods of interacting with database systems. While previous sections covered how to structure and ensure the reliability of a database, the subsequent learning concentrates on communication methods. In practice, interacting with a database is accomplished mostly through libraries integrated into other software environments. The material aims to examine common factors across various programming languages to allow for adaptable database handling. Specific languages covered include Node.js (JavaScript), PHP, and Python.

A key concept explored is how to address databases when handling data originating from external user input versus data generated internally by the code. This process necessitates an understanding of database addressing techniques. The syllabus outlines a progression across 22 weeks, building knowledge systematically. Early topics cover foundational skills, including Week 1 and Week 2, focusing on general data working. Weeks 3 and 4 are dedicated to Relational Databases, covering their essential concepts in depth.

Weeks 5 and 6 detail Reliable Databases, emphasizing critical aspects like Data Integrity and Security. Week 7 introduces the practical application of using databases via libraries and templating. Practical exercises involve connecting to an SQL RDBMS, with a specific introduction to getting practice with MySQL. A session is dedicated to connecting to an SQL RDBMS, which is paired with a corresponding quiz and practice assignment.

Further practical application is demonstrated in connecting for web page serving, utilizing technologies like Node.js and Mustache. Labs are structured, such as a "Making a website with a database backend: node.js Lab." The curriculum also integrates PHP through dedicated modules on "Using PHP SQL libraries." Advanced topics begin in Week 9, marked as Topic 5, and continue with RDBMS topics.

The curriculum expands significantly into advanced database concepts in the latter half of the course. Week 11 and Week 12 cover Distributed Databases and alternative database models. Topics then move into Week 13 and 14, focusing on Semantic Databases. Weeks 15 and 16 are dedicated to understanding and utilizing Linked Data, a crucial area in data modeling. Multimedia and retrieval form the basis of the course in Weeks 17 and 18.

The final phase includes Topics 10, which focuses on Applications (Weeks 19 and 20). The course structure includes various assessments, such as a Mid-term assignment in Week 10. The sequence culminates in Week 21, designated for exam preparation, followed by the final Exam week. Technical learning environments emphasize adaptability, ensuring students can work with nearly any language or environment that requires database communication.

---

## 02_Speaking_to_databases_III_the_core_vocabulary_Video_8_min

# Speaking to databases III: the core vocabulary
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/z8SMB/speaking-to-databases-iii-the-core-vocabulary

This curriculum outlines a comprehensive journey into database management, beginning with foundational concepts in data handling during Weeks 1 and 2. The focus then shifts to mastering Relational Databases (RDBMS) in Weeks 3 and 4, followed by ensuring data reliability through topics on Data Integrity and Security in Weeks 5 and 6. Subsequent learning utilizes these databases for web applications, introducing tools like Node.js and mustache for templating, and PHP SQL libraries for backend functionality (Weeks 7 and 8). Advanced RDBMS concepts are covered in Week 9, before the study progresses to more diverse architectures in Weeks 11 and 12, focusing on Distributed databases and alternative database models. The curriculum then explores specialized data structures, dedicating Weeks 13 and 14 to Semantic databases. Further modernization includes Weeks 15 and 16, which detail the implementation of Linked Data. The final technical phases involve Multimedia and retrieval processes (Weeks 17 and 18), culminating in practical Applications (Weeks 19 and 20). Throughout the course, practical labs are integrated, such as exploring movie data and connecting to an SQL RDBMS. This structured approach prepares students for the Mid-term assignment in Week 10 and the final Exam in Week 22.

---

## 03_Getting_practice_with_MySQL_(Lab_introduction)_Video_17_min

# Getting practice with MySQL (Lab introduction)
Video • 17 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/pwwgx/getting-practice-with-mysql-lab-introduction

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

## 04_Connecting_to_an_SQL_RDBMS_Video_5_min

# Connecting to an SQL RDBMS
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/bhQOt/connecting-to-an-sql-rdbms

This curriculum provides a comprehensive study of database systems, beginning with foundational concepts in Week 1 and Week 2 on Working with Data. The study progresses to Relational Databases (Weeks 3 and 4), followed by critical modules in Weeks 5 and 6 detailing Data Integrity and Security to ensure reliable database operation. Practical application begins in Week 7 and Week 8, focusing on using libraries and templating for data retrieval. Specific technical implementations are detailed through labs connecting to an SQL RDBMS, utilizing Node.js and Mustache for web page serving, and implementing PHP SQL libraries. Advanced theoretical exploration begins in Week 9 with advanced RDBMS topics, transitioning into Week 11 and Week 12 to cover Distributed databases and alternative database models. The curriculum then moves into specialized paradigms, dedicating Weeks 13 and 14 to Semantic databases, and Weeks 15 and 16 to the concepts of Linked Data. Retrieval techniques are covered in Weeks 17 and 18 through the topic of Multimedia and retrieval. The final segment, Weeks 19 and 20, concentrates on database Applications, culminating in comprehensive exam preparation in Week 21 and the final exam in Week 22. The course includes a mid-term assignment in Week 10 to assess understanding across the initial core concepts.

---

## 05_Using_node.js_and_mustache_Video_10_min

# Using node.js and mustache
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/uOiQP/using-node-js-and-mustache

This technical guide outlines the creation of a web application with a database backend, utilizing Node.js, Express, and MySQL. The primary objective is to enable JavaScript to interact with a database to generate dynamic web pages.

The setup utilizes the NPM package manager, which relies on the `package.json` file to list and manage application dependencies. Running `npm install` pulls the necessary libraries, including MySQL for database interaction, Express as the web server, and Mustache-Express for templating.

Express, the web server, is initialized by requiring the module and creating an application instance. Web ports must be declared, allowing the Express server to listen internally, often on a specific port like 8088, while an external server (like Apache) handles the public interface.

The `app.get` method is used to declare specific paths that the application listens for HTTP requests on, such as the top level (`/`). This method accepts a callback function that processes the incoming `request` object (client data) and handles the outgoing `response`.

Within this request handler, `response.render` is called, which sends the generated content to the client.

Mustache serves as the templating language, allowing developers to embed variables directly into HTML. Variables are accessed using double curly brackets, such as `{{variableName}}`, which JavaScript replaces with the actual data value.

A common and complex use of Mustache involves iteration, especially when querying a database that returns multiple rows. This loop construct is defined using bracket hash syntax, `{{#collection}}...{{/}}`, which instructs the template engine to repeat the inner block for every item in the specified iterable object.

The MySQL database integration begins by loading the library using `const mysql = require('mysql')`. Next, `createConnection` is called to establish a connection object, requiring parameters like host, user, password, and the target database.

The connection must be activated by running the `connect` command on the connection object; in the lab setup, this is provided with a callback function to manage potential errors.

To retrieve data, the `query` method is executed, accepting a standard MySQL query string (e.g., `SELECT...`). Due to JavaScript's asynchronous nature, the query does not return results immediately.

Instead, the query method requires a callback function to execute upon completion. This callback function accepts up to three arguments: the potential `error`, the iterable `results` (objects for each row), and the array of `fieldnames`.

The flow dictates that once the database query returns results, the application proceeds to send an HTTP response. The key functionality achieved is the rendering of the data into HTML using Mustache within the Express response cycle, thus completing the database-to-web page process.

---

## 06_Using_PHP_SQL_libraries_Video_4_min

# Using PHP SQL libraries
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/SWYlA/using-php-sql-libraries

This curriculum provides a comprehensive, 22-week study of database systems, beginning with foundational concepts in data working (Weeks 1 & 2). The focus quickly shifts to Relational Databases (RDBMS) in Weeks 3 and 4, followed by crucial modules on Data Integrity and Security for reliable database management (Weeks 5 & 6). Weeks 7 and 8 introduce practical application development, demonstrating how to connect databases using libraries and templating in web service contexts.

A core practical element is detailed in Week 4, where students learn to connect to an SQL RDBMS, coupled with hands-on practice using MySQL. Furthermore, the curriculum covers specific technologies for web serving, including the use of node.js and mustache for database backends (Week 4.1), alongside integrating PHP SQL libraries.

Later modules explore advanced database paradigms, commencing with complex RDBMS topics (Week 9) and moving into Distributed databases and alternative models (Weeks 11 & 12). The specialization continues with a deep dive into Semantic databases (Weeks 13 & 14) and the principles of Linked Data (Weeks 15 & 16).

The final phase of the course broadens scope to include Multimedia and retrieval (Weeks 17 & 18) and culminates in studying various real-world Applications of database systems (Weeks 19 & 20). The instruction integrates multiple learning methods, including dedicated Lab work, specific video tutorials, and practical quizzes, culminating in a Mid-term assignment and final exam preparation.

---

