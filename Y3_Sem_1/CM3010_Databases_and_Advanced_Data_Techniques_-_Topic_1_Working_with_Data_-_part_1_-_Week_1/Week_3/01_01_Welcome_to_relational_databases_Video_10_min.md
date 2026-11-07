# 01_Welcome_to_relational_databases_Video_10_min

# Welcome to relational databases
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/vUfuu/welcome-to-relational-databases

A relational database (RDB) implements the abstract concepts of the relational model. A "model," generally, is a method for abstracting complex real-world data into manageable structures that can be reasoned about. Specifically, in this context, the relational database utilizes tables as its high-level structural approach. A "relation" is essentially a precise definition of a table, encompassing the defined columns (attributes), the definition of what those columns mean, and all the values stored within. The core of the relational model is this combination of definition and stored values.

The relational model establishes strict rules for how these relations must be manipulated. Fundamentally, the first rule dictates that everything within the system must be represented as a relation. All operations within the model must request and operate over tables. Moreover, the system must handle not only the information itself but also information about the information, such as creating new tables, users, or restructing the database through relation manipulation.

For a system to truly implement the model, it must be a robust, abstracted system. This means functionality must remain consistent regardless of physical or software constraints, such as hardware replacement, operating system changes, or changes in disk formatting. Furthermore, if the data is distributed across a network, it must maintain the appearance of being concentrated in a single location.

The course will explore three primary models: the abstract relational model, the entity-relationship (ER) model, and SQL. The ER model is widely used for modeling concepts and data structures, frequently applied to relational databases. However, it is critical to note that the term "relation" in the relational model differs significantly from the term "relationship" used in an ER diagram.

The relational model itself is highly theoretical, yet it has almost never been purely implemented in practice. Instead, SQL (and its variant, Sequal) serves as a practical, partial implementation of the relational model. SQL is not strictly adherence to the abstract model, but its underlying theory is applicable to various RDBMS packages like MySQL, PostgreSQL, and SQLite. These database packages are close enough to SQL that they can possess many of the abstract properties of the relational model. The overall curriculum is structured to meet these concepts, starting with fundamental theory in Week 3 and moving into practical design and implementation using ER diagrams and Basic SQL in Week 2.1. The full scope of the material extends through topics covering data integrity, security, distributed databases, and semantic databases over the coming weeks.

