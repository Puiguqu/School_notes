# 06_Worksheet_Reliable_Databases_Data_Integrity_and_Security_(Topic_3,_Part_1)_Reading_10_min

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

