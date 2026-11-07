# Week 6 - CM3010 Databases and Advanced Data Techniques - Topic 1: Working with Data - part 1 - Week 1

## 01_On_ACID_Guaranteeing_a_DBMS_against_errors_Video_11_min

# On ACID: Guaranteeing a DBMS against errors
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/d0W9a/on-acid-guaranteeing-a-dbms-against-errors

This curriculum progresses through various stages of data management, beginning with foundational concepts like "Working with Data" (Weeks 1 and 2). The focus immediately shifts to "Relational Databases," covering the fundamental theories and structure of RDBMS (Weeks 3 and 4). A crucial segment dedicated to reliable databases, Data Integrity, and Security is covered in Weeks 5 and 6.

Module 3.2 provides a deep dive into ACID and transactions, emphasizing the necessary guarantees for a DBMS against errors. This includes detailed study of transactions and serialisation, reinforced by quizzes and discussion prompts. Module 3.3 further explores security and user accounts, focusing on defending against both malicious and accidental damage using SQL policies.

The learning trajectory then moves to practical implementation, covering "Using Databases: libraries and templating" in Weeks 7 and 8. Week 9 introduces advanced RDBMS topics, preparing students for the Mid-term assignment.

Subsequent weeks explore complex data architectures, beginning with "Distributed databases and alternative database models" (Weeks 11 and 12). This leads into highly specialized fields such as "Semantic databases" (Weeks 13 and 14).

Furthermore, the course addresses modern data structures with "Linked Data" (Weeks 15 and 16). Retrieval methods are covered through "Multimedia and retrieval" (Weeks 17 and 18).

The final phase focuses on practical implementation through "Applications" (Weeks 19 and 20). The course culminates in preparation for the final exam and the exam week.

---

## 02_Transactions_and_serialisation_Video_21_min

# Transactions and serialisation
Video • 21 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/80YzA/transactions-and-serialisation

This transcript provides a comprehensive explanation of database consistency, transaction isolation, and the mechanisms used by Database Management Systems (DBMS) to ensure data integrity (ACID properties).

Here is a structured summary of the key concepts:

---

### 💾 Core Concepts: Consistency and Transactional Integrity

The primary goal of transactional database management is to ensure that no matter how transactions are executed concurrently (interleaved), the database state remains **consistent** and logically correct.

#### 1. The Problem: Inconsistent Analysis (Non-Serializability)
When multiple transactions run simultaneously, they might "read" data in different phases of updates by other transactions. This interleaving can lead to a state that is logically impossible or incorrect.

*   **Example:** If Transaction 1 updates Account A, but Transaction 2 reads A *before* T1’s update is complete, T2 might use stale data. If T2 then updates based on that stale data, the final system state becomes mathematically unsound (e.g., total money in the system suddenly increases when it shouldn't).
*   **The Result:** The database ends up in a non-consistent state that has never actually existed.

#### 2. The Solution: Mechanisms for Isolation and Safety

To prevent inconsistent analysis, DBMS employs sophisticated control mechanisms:

*   **Locking Systems:** This is the standard method of control. Locks dictate which operations are allowed to happen at any given time:
    *   **Write Lock:** If a transaction holds a write lock on data, *no other transaction* can access that data (neither read nor write). This prevents data corruption during modification.
    *   **Read Lock:** Multiple transactions can usually hold read locks on the same data simultaneously. However, if *any* transaction is reading, no other transaction can write to that data.
*   **Snapshot Isolation (Copying the State):** As an alternative, especially for read-only operations, the DBMS can provide the transaction with a temporary copy of the database from the **last known good state**. This allows the transaction to perform its analysis using "stale data" while other transactions are busy rewriting the current state, ensuring safety without blocking the whole system.

#### 3. The Ideal Guarantee: Serializability
The gold standard for transactional safety is **serializability**.

*   **Definition:** A set of concurrent (interleaved) operations is serializable if the final result is identical to the result achieved if those transactions were run one after the other (serially).
*   **Significance:** If the interleaved execution yields the same answer as a serial execution, we know the operations were isolated and safe.
*   **Simplifications:** Interleaving is automatically safe if:
    1.  Transactions operate on completely different pieces of data.
    2.  All transactions are simple `SELECT` (read) operations.

---

### 🎯 Summary for the User (ACID Properties)

From a user's perspective, the complexity of locks, reads, and serializability is managed by the DBMS.

*   **The Key Action:** The user simply declares a logical block of operations as a **Transaction**.
*   **The DBMS Role:** By declaring a transaction, the user gives enough information to the DBMS, which then automatically handles the underlying mechanisms (like locking strategies and failure recovery) to ensure that the **ACID properties** are preserved.

In short, the user focuses on *what* needs to happen (the transaction), and the DBMS focuses on *how* to make sure it happens safely, consistently, and reliably.

---

## 03_More_depth_on_ACID_and_integrity_risks_Reading_1h

# More depth on ACID and integrity risks
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/8iC8F/more-depth-on-acid-and-integrity-risks

From the Database systems subject guide: Lewis, D. CO2209 Database systems. (London: University of London, 2016). acid-and-transactions.pdf PDF File The concept of ACID was introduced in this paper: Härder, T and A. Reuter ‘Principles of Transaction-Oriented Database Recovery’, ACM Computing Surveys, 15/4 1983. This reading is available in the Online Library . More depth on ACID and integrity risks From the Database systems subject guide: Lewis, D. CO2209 Database systems....

---

## 04_Malice_and_accidental_damage_Video_4_min

# Malice and accidental damage
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/09l8W/malice-and-accidental-damage

This course follows a comprehensive 22-week structure, beginning with foundational concepts in Weeks 1 and 2 focusing on general data manipulation. Weeks 3 and 4 dive specifically into Relational Databases, establishing the initial framework for data organization. The next major section, Weeks 5 and 6 (Topic 3), emphasizes reliable databases, centered on the critical technical concept of ACID properties to guarantee integrity during transactions. A detailed study of security, covered in Weeks 6, explores threats like malice and accidental damage, alongside implementing security and user policies using SQL. After a mid-term assignment (Week 10), the course shifts to practical usage, covering libraries and templating in Topic 4 and advanced RDBMS topics in Topic 5. The focus expands into modern architecture with Topic 6, exploring both distributed databases and various alternative database models. Topics 7, 8, and 9 introduce conceptual advances, detailing semantic databases and the mechanism of Linked Data for interconnectivity. Weeks 17 through 19 specialize in data retrieval, covering multimedia and the application of various database models. The final weeks are dedicated to real-world scenarios (Topic 10: Applications) and preparation. The course culminates in week 22 with the final examination, after the intensive preparation period in Week 21.

---

## 05_Security_and_user_policies_with_SQL_Video_11_min

# Security and user policies with SQL
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/OFcum/security-and-user-policies-with-sql

This discussion focuses on controlling user and script access to SQL databases, addressing the security vulnerability where simple data insertion could lead to malicious table drops. The critical concern is why a user needing only data insertion privileges possesses the permissions to restructure or remove tables. SQL systems provide extremely fine-grained controls, far more precise than those found in file systems or operating systems. These granular controls allow definition of privileges for creating/editing users, databases, and specific bits of data. When designing a database, one must determine the required user base and establish the minimum set of necessary privileges for each. Granting only a narrow set of privileges, such as merely the right to `SELECT` data, significantly reduces overall database risk. Sometimes, users require separate roles to ensure they only possess the expected permissions at specific points in time or through different access points.

The mechanism for granting privileges is straightforward, utilizing the command structure: `GRANT [privilege] ON [object] TO [user]`. For example, to create a read-only account, one would use `GRANT SELECT ON databases TO username`. If a user needs to add data but not restructure the table, a suitable privilege combination is `SELECT, INSERT`. Conversely, a powerful combination like `GRANT SELECT, INSERT, DROP` allows for table removal, illustrating the risk of excessive privileges. User creation itself requires the `CREATE USER [name] IDENTIFIED BY [password]` command, though plain text passwords are insecure. The database management system (DBMS) handles internal password encryption, and database management, being relational, is managed through tables.

A key modifier is `WITH GRANT OPTION`, a clause added to the `GRANT` command, allowing the user to pass their privileges on to other users. Privileges can be withdrawn using the `REVOKE` command, which shares the same syntax as `GRANT`. Roles offer an essential abstraction, allowing a generic set of privileges to be assigned without creating a permanent user account. For instance, an 'Astronomer' role might be created first, and then individuals are assigned that role using `GRANT astronomer TO username`. Roles are crucial for efficiently managing users who frequently switch between different operational sets of privileges. The core security principle is minimizing privileges—constraining user access limits the impact of both accidental errors and malicious actions. While playing around with databases, users often operate as a root user; in production systems, reducing privileges must be a core application design decision, not an afterthought.

---

## 06_Topic_3_summary_Video_2_min

# Topic 3 summary
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/LPn0s/topic-3-summary

The curriculum initiates the study of data management with an initial focus on working with data (Topics 1, Weeks 1-2) followed by a detailed exploration of Relational Databases (Topic 2, Weeks 3-4). Topics 3 (Weeks 5-6) delve into reliable database design, dedicating significant focus to Data Integrity and Security. A critical technical component of this section is the concept of ACID (Atomicity, Consistency, Isolation, Durability), which guarantees the reliability of the DBMS against errors, alongside intensive study of transaction processing and serialisation.

The curriculum then expands into practical applications, covering the use of databases through libraries and templating systems (Topic 4, Weeks 7-8). Following this, the focus shifts to more advanced RDBMS topics (Topic 5, Weeks 9-10), culminating in a mid-term assignment.

The later sections tackle scalability and modernization, covering Distributed databases and various alternative database models (Topic 6, Weeks 11-12). Further advanced concepts include Semantic databases (Topic 7, Weeks 13-14) and Linked Data principles (Topic 8, Weeks 15-16). The scope broadens again to include Multimedia and retrieval systems (Topic 9, Weeks 17-18).

The program concludes with practical application studies in various database applications (Topic 10, Weeks 19-20), preparing the student for the final examination. These advanced topics ensure a comprehensive understanding of modern data models, moving from simple relational structures to complex, distributed, and semantic architectures.

---

## 07_Further_reading_Reading_1h

# Further reading
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/hdvyG/further-reading

Chen, P. ‘The entity-relationship model – Toward a unified view of data’, ACM Transactions on Database Systems 1(1) 1976, pp.9–36. This reading is available via the Online Library . Further reading Chen, P. ‘The entity-relationship model – Toward a unified view of data’, ACM Transactions on Database Systems 1(1) 1976, pp.9–36. This reading is available via the Online Library . Mark as completed Dislike Report an issue

---

