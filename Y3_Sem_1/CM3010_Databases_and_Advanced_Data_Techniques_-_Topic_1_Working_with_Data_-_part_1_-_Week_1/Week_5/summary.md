# Week 5 - CM3010 Databases and Advanced Data Techniques - Topic 1: Working with Data - part 1 - Week 1

## 01_Introduction_to_data_Integrity_and_security_Video_5_min

# Introduction to data Integrity and security
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/wUarP/introduction-to-data-integrity-and-security

This curriculum progresses through foundational database concepts, starting with "Working with Data" (Weeks 1-4) and establishing the principles of Relational Databases. A significant focus is placed on data quality, covering "Reliable databases: Data Integrity and Security" (Weeks 5-6), specifically detailing the risk of errors and the application of "Normalisation and the normal forms." Subsequent modules explore system expansion, including "Using Databases: libraries and templating" (Weeks 7-8) and advanced RDBMS topics, culminating in a Mid-term assignment in Week 10. The course transitions to advanced modeling by addressing "Distributed databases and alternative database models" (Weeks 11-12), followed by specialized systems like "Semantic databases" (Weeks 13-14) and "Linked Data" (Weeks 15-16). Technical concepts are broadened further by incorporating "Multimedia and retrieval" (Weeks 17-18) and dedicated sections on general "Applications" (Weeks 19-20). The curriculum concludes with dedicated preparation and the final exam week (Weeks 21-22).

---

## 02_Integrity_and_the_risk_of_errors_Video_9_min

# Integrity and the risk of errors
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/lkL4H/integrity-and-the-risk-of-errors

The discussion centers on ensuring the reliability and maintaining the integrity of a relational database.
Previously, it was established that defining a `PRIMARY` or `UNIQUE KEY` ensures every row is identifiable and unique, thereby avoiding inconsistencies from duplicate data.
Furthermore, specifying a `FOREIGN KEY` imposes a range of integrity constraints, ensuring a reference remains maintainable across multiple tables.
This foreign key capability allows the database to police join constraints, throwing an error if a change would result in an incomprehensible database state.
Alternatively, a foreign key can automatically propagate changes, such as updating a planet's name in a `moons` table based on a change in the `planets` table.
Beyond keys, simple validation constraints can be specified to reject input data that does not match an expected pattern.
Crucially, these constraints only check for data *validity*, meaning the database maintains its logical consistency.
However, these checks do not verify the *truth* of the data; they only ensure the database can maintain consistency.
For instance, while a planet's surface area can be constrained to be non-nonsensical, its factual accuracy cannot be guaranteed.
Structural changes to reduce the risk of anomalies and errors fall under the broad concept of normalization.
An example of a data anomaly is demonstrated using a `planet's` table containing a `MoonCount` column.
If the count is stored directly, deleting a moon from the `moons` table will leave a discrepancy: the planet table will show three moons, but the moons table will only list two.
This stored redundancy necessitates users to manually reinforce constraints whenever one record is changed.
Normalization solves this by eliminating the redundant `MoonCount` column from the `planet's` table.
Instead, the moon count is retrieved using an aggregate function: `SELECT planet name, count stars, MoonName for moons, group by planet name`.
This aggregated value will always accurately reflect the current number of moons in the `moons` table, ensuring inherent consistency.
The text utilizes a real-world dataset of film locations in San Francisco to illustrate these challenges.
The example reveals that data distributed in a single table can suffer from variations and ambiguities.
For example, the same location is specified multiple times using slightly different texts, making it difficult to reconstruct films made at a single place.
Correcting a single factual error, such as the distribution year of *Ant-Man*, necessitates multiple changes to the table.
If these sequential updates fail, the database can be left in an inconsistent state.
The structural database designs aim to prevent such inconsistencies by enforcing integrity rules directly within the system.
The primary finding is that database normalization moves the responsibility of maintaining logical consistency from application software to the database structure itself.
This approach guarantees that if the underlying tables are accurate, the computed data derived from them will also be accurate.

---

## 03_Normalisation_and_the_normal_forms_I_Video_17_min

# Normalisation and the normal forms I
Video • 17 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/3fdUo/normalisation-and-the-normal-forms-i

This course progresses through essential data management concepts, beginning with foundational work in data handling (Weeks 1-2) and transitioning into the structure of Relational Databases (Weeks 3-4). A critical focus is placed on ensuring data quality through reliable databases, specifically covering Data Integrity and Security, which involves detailed study of Normalisation and the normal forms (Week 5). The course then explores the practical application of databases, moving into templating and library usage (Weeks 7-8) and advancing into specialized topics like Advanced RDBMS (Week 9). Subsequent weeks delve into modern database architectures, covering Distributed databases and alternative models (Weeks 11-12), Semantic databases (Weeks 13-14), and Linked Data (Weeks 15-16). Finally, the curriculum expands into complex retrieval methods, including Multimedia and retrieval (Weeks 17-18), Applications (Weeks 19-20), culminating in examination preparation and assessment.

---

## 04_Normalisation_and_the_normal_forms_II_Video_15_min

# Normalisation and the normal forms II
Video • 15 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/2EC4D/normalisation-and-the-normal-forms-ii

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

## 05_On_the_normal_forms_Reading_1h

# On the normal forms
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/CysdE/on-the-normal-forms

A gentle introduction (quite close to the lecture) is in the Database systems subject guide: Lewis, D. CO2209 Database systems. (London: University of London, 2016). normalisation.pdf PDF File The definition of the normal forms can be read here: Codd, E. 'A relational model of data for large shared data banks', Comms of the ACM 13(6) 1970, pp.377–87. This reading is available in the Online Library ....

---

## 06_Worksheet_Reliable_Databases_Data_Integrity_and_Security_(Topic_3,_Part_1)_Reading_10_min

# Worksheet: Reliable Databases: Data Integrity and Security (Topic 3, Part 1)
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/XA5NS/worksheet-reliable-databases-data-integrity-and-security-topic-3-part-1

This module investigates the fundamental question of database reliability: *what can possibly go wrong?*
It begins by surveying the main sources of error and damage within a database system.
These critical sources include bad data entering the system.
Other damages arise from poor application logic execution.
Failed database operations also pose a significant threat to integrity.
Finally, accidental or malicious user activity represents a major vector for corruption.
The module meticulously details the specific tools designed to mitigate each of these four identified threats.
The discussion then shifts to the structural reliability of the database itself.
This structural integrity is enforced through various integrity constraints.
Specific constraints covered are primary keys, unique keys, foreign keys, and check constraints.
These constraints enable the database system to effectively "police its own data."
A crucial technical distinction is made: integrity checks guarantee data *validity*, but they cannot guarantee *truth*.
The central concept of the module is normalization, a foundational process in database design.
Normalization involves breaking down a single, larger relation into smaller, specialized relations.
The primary goal of normalization is to prevent the repetition of information (data redundancy).
This ensures that the database system, rather than application code, maintains complete data consistency.
By the end of this module, students will be able to name the sources of database error and their corresponding mitigations.
Furthermore, participants will be able to explain the precise boundaries of what integrity checks guarantee and what they do not.
Technical proficiency includes reading and writing functional dependencies and correctly determining their direction.
Students will practice testing relations against various normal forms: 1NF, 2NF, 3NF, BCNF, and 4NF.
A key skill involves decomposing a relation into its appropriate normal form using Heath’s theorem.
The learning process is supported by a running example: a small public dataset of film locations in San Francisco, which will be normalized step by step.
Key database terminology includes 'Relation,' which is defined as a table or a set of tuples (rows).
An 'Attribute' corresponds to a column, and a 'Primary Key' is an attribute uniquely identifying every row.
The worksheet requires students to work activities in order, progressing from basic recall to multi-step decomposition, with an estimated time of approximately 60 minutes.

---

