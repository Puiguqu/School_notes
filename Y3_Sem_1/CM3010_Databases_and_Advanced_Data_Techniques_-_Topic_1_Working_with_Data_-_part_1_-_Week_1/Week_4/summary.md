# Week 4 - CM3010 Databases and Advanced Data Techniques - Topic 1: Working with Data - part 1 - Week 1

## 01_Introducing_Joins_Video_9_min

# Introducing Joins
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/FAMiP/introducing-joins

Database joins are essential mechanisms used in relational databases to combine data from multiple tables, allowing queries to access relationships between entities. The concept of a join arises when querying requires linking tables, such as relating planets and their associated moons. There are three primary types of joins discussed: the Cross Join, the Inner Join, and the Outer Join.

The Cross Join is the simplest type, accomplished by listing multiple tables directly in the `FROM` clause of a SQL statement. Its defining characteristic is that it combines every single row from one table with every single row from every other table. For example, if one table has seven records and another has twelve, a Cross Join results in $7 \times 12 = 84$ rows.

A significant technical caution must be applied to Cross Joins because they quickly produce extremely large and often meaningless result sets, such as pairing every planet with every moon regardless of association. Operations like sorting or filtering on these massive tables consume substantial memory or disk resources.

The Inner Join is the most commonly used and constrained join type, focusing only on matches between tables. While an inner join can sometimes be implicitly recognized by the Database Management System (DBMS) using an equals constraint in the `WHERE` clause (e.g., `WHERE planet.name = moon.planet`), a clearer syntax involves explicit joining.

Explicit inner join syntax is defined as `FROM table1 INNER JOIN table2 ON condition`. This method specifies the first table, the join type, the second table, and the exact criterion for combination.

This constrained approach significantly reduces the results; using the previous example of eight planets and 173 moons, a Cross Join yields 1,384 meaningless results, whereas an Inner Join yields only the 173 meaningful, associated results.

The Outer Join, which includes Left and Right variations, preserves records even when no match exists in the other table. Unlike the Inner Join, which discards rows without a match, the Outer Join ensures all rows from one specified table are included.

Specifically, a `LEFT JOIN` (or `LEFT OUTER JOIN`) ensures that all rows from the left-hand table are displayed, regardless of whether a match exists in the right-hand table.

In cases where a row from the left table has no match in the right table, the resulting fields from the right table will contain `NULL` entries. This feature is invaluable for finding records that lack corresponding matches in related datasets.

In summary, joins fundamentally control the row count and content of a query's output. Cross Joins are expansive and must be heavily constrained. Inner Joins are precise, returning only related pairs. Outer Joins ensure data preservation, displaying all records from one side, whether matched or not.

---

## 02_Drawing_a_database_II_More_about_joins_Video_13_min

# Drawing a database II: More about joins
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/lXLXI/drawing-a-database-ii-more-about-joins

This course progresses systematically through database management, beginning with foundational topics in working with data (Weeks 1-2). Weeks 3 and 4 focus heavily on **Relational Databases**, introducing complex structures and detailing the mechanism of **Joins** and their implications through dedicated video and practice assignments. The curriculum then delves into the critical concepts of **Database Integrity and Keys** (Weeks 5-6), emphasizing the role of keys in maintaining data accuracy and structure.

Following database theory, Weeks 7 and 8 cover practical implementation by exploring how databases are used with libraries and templating in application development. The specialization then accelerates with **Advanced RDBMS topics** (Week 9), preceding a mid-term assignment. A significant technical shift occurs in Weeks 11 and 12, which address **Distributed databases and alternative database models**.

Later sections explore highly specialized database architectures: Weeks 13 and 14 focus on **Semantic databases**, while Weeks 15 and 16 cover the implementation of **Linked Data**. Subsequent weeks (17-20) broaden the scope to include **Multimedia and retrieval** and general **Applications**. The final weeks are dedicated to preparation and the examination, concluding the comprehensive study of database systems.

---

## 03_E_R_diagrams_summary_Reading_1h

# E/R diagrams summary
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/2ct3P/e-r-diagrams-summary

The attached section from the Database systems subject guide goes from the basics of E/R diagrams and modelling to more details about problems with the model and the process of implementing it as a relational diagram: Lewis, D. CO2209 Database systems. (London: University of London, 2016)....

---

## 04_Database_integrity_and_the_role_of_keys_Video_9_min

# Database integrity and the role of keys
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/ChTWr/database-integrity-and-the-role-of-keys

Database integrity is the crucial process of anticipating and preventing data anomalies and problems within a database structure. The fundamental goal is to ensure that planned structures minimize the potential for errors when data is entered or managed. The transcript explores these issues using the example of planet and moon data, illustrating various forms of data anomalies.

A primary potential issue is human typographical errors, such as mistyping "Mars" as "Mers," which creates a labeled planet that does not exist. Such an error can cause the moon to disappear in specific queries and lead to incorrect answers when asking questions about the planet's moons.

Another critical technical point is the use of the `NULL` value in the relational model, which introduces ternary logic beyond the standard Boolean true/false. If a planet name is forgotten, the resulting `NULL` value can never align during a database join, causing data to be missed in summary tables.

A third type of anomaly involves the entry of semantically meaningless data, such as recording a negative area (e.g., -495 sq km). Although this might not immediately break the database, any calculations performed using this invalid value will yield meaningless, incorrect results.

The system must distinguish between a harmless typo (e.g., 95 instead of 495) and truly meaningless data (negative area). Another problem arises when contradictory values are present; for instance, if a moon entry gives two different area values for the same moon and planet. While satisfying the unique row constraint (due to differing area), these values are inconsistent and unresolvable.

Further issues arise from inconsistent naming conventions, such as misspelling a moon as "Dimos" in one record and "Deimos" in another, which prevents the database from recognizing they are the same entity.

Duplicate entries can also create problems, such as having "Deimos" and "Dimos" listed separately in the moons table, even though they represent the same object.

A significant conflict arises when there are incompatible values between different parts of the database. For example, if the planet table lists Mars as having two moons, but the moon count calculated from the moons table is three, the system contains conflicting information.

Finally, records can become "orphans," which occur when a reference to a deleted entity persists. If Pluto is deleted from the planets table, its moon, Charon, remains in the moons table, referencing a non-existent planet. This is an orphan record resulting from a database action, not necessarily human error.

In summary, database integrity must address various issues: incorrect linkages, unspecified values (`NULL`), impossible values (negative areas), contradictory data, misspelled identities, and orphaned records. The ultimate objective is to determine which errors can be structurally prevented by the database design and which errors require continual human checking and review.

---

## 05_Speaking_to_Databases_II_SQL_for_joins_and_keys_Video_13_min

# Speaking to Databases II: SQL for joins and keys
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/NK5sU/speaking-to-databases-ii-sql-for-joins-and-keys

This curriculum progresses through several stages of database theory, beginning with foundational data handling in Weeks 1 and 2. Weeks 3 and 4 focus intensely on Relational Databases, specifically introducing complex concepts like Joins and refining understanding through E/R diagrams and associated practice assignments. Subsequent study in Weeks 5 and 6 addresses Data Integrity and Security, emphasizing the crucial role of database keys. The course then moves into practical application in Weeks 7 and 8, focusing on Using Databases through libraries and templating. Advanced topics begin in Week 9, followed by a mid-term assessment in Week 10. The syllabus expands significantly in Weeks 11 and 12 by introducing Distributed databases and alternative database models. Furthermore, Weeks 13 through 16 delve into Semantic databases and Linked Data, providing a comprehensive overview of modern data structuring. The latter half includes coverage of Multimedia and retrieval (Weeks 17-18) and diverse Application models (Weeks 19-20). The entire curriculum culminates with preparation for the final exam in Weeks 21 and 22, building upon essential skills such as SQL for joins and keys.

---

## 06_Topic_2_summary_Video_1_min

# Topic 2 summary
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/LfsJV/topic-2-summary

The course structure covers various aspects of database management, beginning with foundational data modeling concepts. Students first encounter the Entity Relationship (ER) Model, learning how to translate this model into explicit ER diagrams. A key objective is understanding the inherent relationship between the ER Model and the practical Relational Model. The relational principles are subsequently explored in detail. Implementation of the relational model is covered through specific database language, namely SQL. Practical exercises involve working with MySQL to solidify understanding of database manipulation. A significant focus is placed on enhancing database clarity and reliability. This reliability is achieved through the explicit use of joins and keys. Making the data structure explicit is highlighted as crucial for ensuring database integrity.

The curriculum dedicates substantial time to the complexity of relational databases. Specifically, the concept of Joins and their implications is introduced to handle complex data relationships. Furthermore, the topic of integrity and the fundamental role of keys in maintaining data quality is thoroughly explored. Students engage in practical exercises, such as designing and building simple databases using SQL for joins and keys.

Moving beyond foundational relational concepts, the course advances into complex and reliable database architecture. Week 5 and Week 6 delve specifically into Data Integrity and Security within reliable databases. The curriculum then shifts to modern applications, covering how databases are utilized with libraries and templating (Week 7 and Week 8). Advanced topics involve deeper dives into Relational Database Management Systems (RDBMS).

A major segment addresses distributed databases and alternative database models, covering topics across Weeks 11 and 12. Further sophisticated concepts include Semantic databases, which focus on meaning and context. Linked Data, an interconnected approach to information, is covered across Weeks 15 and 16. The scope extends to Multimedia and retrieval systems (Weeks 17 and 18). Finally, the course explores practical Applications of databases in Weeks 19 and 20. The learning culminates with preparation and the examination during Weeks 21 and 22. Throughout the course, quizzes and practice assignments are provided to reinforce key technical knowledge and patterns in ER diagrams.

---

## 07_Further_reading_Reading_1h

# Further reading
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/hdvyG/further-reading

Chen, P. ‘The entity-relationship model – Toward a unified view of data’, ACM Transactions on Database Systems 1(1) 1976, pp.9–36. This reading is available via the Online Library . Further reading Chen, P. ‘The entity-relationship model – Toward a unified view of data’, ACM Transactions on Database Systems 1(1) 1976, pp.9–36. This reading is available via the Online Library . Mark as completed Dislike Report an issue

---

