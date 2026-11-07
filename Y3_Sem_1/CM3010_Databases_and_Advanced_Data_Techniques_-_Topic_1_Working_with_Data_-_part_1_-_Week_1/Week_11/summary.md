# Week 11 - CM3010 Databases and Advanced Data Techniques - Topic 1: Working with Data - part 1 - Week 1

## 01_Introduction_to_distributed_databases_and_alternative_database_models_Video_4_min

# Introduction to distributed databases and alternative database models
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/KFI7R/introduction-to-distributed-databases-and-alternative-database-models

This course provides a comprehensive curriculum structured over 22 weeks, beginning with foundational knowledge on data management and working with data (Weeks 1-2). The initial modules delve into Relational Databases (Weeks 3-4), followed by critical topics concerning Data Integrity and Security in reliable databases (Weeks 5-6). These fundamentals build into practical application topics, including using databases via libraries and templating, and exploring Advanced RDBMS topics (Weeks 7-9). The program includes a Mid-term assignment in Week 10, signaling the transition to modern database architectures. Weeks 11-12 focus heavily on Distributed databases, covering Approaches to distributing RDBMS, and exploring alternative models such as Key/Value databases and MapReduce. The focus then shifts to advanced non-relational paradigms: Semantic databases (Weeks 13-14) and the implementation of Linked Data (Weeks 15-16). Further specialization is covered by studying Multimedia and retrieval (Weeks 17-18) and practical Database Applications (Weeks 19-20). The course culminates in Week 21 for preparation, leading to the final Exam week in Week 22.

---

## 02_Approaches_to_distributing_RDBMS_Video_15_min

# Approaches to distributing RDBMS
Video • 15 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/cmgBc/approaches-to-distributing-rdbms

Distributed databases, while relevant to the web era, are not new, with theoretical work on database distribution predating the web and existing even in the original requirements for relational database management systems. The core aspiration is that the user should perceive no difference between a distributed and a non-distributed system. Key architectural requirements include local autonomy, ensuring each site operates independently without relying on another for its basic operation. Furthermore, there must be no centralization, meaning no single site controls all transactions, which is crucial for reliable recovery. Continuous operation is another aspiration, requiring the system to be highly available and capable of quick, graceful recovery if it fails. Various independence requirements ensure usability, including location independence, where the user does not need to know the physical data location. Partition independence means data can be re-partitioned without affecting overall functionality, even though partitioning can be used for aggressive query optimization. Replication independence states that users should not need to know how data is duplicated or where the copies reside. A critical design principle suggests executing queries close to the data to minimize expensive data movement, leveraging the fact that generated results are typically smaller than the source data. Hardware independence allows the cluster to run on diverse hardware, and OS and network independence ensure smooth operation across different underlying systems. Heterogeneous systems also require support, theoretically allowing distribution across many different DBMSs.

Database distribution primarily involves partitioning, or fragmentation, where data and processing are divided across multiple nodes rather than having identical copies everywhere. Vertical partitioning involves breaking a table into sets of columns, such as splitting columns based on usage patterns or separating read-heavy data from write-heavy data. Horizontal partitioning is extremely common, where a single large table is split into smaller row-based tables across multiple nodes. Partitioning complexity is heightened by foreign key constraints, necessitating that relational metadata, including integrity constraints and catalog information, must also be distributed. Distributed systems require robust recovery control, often utilizing a two-phase commit protocol to coordinate transactions across nodes. This protocol guarantees transaction integrity but necessitates a coordinator, making the process inherently complex. The challenge of preserving ACID rules while maximizing parallelization leads to critical theoretical findings, notably Brewer's Conjecture. This conjecture outlines three essential goals: consistency (convergence to a valid state), availability (every request receives a response), and partition tolerance (continued operation during network failures). Brewer's Conjecture posits that these three goals cannot be fully satisfied simultaneously in all situations. Therefore, architects must prioritize these trade-offs, accepting that a distributed environment often requires compromising some of the strict guarantees inherent in traditional relational databases.

---

## 03_Distributed_database_trade-offs_gains_and_losses_Reading_1h_5m

# Distributed database trade-offs: gains and losses
Reading • 1h 5m - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/7DOf9/distributed-database-trade-offs-gains-and-losses

This text discusses Brewer's conjecture within the broader field of distributed technologies, focusing on the gains and losses associated with distributed database trade-offs. The specific technical paper referenced is Brewer, E.' CAP twelve years later: How the 'rules' have changed,' published in *Computer 45*(2) 2012, pp.23 –29. To access this reading on the IEEE page, users must click the blue 'Institutional Sign In' box and then search for 'University of London: Online Library.' If a user encounters a broken link, the technical instruction provided is to report the issue via the Student Portal.

---

## 04_Key_Value_databases_and_MapReduce_Video_18_min

# Key/Value databases and MapReduce
Video • 18 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/JiqQQ/key-value-databases-and-mapreduce

This curriculum begins by establishing foundational knowledge through Weeks 1-6, focusing on data handling, relational databases, and crucial topics of data integrity and security. Modules in Weeks 7-9 cover practical application, including the use of database libraries and templating, alongside an introduction to advanced RDBMS topics. The focus shifts significantly in Weeks 11-12 to distributed databases and alternative models, beginning with approaches to distributing traditional Relational Database Management Systems (RDBMS). A key technical deep dive covers alternative models like Key/Value databases, introducing concepts such as the MapReduce paradigm, exemplified by the work of Jeffrey Dean and Sanjay Ghemawat. Subsequent topics explore meaning-based structures, starting with Semantic databases (Weeks 13-14) and progressing to the utilization of Linked Data (Weeks 15-16). Weeks 17 and 18 address specialized data types, covering Multimedia and retrieval systems. The program concludes with Weeks 19-20 focused on real-world Applications and implementation. Assessments include a Mid-term assignment in Week 10, culminating in exam preparation and the final examination in Week 22.

---

## 05_Jeffrey_Dean_and_Sanjay_Ghemawat_introducing_MapReduce_Reading_50_min

# Jeffrey Dean and Sanjay Ghemawat introducing MapReduce
Reading • 50 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/CsVyA/jeffrey-dean-and-sanjay-ghemawat-introducing-mapreduce

The original article, 'MapReduce: a flexible data processing tool,' by J. Dean and S. Ghemawat, introduces the MapReduce algorithm and provides insightful commentary on Google's approach to 'big data,' published in Communications of the ACM 53 (1) 2010. This readable technical paper documents the core concepts of the tool designed for flexible data processing.

---

