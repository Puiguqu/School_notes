# Week 3 - CM3010 Databases and Advanced Data Techniques - Topic 1: Working with Data - part 1 - Week 1

## 01_Welcome_to_relational_databases_Video_10_min

# Welcome to relational databases
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/vUfuu/welcome-to-relational-databases

A relational database (RDB) implements the abstract concepts of the relational model. A "model," generally, is a method for abstracting complex real-world data into manageable structures that can be reasoned about. Specifically, in this context, the relational database utilizes tables as its high-level structural approach. A "relation" is essentially a precise definition of a table, encompassing the defined columns (attributes), the definition of what those columns mean, and all the values stored within. The core of the relational model is this combination of definition and stored values.

The relational model establishes strict rules for how these relations must be manipulated. Fundamentally, the first rule dictates that everything within the system must be represented as a relation. All operations within the model must request and operate over tables. Moreover, the system must handle not only the information itself but also information about the information, such as creating new tables, users, or restructing the database through relation manipulation.

For a system to truly implement the model, it must be a robust, abstracted system. This means functionality must remain consistent regardless of physical or software constraints, such as hardware replacement, operating system changes, or changes in disk formatting. Furthermore, if the data is distributed across a network, it must maintain the appearance of being concentrated in a single location.

The course will explore three primary models: the abstract relational model, the entity-relationship (ER) model, and SQL. The ER model is widely used for modeling concepts and data structures, frequently applied to relational databases. However, it is critical to note that the term "relation" in the relational model differs significantly from the term "relationship" used in an ER diagram.

The relational model itself is highly theoretical, yet it has almost never been purely implemented in practice. Instead, SQL (and its variant, Sequal) serves as a practical, partial implementation of the relational model. SQL is not strictly adherence to the abstract model, but its underlying theory is applicable to various RDBMS packages like MySQL, PostgreSQL, and SQLite. These database packages are close enough to SQL that they can possess many of the abstract properties of the relational model. The overall curriculum is structured to meet these concepts, starting with fundamental theory in Week 3 and moving into practical design and implementation using ER diagrams and Basic SQL in Week 2.1. The full scope of the material extends through topics covering data integrity, security, distributed databases, and semantic databases over the coming weeks.

---

## 02_Drawing_a_database_I_Basic_entity-relationship_diagrams_Video_6_min

# Drawing a database I: Basic entity-relationship diagrams
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/mJMrV/drawing-a-database-i-basic-entity-relationship-diagrams

This course explores database concepts beginning with foundational material, including working with data (Weeks 1-2) and delving into relational database theory and design (Week 3). Core technical skills taught involve drawing basic Entity-Relationship Diagrams (ERDs), mastering Basic SQL, and practical application using MySQL in the lab. Subsequent topics focus on ensuring database reliability, covering crucial aspects of Data Integrity and Security across two weeks. Students progress to applying databases via libraries and templating (Weeks 7-8), followed by an exploration of Advanced RDBMS topics (Week 9) and a Mid-term assignment (Week 10). The curriculum then expands to complex architectures, addressing Distributed databases and alternative database models (Weeks 11-12). Advanced specialized models are introduced, specifically Semantic databases and Linked Data (Weeks 13-16). Finally, the course concludes by covering Multimedia and retrieval (Weeks 17-18) and various Applications (Weeks 19-20) before final exam preparation (Weeks 21-22).

---

## 03_Speaking_to_databases_I_Basic_SQL_Video_10_min

# Speaking to databases I: Basic SQL
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/CDVbO/speaking-to-databases-i-basic-sql

Database development requires speaking to database management software to build, populate, and query structured data. The primary language used for this interaction is Structured Query Language (SQL), which is implemented by various database packages. While MySQL is used in the labs, alternatives like PostgreSQL and SQLite offer similar commands and syntax. These implementations, however, may require consulting documentation for specific dialect differences.

The theory of relational databases distinguishes between structure manipulation and data interaction. Data Definition Language (DDL) handles the structure of the database, using commands such as `CREATE`, `DROP`, `TRUNCATE`, and `ALTER`. Data Manipulation Language (DML) focuses on the data within those structures, including commands like `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.

The `SELECT` command is used to retrieve specific information from tables. It introduces a query, and subsequently, the column specification names the desired fields that will appear in the results. The syntax is generally: `SELECT column_name FROM table_name WHERE condition`.

This query structure retrieves data for all entries in the specified table, allowing constraints to filter the results. For example, to find planet names where day length exceeds 200 hours, one uses `SELECT PlanetName FROM Planets WHERE DayLength > 200`. Note that field names must be explicitly listed separate from the constraints used for filtering.

The `CREATE` command, a DDL function, is used to build new structures, specifically tables. The syntax begins with `CREATE TABLE table_name` and requires fields and columns to be defined immediately afterward in brackets.

Each column must be assigned a data type, which dictates the kind of information it holds. Textual data types are designated using `CHAR(n)`, where 'n' specifies the maximum character length. Numerical data types, such as integers, are specified as `INT` for whole numbers.

A crucial concept for defining proper structure is the Primary Key. A primary key enforces a constraint in the relational model, ensuring that every row in a table is unique. This constraint is specified by designating a unique field or combination of fields.

This mechanism ensures that the table maintains both the integrity of a table and the uniqueness required of a relation. The fundamental process involves designing the database, using SQL to manipulate its definitions and data, and enforcing rules like uniqueness and data types.

---

## 04_Speaking_to_databases_II_Using_MySQL_in_the_lab_Video_7_min

# Speaking to databases II: Using MySQL in the lab
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/QB8SB/speaking-to-databases-ii-using-mysql-in-the-lab

This comprehensive curriculum begins with foundational data concepts, covering basic data manipulation and introducing relational databases through Entity-Relationship Diagrams and basic SQL querying. The early modules focus heavily on practical implementation, using MySQL for database creation and querying, alongside understanding the core theory of relational database design. Subsequent modules address the critical operational aspects of reliable databases, specifically focusing on ensuring Data Integrity and Data Security. The advanced portion of the course explores diverse architectural models, including Distributed databases, Semantic databases, and Linked Data, which move beyond standard RDBMS functionality. Practical application is detailed by discussing libraries and templating, followed by specialization in Multimedia and retrieval systems. The learning progression culminates in applications and complex topics before a Mid-term assignment at Week 10. The course concludes with intensive preparation leading up to the final examination in Week 22.

---

