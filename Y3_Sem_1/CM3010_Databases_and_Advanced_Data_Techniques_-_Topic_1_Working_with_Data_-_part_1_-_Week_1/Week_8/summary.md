# Week 8 - CM3010 Databases and Advanced Data Techniques - Topic 1: Working with Data - part 1 - Week 1

## 01_Using_libraries_to_update_data_in_a_database_Video_9_min

# Using libraries to update data in a database
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/srXCZ/using-libraries-to-update-data-in-a-database

The provided text outlines the process and critical security considerations when transitioning from read-only data selection to write operations within a database, specifically using a library to address a MySQL Server. Fundamentally, any SQL command, including an `UPDATE` or `INSERT`, can be sent through the established socket connection; the functional difference between an update command and a query is minimal. However, writing data necessitates strict adherence to security principles to mitigate the risk of malicious commands being executed.

The primary security concern discussed is SQL injection, which occurs when user-supplied data is improperly integrated into a query command, whether the command is a `SELECT` or an `INSERT`. Because inputs can originate from external sources like web forms or HTTP responses, they cannot be inherently trusted to be clean. For example, a quote from a user input, when concatenated directly, can terminate the string and switch the database into command writing mode. This allows malicious users to inject commands, such as the dangerous example, `Drop table students from XKCD`.

There are several ways to reduce the risk associated with SQL injection. One method is restricting the user's database privileges so the script only possesses the necessary operational abilities, preventing destructive actions like dropping tables. Another method involves manual string hygiene, where special characters, like quotes, are escaped by prefixing them with a slash to ensure they are treated as text rather than semantic elements.

A far safer and cleaner approach is using parameterized queries, often implemented via syntax utilizing question marks. Instead of building the full command by concatenating strings manually, one inserts placeholders, such as `INSERT INTO actors VALUES (?, ?, ...)`. In libraries like the Node MySQL library, providing the values as a subsequent array automatically triggers the system to escape these values before insertion.

An alternative robust technique is the utilization of stored procedures, which exist on the database management side rather than the client library side. When defining a stored procedure, care must be taken to manage the command delimiters to ensure the definition completes correctly. The procedure is then called with specific arguments (e.g., `CALL adapter 'Richard Gere', 'male', '1949-08-31'`). The significant advantage is that the web user can be granted execution access only to this specific procedure, protecting them from running any other database code.

While the parameterization technique exists in many libraries, the specific mechanism for automatic escaping is tied to the MySQL library in JavaScript. For completing database operations, specifically after an `INSERT`, it is often necessary to retrieve the new, auto-incremented ID. In a standard MySQL environment, this is achieved using the command `SELECT last insert ID`.

Libraries provide methods for retrieving this ID; for instance, in the Node Janus example, the query function uses a callback. The response object resulting from the `INSERT` command contains an `insert ID` property, which must be accessed to pass the correct foreign key to subsequent relational inserts. This process ensures data integrity during complex relational insertions.

---

## 02_Connecting_to_mysql_from_node_User_definitions_Reading_10_min

# Connecting to mysql from node: User definitions
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/R3oP4/connecting-to-mysql-from-node-user-definitions

Database security dictates that users must be defined with specific access restrictions. These restrictions define not only the database parts allowed and the permitted activities but also the network locations from which connection is possible. When hosting a web server, it is often advisable to restrict user access exclusively to the local machine, or `localhost`. This ensures that attempts at accessing the database remotely are automatically rejected.

On the specific lab machines used, defining a user as `'username'@'localhost'` can lead to connection refusals from a Node.js application. This issue stems from how the MySQL instance interprets `localhost`. Specifically, our MySQL instance defaults to treating `localhost` as a UNIX socket connection. In contrast, the Node.js application inherently connects using TCP/IP by default.

To resolve this conflict, two distinct methods are available to ensure successful connectivity. The first solution involves altering the user definition within the database. Instead of using the constrained local access, the connection limit must be removed by creating the user as `'username'@'%'`. This allows connections from any network host.

The second viable solution involves forcing the Node.js application to utilize a UNIX socket connection instead of relying on TCP/IP. This requires modifying the connection definition within the JavaScript file, such as `index.js`. Specifically, one must add the parameter `socketPath: "/var/run/mysqld/mysqld.sock"`.

Crucially, the user only needs to implement one of these two specified fixes. Following either approach will allow the lab environment to function correctly. It should be noted that these particular connection issues are specific to the lab environment and are less likely to occur when connecting to other database servers.

---

## 03_Python_for_databases_how_and_why_Video_5_min

# Python for databases: how and why?
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/0LUJP/python-for-databases-how-and-why

This curriculum provides a comprehensive study of database systems, starting with basic data handling in Weeks 1 and 2. The core focus shifts in Weeks 3 and 4 to Relational Databases, followed by Weeks 5 and 6, which address the critical aspects of Data Integrity and Security. Database utilization is introduced in Weeks 7 and 8, emphasizing libraries and templating for practical data management. Hands-on application exercises include connecting to MySQL from Node, utilizing Python for database exploration, and plotting data via pyplot. The advanced topics begin in Week 9 with an exploration of advanced RDBMS concepts, leading to a Mid-term assignment in Week 10. Weeks 11 and 12 cover the complexities of Distributed databases and alternative database models. Subsequent modules delve into specialized architectures, including Semantic databases (Weeks 13-14) and Linked Data (Weeks 15-16). Modern data challenges are addressed through Weeks 17-18 on Multimedia and retrieval, and Weeks 19-20 on various database Applications. The intensive learning process concludes with Week 21 dedicated to preparation and Week 22 for the final exam.

---

## 04_Topic_4_summary_Video_2_min

# Topic 4 summary
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/87jep/topic-4-summary

The provided text details both the underlying architecture of relational database management systems (RDBMS) and a comprehensive curriculum structure for database topics.

From an architectural standpoint, connecting to an RDBMS like MySQL or Postgres involves the server listening on a specific TCP port for certain connections and triggers. The specialized libraries used for this function are often referred to as MySQL connectors. These connectors function by utilizing the existing infrastructure of the database software. A core finding is that significant commonality exists in the interaction methods across different programming languages. This similarity is evident because the underlying operations are executed by the same core software. This consistency holds true whether the connection originates internally to a local host port or from an external client to the MySQL server, a process which is completely transparent to the user.

However, variability exists in the interface built on top of this underlying core. Library developers can implement different options regarding transaction management. These include the choice to commit automatically after every operation, or to treat the entire interaction as a single transaction. Interface variations also pertain to how the connection is carried out and presented to the end-user. Furthermore, some libraries may vary in whether the query structure is natively translated into the programming language. This involves deciding whether the user submits a complete command string or utilizes dedicated methods such as a `query()` or `insert()` method. These differences are ultimately classified as interface changes overlaying the consistent core provided by MySQL. This design facilitates easy movement between diverse environments and libraries. The immediate future focus will shift to methods for checking the speed and improving the efficiency of database queries.

The course curriculum is highly structured across 22 weeks, covering various advanced database topics. Week 1 introduces basic working with data, leading into Week 2’s deep dive into data manipulation. Week 3 covers foundational concepts in Relational Databases, followed by Week 4, which continues this relational study. Subsequent topics address data integrity and security in Week 5, with Week 6 focusing on the reliable aspects of databases. Week 7 and 8 introduce the use of libraries and templating for database interaction. Practical application begins with module 4.2, Read/write database applications, which includes a 9-minute video and a 30-minute quiz.

Module 4.2 features specific labs, such as "Connecting to mysql from node" (a 10-minute reading) and "Writing to the database" (a 1-hour lab). Module 4.3 transitions to Python for data exploration, featuring a 5-minute video on "Python for databases: how and why?" This module also includes a 5-minute quiz and a 1-hour lab for plotting data using `pyplot`. The curriculum progresses to advanced topics in Week 9 and Week 11. Week 10 is dedicated to the Mid-term assignment. Weeks 11 and 12 cover Distributed databases and alternative database models.

Later topics delve into specialized systems, starting with Week 13 and Week 14 on Semantic databases. Weeks 15 and 16 cover the complexities of Linked Data. The course culminates with Week 17 and Week 18 on Multimedia and retrieval systems. Week 19 and Week 20 are dedicated to Applications, followed by Week 21 for exam preparation. The curriculum concludes with Exam week in Week 22.

---

## 05_Further_reading_Reading_1h

# Further reading
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/KSA6I/further-reading

Look at the documentation for your favoured language or programming environment. These should always be the first place you look for examples and guidance – they are more likely to be up to date than third party sites are. nodejs PHP Python For those interested in R, there is documentation at Databases using R . Several other languages are detailed in the connectors section of the developer area of the MySQL website. If these links are broken, please let us know via the Student Portal ....

---

