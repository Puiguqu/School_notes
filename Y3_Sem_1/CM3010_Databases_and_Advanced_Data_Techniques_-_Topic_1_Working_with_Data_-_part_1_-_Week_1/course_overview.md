# CM3010 Databases and Advanced Data Techniques - Topic 1: Working with Data - part 1 - Week 1

## Table of Contents

- [Week 1](#week_1)
- [Week 11](#week_11)
- [Week 12](#week_12)
- [Week 13](#week_13)
- [Week 14](#week_14)
- [Week 15](#week_15)
- [Week 16](#week_16)
- [Week 17](#week_17)
- [Week 18](#week_18)
- [Week 19](#week_19)
- [Week 2](#week_2)
- [Week 20](#week_20)
- [Week 21](#week_21)
- [Week 3](#week_3)
- [Week 4](#week_4)
- [Week 5](#week_5)
- [Week 6](#week_6)
- [Week 7](#week_7)
- [Week 8](#week_8)
- [Week 9](#week_9)

## Week 1

### 01_Welcome_to_the_module_Video_4_min_Get_started

# Welcome to the module
Video • 4 min
Get started - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/ttBXG/welcome-to-the-module

This module, "Databases and Advanced Data Techniques," is designed to provide a practical, comprehensive understanding of data management and advanced data utilization. The course activities center on understanding data structure, modeling it, cleaning it for use, and mastering methods for storing, retrieving, and sharing data, particularly within databases.

A fundamental concept introduced is the nature of data modeling itself. When representing a real-world object digitally, the process is necessarily selective and inherently a distorting one. This representation is not objective; it functions as a product of both the real-world object being modeled and the specific preferences and biases of the modeler. This philosophy applies equally to the course design, which results from deliberate selections and points of view.

The instructor, David Lewis, specializes in Digital Musicology, a field within digital humanities. This specialization influences the course approach, noting that digital humanities data is typically smaller compared to data-heavy sciences like computational astronomy or bioinformatics. However, this data is more complex and nuanced than standard commercial e-commerce databases.

The data handled in digital musicology is characterized as varied, contingent, historical, and potentially ambiguous or incorrect. These data types are diverse, encompassing historical and social information, music recordings, music notation, video, and specialized sensor readings like heart rate and skin conductivity. The initial topic focuses on identifying what the data is, how to view it, and the resulting shapes it may take.

The module's technical roadmap covers a wide spectrum of database architectures and practices. The foundational learning begins with Week 1, focusing on working with data, including identifying data sources, linking them, and addressing licensing and ethical concerns.

The course progresses through core database theory, dedicating multiple weeks to Relational Databases (RDBMS). Following this, attention shifts to ensuring data quality through the critical topics of Data Integrity and Security within reliable databases. Practical application is taught through modules on using databases, libraries, and templating.

Advanced concepts are introduced in subsequent weeks, starting with Advanced RDBMS topics. The curriculum then moves into non-relational and distributed structures, covering Distributed Databases and alternative database models. This is followed by deep dives into specialized data frameworks.

Modules 13 and 14 cover Semantic Databases, which relate data based on meaning rather than just structure. Modules 15 and 16 focus on Linked Data, enabling the connection of diverse data sets. The course further addresses how to handle complex media through Multimedia and retrieval techniques. Finally, the module culminates with dedicated sessions on practical applications of these advanced database techniques.

---

### 02_Module_syllabus_Reading_10_min

# Module syllabus
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/c3dk2/module-syllabus

Databases and data services are foundational to the systems used in modern society. Each stage in the data process presents complex challenges. This process includes collecting, modelling, storing, filtering, and processing data. These challenges can be of technical, conceptual, methodological, and ethical nature. Students must engage with these challenges in a critically aware manner.

This module advances prior knowledge regarding data structures, data handling, and web technologies. It provides advanced techniques for computational data environments. The course focuses on developing critical thinking regarding how to approach and work with data. Key subjects include the use of relational databases. The course also explores alternative data approaches. These alternatives encompass NoSQL databases, XML, and Linked Data.

Furthermore, the module addresses crucial ethical dimensions. Participants will explore the ethics of gathering, processing, and sharing data. Security issues related to data must also be examined. Students will gain instruction on handling rich data sources. This includes strategies for working with text, audio, and video data.

Upon successful completion, students will achieve several specific competencies. First, they will be able to design and explain an appropriate data model. This includes utilizing both the entity/relationship model and the relational model. Secondly, they will learn how to implement a functional database within an SQL RDBMS. Thirdly, they will write effective SQL queries. These queries will specifically utilize indexes and joins for both reading and writing data.

Fourth, students will gain the ability to access full SQL database functionality. This functionality can be achieved from various programming languages. They will also build a simple web application to facilitate data reading and writing. Fifth, they will understand and explain the principles, forms, and commands specific to NoSQL databases. Sixth, they will explore different data modelling paradigms. This focus includes a deep dive into the Semantic Web and Linked Data concepts.

Seventh, students must be able to discuss critical issues surrounding data ethics and security. They must also apply this theoretical knowledge to practical, particular situations. Finally, they will understand the inherent challenges of working with text and media. They will also explain how existing systems overcome these specific data challenges.

---

### 03_Getting_started_on_this_module_Reading_10_min

# Getting started on this module
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/gVZEs/getting-started-on-this-module

The module team offers a warm welcome and encourages students to immediately familiarize themselves with the module structure and forthcoming tasks. Essential initial steps include reading the module syllabus and watching the dedicated module introduction video. Students must review the learning outcomes found within the syllabus to summarize the key knowledge and skills they are expected to demonstrate. Furthermore, a review of the assessment component in the syllabus is crucial to understand how the module can be successfully passed.

If a student is new to the Coursera platform, or wishes to deepen their understanding of success tools, the Orientation course is recommended for guidance. Throughout the program, three primary communication tools will be used: discussion forums, Slack, and Zoom. Detailed information regarding these three tools is provided within the Orientation course.

Students are advised to engage by saying "Hello" to classmates in the designated ‘Introduce yourself’ discussion forum. Before participating in the forums, guidelines on usage must be reviewed and essential rules followed, information found in the Orientation course.

The program provides extensive academic support resources, starting with the Online Library. A specific tutorial is available for the Online Library, offering a wealth of information and resources to aid studies.

Additionally, students will be introduced to Studiosity, a new online service currently being piloted by the University. This service is designed to support academic writing and offers additional help for any topics requiring a study refresher.

Regarding career development, the University of London Careers Service supports all students regardless of their current career status. This service is beneficial whether the student is a career starter, an experienced career developer, or someone looking to change their career path. Students are encouraged to read more about enhancing career prospects and the specific services provided by the University of London Careers Service via the Orientation course.

Aligning one's study with professional career goals is strongly emphasized to maintain motivation and ensure success. Students can begin exploring career opportunities by utilizing the Careers Connect platform. They are also encouraged to attend live, targeted BSc Computer Science careers webinars scheduled throughout the program.

For those classified as a career starter, a dedicated video offers insights into developing and demonstrating work experience. Specific resources tailored for career starters are also made available for deeper exploration of this topic. The module team concludes by expressing hope that students enjoy the module and looking forward to their contributions.

---

### 04_Where_does_data_come_from_Video_6_min

# Where does data come from?
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/VuQgW/where-does-data-come-from

This curriculum outlines a comprehensive module focusing on advanced data techniques and database management, progressing systematically over 22 weeks. The initial segment (Week 1) establishes foundational knowledge through discussions on data sources, analyzing data characteristics, and the practical methods of using and linking diverse data sources. Crucially, this foundation incorporates ethical considerations, specifically covering licensing, sharing, and data ethics. Topics build upon this base, moving into the core structural concepts of Relational Databases (Week 3 and Week 4).

Weeks 5 and 6 introduce the critical concepts of reliable databases, delving deeply into data integrity and security protocols. Following this, the module shifts focus to practical implementation through the study of using databases via libraries and templating (Week 7 and Week 8). The progression then moves into specialized database theory, beginning with Advanced RDBMS topics in Week 9.

The mid-term assessment occurs in Week 10, marking the transition to more complex and modern database architectures. Weeks 11 and 12 tackle Distributed databases and alternative database models, exploring systems that operate across multiple locations. This is followed by an exploration of Semantic databases in Weeks 13 and 14, focusing on knowledge representation.

The module then covers interoperability through Linked Data in Weeks 15 and 16. Further specialization occurs with the examination of Multimedia and retrieval systems (Week 17 and Week 18). The practical application of these concepts is addressed in Weeks 19 and 20, focusing on various system Applications.

The final weeks are dedicated to preparation, with Week 21 focused on exam readiness. The module concludes with the final examination in Week 22, completing the journey from basic data sourcing to advanced database model deployment.

---

### 05_What_does_your_data_look_like_Video_6_min

# What does your data look like?
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/MGDZv/what-does-your-data-look-like

The foundational principle discussed is that modeling real-life data for a database necessitates careful consideration of the data's eventual use and audience. External data sources are often ambiguous or incomplete because the required level of detail varies significantly among different user groups. Therefore, before inputting data into a database, one must define the intended purpose and the specific information required.

To illustrate this, the concept of encoding a book into a database is examined. A researcher focused on physical properties might need the book's weight, noting the example of a weight slightly over 500 grams. Conversely, a librarian concerned with physical storage needs the specific shelf height. An aesthetic user might only care about observable features, such as the book being red and having a red spine.

The necessity of varying data representation is highlighted through the title itself. For simple shelf retrieval, the short title "gardener's calendar" suffices. However, for academic comparison with other editions, the longer, more extensive title, "Every Man His Own Gardener," is necessary.

Further metadata points include recording authors; the title page listed Thomas More and John Abercrombie. It is noted that sometimes one author's name, like Thomas More, serves primarily as a marketing element, referencing his role as a gardener to the Duke of Leeds. Date and edition are critical details, specifically noting the 1803 publication date and the fact that it was the 17th edition.

Ultimately, even the deep content of the book, such as observations on pruning fruit trees, holds valuable information for a specialized historian. This underscores the key finding that differing user interests dictate the exact shape and content of the represented data.

The accompanying course structure outlines a comprehensive curriculum spanning 22 weeks. Week 1 focuses on "Working with Data - part 1," covering data sources, linking data, and ethical considerations regarding licenses and sharing. Subsequent weeks progress systematically through advanced database topics. Weeks 3 and 4 cover Relational Databases, followed by Weeks 5 and 6, which address Data Integrity and Security.

The curriculum introduces practical application in Weeks 7 and 8, utilizing libraries and templating methods. Advanced system architecture is explored in Week 9 with Advanced RDBMS topics. Week 11 and 12 delve into Distributed databases and alternative database models. The study then shifts toward advanced knowledge structures, covering Semantic databases in Weeks 13 and 14.

Further complexity is introduced through Linked Data (Weeks 15 and 16) and Multimedia and retrieval (Weeks 17 and 18). The final weeks concentrate on Applications (Weeks 19 and 20) before exam preparation. The module utilizes a structured format, incorporating Videos, Reading materials, Quizzes, and Practice Assignments. Technical navigation aids are provided for accessibility, including keyboard shortcuts (e.g., H, J, K, L for screen readers) and controls like CTRL + S. A significant milestone in the course is the Mid-term assignment scheduled for Week 10.

---

### 06_Bringing_data_sources_together_Reading_30_min

# Bringing data sources together
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/ijIGZ/bringing-data-sources-together

The Linked Jazz project is a resource dedicated to publishing and connecting comprehensive information about jazz musicians. Its primary function is to enrich the historical exploration of jazz by synthesizing data from multiple sources. This methodology specifically utilizes information from various databases, including Wikipedia, to broaden the scope of historical study. The material itself is presented as a short news article located on the official Pratt Institute website. The academic source is cited as The Pratt Institute, published in 2020. The core concept emphasized by the reading is how mapping relationships between jazz musicians elevates unsung histories. Finally, the document includes a technical instruction for users, directing that any broken link should be reported via the Student Portal.

---

### 07_Licenses,_sharing_and_ethics_Video_10_min

# Licenses, sharing and ethics
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/8lLnG/licenses-sharing-and-ethics

This curriculum outlines a comprehensive 22-week module on advanced data techniques and database management. The initial phase, Week 1, Topic 1, introduces "Working with Data - part 1," covering the origins of data, utilizing and linking diverse data sources, and addressing critical concerns like licenses, sharing, and ethics. Week 2 completes this initial stage with "Working with Data - part 2."

The focus shifts substantially in Weeks 3 and 4 to "Relational Databases - part 1 and part 2," establishing the foundational principles of structured data management. Building on this foundation, Weeks 5 and 6 introduce "Reliable databases: Data Integrity and Security," detailing necessary measures to ensure data robustness.

The progression continues in Weeks 7 and 8 by exploring "Using Databases: libraries and templating," moving from theoretical integrity to practical implementation. Week 9 covers advanced concepts related to Relational Database Management Systems (RDBMS), titled "Advanced RDBMS topics - part 1."

The curriculum then addresses scalability in Weeks 11 and 12 through the study of "Distributed databases and alternative database models - part 1 and part 2." Subsequent advanced topics include Week 13 and 14 on "Semantic databases - part 1 and part 2."

Further specializing in data connectivity, Weeks 15 and 16 are dedicated to "Linked Data - part 1 and part 2." Topics 9 and 10 focus on retrieval and application. Week 17 and 18 cover "Multimedia and retrieval - part 1 and part 2," while Weeks 19 and 20 address "Applications - part 1 and part 2."

Mid-term assessment occurs in Week 10, leading into Week 21, which is dedicated to preparation for the final exam. The course concludes in Week 22 with the official examination period.

---

### 08_Licensing_Reading_1h

# Licensing
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/9PDys/licensing

Decisions about whether your data will be proprietary or open are often taken at an institutional level. Research funding bodies, normally require your data to be open, and many governments and their agencies have similar restrictions. Whichever way these decisions go, the exact nature and terms of the license can have a significant impact on the legal re-use of your data. The Ball article summarises some of the issues, the advantages and the disadvantages of different licenses for open data....

---

### 09_Worksheet_Working_with_Data_(Topic_1,_Part_1)_Reading_10_min

# Worksheet: Working with Data (Topic 1, Part 1)
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/tQkHk/worksheet-working-with-data-topic-1-part-1

This module, Topic 1: Working with Data, provides a practical examination of data management. The module structure encompasses understanding data structure, obtaining and cleaning it, storing and retrieving it, and finally, using and sharing it. This specific worksheet deepens the focus on several critical areas within data handling. Specifically, it addresses the origins of data and how the intended use dictates the structure of the data model. Furthermore, the worksheet investigates the legal and ethical considerations that arise when data is reused or repurposed. A simple example, such as a book, illustrates this dependency effectively. An online retailer, for instance, might prioritize the book’s weight. Conversely, a librarian may be interested only in the book’s shelf height. A historian, however, would likely focus heavily on the book's actual content. By completing this worksheet, the student is expected to achieve several specific competencies. These objectives include the ability to classify various data sources. Students must also be able to select appropriate data fields tailored to different user needs. Another key skill is the capacity to thoroughly evaluate any external data source before use. Finally, the module requires learners to critically weigh the arguments for and against the use of open data. The terminology introduced is crucial for navigating these data processes. A fundamental concept is the definition of a data source itself. A data source refers simply to where the data originates: whether it is new, pre-existing, or external. New data is defined as data created or entered specifically for a new system, whether done incrementally or in a large batch. Pre-existing data is information the organization already holds, often within a legacy database or spreadsheet. Legacy data is a specialized type of pre-existing data, characterized as older information kept from previous systems or past working methods. External data is data provided by an entity outside the immediate organization. This external supply could be sourced, bought, or simply found. The process of bulk data entry involves inputting a substantial volume of data all at once. This is frequently done using methods like crowd sourcing or paid staff input. Extraction describes the method of getting data out of an older system into a more usable format. Conversion is the process of transforming data into a form that successfully meets new system requirements. This content is part of a worksheet estimated to take approximately 60 minutes to complete. The instructional material emphasizes working through the activities sequentially. Learners are encouraged to make a genuine attempt at the activities before consulting the provided answers.

---

## Week 11

### 01_Introduction_to_distributed_databases_and_alternative_database_models_Video_4_min

# Introduction to distributed databases and alternative database models
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/KFI7R/introduction-to-distributed-databases-and-alternative-database-models

This course provides a comprehensive curriculum structured over 22 weeks, beginning with foundational knowledge on data management and working with data (Weeks 1-2). The initial modules delve into Relational Databases (Weeks 3-4), followed by critical topics concerning Data Integrity and Security in reliable databases (Weeks 5-6). These fundamentals build into practical application topics, including using databases via libraries and templating, and exploring Advanced RDBMS topics (Weeks 7-9). The program includes a Mid-term assignment in Week 10, signaling the transition to modern database architectures. Weeks 11-12 focus heavily on Distributed databases, covering Approaches to distributing RDBMS, and exploring alternative models such as Key/Value databases and MapReduce. The focus then shifts to advanced non-relational paradigms: Semantic databases (Weeks 13-14) and the implementation of Linked Data (Weeks 15-16). Further specialization is covered by studying Multimedia and retrieval (Weeks 17-18) and practical Database Applications (Weeks 19-20). The course culminates in Week 21 for preparation, leading to the final Exam week in Week 22.

---

### 02_Approaches_to_distributing_RDBMS_Video_15_min

# Approaches to distributing RDBMS
Video • 15 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/cmgBc/approaches-to-distributing-rdbms

Distributed databases, while relevant to the web era, are not new, with theoretical work on database distribution predating the web and existing even in the original requirements for relational database management systems. The core aspiration is that the user should perceive no difference between a distributed and a non-distributed system. Key architectural requirements include local autonomy, ensuring each site operates independently without relying on another for its basic operation. Furthermore, there must be no centralization, meaning no single site controls all transactions, which is crucial for reliable recovery. Continuous operation is another aspiration, requiring the system to be highly available and capable of quick, graceful recovery if it fails. Various independence requirements ensure usability, including location independence, where the user does not need to know the physical data location. Partition independence means data can be re-partitioned without affecting overall functionality, even though partitioning can be used for aggressive query optimization. Replication independence states that users should not need to know how data is duplicated or where the copies reside. A critical design principle suggests executing queries close to the data to minimize expensive data movement, leveraging the fact that generated results are typically smaller than the source data. Hardware independence allows the cluster to run on diverse hardware, and OS and network independence ensure smooth operation across different underlying systems. Heterogeneous systems also require support, theoretically allowing distribution across many different DBMSs.

Database distribution primarily involves partitioning, or fragmentation, where data and processing are divided across multiple nodes rather than having identical copies everywhere. Vertical partitioning involves breaking a table into sets of columns, such as splitting columns based on usage patterns or separating read-heavy data from write-heavy data. Horizontal partitioning is extremely common, where a single large table is split into smaller row-based tables across multiple nodes. Partitioning complexity is heightened by foreign key constraints, necessitating that relational metadata, including integrity constraints and catalog information, must also be distributed. Distributed systems require robust recovery control, often utilizing a two-phase commit protocol to coordinate transactions across nodes. This protocol guarantees transaction integrity but necessitates a coordinator, making the process inherently complex. The challenge of preserving ACID rules while maximizing parallelization leads to critical theoretical findings, notably Brewer's Conjecture. This conjecture outlines three essential goals: consistency (convergence to a valid state), availability (every request receives a response), and partition tolerance (continued operation during network failures). Brewer's Conjecture posits that these three goals cannot be fully satisfied simultaneously in all situations. Therefore, architects must prioritize these trade-offs, accepting that a distributed environment often requires compromising some of the strict guarantees inherent in traditional relational databases.

---

### 03_Distributed_database_trade-offs_gains_and_losses_Reading_1h_5m

# Distributed database trade-offs: gains and losses
Reading • 1h 5m - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/7DOf9/distributed-database-trade-offs-gains-and-losses

This text discusses Brewer's conjecture within the broader field of distributed technologies, focusing on the gains and losses associated with distributed database trade-offs. The specific technical paper referenced is Brewer, E.' CAP twelve years later: How the 'rules' have changed,' published in *Computer 45*(2) 2012, pp.23 –29. To access this reading on the IEEE page, users must click the blue 'Institutional Sign In' box and then search for 'University of London: Online Library.' If a user encounters a broken link, the technical instruction provided is to report the issue via the Student Portal.

---

### 04_Key_Value_databases_and_MapReduce_Video_18_min

# Key/Value databases and MapReduce
Video • 18 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/JiqQQ/key-value-databases-and-mapreduce

This curriculum begins by establishing foundational knowledge through Weeks 1-6, focusing on data handling, relational databases, and crucial topics of data integrity and security. Modules in Weeks 7-9 cover practical application, including the use of database libraries and templating, alongside an introduction to advanced RDBMS topics. The focus shifts significantly in Weeks 11-12 to distributed databases and alternative models, beginning with approaches to distributing traditional Relational Database Management Systems (RDBMS). A key technical deep dive covers alternative models like Key/Value databases, introducing concepts such as the MapReduce paradigm, exemplified by the work of Jeffrey Dean and Sanjay Ghemawat. Subsequent topics explore meaning-based structures, starting with Semantic databases (Weeks 13-14) and progressing to the utilization of Linked Data (Weeks 15-16). Weeks 17 and 18 address specialized data types, covering Multimedia and retrieval systems. The program concludes with Weeks 19-20 focused on real-world Applications and implementation. Assessments include a Mid-term assignment in Week 10, culminating in exam preparation and the final examination in Week 22.

---

### 05_Jeffrey_Dean_and_Sanjay_Ghemawat_introducing_MapReduce_Reading_50_min

# Jeffrey Dean and Sanjay Ghemawat introducing MapReduce
Reading • 50 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/CsVyA/jeffrey-dean-and-sanjay-ghemawat-introducing-mapreduce

The original article, 'MapReduce: a flexible data processing tool,' by J. Dean and S. Ghemawat, introduces the MapReduce algorithm and provides insightful commentary on Google's approach to 'big data,' published in Communications of the ACM 53 (1) 2010. This readable technical paper documents the core concepts of the tool designed for flexible data processing.

---

## Week 12

### 01_Document_databases_and_MongoDB_Video_18_min

# Document databases and MongoDB
Video • 18 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/WYN9l/document-databases-and-mongodb

A key-value database and a relational database represent extreme ends of a database spectrum. While relational databases enforce rules via joints and integrity constraints, key-value databases simply store a key and a value, expecting rows to have no relational connection. Although this key-value approach is not universally ideal, giving up structural constraints allows for easier distribution of both data and processing. A middle ground between the complexity of relational models and the extreme simplicity of key-value pairs is the document-based database model. A "document" is a structure treated separately, similar to a row in a key-value store, but is far more complicated than a simple record. Document structures are typically less strictly controlled than relational tables, meaning columns and their required number are not rigidly prescribed. This flexibility allows for nested and deep data structures, which can effectively function as trees rather than tables. Furthermore, because the structure is not predefined, documents can repeat elements, a capability disallowed by strict relational constraints. Unlike the relations themselves, which are by definition unordered, document structures can be order-sensitive by default

---

### 02_Topic_6_Summary_Distributed_databases_Video_3_min

# Topic 6 Summary: Distributed databases
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/SdUv4/topic-6-summary-distributed-databases

This comprehensive database course begins with foundational concepts in Week 1-2, progresses through the core theory of Relational Databases in Week 3-4, and covers Data Integrity and Security in Week 5-6. Modules then transition to practical usage, exploring databases via libraries and templating (Week 7-8), followed by an advanced deep dive into RDBMS topics (Week 9) and a mid-term assessment in Week 10. The latter half of the course focuses heavily on advanced and alternative database models, starting with Distributed Databases (Week 11-12), which includes specific coverage on Document Databases and MongoDB (Week 12). Topics continue with Semantic Databases (Week 13-14) and Linked Data (Week 15-16), leading into Multimedia and Retrieval (Week 17-18) and practical Applications (Week 19-20). The course concludes with final preparation and the examination in Week 21-22.

---

### 03_Further_reading_Reading_1h

# Further reading
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/wD2Kq/further-reading

The text serves as a recommendation for users who wish to read in more depth following the completion of the current topic. It suggests an extended and detailed survey specifically covering MapReduce techniques. The article is noted for its ability to cover a wide range of ground while remaining accessible in its language. The key focus of this survey is the comprehensive analysis of MapReduce strengths and weaknesses. The recommended work was published in 2014. The authors responsible for this detailed survey are F. Li, B.C. Ooi, M.T. Özsu, and S. Wu. The article is titled, "Distributed data management using MapReduce." It was published in *ACM Computing Surveys*, specifically Volume 46, Issue 3, bearing Article 31. Readers can access the full text of this resource via the mentioned Online Library. This material is highly recommended for those seeking advanced knowledge on distributed data management.

---

## Week 13

### 01_Introduction_to_semantic_databases_Video_2_min

# Introduction to semantic databases
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/ZSjwV/introduction-to-semantic-databases

This document introduces the critical concepts of semantic databases and the broader field of semantics in data management. Traditional database systems often treat data as if it exists in a vacuum. In this conventional model, the meanings, structures, and relationships of the data are specified internally and solely for that particular database. However, much of the data utilized, such as names, weights, or dates of birth, is frequently represented across multiple external databases.

The core concept of semantic databases addresses this limitation by allowing common meanings to be shared more effectively. Semantic technology enables the communication of structures and information between disparate databases. This sharing capability overcomes the inherent awkwardness found in traditional database structures.

The overarching topic of semantic databases is systematically divided into two primary learning modules. The first module focuses specifically on XML and the associated technologies required for managing semantics. Following this, the second module delves into Linked Data and the application of the Semantic Web.

The curriculum is structured across various topics, starting with foundational data concepts in Week 1. Early topics cover working with data and the principles of Relational Databases (RDBMS) in Weeks 2, 3, and 4. Weeks 5 and 6 are dedicated to Reliable databases, focusing on Data Integrity and Security. Weeks 7 and 8 explore the practical application of using databases through libraries and templating.

Advanced RDBMS topics are covered in Week 9. Mid-term assessment is scheduled for Week 10. The study then transitions to Week 11 and 12, covering Distributed databases and alternative database models. The primary focus on the topic is situated in Week 13, marking the start of "Semantic databases - part 1."

Specific learning resources are assigned to support the technical understanding of semantics. The module "What are semantics? How can they be communicated?" is a key video resource. Complementary materials include practice assignments and quizzes designed to test conceptual knowledge. The discussion of XML is reinforced through specific video lessons and a dedicated discussion prompt.

The subsequent study of semantic databases continues in Week 14 with "Semantic databases - part 2." The course then proceeds into the second major area of study. Week 15 marks the beginning of "Linked Data - part 1," followed by "Linked Data - part 2" in Week 16.

Technical and data retrieval concepts are addressed in Weeks 17 and 18 with the topic "Multimedia and retrieval." Practical implementation examples and system applications are explored across Weeks 19 and 20. The latter stages of the course include Week 21 for examination preparation. The entire structure culminates with the final Exam week in Week 22. The instructional materials provide structured guidance, ensuring deep technical engagement with these complex data models.

---

### 02_Semantic_databases_What_does_a_table_actually_tell_us_Video_12_min

# Semantic databases: What does a table actually tell us?
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/FAJZu/semantic-databases-what-does-a-table-actually-tell-us

This course begins with foundational knowledge on **Working with Data** (Weeks 1-2), transitioning into the core concepts of **Relational Databases** (Weeks 3-4). The curriculum subsequently addresses database reliability through **Data Integrity and Security** (Weeks 5-6), followed by practical implementation techniques using libraries and templating (Weeks 7-8). Building upon these basics, the study delves into **Advanced RDBMS topics** (Week 9), culminating in a Mid-term assignment (Week 10).

The focus broadens in Weeks 11-12 to **Distributed databases and alternative database models**. A significant shift occurs in Week 13, introducing **Semantic databases** (Topic 7), which explores semantics, XML documentation, and understanding what a database table actually tells us, complemented by multiple practical assignments (videos and quizzes). This semantic focus continues through Week 14, followed by the dedicated study of **Linked Data** (Weeks 15-16).

The final major technical areas include **Multimedia and retrieval** (Weeks 17-18) and practical **Applications** (Weeks 19-20). The course concludes with comprehensive preparation and the final examination week (Weeks 21-22).

---

### 03_Shared_meaning_in_the_real_world_Video_5_min

# Shared meaning in the real world
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/0mQOj/shared-meaning-in-the-real-world

The core concept of communicating meaning, particularly in semantic databases and languages, is inherently paradoxical. This paradox arises because one attempts to specify a meaning—the intended message—using the very same language in which the information is being communicated.
Similar to how an English dictionary is written in English, defining terms requires a rich and complex vocabulary that often includes the word being defined.
Consequently, the definition of a semantic database or language often must be framed within the terms of that language itself, although this is not always the case in practice.
Semantics can be shared at various levels, including the sharing of documents themselves, which inherently carry and communicate meaning.
Ideally, documents should explicitly convey the set of semantics they employ, but this is not always mandatory for successful communication.
Formal specifications are essential to provide structure to documents, defining how they are constructed and interpreted.
Furthermore, human-readable definitions remain crucial, preventing information from being inconsistent even if the computer's semantics are perfectly defined.
The process of sharing meaning relies on the successful implementation of three critical elements.
These three required elements are: ways of reliably communicating the information itself.
Secondly, they require reliable methods for conveying structures and semantics in a format readable by a computer.
Thirdly, they mandate methods for communicating the structure and semantics, specifically the semantics, in a way that is accessible to humans.
These three elements enable the effective sharing and communication of meaning.
The technical implementation of this concept is illustrated by examples of structured documentation.
One example involves a STEM music notation attribute, where a specific attribute has a defined set of legal values or a choice list.
Beyond the list of options, human-readable documentation provides rules, such as defining that the value 'left' means the STEM on the line points left.
From this single foundational document, system rules for checking the validity of an encoding can be generated for the computer.
Simultaneously, human-readable documentation telling people how to properly encode the notation can be generated for human users.
Another key illustration is the PROV model, a W3 standard used by the provenance authority.
This model defines a class of entity, providing both a human-readable definition and practical examples.
A critical finding regarding documentation is the necessity of including examples within the human-readable definitions.
In the broader context of database studies, this material supports the deeper exploration of semantic databases (Weeks 13-14).
It also covers related advanced topics such as Linked Data (Weeks 15-16) and XML: Documents with semantics.
These concepts are interwoven with foundational database topics, including Relational Databases (Weeks 3-4) and Data Integrity (Weeks 5-6).

---

### 04_XML_Documents_with_semantics_Video_8_min

# XML: Documents with semantics
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/t5Xiv/xml-documents-with-semantics

The curriculum begins with foundational concepts, dedicating Weeks 1 through 4 to working with data and the principles of Relational Databases (part 1 and part 2). Following this, Weeks 5 and 6 address reliable databases, focusing specifically on Data Integrity and Security (part 1 and part 2). The practical application phase spans Weeks 7 to 9, covering the use of databases via libraries and templating (part 1 and part 2), culminating in an introduction to Advanced RDBMS topics (part 1). A Mid-term assignment is scheduled for Week 10, marking the course's first major assessment point.

The focus then shifts in Weeks 11 and 12 to large-scale architectures, exploring Distributed databases and other alternative database models (part 1 and part 2). Semantic databases form a major topic, starting in Week 13 and continuing in Week 14. The detailed unit on semantics includes specific learning elements: a 2-minute Introduction Video, a 12-minute "What are semantics?" Video, and associated quizzes. Furthermore, the semantic section mandates a detailed study of XML, including an 8-minute XML Video and a Discussion Prompt on applying XML.

The advanced concepts continue with Linked Data, covered across Weeks 15 and 16 (part 1 and part 2). Weeks 17 and 18 explore Multimedia and Retrieval, followed by the culmination of specialized knowledge in Weeks 19 and 20, addressing various Applications (part 1 and part 2). The course concludes with Week 21 dedicated to preparation for the final examination, which occurs in Week 22.

---

## Week 14

### 01_XML_versus_RDBMS_Video_4_min

# XML versus RDBMS
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/jLQt8/xml-versus-rdbms

The text primarily contrasts XML-based database technologies with Relational Database Systems (RDBMS), asserting that the comparison is "unfair" because the systems fulfill fundamentally different functions. The core difference lies in their data structure: XML organizes data as a tree that is characterized by a looser and less structured format. Processing XML requires traversing this tree, relying on external processing mechanisms rather than a predefined tabular schema. This inherent lack of rigid, upfront structure makes indexing more complex compared to RDBMS, often necessitating third-party indexing tools like Lucene applied to a transformed version of the data.

Despite indexing challenges, XML is highly amenable to parallelization from the beginning. Individual XML documents can be processed separately, allowing for heavy parallelization, even if a single file must be processed in a strict, left-to-right order. Crucially, the operations examined are side-effect free, enabling multiple operations to run simultaneously and the resulting data to be compiled linearly. Furthermore, XML files possess the capability of being directly shared and functioning as web links, something a typical relational database cannot inherently do.

The philosophical foundation of RDBMS, as introduced by Codd, aims to be a general-purpose, guaranteed, and effective system. Codd designed RDBMS in reaction to existing specialized and deductive databases, advocating for a simpler, more repeatable structure that maintains less prior knowledge about the data, believing this simplicity was more intuitive and provable.

The academic schedule details a comprehensive study of database models. Topics range from basic concepts (Week 1) through advanced RDBMS features (Week 9). The curriculum heavily covers distributed and alternative database models (Week 11 and 12). Specific technical modules include semantic databases (Weeks 13 and 14) and Linked Data (Weeks 15 and 16).

Practical application is emphasized through modules like "Transforming XML: XML Pipelines" (16 min video) and dedicated studies on XML Schemata (26 min video). The course includes numerous practice opportunities, such as the "XML versus RDBMS quiz" and "Transforming concert data Lab." The structure is cumulative, leading to a major Mid-term assignment in Week 10 and culminating in the final examination in Week 22.

---

### 02_Transforming_XML_XML_Pipelines_Video_16_min

# Transforming XML: XML Pipelines
Video • 16 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/UFJDy/transforming-xml-xml-pipelines

This curriculum initiates with foundational principles in data management, covering the fundamentals of "Working with Data" in the initial weeks. The core focus shifts to Relational Databases (RDBMS), detailing their structure and the critical concepts of Data Integrity and Security. Practical database usage is explored, including the implementation of libraries and templating, followed by advanced RDBMS topics. A significant technical transition occurs with the detailed study of XML, moving beyond traditional relational structures. This involves understanding the contrast between XML and RDBMS, utilizing XML pipelines for data transformation, and defining precise XML Schemata for structured data. Further complexity is introduced by exploring Distributed databases and Semantic databases, which model data across multiple systems and integrate specialized knowledge, respectively. Later modules focus on advanced data modeling, particularly through the implementation of Linked Data. Additionally, the curriculum addresses "Multimedia and retrieval," covering how diverse data types are managed and accessed. These topics culminate in practical "Applications" of these various database paradigms. Throughout the course, students engage in hands-on assignments, including XML transformation labs and schema discussions. The latter weeks involve preparation for the final exam, solidifying knowledge across all database models studied. Ultimately, the course provides a comprehensive overview of modern data architecture, from basic relational systems to complex distributed and semantic models.

---

### 03_XML_Schemata_Syntax_and_semantics_for_XML_Video_26_min

# XML Schemata: Syntax and semantics for XML
Video • 26 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/DG1M8/xml-schemata-syntax-and-semantics-for-xml

This lecture provides an overview of various sophisticated language standards used for defining the structure and rules (schemas) of data, moving beyond basic Document Type Definitions (DTDs).

Here is a summary of the key concepts:

### 1. Defining Data Structure and Order
The lecture first establishes that schemas define the expected structure of data. When dealing with complex types, such as sequences, schemas can specify not only that elements must be present, but also the **strict order** in which they must appear (e.g., Location $\rightarrow$ Venue $\rightarrow$ Date $\rightarrow$ Time).

The concept of **multiplicity** is introduced, allowing fine-grained control over the number of occurrences—such as specifying that at least one concert must exist, or that there can be an unlimited number of concert entries.

### 2. Relax NG (Next Generation Schema)
Relax NG is presented as a more intuitive alternative to traditional XML Schemas. Its philosophy is to leverage the fact that the language itself is based on tree structures. Instead of merely enforcing element presence, Relax NG allows for a more graphical and conceptual representation of the data tree, making the structure easier to visualize.

### 3. SchemaTron (Rules and Patterns)
SchemaTron is discussed as a fundamental shift from traditional schemers. While other languages primarily concern themselves with the **presence or absence** of an element, SchemaTron is focused on enforcing **patterns and arbitrary rules**.

*   **Integrity Checks:** It uses XPath for pattern matching and retrieval. This allows the schema to perform "integrity checks" (analogous to SQL constraints). For instance, a rule can assert that a concert date within the data must always be less than the current date, ensuring the database contains only past or future announcements, but never a date in the far future.
*   **Business Logic:** These rules operate at a high level, representing "business language" (e.g., "No product can have negative stock numbers"), making them more powerful than simple structural validation.

### 4. The Meta-Schemer: ODD
The lecture concludes by introducing **ODD (Open Document Definition)**. ODD is presented as a meta-schema language—a "super set"—designed to solve the problem of having many similar schema languages (like Relax NG, XML Schema, and SchemaTron). ODD allows developers to define a set of high-level meta-rules that can then be compiled into any of the specific schema languages, providing a powerful framework for data standardization.

***

**In essence, the lecture demonstrates an evolution in data validation:**
*   **DTD/Basic Schemas:** Focus on *structure* (Is the element here? Is it in the right order?).
*   **Relax NG:** Focuses on *intuitive structure* (How does the tree look?).
*   **SchemaTron:** Focuses on *meaning and integrity* (Does this data make sense according to business rules?).
*   **ODD:** Focuses on *unification* (How can we build a common standard for all of these?).

---

### 04_Not_just_text_markup_XML_and_Music_Video_13_min

# Not just text markup: XML and Music
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/fKEY0/not-just-text-markup-xml-and-music

This course provides a comprehensive exploration of data management, beginning with foundational concepts in working with data (Weeks 1 and 2). The study then transitions into Relational Databases, covering fundamental principles, and subsequently focuses on guaranteeing data integrity and security in reliable systems (Weeks 3 through 6). Practical database usage is detailed through libraries and templating, leading into an examination of advanced RDBMS topics (Weeks 7 and 9).

A major section is dedicated to XML, contrasting it with RDBMS structures, and detailing the use of XML Pipelines for data transformation, exemplified by concert data (Weeks 7.2, 7.3). Crucial technical study involves XML Schemata, which govern the syntax and semantics of XML markup, and their application in specialized contexts like TEI documentation and music data (Weeks 7.3). The course expands beyond structured data into modern paradigms, introducing Distributed databases and alternative models, including Semantic databases (Weeks 11 through 14).

The curriculum then advances to cutting-edge data concepts, focusing on Linked Data structures (Weeks 15 and 16). The final thematic unit addresses Multimedia and retrieval systems, alongside real-world applications of these complex data models (Weeks 17 through 20). This detailed progression culminates in final application topics and preparation for the comprehensive examination (Weeks 21 and 22).

---

### 05_Topic_7_summary_Video_3_min

# Topic 7 summary
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/FppeD/topic-7-summary

XML (eXtensible Markup Language) is presented as a highly successful technological framework. It forms the foundational basis for several major file formats. Notably, XML underpins Microsoft Office file formats such as XLSX and DOCX. Furthermore, it is integral to various web formats and complex academic encoding formats. These academic formats include TEI and MEI. XML has become crucial for scientific databases, which are frequently realized as XML databases. These databases can be supported by specialized XML database management systems like eXist. Data transformations using these systems can be performed using established technologies like XSLT or XQuery. Consequently, XML is deeply embedded in industrial and research computing environments. Simultaneously, it has found widespread adoption among personal desktop users in homes.

The primary advantage of XML is the shared semantics it enables, which is described as "monumental." XML provides a higher degree of shared meaning compared to previous file formats. In contrast, data shared in CSV formats often lacks even basic definitions of the underlying relational columns. XML formats solve this problem by allowing users to communicate schemas online. They permit the sharing of database definitions, along with essential structures like foreign key relations. XML also allows the explicit sharing of integrity constraints, enhancing data reliability.

However, the text identifies a specific limitation in XML's utility regarding semantic depth. XML rarely facilitates the sharing of smaller, nuanced units of meaning between unrelated databases. For instance, linking the concept of "people" from a movie database to the semantic structure used in an employee database is challenging. Furthermore, the concept of reusing geolocation structures from a mapping database across different applications is complicated.

To overcome this limitation and achieve deeper semantic sharing, the discussion points toward the need for Linked Data. Linked Data and the Semantic Web represent the next critical conceptual evolution in data management. The course outline emphasizes this progression, covering Semantic Databases in Weeks 13 and 14. The structure of the curriculum progressively builds knowledge toward this solution. Early topics involve working with data (Weeks 1-2), followed by a deep dive into Relational Databases (Weeks 3-4). The need for reliable data leads to examining Data Integrity and Security (Weeks 5-6).

The focus then shifts to practical implementation using XML, starting in Week 7. Detailed technical modules address the comparison between XML and RDBMS. Subsequent sections specifically cover XML Schemata, detailing their syntax and semantics for robust data modeling. Practical skills are emphasized through assignments like "Transforming XML: XML Pipelines," which utilize XML transformations. Further technical study covers how XML applies to specialized domains, including non-textual markup like music (e.g., the "Not just text markup: XML and Music" video). The journey concludes by exploring Distributed Databases and Alternative Database Models (Weeks 11-12), culminating in the advanced application of Linked Data (Weeks 15-16). The entire framework provides a complete roadmap from structured data storage to sophisticated semantic knowledge representation.

---

### 06_Further_reading_Reading_1h_30m

# Further reading
Reading • 1h 30m - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/q1DL5/further-reading

For an industrial overview of XML and its relationship to RDBMS, the conference paper "A decade of XML data management: An industrial experience report from Oracle" by Hua Liu, Z. and R. Murthy is recommended. This study was presented at the 2009 IEEE 25th International Conference on Data Engineering, and it can be found on pp.1351-1362. For general guidance on utilizing XML technologies, O'Reilly offers a substantial selection of reference books and primers. Shifting focus to the humanities, the Music Encoding Initiative (MEI) is covered in depth by Crawford and Lewis. Their article, "Music encoding initiative," was published in the Journal of the American Musicological Society, specifically in 69(1)2016, on pp.273-285. Detailed technical information regarding MEI is available on the official Music Encoding Initiative's website. Users should note that if this link is broken, feedback can be provided via the Student Portal. Both of these referenced articles can be searched and accessed through the Online Library.

---

## Week 15

### 01_Introduction_to_Linked_Data_and_the_Semantic_Web_Video_9_min

# Introduction to Linked Data and the Semantic Web
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/MWlQe/introduction-to-linked-data-and-the-semantic-web

This course provides a comprehensive exploration of data management, beginning with foundational concepts in working with data (Weeks 1-2) and progressing through the structure of Relational Databases (Weeks 3-4). Key security and robustness concepts are covered in Topic 3, focusing on Data Integrity and Security within reliable databases (Weeks 5-6). The curriculum transitions into practical application, addressing how databases are used via libraries and templating (Weeks 7-8) and delves into Advanced RDBMS topics (Week 9).

A major shift occurs with the study of modern infrastructure, covering Distributed databases and alternative database models (Weeks 11-12). The focus then pivots to highly abstract structures with the study of Semantic databases (Weeks 13-14).

Topics 8 and 16 specifically introduce Linked Data and the Semantic Web, initiating the deep dive into graph-based data models. This section emphasizes RDF (Resource Description Framework) as the foundational model and its various serializations, facilitating thinking in graphs. To achieve semantic meaning in Linked Data, the course utilizes Web ontologies, providing modules on choosing, designing, and evaluating these complex models.

The later stages continue this theme by covering Linked Data in depth (Week 16) and expanding into broader applications, including Multimedia and retrieval (Weeks 17-18) and various real-world Applications (Weeks 19-20). The course culminates in preparatory phases and the final Examination.

---

### 02_Open,_Linked_and_Data_Video_6_min

# Open, Linked and Data
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/OiUL0/open-linked-and-data

The presentation introduces the concept of the Semantic Web of semantics, focusing specifically on Linked Data and Linked Open Data. While the Semantic Web is a broad concept, Linked Data requires a precise understanding of three foundational terms: data, open, and linked. Defining data is initially left vague but the concept of "openness" is crucial for the overall discussion. Generally, open data implies cost-free access and the removal of barriers to use.

Openness further requires that the data must be findable, accessible in various ways, and restriction-free for reuse, often governed by specific licenses. An increasingly important set of criteria is the FAIR principles, adopted by international governmental organizations. FAIR stands for Findable, Accessible, Interoperable, and Reusable, providing an additional layer of requirement beyond simple openness.

The speaker explicitly distinguishes between these terms: data can be closed; data can be open but not linked (e.g., a static spreadsheet); and data can be linked but not necessarily open. The ideal state is Linked Open Data.

Linked data fundamentally relies on web links, specifically URLs, which have been central to web architecture since Tim Berners-Lee’s 1989 proposal. Early hypertext systems struggled because link integrity was difficult to maintain, as there was no centralized coordination.

A key innovation of the URL is that linking is one-way and does not require permission or input from the organization being linked to. This decentralized approach makes the system "Wild West" in nature, meaning links can break.

However, in Linked Data, the expectation is that linking occurs specifically at the URL level. URLs possess guaranteed uniqueness globally, which is a significant advantage over traditional database keys. The maintenance responsibility is clearly tied to the registering individual or organization associated with the domain name.

The use of shared identifiers (URLs) offers immense advantages for shared, distributed, web-scale databases. Specifically, these identifiers are unlimited in number, independent of hardware and software, and universally applicable. This robustness makes URLs extremely useful as unique keys for distributed data systems. This entire framework allows for the construction of linked open data.

---

### 03_Tim_Berners-Lee's_Proposal_inventing_the_web_Reading_1h

# Tim Berners-Lee's Proposal – inventing the web
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/Dkq8p/tim-berners-lees-proposal-inventing-the-web

Tim Berners-Lee's original proposal for the Web was submitted to his managers at the CERN particle physics laboratories. This document, titled 'Information management: A proposal', is described as fascinating and highly accessible. The text provides insight into how the burgeoning Web fit into the context of existing hypertext systems. Most critically, the proposal shows that Berners-Lee was thinking beyond the constraints of mere HTML. He advocated for a more comprehensive Web that utilized the power of Linked Data. The official source material is cited as: Berners-Lee, T. 'Information management: A proposal', CERN 1989, converted and republished by W3C. Users can access the material under the heading "Tim Berners-Lee's Proposal – inventing the web." Furthermore, users are advised to contact the Student Portal if the associated link is found to be broken.

---

### 04_RDF_the_model_and_its_serialisations_Video_26_min

# RDF: the model and its serialisations
Video • 26 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/OJCTr/rdf-the-model-and-its-serialisations

This course comprehensively covers database management, beginning with foundational skills in data handling (Weeks 1-2) and advancing into the structure of relational databases (Weeks 3-4). Key early topics include ensuring reliable database operations through detailed study of data integrity and security principles (Weeks 5-6). The curriculum then shifts to practical application, exploring how databases are utilized through libraries and templating, alongside advanced Real-World Database Management System (RDBMS) topics (Weeks 7-9). Subsequent modules tackle system architecture by introducing the concepts of distributed databases and alternative database models (Weeks 11-12). A major conceptual transition occurs with the study of semantic databases (Weeks 13-14), which lays the groundwork for modern interconnected data systems. The course dedicates significant time to Linked Data (Weeks 15-16), focusing on how information can be interconnected across the Semantic Web. Technical details are explored in depth through RDF: the model and its various serialisations, emphasizing the importance of thinking in graphs. Furthermore, the material delves into Web ontologies (Weeks 8.2), covering the design, evaluation, and utilization of structured knowledge representations. The syllabus also addresses multimedia and retrieval methods (Weeks 17-18), preparing students for diverse modern data applications (Weeks 19-20). The final segments involve preparation for the comprehensive exam (Week 21) and a dedicated focus on the underlying principles of RDF (Week 22). This progression moves from basic data manipulation through relational systems to advanced conceptual models like distributed and semantic data structures.

---

### 05_Thinking_in_graphs_Video_5_min

# Thinking in graphs
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/WeWqh/thinking-in-graphs

The discussion centers on the nature and complexity of working with graphs and graph diagrams in modeling abstract concepts. Some individuals find this abstract modeling liberating, while others find it intimidating due to its lack of concrete structure. Modeling begins by selecting a point in a semantic space, which is typically marked with a circle and a name. Initial simple relationships, such as "Film has cast member actor," are often oversimplified for complex real-world data. For instance, merely attaching a role to an actor's URI only provides a list of roles without connecting them to the specific film. A more complex structure is required, such as "Film has a role which is a character" and "That character is played by an actor." Furthermore, complex systems require even greater intricacy, such as differentiating between a young and an old version of the same character. A general rule advises utilizing existing structures developed by others, provided they are adopted critically.

Graphs differ fundamentally from structures like JSON and XML, which inherently possess a hierarchical tree structure. Crucially, graphs lack an inherent, fixed order. This lack of order is especially important in a web environment where graph components may arrive unpredictably from different servers or URLs. In graph theory, any combination of a circle, an arrow, and another circle constitutes exactly one triple. Once a graph is drawn, it can be easily translated into RDF serialization, which effectively stores all data. Extracting data involves counting the cycles and areas within the finalized graph structure.

Beyond the graph concept, the course structure details a comprehensive exploration of database models. Topics progress from Week 1 (Working with Data - part 1) through Week 6 (Reliable databases: Data Integrity and Security - part 2). This leads into Week 11 and Week 12, which focus on Distributed databases and alternative database models. A major shift occurs in Weeks 13 through 15, dedicated to Semantic databases and Linked Data.

Specifically, Section 8.0 introduces Linked Data and the Semantic Web, referencing Tim Berners-Lee's foundational proposal. Section 8.1 focuses on RDF, detailing the model and its various serializations, reinforced by activities like "Thinking in graphs." Finally, Section 8.2 delves into Semantics in Linked Data via Web ontologies. This area includes practical assignments on choosing, designing, and drawing ontologies, demonstrating the technical application of semantic web concepts.

---

### 06_Introduction_to_web_ontologies_Video_27_min

# Introduction to web ontologies
Video • 27 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/o7rgD/introduction-to-web-ontologies

This curriculum outlines a comprehensive study of data management, progressing from basic data operations to advanced semantic web technologies. The initial weeks focus on fundamental data handling, covering both data processing and the structure of traditional relational databases (RDBMS). Following this foundation, subsequent weeks address data robustness through topics in Data Integrity and Security within reliable databases.

The course then transitions to the practical application of databases, exploring how libraries and templating mechanisms facilitate database interaction. Advanced RDBMS concepts are covered, before introducing more modern architectures such as distributed databases and alternative database models. The focus shifts further toward semantic data management, starting with an introduction to Semantic Databases.

Central to the later modules is the concept of Linked Data and the Semantic Web, which aims to connect data across the internet. A key technical element introduced is RDF (Resource Description Framework), the model and its various serializations, often visualized as graphs. The utilization of Web Ontologies is crucial, providing the semantic framework necessary for machines to interpret data relationships.

Finally, the course covers practical applications and the retrieval of multimedia data. The curriculum concludes by exploring the integration of these sophisticated data models, culminating in specialized topics like Linked Data application, multimedia retrieval, and a comprehensive exam.

---

### 07_Choosing_ontologies_Linked_Jazz_and_other_performance-related_Linked_Data_Reading_1h

# Choosing ontologies: Linked Jazz and other performance-related Linked Data
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/uHnJG/choosing-ontologies-linked-jazz-and-other-performance-related-linked-data

This article explores the intricate process of choosing, combining, and extending ontologies, framing this complicated yet enjoyable endeavor. The research specifically details the stages involved in creating prototypes that aggregate musicological datasets on the semantic web. A key focus is placed on utilizing Linked Jazz and other performance-related Linked Data for these semantic implementations. The work provides helpful illustrations and graphs to walk through the complex stages of ontological development. The full technical findings are presented in the paper titled ' Building prototypes aggregating musicological datasets on the semantic web '. This research was conducted by Nurmikko-Fuller T., D. Bangert, A. Dix, D. Weigl, and K. Page. The article is published in *Bibliothek Forschung und Praxis*, Volume 42, Issue 2, in 2018, spanning pages 206-221.

---

### 08_Designing_an_ontology_Video_6_min

# Designing an ontology
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/T6XIA/designing-an-ontology

Designing a Web Ontology shares similarities with creating a relational database schema, often starting with an Entity Relationship model (ER model). However, Web Ontologies require extra care because they are highly exposed and can accidentally create industry standards. When utilizing external concepts, it is crucial to ensure the ontology is used in the manner it was originally intended. Ontology design and modeling must be undertaken with the foresight that other parties will utilize the resulting structures and data. Web Ontologies are significantly more explicit about various aspects than a simple database schema, requiring more nuanced decision-making. A fundamental best practice is to always review existing, external ontologies, as they represent a significant amount of prior expert effort. For collaborative projects, joining forces with others working on similar initiatives helps move towards generally useful outcomes. It is vital to test the ontology design using real data and workshop specific scenarios to validate functionality. A key principle is to avoid excessive detail, adhering to the rule: do not add detail you will not need fairly immediately. It is preferable to prioritize getting something done over achieving absolute completeness in the initial stages. Furthermore, it is better to be slightly over-general than to publish completely inaccurate data on the Web of Knowledge. Good ontologies require substantial time, often taking days of collaborative workshopping even within a small project. It is essential to gather multiple viewpoints and allocate sufficient time for thorough review of the completed structure. Visual aids, such as big whiteboards and large flip pads, are highly recommended to help nail down and formalize the concepts. The process demands explicitness to determine precise statements, enabling stakeholders to raise questions like, "We can't have that," or "We will have an exception." Once the basic design is complete, specialized tools can be used to formalize the structure. Protege is a notable free and open-source software tool designed by Stanford for specifying ontologies. A web-based version, WebProtege, allows users to register with Stanford and construct an ontology in a user-friendly manner. The final ontology is then exported in the OWL format. It is not generally necessary to construct a gigantic ontology entirely from scratch. Most practical projects involve a small amount of new ontology development combined with a large amount of selecting and importing established terms. The primary effort in implementation involves reviewing and integrating these pre-existing ontologies, not building them de novo. These practices support the broader goals of Semantic Databases and Linked Data, fundamental concepts in the Semantic Web.

---

## Week 16

### 01_Triplestores_and_SPARQL_Video_22_min

# Triplestores and SPARQL
Video • 22 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/gAiTd/triplestores-and-sparql

This course provides a comprehensive study of database management, beginning with foundational concepts in data handling (Weeks 1-2). It then progresses to detailed analysis of Relational Databases (RDBMS) in Weeks 3-4, followed by critical topics of Data Integrity and Security necessary for reliable database operation (Weeks 5-6). Practical application is introduced through utilizing databases via libraries and templating (Weeks 7-8), leading into an examination of Advanced RDBMS topics and a mid-term assessment (Weeks 9-10). The curriculum then explores complex architectures, covering Distributed databases and various alternative database models (Weeks 11-12). A major technical focus is placed on Semantic databases (Weeks 13-14), which enable complex meaning representation and logical inferencing. The study culminates with Linked Data (Weeks 15-16), specifically addressing Triplestores and the powerful query language, SPARQL. Linked Data techniques involve both internal graph database utilization and external methods, such as Dereferencing URIs and implementing Schema.org for SEO. Detailed resources include dedicated lessons on Triplestores and SPARQL, as well as prompts comparing SPARQL to SQL and exploring DBpedia. The final segments address Multimedia and retrieval (Weeks 17-18) and practical database Applications (Weeks 19-20). The course structure concludes with dedicated preparation time and the final comprehensive examination (Weeks 21-22).

---

### 02_Using_open_linked_data_Reading_1h

# Using open linked data
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/C1Ui2/using-open-linked-data

Carnegie Hall, the notable concert venue situated in New York, has made a significant data initiative public. Their archives have been released as Linked Open Data (LOD), allowing broad data access. Users can interact with this data through the defined endpoint at `http://data.carnegiehall.org/sparql/`. This release facilitates extensive exploration, detailed within the venue's accompanying blog and experimental discussions. One notable project highlighted is "Whose birthday is today?". This specific experiment showcases the power of data aggregation and visualization. The "Whose birthday is today?" feature leverages Wikidata's robust querying capabilities. It utilizes data visualization techniques to map composers and performers associated with Carnegie Hall. The mapping function dynamically plots individuals if the current date matches their birthday. Additional plots and supplementary examples are accessible on the same official site for review. Finally, users are encouraged to report any issues or broken links using the Student Portal mechanism.

---

### 03_Dereferencing_URIs_and_following_your_nose_Video_6_min

# Dereferencing URIs and following your nose
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/sZUtt/dereferencing-uris-and-following-your-nose

Sparkle serves as a powerful tool enabling the treatment of the linked data world as a unified database. It allows users to query a triple store specifically through a Sparkle endpoint. A key feature is the facility for federated queries, which addresses the need to combine information from multiple sources. These queries can simultaneously address various Sparkle endpoints, including those for Wikidata, local libraries, or commercial organizations. This capability allows the construction of worldwide-level queries across disparate datasets. However, the vast majority of linked data does not reside within triple stores. Furthermore, relatively few existing Sparkle endpoints support federated querying of their data. This limitation is often due to the significant costs and dependency risks associated with waiting for external endpoints. The barrier to publishing plain linked data is extremely low, meaning there are far more plain linked data publications than established Sparkle endpoints. Consequently, when dealing with real-world linked data, an alternative strategy must be employed. This alternative strategy is known as "follow your nose." Dereferencing is an extremely useful technique within linked data, though it is not a mandatory component. The concept starts with possessing a URI, which uniquely identifies a specific entity within a triple store. The process of dereferencing involves taking that URI and requesting the document found at the end of that address. The request is made as an HTTP request, allowing the user to specify the desired data types, such as RDF. If successful, the response will contain RDF data, presenting a large set of triples. Within these returned triples, the original URL serves as either the subject or the object, linking to numerous other URLs. To gain more information about these referenced objects, the process must be repeated. The subsequent action is to dereference those secondary URLs. This cycle of requesting the URL and receiving back RDF information is repeated continuously. This recursive iteration allows a local knowledge graph to be built based on the data discovered through traversal. This methodology is analogous to "chaining," which is the term used for the human practice of following links while browsing the web. In the linked data context, this method is termed "following your nose." This agent-based traversal builds local knowledge until the required information needed to resolve a specific query is obtained. This operational paradigm differs fundamentally from using SPARQL to perform an explicit query against a defined dataset. Nonetheless, any information gathered through dereferencing can be easily imported into a triple store for explicit inquiry later.

---

### 04_Schema.org_SEO_and_linked_data_Video_2_min

# Schema.org: SEO and linked data
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/hhRHl/schema-org-seo-and-linked-data

This curriculum is structured in 22 weeks, progressing from fundamental data management to advanced semantic and distributed database technologies. The initial phase covers core topics on Working with Data (Weeks 1 and 2), followed by a detailed study of Relational Databases (Weeks 3 and 4). This foundational knowledge is expanded in Weeks 5 and 6, focusing on critical aspects of Data Integrity and Security within database systems.

Practical usage is introduced in Weeks 7 and 8 via libraries and templating, advancing to specific Advanced RDBMS topics in Week 9. The study then shifts to modern architectures, examining Distributed databases and other alternative models in Weeks 11 and 12. Weeks 13 and 14 are dedicated to the concepts of Semantic databases, a key step toward intelligent data management.

A major focus of the course is Linked Data (Weeks 15 and 16), which is practically explored through Triplestores and querying using SPARQL, juxtaposed against standard SQL (8.3). Further technical detail covers Linked Data outside of a database, detailing Dereferencing URIs and the application of Schema.org for SEO (8.4). The final segments integrate these concepts by covering Multimedia and Retrieval (Weeks 17 and 18) and practical Applications (Weeks 19 and 20). The course concludes with preparation for the final exam in Weeks 21 and 22.

---

### 05_Topic_8_summary_Video_3_min

# Topic 8 summary
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/LZZmR/topic-8-summary

Linked data and semantic web technologies, despite their age, are still evolving and face challenges in scaling public datasets. A primary ongoing effort involves finding the best methods for sharing the fruits of labor, specifically in terms of ontologies and structured data. In 2007, the Linked Open Data Cloud had specific criteria for qualification. To join this graph, participants had to publish a defined amount of data and include external links to other data sources. DBpedia is noted as a significant example of an early adopter of this technology. Other quick participants included music-related projects such as Jamendo, MusicBrainz, and DBTune.

The graph has experienced massive expansion over time, moving beyond early initiatives like the American Census data of 2007. As of later versions, the graph shows major growth into specialized fields like sciences and biosciences, particularly in bioinformatics databases. Linguistics and governmental data represent other very large regional sections of the data graph. The structure has become immensely complex, evident in the 2021 graph which required thematic arrangement to manage the massive connections.

It is crucial to understand the distinction between data participation and data consumption. Many large organizations, such as Google and Facebook, utilize private graph databases but do not participate by publicly sharing their own data. This current representation highlights the public-facing scope of linked data applications. The field has been an incredible success, but significant technical challenges still exist before its potential can be fully realized.

The educational curriculum details this progression through various database models, including Relational, Reliable, and Distributed databases. A core focus is placed on Semantic databases and the specific methodology of Linked Data. The course delves into practical components, such as Triplestores and the query language, SPARQL. A comparison of SPARQL and SQL is presented to highlight the differences between graph-based and relational querying.

Furthermore, the learning structure covers how to work with data both inside and outside of a database environment. This includes understanding Dereferencing URIs and the process of "following your nose" through a data graph. Schema.org is specifically mentioned as a key tool linking linked data with Search Engine Optimization (SEO). These topics are integrated within a larger structure, including dedicated units on advanced RDBMS and multimedia retrieval. The curriculum progresses toward specialized application knowledge, leading up to the final exam preparation.

---

### 06_Further_reading_Reading_1h

# Further reading
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/8bYqN/further-reading

It is often useful to place Linked Open Data in a wider context of good practices for data management and sharing. This article gives a good overview of approaches to sustainable and repeatable science, and the place of Linked Data in that. Bechhofer, S. et al., 'Why linked data is not enough for scientists', Future Generation Computer Systems, 29(2) 2013, pp.599-611. A short, earlier conference paper relates Linked Data technologies to another important web publishing approach – REST....

---

## Week 17

### 01_Introduction_to_multimedia_databases_and_information_retrieval_Video_2_min

# Introduction to multimedia databases and information retrieval
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/DLU1A/introduction-to-multimedia-databases-and-information-retrieval

This curriculum progresses from basic data management principles, starting with fundamental topics on "Working with Data" (Weeks 1-2) before moving into the core concepts of Relational Databases (Weeks 3-4). Essential to robust systems, Weeks 5 and 6 focus on "Reliable databases," detailing critical concepts of Data Integrity and Security. Following the foundation, the course explores practical implementation (Weeks 7-8) and advanced structural topics, including Advanced RDBMS (Week 9) and distributed database models (Weeks 11-12). The curriculum then branches into specialized database paradigms, covering Semantic databases (Weeks 13-14) and Linked Data technologies (Weeks 15-16), emphasizing data meaning and interconnectivity. A significant portion is dedicated to handling complex data through "Multimedia and retrieval" (Weeks 17-18), discussing Information Retrieval and the use of features, exemplified by the functionality of Shazam. This knowledge is then applied in comprehensive "Applications" (Weeks 19-20), synthesizing all acquired technical details. The learning process is punctuated by a Mid-term assignment in Week 10 and preparation leading up to the final Exam in Week 22. Overall, the course provides a comprehensive journey from basic data handling to advanced distributed, semantic, and multimedia database architectures.

---

### 02_Information_retrieval_Querying_rich_data_Video_12_min

# Information retrieval: Querying rich data
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/6agMX/information-retrieval-querying-rich-data

Information retrieval faces several common and complex challenges, as demonstrated by the music playing system example. One primary issue is the ill-defined nature of the user's need or requirement, such as defining what constitutes "slow" or "quiet" music. Secondly, summarizing large data units presents difficulty, requiring task-dependent approaches for aggregation. For instance, a piece of music might contain one excellent sentence but be otherwise terrible, making an aggregate "good" descriptor inaccurate. Another challenge arises because highly expressive human needs may not be clearly reducible to a simple definition or a binary (yes/no) answer.

A third major problem is the distinction between local and global summary requirements. A simple yes/no answer might be possible for a small region of data, but answering the question at a higher, aggregate level necessitates knowledge of the user's underlying needs. Furthermore, information is often not explicitly present in the signal itself. For example, knowing a piece's tempo (e.g., 80 bpm) requires detailed data analysis, as there is no embedded data bit stating the speed.

Crucially, subjective information, such as a composer's origin or date (e.g., "1803" or "Viennese"), may not be contained in the sound signal whatsoever. These vagaries mean that answers are frequently subjective, and there is no absolute "oracle" to verify a user's correctness. These combined factors create a significantly different environment for designing and analyzing retrieval algorithms compared to traditional database systems.

Historically, Vannevar Bush's Memex addressed the limitations of early indexing systems. Bush noted that the inefficiency in locating records is often caused by the artificiality of structured indexing systems, such as filing alphabetically or numerically. Such over-structured systems fail to resemble the associative nature of the human mind. The human mind operates by snapping instantly between associated thoughts, creating an intricate web, or "semantic web."

Bush also highlighted that a human query is not easily translated into the strict relational operations common in structured data. The core idea of IR is that the user possesses an information need, which must be translated into a system-responsive query. The query is thus the only clue system designers have about the user's true information need.

The paradigm most often used in IR is the ranked list, not a set of equal results, unlike traditional SQL queries. In SQL, results are expected to be strictly true or false; in IR, results are ranked based on relevance. A retrieved document may satisfy the query's syntactic requirements but still fail to be relevant to the user’s actual information need. This suggests that the method used to elicit queries may not be perfectly suited to the user’s deep informational needs.

---

### 03_What_is_a_feature_Video_13_min

# What is a feature?
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/REYXl/what-is-a-feature

This curriculum systematically covers database management, beginning with foundational concepts in Week 1 and Week 2: "Working with Data." The focus then shifts to structured data models in Weeks 3 and 4, exploring Relational Databases, followed by critical concepts of reliability, integrity, and security in Weeks 5 and 6. Weeks 7 and 8 introduce practical database application using libraries and templating mechanisms.

The advanced stages begin with Week 9, covering sophisticated RDBMS topics, leading into the complex world of data architecture in Weeks 11 and 12, which address Distributed databases and alternative database models. Further specialization occurs in Weeks 13 and 14 with the study of Semantic databases, preceding Week 15 and 16 on Linked Data.

The later weeks transition to complex data types, detailing multimedia and retrieval in Weeks 17 and 18, including features for complex data and information retrieval mechanisms like Shazam. Finally, the course culminates in Weeks 19 and 20, focusing on practical applications before the preparation and final examination period.

---

### 04_Music_information_retrieval_in_practice_How_does_Shazam_work_Reading_1h

# Music information retrieval in practice: How does Shazam work
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/z5Usn/music-information-retrieval-in-practice-how-does-shazam-work

Music Information Retrieval (MIR) is defined as a broad and diverse discipline. It encompasses both industrial research initiatives and university-based studies. MIR occupies a somewhat distinct and atypical niche within the broader field of Information Retrieval generally. To provide context for this field, the text references two notably old but significant research papers. A prime example of MIR challenge is Shazam, which involves searching audio data based on an audio query. This task presented substantial technical difficulties, particularly given the constraints of 2003 hardware. Back then, servers possessed significantly less processing power than today. Furthermore, audio storage was much more costly, making the creation of large audio databases difficult to manage and search.

Shazam’s central selling point was its ability to recognize music captured by a mobile phone in a noisy public setting. This feature introduced several complex challenges to the system design. Key limitations included the poor sound quality inherent in mobile phone recordings. Mobile bandwidth constraints also posed a significant hurdle to effective data transmission. Processing power limitations on the mobile device further compounded the difficulty of the recognition task. The presence of distortions from ambient noise made robust audio detection exceptionally challenging.

For a detailed analysis of how Shazam solved this complex problem, the conference paper by Li-Chun Wang is recommended. This specific paper is titled "An industrial-strength audio search algorithm." It was presented at the 4th International Conference on Music Information Retrieval (ISMIR) in 2003. For researchers interested in user-related aspects of MIR, a later paper offers valuable insights. This paper, "The neglected user in music information retrieval research," was written by M. Schedl, A. Flexer, and J. Urbano. It appeared in the Journal of Intelligent Information Systems, specifically in issue 41/3, pp.523-539, in 2013. Readers may search for these articles using the provided Online Library resource. The text also instructs users to report any broken links via the Student Portal.

---

## Week 18

### 01_9.201_Feature_space_a_visitor's_guide_Video_10_min

# 9.201 Feature space: a visitor's guide
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/5b3jM/9-201-feature-space-a-visitors-guide

The core objective in utilizing features to address user information needs is to understand how various features can be combined and used within a conceptual framework known as feature space. This feature space is variable in structure, but it can be illustrated using simple examples, such as a two-dimensional feature space. In a two-dimensional space, each data point often represents a single document summarized across two numerical dimensions, such as tempo and loudness. For instance, this space could map music features to help users find slow, quiet tunes or fast, loud ones. Alternatively, the dimensions could represent average readability and book length to suggest suitable reading material for specific language learners.

Common machine learning applications in this feature space include clustering, where similarity is identified among data points even without a specific user query. Clustering groups entities that share common characteristics, allowing us to learn about the underlying data distribution. Another primary application is nearest neighbor search, where a user specifies a preference (e.g., "slow quiet music"), establishing a target point in the feature space. The system then ranks and presents the nearest $N$ points to this target, ordered by their distance from the query point. While the initial example is two-dimensional, the principle applies to feature spaces with arbitrary numbers of dimensions.

Feature representation evolves beyond simple individual points, especially when modeling changes over time, such as in timed media or progress through a book. In these cases, data forms trajectories, which are sequences of points mapping a feature against time, or across multiple dimensions. A single-dimension, time-based graph might show how a performance's tempo (the blue graph) accelerates and then slows, while another (the orange graph) decelerates. To assess similarity, one might compare not just numerical values, but the shapes or trends of these lines.

Expanding into multiple dimensions, time series are described not by a single axis, but by a set of vector points representing how an entity changes. For example, a time series might track both tempo (X-axis) and loudness (Y-axis) over sequential points, creating a trajectory of vectors. This allows for granular comparisons, such as comparing two performances of the same piece—one changing tempo, and another changing dynamics—by examining their entire trajectories.

A crucial technical detail is the requirement that features must be measurable and mappable to a quantitative space that supports notions of greater than or less than. Simple features, like word count or loudness, are easily quantifiable numbers. However, mapping abstract concepts requires careful consideration of how that space is structured.

The choice of mapping is critical, particularly when dealing with sensory data like audio. For instance, frequency (measured in Hertz) is continuous, but human perception often involves logarithmic scales, as constructed by our ears and brains. In Western classical music, frequency is often binned and mapped into a 12-tone sequence of pitches (e.g., C, C-sharp, D).

The raw physical frequency mapping often does not align with cultural or perceptual musical structures. For example, a pitch distribution derived purely from Hertz may look random, lacking discernible patterns for retrieval. However, if this space is remapped according to music theory, such as using a cycle of fifths, the data can become far more coherent.

This demonstrates that the choice of numerical space must be informed by a deep understanding of the features themselves. Developing an appropriate feature space is, therefore, the prerequisite step for effectively utilizing that feature space in retrieval and analysis.

---

### 02_9.203_Distances_and_similarity_in_feature_space_Video_12_min

# 9.203 Distances and similarity in feature space
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/yGilj/9-203-distances-and-similarity-in-feature-space

This course provides a comprehensive study of data management, beginning with fundamental concepts in working with data (Weeks 1–2). The curriculum then delves into relational databases (Weeks 3–4), followed by critical examination of data reliability through concepts of Data Integrity and Security (Weeks 5–6). Practical application of databases is covered through libraries and templating (Weeks 7–8) and advanced RDBMS topics (Week 9). The scope broadens significantly by addressing modern database architectures, including distributed databases and alternative models (Weeks 11–12). Furthermore, specialized database structures such as semantic databases (Weeks 13–14) and Linked Data principles (Weeks 15–16) are explored. Topic 9 focuses heavily on Multimedia and Retrieval, detailing feature retrieval in multiple dimensions within a defined feature space. Key technical concepts in retrieval include calculating distances and similarity within the feature space and understanding the issues of speed and indexing. Evaluation of search results is addressed through approximate matching, specifically utilizing Precision and Recall to measure system success (Sections 9.2 and 9.3). The course culminates with studying practical Applications (Weeks 19–20) and covering specific retrieval methods like Exotic distance measures. Assessment includes a Mid-term assignment (Week 10), leading up to the final Exam week (Week 22). The content is consistently supported by video lectures, practice assignments, and detailed reading materials, ensuring a holistic learning experience.

---

### 03_Issues_of_speed_and_indexing_Video_6_min

# Issues of speed and indexing
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/kZO9X/issues-of-speed-and-indexing

Information retrieval (IR) systems are fundamentally driven by user needs, requiring queries to efficiently satisfy the information need posed by the user. A critical operational concern for many IR systems is speed, especially when dealing with interactions involving timed media, like the Google paradigm of exploring large resource collections. To mitigate computational effort and improve retrieval speed, systems utilize precomputed features that function as indexes into vast and complex data.

These feature sets are often rich and complex, necessitating optimization strategies for efficient searching over large datasets. Since information retrieval often involves large numbers of disparate documents, these tasks are highly suitable for parallel processing. This suitability led to the development of technologies like Google’s MapReduce framework, which divides data and processing into manageable tasks.

When searching within a complex feature space, systems rely heavily on spatial indexes, particularly those operating within metric spaces. These metric spaces must obey specific mathematical observations: if distance is zero, the points are identical; distance must be symmetric (distance of X to Y equals Y to X); and the triangle inequality must hold. If these conditions are met, spatial indexes can achieve very fast retrieval times, often providing $log(n)$ performance. Structures such as R-trees are examples of spatial indexing utilized in SQL databases.

Optimization efforts include making the feature space well-behaved and reducing the number of dimensions in the feature set. Dimensionality reduction is valuable because irrelevant or non-salient data increases the risk of false positives. Furthermore, irrelevant data can corrupt the integrity of the distance metrics used for comparison.

However, some searches cannot be adequately addressed solely in feature space, requiring live operations directly on the data signal. For instance, complex domains like music notation search demand domain-specific algorithmic approaches. In these specialized areas, general rules are scarce, emphasizing the importance of deeply understanding both the specific domain and the nature of the data.

The scope of modern IR extends across various sophisticated data types, including relational, semantic, and linked data. Dedicated technical segments address the evaluation of system success using concepts like Precision and Recall, which measure the accuracy of retrieved results and the effectiveness of approximate matching. Retrieval also covers advanced topics such as multimedia and the analysis of exotic distance measures within feature space. Ultimately, successful IR relies on balancing speed optimization, complex indexing, and domain-specific knowledge.

---

### 04_Exotic_distance_measures_Reading_1h

# Exotic distance measures
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/cCeml/exotic-distance-measures

Many applications succeed using traditional metrics like Euclidean or Manhattan distance. However, certain fields, such as music notation, demand sophisticated methods for measuring similarity. Earth Movers distance, also known as Transportation Distance, is a specialized form of edit distance designed to address this complexity. Technically, it is characterized by its ability to apply different weights to varying points. This means the computational cost of a change is not uniform but varies depending on its location within the data structure. The Dutch Song Database specifically employs the Earth Movers distance metric for its analyses. This method is founded upon research and development conducted by Rainer Typke and his colleagues. Specifically, the seminal work was published in the 4th International Conference on Music Information Retrieval in 2003. The primary citation for this foundational work is Typke, R., Giannopoulos, P., Veltkamp, R. C., Wiering, F., and van Oostrum, R. These specialized measures have been further evaluated using the Dutch Song Database. Recent comparative studies contrasted Earth Movers distance with other measures, including the common Euclidean distance. The key finding of these later evaluations was that while Euclidean distance is functional, the specialist distance measures significantly outperform it. This is supported by research from Janssen, B., van Kranenburg, P., and Volk, A.

---

### 05_Precision_and_recall_measuring_success_Video_20_min

# Precision and recall: measuring success
Video • 20 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/5Pg2W/precision-and-recall-measuring-success

This course structure guides students through a comprehensive study of data management, moving from foundational concepts to advanced distributed systems. Initial weeks (Weeks 1–2) focus on "Working with Data," establishing the basic principles of data handling. Weeks 3 and 4 delve into Relational Databases, covering the core mechanics of these database systems. Subsequently, Weeks 5 and 6 address reliable databases, emphasizing crucial concepts like Data Integrity and Security.

The curriculum transitions in Weeks 7 and 8 to practical database usage, specifically exploring libraries and templating mechanisms for interaction. The focus expands further in Weeks 9–12, covering Advanced RDBMS topics and introducing Distributed databases and alternative database models. Following this, Weeks 13–16 explore sophisticated concepts, specifically Semantic databases and Linked Data, enabling richer data interpretation.

Weeks 17 and 18 are dedicated to multimedia and retrieval, where the specialized area of Feature retrieval is detailed in section 9.2. This includes defining the "Feature space," examining "Distances and similarity," and addressing "Issues of speed and indexing." A critical component of retrieval systems is covered in section 9.3, focusing on approximating matching and quantifying success through Precision and Recall. The final portion of the course (Weeks 19–22) applies these knowledge bases to practical Applications, culminating in an examination of multimedia retrieval.

---

### 06_Topic_9_summary_Video_2_min

# Topic 9 summary
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/avTgw/topic-9-summary

Information retrieval (IR) is recognized as a highly varied and mixed field, where perspectives often diverge depending on the domain focus. The speaker emphasizes that IR is deeply domain-specific, meaning that while common concepts like "query" and "user's information needs" exist, the underlying execution varies significantly. The challenge involves transforming raw, complex, and rich data into a processable format tailored to service a specific user need.

Handling various material types necessitates distinct approaches; for example, music or natural language is treated differently than a CV, a movie, choreographic planning data, or an architect's drawing. Success in IR requires specialized domain knowledge, which is crucial for understanding the user’s path from initial information need to the formulation of a query. A key technical challenge is navigating the "semantic gap"—the distance between the user's query statement and the underlying data features.

While the fundamental processes, stages, and some mathematical foundations of IR remain consistent, the sensitivity to the specific domain being addressed is vital for achieving successful retrieval. This academic framework is supported by a structured curriculum detailing advanced database and multimedia concepts.

The coursework begins by addressing fundamental data handling principles in Weeks 1 and 2. Subsequent topics focus on Relational Databases (RDBMS) in Weeks 3 and 4. Reliability is covered in Weeks 5 and 6, detailing Data Integrity and Security within databases.

Weeks 7 and 8 explore the practical application of databases, including libraries and templating techniques. Advanced RDBMS topics are covered in Week 9. The focus then shifts to scalable architecture, addressing Distributed databases and alternative database models in Weeks 11 and 12.

More specialized data models are examined subsequently, starting with Semantic databases in Weeks 13 and 14. Linked Data, a critical component for connecting disparate data sources, is covered in Weeks 15 and 16. The curriculum places significant emphasis on Multimedia and retrieval in Weeks 17 and 18.

Topic 9 specifically addresses Feature retrieval in multiple dimensions, introducing concepts like "Feature space: a visitor's guide" and "Distances and similarity in feature space." Furthermore, the methodology for measuring successful retrieval involves approximate matching, specifically utilizing "Precision and recall." Supplemental learning materials include quizzes and discussion prompts, such as those focusing on "Exotic distance measures." The educational timeline culminates with a Mid-term assignment in Week 10 and preparation for the final exam in Week 22.

---

### 07_Further_reading_Reading_45_min

# Further reading
Reading • 45 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/ufAG5/further-reading

This short article provides a detailed overview of Visual Information Retrieval (VIR). It specifically examines both the challenges and the successes encountered within the field of VIR. Although described as lightweight in scope, the text offers valuable references to assist readers who wish to start their research. The primary recommended reference is authored by O. Marques. This work is titled 'Visual information retrieval: The state of the art'. The full citation details are: IT Professional, 18(4), covering pages 7 through 9. Readers can search for this authoritative article within the Online Library.

---

## Week 19

### 01_Exploring_practical_considerations_through_examples_Video_2_min

# Exploring practical considerations through examples
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/fEMVE/exploring-practical-considerations-through-examples

This curriculum covers database management, beginning with foundational concepts in Weeks 1 and 2 ("Working with Data - part 1" and "part 2"). Weeks 3 and 4 focus on Relational Databases, establishing the core structure for data organization. Subsequently, Weeks 5 and 6 delve into data reliability, emphasizing critical concepts of Data Integrity and Security. The application of these concepts starts in Week 7 and Week 8 ("Using Databases: libraries and templating - part 1" and "part 2").

The study expands into advanced database theory, covering "Advanced RDBMS topics" in Week 9, followed by a Mid-term assignment in Week 10. The focus broadens significantly in Week 11 and Week 12, exploring Distributed databases and alternative database models. Weeks 13 and 14 introduce Semantic databases, followed by a deep dive into Linked Data in Weeks 15 and 16.

The curriculum then transitions to multimedia management, covering "Multimedia and retrieval" in Weeks 17 and 18. The final major topic block, Week 19 and Week 20 ("Applications - part 1" and "part 2"), uses practical examples to demonstrate real-world database use. Specifically, the course details projects such as mapping medieval manuscript migrations across three databases. Further technical examples include using The collector: Schoenberg Database of manuscripts, the Bibale research institute database, and the Medieval manuscripts in Oxford Libraries database. These practical case studies are supplemented by quizzes, practice assignments, and discussion prompts, preparing students for the final exam in Week 21.

---

### 02_Mapping_manuscript_migrations_a_tale_of_3_databases_Video_18_min

# Mapping manuscript migrations: a tale of 3 databases
Video • 18 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/SecSD/mapping-manuscript-migrations-a-tale-of-3-databases

Different stakeholders require different data views for the same object, such as a book or manuscript, leading to diverse data models and organizational requirements. This video examines how three distinct groups created three different databases based on their unique interests, demonstrating how different views shape database design

---

### 03_The_collector_Schoenberg_Database_of_anuscripts_Video_8_min

# The collector: Schoenberg Database of anuscripts
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/h7urs/the-collector-schoenberg-database-of-anuscripts

This course systematically covers fundamental to advanced concepts in database systems across twenty-two weeks. Initial modules introduce working with data, followed by an in-depth study of Relational Databases (Weeks 3 and 4). Reliable database operation is addressed in Weeks 5 and 6, focusing on critical concepts of Data Integrity and Security. Subsequently, the course explores practical implementation by detailing how databases are used through libraries and templating (Weeks 7 and 8).

Advanced database theory is covered in Week 9, before transitioning to more complex architectures in Weeks 11 and 12, specifically focusing on Distributed databases and alternative database models. Topics then progress to specialized database types, including Semantic databases (Weeks 13 and 14) and the integration of Linked Data (Weeks 15 and 16).

Further specialized topics include Multimedia and retrieval (Weeks 17 and 18), culminating in an exploration of real-world Applications in Weeks 19 and 20. Practical applications are illustrated through examples, such as mapping manuscript migrations, and case studies featuring specific systems like The collector: Schoenberg Database of Manuscripts and the research institute Bibale.

The curriculum utilizes various resources, including videos and quizzes, to reinforce learning, demonstrated by assignments associated with topics such as medieval manuscripts in Oxford Libraries. The course structure ensures a thorough understanding of database architecture, moving from standard relational models to cutting-edge concepts like semantic and distributed systems. Week 10 marks the mid-term assessment, while Week 21 prepares students for the final examination, which takes place in Week 22.

---

### 04_The_collector_Schoenberg_Database_of_Manuscripts_Reading_1h

# The collector: Schoenberg Database of Manuscripts
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/rPkzI/the-collector-schoenberg-database-of-manuscripts

The Schoenberg Database of Manuscripts (SDBM) is accessible at the following link: https://sdbm.library.upenn.edu/. For a high-level understanding of the data model, slides detailing the structure are available directly on the site. The accompanying user manual provides crucial insight into how the data is structured, specifically addressing the degree of explicitness in both the database itself and the data entry documentation. The core functions and structure of the SDBM, managed by The collector: Schoenberg Database of Manuscripts, can be learned through these resources. If any of the provided links are found to be broken, users are instructed to notify the appropriate party via the Student Portal.

---

### 05_The_research_institute_Bibale_Video_9_min

# The research institute: Bibale
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/5jYjh/the-research-institute-bibale

The Bible database contrasts significantly in design, purpose, and history compared to the Schoenberg database. Its origins trace back to the Card catalogues of Yazdi, a research institute founded in the 1930s. This institution accumulated increasingly complex data without imposing limitations on vocabulary or structure. The resulting data source is exceptionally rich and complex, dealing with the messy nature of humanities research.

The major design challenge was modeling this highly unstructured richness within a rigid relational database framework. The resulting database utilizes a specialized, slightly unconventional relational structure. It is fundamentally built around generic structures, specifically the concept of an object possessing a defined type and a name. Objects, such as persons or books, are stored in a primary table, each having a type, a name, and an ID.

A separate mechanism handles elements, which are attached to these objects and possess a type value (e.g., 'death date' or 'sex'). This structure deviates from conventional relational design, which typically allocates a column for every attribute. Instead, the database structure uses a row for each extra attribute or element. This decision renders the tables dense rather than sparse. The rationale for this design choice is crucial: it enables the easy addition of new attributes and relationships without requiring complex database structure redesigns.

By bypassing explicit database structure enforcement, the designers shifted the responsibility for maintaining data structures onto the end-users. This trade-off provides greater flexibility but introduces slightly riskier code execution. Consequently, the data modeling is straightforward from the database builder's perspective, yet complex for those tasked with processing or displaying the data.

A critical finding is that this architecture empowers scholars, allowing them to enrich the data model without being constrained by a rigid schema. The model itself resides primarily in documentation, not in the SQL schema, which presents a challenge for developers. The logic and enforcement of rules are often informal, communicated directly to the catalogers.

Practically, the system's limitations mean catalogers frequently adopt shortcuts because the database does not enforce documented rules. Researchers, therefore, must model not only the prescribed structures but also the practical, informal usage patterns of the database. These project characteristics are typical of large humanities database initiatives. Contextually, related topics include Weeks 3 and 6 concerning Relational Databases and Data Integrity. Advanced concepts such as Semantic Databases (Weeks 13/14) and Linked Data (Weeks 15/16) are also relevant to these historical data projects. The module structure includes detailed examples such as "Mapping manuscript migrations: a tale of 3 databases."

---

### 06_Bibale_and_IRHT_Reading_1h

# Bibale and IRHT
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/6Aope/bibale-and-irht

Bibale is a digital tool utilized by the IRHT for researching manuscript provenance; a comprehensive introduction to its data model and role is found in H. Wijsman’s article, 'The Bibale database at the IRHT: A digital tool for researching manuscript provenance,' published in *Manuscript Studies* 1(2) 2017, pp.328–341. For technical maintenance, users are instructed to report any broken link related to this resource via the Student Portal.

---

### 07_The_library_Medieval_manuscripts_in_Oxford_Libraries_Video_17_min

# The library: Medieval manuscripts in Oxford Libraries
Video • 17 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/LR5Yd/the-library-medieval-manuscripts-in-oxford-libraries

This course progresses through fundamental database concepts, beginning with introductory work with data (Week 1 & 2). The curriculum moves into Relational Databases (Week 3 & 4), establishing the core principles of structured data management. Subsequently, Weeks 5 and 6 address the critical need for reliable databases by focusing on Data Integrity and Security. The course then delves into practical application using databases via libraries and templating (Week 7 & 8).

Advanced RDBMS topics are covered in Week 9, preparing students for the Mid-term assignment in Week 10. The focus shifts dramatically in Weeks 11 and 12, exploring Distributed databases and alternative database models. Subsequent sections cover specialized conceptual models, starting with Semantic databases (Week 13 & 14). Weeks 15 and 16 are dedicated to understanding Linked Data, a key component of modern information systems.

The curriculum also includes Multimedia and retrieval techniques (Week 17 & 18), followed by practical applications in Week 19. Topic 10, Applications, introduces practical considerations through examples, including case studies like databases of medieval manuscripts. Specific examples are detailed, such as mapping manuscript migrations, The collector: Schoenberg Database of Manuscripts, Bibale, and Medieval manuscripts in Oxford Libraries. These final weeks reinforce learning with the completion of Part 2 of Applications (Week 20) and preparation for the final exam (Week 21 & 22).

---

### 08_Mapping_manuscript_migrations_Putting_it_together_Video_5_min

# Mapping manuscript migrations: Putting it together?
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/j5zo0/mapping-manuscript-migrations-putting-it-together

The project's primary goal was to map manuscript migrations by integrating insights from three distinct and specialized databases. These databases—the Schoenberg Database, the Oxford database, and others—possess varied structures and aims. The confluence of these differences creates a rich and valuable composite dataset. The central research question driving the project was "how" to successfully combine the data from these divergent sources. The team firmly believed that asking questions across all three datasets would unlock research possibilities inaccessible to individual sources. The major technical challenge, therefore, involved developing a method to allow the systematic exploration of these three datasets simultaneously.

The first technical question concerned the method of data combination. Candidates included merging all data into an existing repository, such as stacking bottling data into the Schoenberg Database. Alternatively, the team considered creating a completely new union database encompassing all sources. A third complex option involved employing federated queries, which would send requests to all databases without creating a single, combined entity.

Another critical logistical hurdle was ensuring data integrity and consistency across the system. Specifically, the system needed a mechanism to guarantee that any updates made to the original client databases would successfully propagate throughout the combined dataset. A separate issue arose regarding the fate of auxiliary datasets, such as correction databases, and where they would reside long-term.

This challenge led to profound questions regarding the project's permanence and infrastructure. Since the project itself was short-lived, but the datasets are long-term institutional assets, durability is paramount. There is no guarantee of the permanent existence of the infrastructure, nor is there a permanent staffing commitment after the project concludes.

A crucial practical difficulty involves reconciling the diverse data models. The three sources operate using radically different approaches and levels of detail. For example, the Schoenberg Database provides strong observations of manuscripts but is notably hazy on manuscript existence. Conversely, the Oxford database is highly definite regarding manuscripts when they are known to be in the library. This difference in granularities presents a significant modeling problem.

The team had to determine how to reconcile these varying levels of detail while ensuring the solution scales efficiently to handle tens of thousands of records. The overall challenge requires solving issues spanning data architecture, system longevity, and semantic modeling. The project served as a practical exploration of these complex database management migrations. Ultimately, the study highlights the necessity of developing robust, scalable methods for integrating disparate, heterogeneous data. These challenges underscore the complexities inherent in modern data science and library management.

---

## Week 2

### 01_What_shape_is_your_data_Introduction_Video_4_min

# What shape is your data? Introduction
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/OmmBF/what-shape-is-your-data-introduction

Data structures are fundamental when designing database applications, requiring careful consideration of how data is organized. These structures exist at a higher level of abstraction than basic programming types like arrays, objects, and floats. Data modeling focuses on representing how data should be brought together and what relationships exist between different pieces of information. Structuring data is critical for successful serialization, which is the process of writing data out to a file or a network connection for reading elsewhere. Serialization is closely related to exchange protocols, which require data structures optimized for inter-application data transmission over connections like sockets. Furthermore, data structure choices must account for human communication, as users have preferences regarding how complex information is presented. If data contains inherent complexity, the presentation structure should be altered to maximize user comprehension and clarity. While low-level operations are handled by algorithms and data structures, this module focuses on high-level data modeling concepts. Specific data shapes, such as tables, trees, and graphs, will be examined in detail. Tables are presented as one of the most intuitive and general-purpose methods for structuring data. Trees are employed to introduce hierarchical relationships into the data structure. Graphs are excellent structures for representing highly interconnected datasets. Briefly, the concepts of objects and documents are also mentioned, though the database itself does not deeply understand their internal workings. The selection of an appropriate data shape will critically inform the underlying database paradigm that is ultimately used. The course begins in Week 1, covering foundational topics such as "Working with Data." Week 1 focuses specifically on the introduction to data structures and includes videos on tables, trees, and other structures. Week 2 delves further into data structure concepts, including assignments and quizzes to reinforce learning. Topic 2, Relational Databases, begins in Week 3 and continues through Week 4. Week 5 introduces Topic 3, covering Data Integrity and Security within reliable databases. The practical application of databases is covered in Weeks 7 and 8, focusing on libraries and templating. Advanced Relational Database Management Systems (RDBMS) topics are addressed in Week 9. A mid-term assignment is scheduled for Week 10, acting as a key assessment point. Topic 6, Distributed databases and alternative models, is covered in Weeks 11 and 12. Weeks 13 and 14 focus on Semantic databases, a specialized area of data storage. Topics 8 and 9 cover Linked Data and Multimedia and Retrieval, respectively, in Weeks 15 through 18. The final two topics, Applications (Weeks 19 and 20), and preparation (Week 21) lead into the comprehensive exam in Week 22.

---

### 02_What_shape_is_your_data_Tables_Video_8_min

# What shape is your data? Tables
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/M8kZI/what-shape-is-your-data-tables

This comprehensive curriculum outlines a 22-week deep dive into data structures and advanced database technologies, starting with foundational concepts.

The initial phase (Week 1 & 2) focuses on fundamental data structures, detailing "What shape is your data?" through structured modules. This includes specific instruction on Tables (8-minute video), Trees (7-minute video), and "Other" structures (11-minute video), supplemented by quizzes and practice assignments. An introductory reading on employability is also introduced during this period.

The core of the learning begins in Week 3 and Week 4 with Topic 2: Relational Databases, establishing the structure for data management. Weeks 5 and 6 then transition to Topic 3, addressing reliable databases through the crucial technical details of Data Integrity and Security.

Practical application and advanced implementation are covered in Weeks 7 and 8 (Topic 4: Libraries and Templating) and Week 9 (Topic 5: Advanced RDBMS topics).

A major milestone occurs in Week 10 with the Mid-term assignment, assessing understanding of foundational and relational concepts.

The focus broadens considerably in Weeks 11 and 12 (Topic 6), which explore Distributed databases and alternative database models necessary for large-scale data. Following this, Weeks 13 and 14 (Topic 7) delve into specialized Semantic databases, connecting data via formal meaning.

The syllabus then moves to Weeks 15 and 16 (Topic 8), focusing on Linked Data, a method for establishing semantic relationships across datasets. Weeks 17 and 18 (Topic 9) address complex concepts of Multimedia and retrieval.

The final learning phase comprises Weeks 19 and 20 (Topic 10), applying these knowledge bases to real-world Applications. The curriculum concludes with Week 21 dedicated to preparation for the final exam, followed by the final assessment in Week 22.

---

### 03_What_shape_is_your_data_Trees_Video_7_min

# What shape is your data? Trees
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/S7FQh/what-shape-is-your-data-trees

Data structures in computer science derive their logic and organization from metaphorical representations, primarily drawing inspiration from both botanical and family trees. A botanical tree structure features a root note from which everything originates, branching multiple times at various points. Every node in this structure can trace back through parent branch points until it reaches the ultimate root. Furthermore, any two nodes can be traced back to a common branch point they share.

However, when encoding tree structures in computing, the iconography and language often adopt an abstracted metaphor derived from the family tree. This family tree depiction requires an important visual shift: the root node, representing the origin, is placed at the top, and children descend towards the bottom. The parents reside at the top levels, while the leaf nodes indicate the end of a branch.

To maintain focus on the technical concept, the vocabulary used differentiates concepts such as parent nodes, child nodes, ancestors, and descendants. It is crucial to distinguish between the metaphorical sources, particularly regarding parent nodes. While a standard family tree often shows two parent nodes for most child nodes, most common computer science implementations limit a node to having only one parent node.

Trees are employed to represent complex, deep, and highly heterogeneous data in a contained fashion. The practical application involves defining a top object, such as the "Harry Potter series," which serves as the root node. Knowledge about this series is then attached via subsequent branches and child nodes.

For example, within the series, branches lead to individual parts, such as "Harry Potter and the Philosopher's Stone." This single node can then have diverse information attached as its child nodes. One child node might hold the publication date (1997) and the publisher, demonstrating varying data types. Another child node, representing the film version, might hold its date (2001) and the list of actors, like Daniel Radcliffe and Emma Watson.

This structure highlights the power of trees for modeling highly varied data, where the number or specific order of sub-elements is not predetermined. This concept of working with data, particularly in the form of trees, is a foundational topic within the course curriculum.

The overall academic study of data shapes encompasses various topics, including working with tables, trees, and other data structures. Subsequent modules delve into Relational Databases (Week 3 and Week 4), focusing heavily on Data Integrity and Security (Week 5 and Week 6). Further advanced topics include leveraging databases through libraries and templating, and exploring advanced Relational Database Management System (RDBMS) concepts.

The course continues into modern database architecture, covering Distributed Databases and alternative database models (Week 11 and Week 12). It then introduces specialized data types, such as Semantic Databases (Week 13 and Week 14) and Linked Data (Week 15 and Week 16). Finally, the curriculum addresses Multimedia and retrieval (Week 17 and Week 18), concluding with Applications.

---

### 04_What_shape_is_your_data_Other_Video_11_min

# What shape is your data? Other
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/x2RHO/what-shape-is-your-data-other

### Week 1 Topic 1: Working with Data - part 1 ### Week 2 Topic 1: Working with Data - part 2 #### 1.3 Data structures - What shape is your data? Introduction Video . Duration: 4 minutes 4 min - What shape is your data? Tables Video . Duration: 8 minutes 8 min - What shape is your data? Tables quiz Practice Assignment . Duration: 5 minutes 5 min - What shape is your data? Trees Video . Duration: 7 minutes 7 min - What shape is your data? Trees quiz Practice Assignment ....

---

### 05_Worksheet_Working_with_Data_(Topic_1,_Part_2)_Reading_10_min

# Worksheet: Working with Data (Topic 1, Part 2)
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/S2rJH/worksheet-working-with-data-topic-1-part-2

This worksheet introduces the fundamental concepts regarding the shape and organization of data. The focus shifts from low-level programming types, such as arrays, objects, and numbers. Instead, the emphasis is placed on higher-level data shapes. These shapes are crucial for various technical functions. Specifically, they support data modelling and serialisation processes. They are also essential for implementing exchange protocols and ensuring human-readable presentation of data. The estimated time commitment for this material is approximately 60 minutes.

A core learning objective is the ability to distinguish various data shapes. These include tables, trees, graphs, media files, raw data, and simple unindexed lists. Students will learn to explain the specific utility of each data shape. They will also be able to ask critical questions about data origins and future usage.

Several key terms are defined to aid understanding. A data structure is defined as a shape or organization used to hold and relate data. A Table is a specific grid configuration. In this grid, each row represents a single entity, or "thing." A Row is the horizontal line of cells within the grid, and it represents a thing. Conversely, a Column is the vertical line of cells, and it represents a specific type of information. The Cell is the defined value found at the intersection of a given row and column.

Regarding data handling processes, Serialisation is the method of writing data to a file or network connection. This process ensures the data can be subsequently read elsewhere. An Exchange protocol is established as an agreed way for various applications to pass data over a network connection.

The text also introduces the concepts of hierarchical data, represented by a Tree. A Tree is characterized as a hierarchical structure possessing a single root node. The Root node functions as the top element and has no parent. Any node positioned directly above a specific node is identified as the Parent node. A Child node is defined as any node located directly below a parent node. A Leaf node is distinguished as a node that contains absolutely no children. An Ancestor is defined as any node that is positioned above a given node. Finally, a Descendant is defined as any node that exists below a given node.

---

### 06_Employability_beyond_this_module_and_beyond_the_BSc_Reading_10_min

# Employability: beyond this module and beyond the BSc
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/T9Kit/employability-beyond-this-module-and-beyond-the-bsc

This reading and the accompanying video are designed to help students reflect critically on the value gained from the degree program and how this knowledge will make them valuable to potential employers. A primary focus is exploring workplace trends, specifically how the professional environment has been affected by advancements in AI and Large Language Models (LLMs). The video provides insights from industry professionals who reflect on what skills and attributes are most valued in the current workplace. For further technical insights, students can access the UoL Careers Service webinar recording library. This extensive resource library is also accessible through the centralized CareersConnect portal. Specifically, the November 2025 panel on Careers in Data Science is highlighted as a topic of particular interest for prospective students. Students interested in exploring specific career pathways can review industry briefings, such as "Career Options in Web & Mobile Development." Additionally, a comprehensive collection of career option briefings is available within the Computer Science, Cybersecurity, and Data Science Careers Resources. All these specialized resources can be found through the dedicated CareersConnect portal. Ultimately, the module aims to bolster employability beyond the completion of the BSc.

---

### 07_Employer_voices_on_AI_trends_Video_11_min

# Employer voices on AI trends
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/e3lB0/employer-voices-on-ai-trends

The modern technological landscape is defined by Hyperautomation, which significantly transcends simple Robotic Process Automation (RPA). Hyperautomation integrates advanced technologies such as Artificial Intelligence (AI), machine learning, and process mining to automate, augment, and expand human work capabilities. This integration leads toward near autonomy as systems are designed to observe, learn, and optimize themselves, sometimes without requiring human triggers. Consequently, job design is shifting toward emphasizing human-machine collaboration, leveraging distinctly human traits like creativity, ethical oversight, judgment, and emotional intelligence.

The World Economic Forum's Future of Jobs report (2025) highlights this shift, suggesting that 40% of current professional skills will change by 2027. While traditional roles persist, new specializations are emerging, such as AI security, technology governance, and responsible innovation designers. The demand for roles involving "framing an intelligent problem" has risen, requiring translators who bridge technology and business end-users.

To prepare for this evolving market, students must become T-shaped professionals, possessing both deep core knowledge and broad horizontal facets. Furthermore, business fluency

---

### 08_Topic_1_summary_Video_2_min

# Topic 1 summary
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/s5nGi/topic-1-summary

This course provides an intensive study of data structures and database management systems across 22 weeks. The initial phase (Weeks 1-2) focuses on data structures, specifically exploring the differing shapes of data through tables, trees, and other complex models. Following this foundation, Weeks 3 and 4 introduce core concepts of Relational Databases. A significant focus is placed on data trustworthiness in Weeks 5 and 6, addressing essential topics of Data Integrity and Security.

Weeks 7 and 8 transition into practical implementation, covering the use of databases via specific libraries and templating techniques. The curriculum then deepens its technical scope in Week 9 with an exploration of Advanced RDBMS topics. A major thematic shift occurs in Weeks 11 and 12, detailing Distributed databases and various alternative database models.

The study of knowledge representation begins in Weeks 13 and 14 by analyzing Semantic databases. This is followed by a dedicated focus on Linked Data in Weeks 15 and 16, which addresses interconnected data sets. Weeks 17 and 18 tackle the specialized areas of Multimedia and retrieval.

The final phases of the course (Weeks 19-20) apply these concepts through various Applications, culminating in exam preparation during Weeks 21 and 22. Key professional considerations are integrated throughout, highlighted by sessions on Employability and AI trends. An important mid-term assignment is scheduled for Week 10. The module structure maintains a consistent review cycle, utilizing quizzes and extensive readings for continuous knowledge reinforcement.

---

### 09_Further_reading_Reading_50_min

# Further reading
Reading • 50 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/oBuB1/further-reading

This text details a specific example of a digital humanities dataset concerning menus. The dataset, focusing on menus, has been released as Open Data by the New York Public Library. Trevor Munoz, the Interim Head of the Maryland Institute for Technology in the Humanities, introduced and explored this dataset in two blog posts. These posts are titled "What IS on the menu" and "Refining the problem." The project maintains a dedicated full website. This website allows users to explore the menus. Furthermore, it provides the functionality to download the transcribed data. Contributors are also invited to contribute to the dataset. The official project link is cited as New York Public Library ’What’s on the menu’ (2025). However, the approach to data handling employed in this project is not universally accepted. There is academic debate regarding this methodology. For a discussion on data cleaning related to the ‘What’s on the menu?’ project, a specific resource is provided. This resource is the article, "Against cleaning," authored by Rawson, K. and T. Muñoz. This article appears in the publication "Debates in the Digital Humanities," Volume 5. The publication is associated with the University of Minnesota Press, dated 2019. The text also includes a functional disclaimer regarding potential link breakage. Users are instructed to report broken links via the Student Portal. (Total sentences: 15)

---

## Week 20

### 01_Mapping_manuscript_migrations_Putting_it_together_Video_12_min

# Mapping manuscript migrations: Putting it together
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/e1pZb/mapping-manuscript-migrations-putting-it-together

This course provides a comprehensive curriculum on data management, structured across 22 weeks. The initial weeks focus on foundational topics, starting with "Working with Data - part 1" (Week 1) and "Working with Data - part 2" (Week 2). Following this, the course delves into "Relational Databases - part 1" and "Relational Databases - part 2" (Weeks 3 and 4). Weeks 5 and 6 address the vital concepts of "Reliable databases: Data Integrity and Security - part 1" and "Reliable databases: Data Integrity and Security - part 2."

The module structure continues by exploring practical database use, covering "Using Databases: libraries and templating - part 1" and "Using Databases: libraries and templating - part 2" (Weeks 7 and 8). Week 9 is dedicated to "Advanced RDBMS topics - part 1," preceding the mid-term assignment in Week 10.

A significant portion of the curriculum addresses complex database architectures, beginning with "Distributed databases and alternative database models - part 1" and concluding with "Distributed databases and other database models - part 2" (Weeks 11 and 12). Following this, the focus shifts to specialized paradigms, specifically "Semantic databases - part 1" and "Semantic databases - part 2" (Weeks 13 and 14). These are succeeded by "Linked Data - part 1" and "Linked Data - part 2" (Weeks 15 and 16).

Later topics broaden the scope to include "Multimedia and retrieval - part 1" and "Multimedia and retrieval - part 2" (Weeks 17 and 18), and finally "Applications - part 1" and "Applications - Part 2" (Weeks 19 and 20). Week 10 also features "Practical examples: Combining databases of medieval manuscripts," detailing videos like "Mapping manuscript migrations: Putting it together" (12 min) and "MMM modelling" (29 min), each with associated quizzes and practice assignments.

The curriculum also addresses data structure in Section 10.3, with videos exploring "What shape is my data?" (3 min) and "What shape do I want my data to be?" (2 min). The course culminates with a final preparation week (Week 21) and the exam week (Week 22).

---

### 02_MMM_modelling_Video_29_min

# MMM modelling
Video • 29 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/oreUL/mmm-modelling

This transcript provides a detailed lecture on **information modeling for cultural heritage**, specifically focusing on how to represent the complex relationships between creative works, their different versions, and their physical manifestations (like manuscripts or prints).

The discussion moves from high-level conceptual models (inspired by FRBR and adapted for CIDOC CRM) to the practical challenges of implementing these models in a database environment.

Here is a summary of the key concepts:

---

### 1. The Conceptual Hierarchy: Work, Expression, and Manifestation

The lecture establishes a strict hierarchy to categorize artifacts, ensuring that abstract concepts are clearly separated from physical objects:

*   **Work (Abstract Concept):** The underlying, original intellectual creation (e.g., the abstract concept of "Psalm 150," or Beethoven's overall composition).
*   **Expression (Version):** A specific realization or transformation of the work (e.g., the Hebrew version of Psalm 150, or the specific piano duet arrangement).
*   **Manifestation (Physical Item):** The actual, tangible object that embodies the expression (e.g., a specific printed edition, or a unique manuscript).
*   **Singleton:** In the manuscript case, this refers to the unique, singular physical object.

**Key Principle:** The *Work* is realized in an *Expression*, and the *Expression* is embodied in an *actual physical thing* (*Manifestation*).

### 2. Adapting the Model for Events (CIDOC CRM)

The standard FRBR model is adapted using **CIDOC CRM (Conceptual Reference Model)** because it is strongly focused on **events**. In this model, actions are not just static links but explicit *acts of creation* that require tracking:

*   **Agent Tracking:** The model must track *who* performed an act (e.g., "Beethoven made this arrangement," so the agent can be assigned to the creation event).
*   **Event Tracking:** This allows the system to say *when* and *by whom* an expression was turned into a specific manuscript.

### 3. The Core Modeling Challenge: Ownership and Custody

The most complex part of the lecture is addressing the challenges of modeling **provenance and ownership**, using examples from manuscript studies and the Schoenberg database.

*   **The Need for Richness:** Simple models fail because they cannot distinguish between different types of ownership:
    1.  **Collection Ownership:** A manuscript might be part of a large, long-standing **family library** (e.g., the Cecil family), where ownership is diffused over centuries, but the specific acquisition/disposal dates are unknown.
    2.  **Transaction Ownership:** The item may have gone through a clear, documented **sale or transfer of custody** (e.g., a recorded sale in the Schoenberg database).

*   **The Modeling Solution:** To avoid damaging the fidelity of the information, the final model must be **rich** rather than strictly simple.
    *   It must allow for multiple, sometimes overlapping, ways of saying the same information.
    *   For example, the system must be able to record a resource as being *part of a collection* (a general statement) while also maintaining specific *transaction triples* (a detailed event record).

### 4. Conclusion: Fidelity vs. Simplicity

The lecture concludes that while this **rich model** makes data retrieval and querying significantly more complicated, it is a necessary trade-off to preserve the nuances, subtle differences, and complete information integrity found in the source records.

---

### 📚 Context within the Course Material

The supplementary course material confirms that this lecture is part of a larger module dedicated to **Semantic Databases and Linked Data**.

*   **The goal of the project (MMM modelling)** is to move beyond traditional relational tables (RDBMS) to create a semantic, knowledge-graph-based model (like the one discussed in the transcript) capable of handling complex, non-uniform data relationships inherent in cultural heritage.
*   **"Mapping manuscript migrations"** is the practical exercise derived directly from the conceptual problems raised in the lecture—tracking the movement and change of custody (manifestations) over time.

---

### 03_MMM_Data_conversion_Video_10_min

# MMM Data conversion
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/xjsT3/mmm-data-conversion

The curriculum progresses from foundational concepts in data management, starting with an intensive focus on "Working with Data" (Weeks 1 and 2). The core of database theory is established in Weeks 3 and 4, detailing the principles of Relational Databases. Subsequently, Weeks 5 and 6 address the critical topic of "Reliable databases," focusing specifically on Data Integrity and Security mechanisms.

The practical application of these concepts begins in Weeks 7 and 8, covering the use of databases via libraries and templating. This foundational knowledge is advanced in Week 9 with a deep dive into advanced RDBMS topics, leading up to a Mid-term assignment in Week 10.

The course then shifts to modern architectural paradigms, covering Distributed Databases and alternative database models across Weeks 11 and 12, which addresses scalability. Following this, Weeks 13 and 14 introduce Semantic databases, emphasizing knowledge representation and the meaning of data.

The sequence continues with Weeks 15 and 16 dedicated to Linked Data, a vital technique for connecting disparate datasets across the web. Concepts expand further in Weeks 17 and 18 to cover Multimedia and retrieval techniques for complex data types. Weeks 19 and 20 synthesize all prior learning by focusing on real-world Applications.

Week 20 features practical examples, notably the project combining medieval manuscript databases (MMM). This case study reinforces data modeling through sections like "What shape is my data?" and "What shape do I want my data to be?" The material concludes with a final preparation week (Week 21) leading to the comprehensive examination in Week 22.

---

### 04_MMM_user_interfaces_Video_9_min

# MMM user interfaces
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/G9c2T/mmm-user-interfaces

The project was designed to create a sophisticated and rich resource suitable for humanities and manuscript scholars. This effort involved building a complex dataset that significantly surpasses the complexity of the individual sources it incorporates. Although user studies were conducted, limited resources prevented the development of a cutting-edge, highly sophisticated user interface. The primary goal was not to build a single perfect interface, but rather to demonstrate the potential of the merged data itself.

One initial realization was that the data is the core asset, and the interfaces are merely tools for its interrogation. The first created tool was a relatively straightforward web database structure, accessible at `manuscriptmigrations.org`. This database provided a faceted browsing interface, allowing users to track the migrations and locations of resources. For example, it could trace all sources of Josephus copied in France and visualize their subsequent travel. However, this first interface was ultimately limited, slow, and "boxed in" regarding the types of research questions that could be asked.

The project then built a second interface, "Research Space," which was funded by the British Museum and utilizes the C.CRM data model. This alternative interface enabled a more exploratory and browsing-based approach to inquiry. By utilizing a path of exploration, users could build up the size and complexity of their initial research questions. The existence of these two distinct paradigms proved that fundamentally different ways of exploring data can be applied to the same underlying information.

A critical turning point occurred when domain specialists initially criticized the primitive interfaces, viewing the UI limitations as deficiencies in the data itself. The project corrected this perception by teaching researchers to utilize a query language called Sparkle. Sparkle allowed the scholars to directly construct complex queries, revealing the true richness of the merged dataset. This provided an interesting contrast between the intuitive accessibility of a shiny UI and the power and expressiveness achievable programmatically.

Researchers evaluated twenty-five clear and unambiguous research questions against the databases to gauge their feasibility. Of these, eight questions proved impossible to answer using the Bibale Database. Likewise, six questions were impossible to answer solely with the SDBM database. The successful combination of these diverse datasets ensured that no questions remained unanswerable. Ultimately, 17 of the 25 research questions were fully answered using the combined databases (a success rate of 79%). While the combined data was often difficult to navigate via the user interfaces, the process became significantly easier when leveraging Sparkle. This project successfully demonstrated the crucial ability to combine different data models and approaches to create a synergy greater than the sum of its individual parts.

---

### 05_The_mapping_manuscript_migrations_project_Reading_1h

# The mapping manuscript migrations project
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/Hb82v/the-mapping-manuscript-migrations-project

The Manuscript Migrations Project (MMM) is introduced as a major initiative focused on metadata harmonization. The clearest published description of this project is found in the article, ‘Harmonizing and publishing heterogeneous premodern manuscript metadata as linked open data.’ This article was authored by Koho and numerous colleagues and published in the *Journal of the Association for Information Science and Technology* in 2021, spanning pages 1–18. For further information on the MMM project, the resource mappingmanuscriptmigrations.org is provided. Users are directed to explore the interface on this specific website for all coming discussions. Students are expected to utilize the interface on mappingmanuscriptmigrations.org throughout the course. Lastly, any instances where these provided links are broken must be reported via the Student Portal.

---

### 06_What_shape_is_my_data_Video_3_min

# What shape is my data?
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/2JxLy/what-shape-is-my-data

This course provides a comprehensive, 22-week curriculum focused on data management and advanced database systems. The foundational learning begins with Weeks 1 and 2, covering fundamental concepts in "Working with Data - part 1 and part 2." Weeks 3 and 4 transition into structured data management, detailing "Relational Databases - part 1 and part 2."

A significant emphasis is placed on reliability in Weeks 5 and 6, dedicated to "Reliable databases: Data Integrity and Security - part 1 and part 2." Subsequent weeks focus on implementation, with Weeks 7 and 8 exploring "Using Databases: libraries and templating - part 1 and part 2." Week 9 covers "Advanced RDBMS topics - part 1," consolidating deep knowledge of Relational Database Management Systems.

The scope expands in Weeks 11 and 12 to "Distributed databases and alternative database models - part 1 and part 2." Further specialization continues in Weeks 13 and 14, analyzing "Semantic databases - part 1 and part 2," followed by a deep dive into the modern framework of "Linked Data - part 1 and part 2" (Weeks 15 and 16).

Technical applications are explored in Weeks 17 and 18 through "Multimedia and retrieval - part 1 and part 2," leading into practical "Applications" in Weeks 19 and 20. The latter part of the course features a practical project, "10.2 Practical examples: Combining databases of medieval manuscripts," which includes specific exercises such as "Mapping manuscript migrations" (Video, 12 min) and "MMM modelling" (Video, 29 min).

Additional technical concepts addressed include "10.3 What shape does my data want to be?" and "10.4 Summary - Further reading." The structure culminates with Week 21 dedicated to exam preparation, followed by the comprehensive Week 22 examination.

---

### 07_What_shape_do_I_want_my_data_to_be_Video_2_min

# What shape do I want my data to be?
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/wL9Pu/what-shape-do-i-want-my-data-to-be

The core concept of data management revolves around determining the optimal shape for data to meet specific use requirements. Instead of focusing solely on the necessities of the data, one must determine what is desired from it, how questions will be asked, and what applications will be built upon it. This requires defining how the data will ultimately be used by various stakeholders. Crucial decisions include controlling the data, maintaining its integrity, and planning its handover to other parties.

The choice of data structure can be varied, encompassing mapping the data to a tree, a traditional tabular structure, object structures, or complex graphs. These decisions dictate the eventual technological environment. Consideration must be given to the intended audience: whether the data will be published publicly online or restricted to a proprietary corporate box.

Technological practicality is a major factor, particularly when considering the available skill sets for development. Building good tools on a traditional SQL database is often easier than specializing in a triple store or statically published RDF format. XML, while a well-established technology, represents a relatively specialized skill set compared to developing for systems like MongoDB or other distributed databases.

Ultimately, the selection of a database model must be rooted in the underlying purpose of the data. The guiding question remains: Why does this data exist, and for whom is the database being built? This pursuit ensures that the design best empowers the intended use of the data.

The course structure outlines a comprehensive study spanning various database paradigms. Topics begin with Relational Databases (RDBMS) and progression to reliable databases, focusing on Data Integrity and Security. The curriculum then moves into advanced RDBMS concepts and distributed databases.

A significant portion of the material is dedicated to modern data paradigms, specifically Semantic Databases and Linked Data. These modules introduce advanced modeling concepts crucial for modern data integration. Practical examples, such as "Mapping manuscript migrations," illustrate how complex real-world data can be put together using these models.

The study further explores practical applications, including multimedia and retrieval, and culminates in a deep dive into specific database models. This progression moves from basic data working concepts to utilizing libraries and templating for effective database interaction. The curriculum culminates in a comprehensive understanding of practicalities and is designed to prepare students for advanced data engineering and modeling tasks.

---

### 08_Further_reading_Reading_1h

# Further reading
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/iCo6k/further-reading

The discussion centers on the field of linking diverse musical datasets across different academic disciplines. The author of the introduction notes that their own perspective on dataset linkage is rooted in a historical background. Johanna Devaney addresses this question by proposing a contrasting methodological framework. Devaney's approach significantly shifts the focus toward perceptual and analytical aspects of music data. The core of her work utilizes note-level music encodings as a mechanism for analysis. This technical tool is employed to facilitate interdisciplinary research efforts. The overarching objective of this research is to better understand human engagement with music. The study is detailed in the article by Devaney, J. The full citation is: Devaney, J. ‘Using note-level music encodings to facilitate interdisciplinary research on human engagement with music’. This research was published in *Transactions of the International Society for Music Information Retrieval*, specifically in volume 3(1) from 2020. Readers seeking this material are directed to search for the article within the Online Library.

---

## Week 21

### 01_Revision_Reading_10_min

# Revision
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/p5sSn/revision

Use this week to revise the learning materials of the course and get prepared for the exam. You can use the list of key concepts and the revision quizzes in this section to help you with your revision. Revision Use this week to revise the learning materials of the course and get prepared for the exam. You can use the list of key concepts and the revision quizzes in this section to help you with your revision. Mark as completed Dislike Report an issue

---

## Week 3

### 01_Welcome_to_relational_databases_Video_10_min

# Welcome to relational databases
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/vUfuu/welcome-to-relational-databases

A relational database (RDB) implements the abstract concepts of the relational model. A "model," generally, is a method for abstracting complex real-world data into manageable structures that can be reasoned about. Specifically, in this context, the relational database utilizes tables as its high-level structural approach. A "relation" is essentially a precise definition of a table, encompassing the defined columns (attributes), the definition of what those columns mean, and all the values stored within. The core of the relational model is this combination of definition and stored values.

The relational model establishes strict rules for how these relations must be manipulated. Fundamentally, the first rule dictates that everything within the system must be represented as a relation. All operations within the model must request and operate over tables. Moreover, the system must handle not only the information itself but also information about the information, such as creating new tables, users, or restructing the database through relation manipulation.

For a system to truly implement the model, it must be a robust, abstracted system. This means functionality must remain consistent regardless of physical or software constraints, such as hardware replacement, operating system changes, or changes in disk formatting. Furthermore, if the data is distributed across a network, it must maintain the appearance of being concentrated in a single location.

The course will explore three primary models: the abstract relational model, the entity-relationship (ER) model, and SQL. The ER model is widely used for modeling concepts and data structures, frequently applied to relational databases. However, it is critical to note that the term "relation" in the relational model differs significantly from the term "relationship" used in an ER diagram.

The relational model itself is highly theoretical, yet it has almost never been purely implemented in practice. Instead, SQL (and its variant, Sequal) serves as a practical, partial implementation of the relational model. SQL is not strictly adherence to the abstract model, but its underlying theory is applicable to various RDBMS packages like MySQL, PostgreSQL, and SQLite. These database packages are close enough to SQL that they can possess many of the abstract properties of the relational model. The overall curriculum is structured to meet these concepts, starting with fundamental theory in Week 3 and moving into practical design and implementation using ER diagrams and Basic SQL in Week 2.1. The full scope of the material extends through topics covering data integrity, security, distributed databases, and semantic databases over the coming weeks.

---

### 02_Drawing_a_database_I_Basic_entity-relationship_diagrams_Video_6_min

# Drawing a database I: Basic entity-relationship diagrams
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/mJMrV/drawing-a-database-i-basic-entity-relationship-diagrams

This course explores database concepts beginning with foundational material, including working with data (Weeks 1-2) and delving into relational database theory and design (Week 3). Core technical skills taught involve drawing basic Entity-Relationship Diagrams (ERDs), mastering Basic SQL, and practical application using MySQL in the lab. Subsequent topics focus on ensuring database reliability, covering crucial aspects of Data Integrity and Security across two weeks. Students progress to applying databases via libraries and templating (Weeks 7-8), followed by an exploration of Advanced RDBMS topics (Week 9) and a Mid-term assignment (Week 10). The curriculum then expands to complex architectures, addressing Distributed databases and alternative database models (Weeks 11-12). Advanced specialized models are introduced, specifically Semantic databases and Linked Data (Weeks 13-16). Finally, the course concludes by covering Multimedia and retrieval (Weeks 17-18) and various Applications (Weeks 19-20) before final exam preparation (Weeks 21-22).

---

### 03_Speaking_to_databases_I_Basic_SQL_Video_10_min

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

### 04_Speaking_to_databases_II_Using_MySQL_in_the_lab_Video_7_min

# Speaking to databases II: Using MySQL in the lab
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/QB8SB/speaking-to-databases-ii-using-mysql-in-the-lab

This comprehensive curriculum begins with foundational data concepts, covering basic data manipulation and introducing relational databases through Entity-Relationship Diagrams and basic SQL querying. The early modules focus heavily on practical implementation, using MySQL for database creation and querying, alongside understanding the core theory of relational database design. Subsequent modules address the critical operational aspects of reliable databases, specifically focusing on ensuring Data Integrity and Data Security. The advanced portion of the course explores diverse architectural models, including Distributed databases, Semantic databases, and Linked Data, which move beyond standard RDBMS functionality. Practical application is detailed by discussing libraries and templating, followed by specialization in Multimedia and retrieval systems. The learning progression culminates in applications and complex topics before a Mid-term assignment at Week 10. The course concludes with intensive preparation leading up to the final examination in Week 22.

---

## Week 4

### 01_Introducing_Joins_Video_9_min

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

### 02_Drawing_a_database_II_More_about_joins_Video_13_min

# Drawing a database II: More about joins
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/lXLXI/drawing-a-database-ii-more-about-joins

This course progresses systematically through database management, beginning with foundational topics in working with data (Weeks 1-2). Weeks 3 and 4 focus heavily on **Relational Databases**, introducing complex structures and detailing the mechanism of **Joins** and their implications through dedicated video and practice assignments. The curriculum then delves into the critical concepts of **Database Integrity and Keys** (Weeks 5-6), emphasizing the role of keys in maintaining data accuracy and structure.

Following database theory, Weeks 7 and 8 cover practical implementation by exploring how databases are used with libraries and templating in application development. The specialization then accelerates with **Advanced RDBMS topics** (Week 9), preceding a mid-term assignment. A significant technical shift occurs in Weeks 11 and 12, which address **Distributed databases and alternative database models**.

Later sections explore highly specialized database architectures: Weeks 13 and 14 focus on **Semantic databases**, while Weeks 15 and 16 cover the implementation of **Linked Data**. Subsequent weeks (17-20) broaden the scope to include **Multimedia and retrieval** and general **Applications**. The final weeks are dedicated to preparation and the examination, concluding the comprehensive study of database systems.

---

### 03_E_R_diagrams_summary_Reading_1h

# E/R diagrams summary
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/2ct3P/e-r-diagrams-summary

The attached section from the Database systems subject guide goes from the basics of E/R diagrams and modelling to more details about problems with the model and the process of implementing it as a relational diagram: Lewis, D. CO2209 Database systems. (London: University of London, 2016)....

---

### 04_Database_integrity_and_the_role_of_keys_Video_9_min

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

### 05_Speaking_to_Databases_II_SQL_for_joins_and_keys_Video_13_min

# Speaking to Databases II: SQL for joins and keys
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/NK5sU/speaking-to-databases-ii-sql-for-joins-and-keys

This curriculum progresses through several stages of database theory, beginning with foundational data handling in Weeks 1 and 2. Weeks 3 and 4 focus intensely on Relational Databases, specifically introducing complex concepts like Joins and refining understanding through E/R diagrams and associated practice assignments. Subsequent study in Weeks 5 and 6 addresses Data Integrity and Security, emphasizing the crucial role of database keys. The course then moves into practical application in Weeks 7 and 8, focusing on Using Databases through libraries and templating. Advanced topics begin in Week 9, followed by a mid-term assessment in Week 10. The syllabus expands significantly in Weeks 11 and 12 by introducing Distributed databases and alternative database models. Furthermore, Weeks 13 through 16 delve into Semantic databases and Linked Data, providing a comprehensive overview of modern data structuring. The latter half includes coverage of Multimedia and retrieval (Weeks 17-18) and diverse Application models (Weeks 19-20). The entire curriculum culminates with preparation for the final exam in Weeks 21 and 22, building upon essential skills such as SQL for joins and keys.

---

### 06_Topic_2_summary_Video_1_min

# Topic 2 summary
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/LfsJV/topic-2-summary

The course structure covers various aspects of database management, beginning with foundational data modeling concepts. Students first encounter the Entity Relationship (ER) Model, learning how to translate this model into explicit ER diagrams. A key objective is understanding the inherent relationship between the ER Model and the practical Relational Model. The relational principles are subsequently explored in detail. Implementation of the relational model is covered through specific database language, namely SQL. Practical exercises involve working with MySQL to solidify understanding of database manipulation. A significant focus is placed on enhancing database clarity and reliability. This reliability is achieved through the explicit use of joins and keys. Making the data structure explicit is highlighted as crucial for ensuring database integrity.

The curriculum dedicates substantial time to the complexity of relational databases. Specifically, the concept of Joins and their implications is introduced to handle complex data relationships. Furthermore, the topic of integrity and the fundamental role of keys in maintaining data quality is thoroughly explored. Students engage in practical exercises, such as designing and building simple databases using SQL for joins and keys.

Moving beyond foundational relational concepts, the course advances into complex and reliable database architecture. Week 5 and Week 6 delve specifically into Data Integrity and Security within reliable databases. The curriculum then shifts to modern applications, covering how databases are utilized with libraries and templating (Week 7 and Week 8). Advanced topics involve deeper dives into Relational Database Management Systems (RDBMS).

A major segment addresses distributed databases and alternative database models, covering topics across Weeks 11 and 12. Further sophisticated concepts include Semantic databases, which focus on meaning and context. Linked Data, an interconnected approach to information, is covered across Weeks 15 and 16. The scope extends to Multimedia and retrieval systems (Weeks 17 and 18). Finally, the course explores practical Applications of databases in Weeks 19 and 20. The learning culminates with preparation and the examination during Weeks 21 and 22. Throughout the course, quizzes and practice assignments are provided to reinforce key technical knowledge and patterns in ER diagrams.

---

### 07_Further_reading_Reading_1h

# Further reading
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/hdvyG/further-reading

Chen, P. ‘The entity-relationship model – Toward a unified view of data’, ACM Transactions on Database Systems 1(1) 1976, pp.9–36. This reading is available via the Online Library . Further reading Chen, P. ‘The entity-relationship model – Toward a unified view of data’, ACM Transactions on Database Systems 1(1) 1976, pp.9–36. This reading is available via the Online Library . Mark as completed Dislike Report an issue

---

## Week 5

### 01_Introduction_to_data_Integrity_and_security_Video_5_min

# Introduction to data Integrity and security
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/wUarP/introduction-to-data-integrity-and-security

This curriculum progresses through foundational database concepts, starting with "Working with Data" (Weeks 1-4) and establishing the principles of Relational Databases. A significant focus is placed on data quality, covering "Reliable databases: Data Integrity and Security" (Weeks 5-6), specifically detailing the risk of errors and the application of "Normalisation and the normal forms." Subsequent modules explore system expansion, including "Using Databases: libraries and templating" (Weeks 7-8) and advanced RDBMS topics, culminating in a Mid-term assignment in Week 10. The course transitions to advanced modeling by addressing "Distributed databases and alternative database models" (Weeks 11-12), followed by specialized systems like "Semantic databases" (Weeks 13-14) and "Linked Data" (Weeks 15-16). Technical concepts are broadened further by incorporating "Multimedia and retrieval" (Weeks 17-18) and dedicated sections on general "Applications" (Weeks 19-20). The curriculum concludes with dedicated preparation and the final exam week (Weeks 21-22).

---

### 02_Integrity_and_the_risk_of_errors_Video_9_min

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

### 03_Normalisation_and_the_normal_forms_I_Video_17_min

# Normalisation and the normal forms I
Video • 17 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/3fdUo/normalisation-and-the-normal-forms-i

This course progresses through essential data management concepts, beginning with foundational work in data handling (Weeks 1-2) and transitioning into the structure of Relational Databases (Weeks 3-4). A critical focus is placed on ensuring data quality through reliable databases, specifically covering Data Integrity and Security, which involves detailed study of Normalisation and the normal forms (Week 5). The course then explores the practical application of databases, moving into templating and library usage (Weeks 7-8) and advancing into specialized topics like Advanced RDBMS (Week 9). Subsequent weeks delve into modern database architectures, covering Distributed databases and alternative models (Weeks 11-12), Semantic databases (Weeks 13-14), and Linked Data (Weeks 15-16). Finally, the curriculum expands into complex retrieval methods, including Multimedia and retrieval (Weeks 17-18), Applications (Weeks 19-20), culminating in examination preparation and assessment.

---

### 04_Normalisation_and_the_normal_forms_II_Video_15_min

# Normalisation and the normal forms II
Video • 15 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/2EC4D/normalisation-and-the-normal-forms-ii

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

### 05_On_the_normal_forms_Reading_1h

# On the normal forms
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/CysdE/on-the-normal-forms

A gentle introduction (quite close to the lecture) is in the Database systems subject guide: Lewis, D. CO2209 Database systems. (London: University of London, 2016). normalisation.pdf PDF File The definition of the normal forms can be read here: Codd, E. 'A relational model of data for large shared data banks', Comms of the ACM 13(6) 1970, pp.377–87. This reading is available in the Online Library ....

---

### 06_Worksheet_Reliable_Databases_Data_Integrity_and_Security_(Topic_3,_Part_1)_Reading_10_min

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

## Week 6

### 01_On_ACID_Guaranteeing_a_DBMS_against_errors_Video_11_min

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

### 02_Transactions_and_serialisation_Video_21_min

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

### 03_More_depth_on_ACID_and_integrity_risks_Reading_1h

# More depth on ACID and integrity risks
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/8iC8F/more-depth-on-acid-and-integrity-risks

From the Database systems subject guide: Lewis, D. CO2209 Database systems. (London: University of London, 2016). acid-and-transactions.pdf PDF File The concept of ACID was introduced in this paper: Härder, T and A. Reuter ‘Principles of Transaction-Oriented Database Recovery’, ACM Computing Surveys, 15/4 1983. This reading is available in the Online Library . More depth on ACID and integrity risks From the Database systems subject guide: Lewis, D. CO2209 Database systems....

---

### 04_Malice_and_accidental_damage_Video_4_min

# Malice and accidental damage
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/09l8W/malice-and-accidental-damage

This course follows a comprehensive 22-week structure, beginning with foundational concepts in Weeks 1 and 2 focusing on general data manipulation. Weeks 3 and 4 dive specifically into Relational Databases, establishing the initial framework for data organization. The next major section, Weeks 5 and 6 (Topic 3), emphasizes reliable databases, centered on the critical technical concept of ACID properties to guarantee integrity during transactions. A detailed study of security, covered in Weeks 6, explores threats like malice and accidental damage, alongside implementing security and user policies using SQL. After a mid-term assignment (Week 10), the course shifts to practical usage, covering libraries and templating in Topic 4 and advanced RDBMS topics in Topic 5. The focus expands into modern architecture with Topic 6, exploring both distributed databases and various alternative database models. Topics 7, 8, and 9 introduce conceptual advances, detailing semantic databases and the mechanism of Linked Data for interconnectivity. Weeks 17 through 19 specialize in data retrieval, covering multimedia and the application of various database models. The final weeks are dedicated to real-world scenarios (Topic 10: Applications) and preparation. The course culminates in week 22 with the final examination, after the intensive preparation period in Week 21.

---

### 05_Security_and_user_policies_with_SQL_Video_11_min

# Security and user policies with SQL
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/OFcum/security-and-user-policies-with-sql

This discussion focuses on controlling user and script access to SQL databases, addressing the security vulnerability where simple data insertion could lead to malicious table drops. The critical concern is why a user needing only data insertion privileges possesses the permissions to restructure or remove tables. SQL systems provide extremely fine-grained controls, far more precise than those found in file systems or operating systems. These granular controls allow definition of privileges for creating/editing users, databases, and specific bits of data. When designing a database, one must determine the required user base and establish the minimum set of necessary privileges for each. Granting only a narrow set of privileges, such as merely the right to `SELECT` data, significantly reduces overall database risk. Sometimes, users require separate roles to ensure they only possess the expected permissions at specific points in time or through different access points.

The mechanism for granting privileges is straightforward, utilizing the command structure: `GRANT [privilege] ON [object] TO [user]`. For example, to create a read-only account, one would use `GRANT SELECT ON databases TO username`. If a user needs to add data but not restructure the table, a suitable privilege combination is `SELECT, INSERT`. Conversely, a powerful combination like `GRANT SELECT, INSERT, DROP` allows for table removal, illustrating the risk of excessive privileges. User creation itself requires the `CREATE USER [name] IDENTIFIED BY [password]` command, though plain text passwords are insecure. The database management system (DBMS) handles internal password encryption, and database management, being relational, is managed through tables.

A key modifier is `WITH GRANT OPTION`, a clause added to the `GRANT` command, allowing the user to pass their privileges on to other users. Privileges can be withdrawn using the `REVOKE` command, which shares the same syntax as `GRANT`. Roles offer an essential abstraction, allowing a generic set of privileges to be assigned without creating a permanent user account. For instance, an 'Astronomer' role might be created first, and then individuals are assigned that role using `GRANT astronomer TO username`. Roles are crucial for efficiently managing users who frequently switch between different operational sets of privileges. The core security principle is minimizing privileges—constraining user access limits the impact of both accidental errors and malicious actions. While playing around with databases, users often operate as a root user; in production systems, reducing privileges must be a core application design decision, not an afterthought.

---

### 06_Topic_3_summary_Video_2_min

# Topic 3 summary
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/LPn0s/topic-3-summary

The curriculum initiates the study of data management with an initial focus on working with data (Topics 1, Weeks 1-2) followed by a detailed exploration of Relational Databases (Topic 2, Weeks 3-4). Topics 3 (Weeks 5-6) delve into reliable database design, dedicating significant focus to Data Integrity and Security. A critical technical component of this section is the concept of ACID (Atomicity, Consistency, Isolation, Durability), which guarantees the reliability of the DBMS against errors, alongside intensive study of transaction processing and serialisation.

The curriculum then expands into practical applications, covering the use of databases through libraries and templating systems (Topic 4, Weeks 7-8). Following this, the focus shifts to more advanced RDBMS topics (Topic 5, Weeks 9-10), culminating in a mid-term assignment.

The later sections tackle scalability and modernization, covering Distributed databases and various alternative database models (Topic 6, Weeks 11-12). Further advanced concepts include Semantic databases (Topic 7, Weeks 13-14) and Linked Data principles (Topic 8, Weeks 15-16). The scope broadens again to include Multimedia and retrieval systems (Topic 9, Weeks 17-18).

The program concludes with practical application studies in various database applications (Topic 10, Weeks 19-20), preparing the student for the final examination. These advanced topics ensure a comprehensive understanding of modern data models, moving from simple relational structures to complex, distributed, and semantic architectures.

---

### 07_Further_reading_Reading_1h

# Further reading
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/hdvyG/further-reading

Chen, P. ‘The entity-relationship model – Toward a unified view of data’, ACM Transactions on Database Systems 1(1) 1976, pp.9–36. This reading is available via the Online Library . Further reading Chen, P. ‘The entity-relationship model – Toward a unified view of data’, ACM Transactions on Database Systems 1(1) 1976, pp.9–36. This reading is available via the Online Library . Mark as completed Dislike Report an issue

---

## Week 7

### 01_Introduction_to_using_relational_databases_Video_1_min

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

### 02_Speaking_to_databases_III_the_core_vocabulary_Video_8_min

# Speaking to databases III: the core vocabulary
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/z8SMB/speaking-to-databases-iii-the-core-vocabulary

This curriculum outlines a comprehensive journey into database management, beginning with foundational concepts in data handling during Weeks 1 and 2. The focus then shifts to mastering Relational Databases (RDBMS) in Weeks 3 and 4, followed by ensuring data reliability through topics on Data Integrity and Security in Weeks 5 and 6. Subsequent learning utilizes these databases for web applications, introducing tools like Node.js and mustache for templating, and PHP SQL libraries for backend functionality (Weeks 7 and 8). Advanced RDBMS concepts are covered in Week 9, before the study progresses to more diverse architectures in Weeks 11 and 12, focusing on Distributed databases and alternative database models. The curriculum then explores specialized data structures, dedicating Weeks 13 and 14 to Semantic databases. Further modernization includes Weeks 15 and 16, which detail the implementation of Linked Data. The final technical phases involve Multimedia and retrieval processes (Weeks 17 and 18), culminating in practical Applications (Weeks 19 and 20). Throughout the course, practical labs are integrated, such as exploring movie data and connecting to an SQL RDBMS. This structured approach prepares students for the Mid-term assignment in Week 10 and the final Exam in Week 22.

---

### 03_Getting_practice_with_MySQL_(Lab_introduction)_Video_17_min

# Getting practice with MySQL (Lab introduction)
Video • 17 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/pwwgx/getting-practice-with-mysql-lab-introduction

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

### 04_Connecting_to_an_SQL_RDBMS_Video_5_min

# Connecting to an SQL RDBMS
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/bhQOt/connecting-to-an-sql-rdbms

This curriculum provides a comprehensive study of database systems, beginning with foundational concepts in Week 1 and Week 2 on Working with Data. The study progresses to Relational Databases (Weeks 3 and 4), followed by critical modules in Weeks 5 and 6 detailing Data Integrity and Security to ensure reliable database operation. Practical application begins in Week 7 and Week 8, focusing on using libraries and templating for data retrieval. Specific technical implementations are detailed through labs connecting to an SQL RDBMS, utilizing Node.js and Mustache for web page serving, and implementing PHP SQL libraries. Advanced theoretical exploration begins in Week 9 with advanced RDBMS topics, transitioning into Week 11 and Week 12 to cover Distributed databases and alternative database models. The curriculum then moves into specialized paradigms, dedicating Weeks 13 and 14 to Semantic databases, and Weeks 15 and 16 to the concepts of Linked Data. Retrieval techniques are covered in Weeks 17 and 18 through the topic of Multimedia and retrieval. The final segment, Weeks 19 and 20, concentrates on database Applications, culminating in comprehensive exam preparation in Week 21 and the final exam in Week 22. The course includes a mid-term assignment in Week 10 to assess understanding across the initial core concepts.

---

### 05_Using_node.js_and_mustache_Video_10_min

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

### 06_Using_PHP_SQL_libraries_Video_4_min

# Using PHP SQL libraries
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/SWYlA/using-php-sql-libraries

This curriculum provides a comprehensive, 22-week study of database systems, beginning with foundational concepts in data working (Weeks 1 & 2). The focus quickly shifts to Relational Databases (RDBMS) in Weeks 3 and 4, followed by crucial modules on Data Integrity and Security for reliable database management (Weeks 5 & 6). Weeks 7 and 8 introduce practical application development, demonstrating how to connect databases using libraries and templating in web service contexts.

A core practical element is detailed in Week 4, where students learn to connect to an SQL RDBMS, coupled with hands-on practice using MySQL. Furthermore, the curriculum covers specific technologies for web serving, including the use of node.js and mustache for database backends (Week 4.1), alongside integrating PHP SQL libraries.

Later modules explore advanced database paradigms, commencing with complex RDBMS topics (Week 9) and moving into Distributed databases and alternative models (Weeks 11 & 12). The specialization continues with a deep dive into Semantic databases (Weeks 13 & 14) and the principles of Linked Data (Weeks 15 & 16).

The final phase of the course broadens scope to include Multimedia and retrieval (Weeks 17 & 18) and culminates in studying various real-world Applications of database systems (Weeks 19 & 20). The instruction integrates multiple learning methods, including dedicated Lab work, specific video tutorials, and practical quizzes, culminating in a Mid-term assignment and final exam preparation.

---

## Week 8

### 01_Using_libraries_to_update_data_in_a_database_Video_9_min

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

### 02_Connecting_to_mysql_from_node_User_definitions_Reading_10_min

# Connecting to mysql from node: User definitions
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/R3oP4/connecting-to-mysql-from-node-user-definitions

Database security dictates that users must be defined with specific access restrictions. These restrictions define not only the database parts allowed and the permitted activities but also the network locations from which connection is possible. When hosting a web server, it is often advisable to restrict user access exclusively to the local machine, or `localhost`. This ensures that attempts at accessing the database remotely are automatically rejected.

On the specific lab machines used, defining a user as `'username'@'localhost'` can lead to connection refusals from a Node.js application. This issue stems from how the MySQL instance interprets `localhost`. Specifically, our MySQL instance defaults to treating `localhost` as a UNIX socket connection. In contrast, the Node.js application inherently connects using TCP/IP by default.

To resolve this conflict, two distinct methods are available to ensure successful connectivity. The first solution involves altering the user definition within the database. Instead of using the constrained local access, the connection limit must be removed by creating the user as `'username'@'%'`. This allows connections from any network host.

The second viable solution involves forcing the Node.js application to utilize a UNIX socket connection instead of relying on TCP/IP. This requires modifying the connection definition within the JavaScript file, such as `index.js`. Specifically, one must add the parameter `socketPath: "/var/run/mysqld/mysqld.sock"`.

Crucially, the user only needs to implement one of these two specified fixes. Following either approach will allow the lab environment to function correctly. It should be noted that these particular connection issues are specific to the lab environment and are less likely to occur when connecting to other database servers.

---

### 03_Python_for_databases_how_and_why_Video_5_min

# Python for databases: how and why?
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/0LUJP/python-for-databases-how-and-why

This curriculum provides a comprehensive study of database systems, starting with basic data handling in Weeks 1 and 2. The core focus shifts in Weeks 3 and 4 to Relational Databases, followed by Weeks 5 and 6, which address the critical aspects of Data Integrity and Security. Database utilization is introduced in Weeks 7 and 8, emphasizing libraries and templating for practical data management. Hands-on application exercises include connecting to MySQL from Node, utilizing Python for database exploration, and plotting data via pyplot. The advanced topics begin in Week 9 with an exploration of advanced RDBMS concepts, leading to a Mid-term assignment in Week 10. Weeks 11 and 12 cover the complexities of Distributed databases and alternative database models. Subsequent modules delve into specialized architectures, including Semantic databases (Weeks 13-14) and Linked Data (Weeks 15-16). Modern data challenges are addressed through Weeks 17-18 on Multimedia and retrieval, and Weeks 19-20 on various database Applications. The intensive learning process concludes with Week 21 dedicated to preparation and Week 22 for the final exam.

---

### 04_Topic_4_summary_Video_2_min

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

### 05_Further_reading_Reading_1h

# Further reading
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/KSA6I/further-reading

Look at the documentation for your favoured language or programming environment. These should always be the first place you look for examples and guidance – they are more likely to be up to date than third party sites are. nodejs PHP Python For those interested in R, there is documentation at Databases using R . Several other languages are detailed in the connectors section of the developer area of the MySQL website. If these links are broken, please let us know via the Student Portal ....

---

## Week 9

### 01_Introduction_to_Advanced_RDBMS_topics_Video_2_min

# Introduction to Advanced RDBMS topics
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/OAKgw/introduction-to-advanced-rdbms-topics

This course structure begins by establishing foundational concepts in data handling (Week 1-2) and Relational Databases (Week 3-4), followed by critical modules on ensuring system reliability through Data Integrity and Security (Week 5-6). The curriculum transitions to practical application by covering libraries and templating for database use (Week 7-8), before introducing Advanced RDBMS topics (Week 9). A key focus within Advanced RDBMS is improving Query efficiency through the analysis of join-based queries and strategically using denormalization to boost performance. Subsequent modules explore alternative architectures, specifically Distributed databases, Semantic databases, and Linked Data (Week 11-16), before delving into Multimedia and retrieval systems (Week 17-18). The course culminates with a study of practical Applications (Week 19-20), culminating in a Mid-term assignment (Week 10) and final exam preparation (Week 21-22).

---

### 02_Query_efficiency_Video_33_min

# Query efficiency
Video • 33 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/nEItW/query-efficiency

This transcript provides a deep dive into **query efficiency** in relational databases, demonstrating how the database engine optimizes complex `JOIN` operations by leveraging indexes and choosing the correct execution strategy.

Here is a summary of the key concepts, experiments, and takeaways:

---

### 🚀 Core Concepts Discussed

**1. Query Execution and Joins:**
The lecture focuses on joining two tables (`movie_locations` and `actors`). The database engine must decide the most efficient way to match rows between these tables.

**2. Hash Join:**
In the initial stages, when joining the 40,000 rows in the `actors` table, the database uses a **Hash Join**. This relatively modern technique builds a hash table while copying data, allowing the engine to filter the massive dataset very quickly (estimating that only 10% of the rows are relevant).

**3. The Role of Indexes:**
Indexes are crucial for performance, but their *placement* (on which column) dictates the success of the query. They allow the database to avoid slow, full table scans.

**4. `EXPLAIN ANALYZE`:**
The most important tool discussed is `EXPLAIN ANALYZE`. This command doesn't just tell you *what* the query *will* do (the plan); it actually **runs the query** (or a dummy run), providing a breakdown of how long each stage takes and estimating the operational cost.

---

### 🧪 The Experimental Results (Optimization Attempts)

The speaker conducted two experiments by strategically adding indexes to see how the query planner reacted:

**➡️ Experiment 1: Index on `movie_locations` for `actors`**
*   **Action:** An index was created on `movie_locations` related to `actors`.
*   **Result:** The query planner changed the order, allowing the engine to filter the necessary data much faster in the second stage (only needing to consider 7 rows). This led to a significant speedup.

**➡️ Experiment 2: Index on `actors.names`**
*   **Action:** An index was created specifically on the `actors.names` column.
*   **Result:** This produced the most dramatic speed improvement. The query no longer needed to "search" or estimate; it could use its prepared indexes directly from the start. **This run was shown to be up to 10 times faster than the initial baseline run.**

---

### 🎯 Key Takeaways and Best Practices

1.  **Strategy Over Existence:** Simply adding an index is not enough. You must understand *which* indexes the query planner needs and *where* to place them to force the database to use the most efficient join order.
2.  **Use `EXPLAIN ANALYZE`:** Never judge query performance based on a single timing measurement. Use `EXPLAIN ANALYZE` to understand the underlying cost model and to run the query many times to account for system overhead.
3.  **Cost Management:** Database operations have computational costs. The speaker noted that in some cases, it might be more efficient to shift the final processing burden away from the central database server and handle it on the web server or client side to save server effort.

---

### 03_Removing_the_safety_net_denormalisation_Video_8_min

# Removing the safety net: denormalisation
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/V9ETv/removing-the-safety-net-denormalisation

This course progression begins with foundational concepts in working with data, transitioning through the core principles of Relational Databases and establishing necessary structures for Data Integrity and Security. Subsequent modules detail the application of databases via libraries and templating, culminating in an exploration of Advanced RDBMS topics. A critical focus in advanced RDBMS includes performance optimization, covering Query efficiency and the strategic approach of "Removing the safety net: denormalisation." The curriculum then expands into modern architectures, covering Distributed databases and alternative database models, followed by dedicated study of Semantic databases. Specialized data handling is addressed through modules on Linked Data and Multimedia and retrieval. Finally, the course explores practical Applications and concludes with exam preparation, ensuring a comprehensive understanding of database theory and practice.

---

### 04_Topic_5_summary_Video_6_min

# Topic 5 summary
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/1OwyJ/topic-5-summary

The text summarizes the conclusion of a detailed study of Relational Database Management Systems (RDBMS) and Relational Theory. RDBMS are described as powerful generalist tools capable of handling a wide variety of situations efficiently. These systems benefit from over forty years of intensive optimization work, resulting in significant efficiency gains despite modern, more powerful hardware. Their effectiveness is fundamentally grounded in theory, providing a reliable framework for understanding their behavior. Crucially, RDBMS theory allows for the provable validation of the ACID properties under specific, known conditions.

The relational database structure is highly adaptable because it utilizes a single, simple fundamental unit: the table. While mature relational databases have evolved and enriched their features, their core structure remains well understood across different providers. This standardization facilitates ease of movement between systems, as exemplified by alternatives like MariaDB and PostgreSQL maintaining syntax compatibility with MySQL. This commitment to standards is a significant advantage, helping manage system migration efforts.

However, RDBMS are weak regarding minor, specialized "tweaks" or adaptations. While the relational model is best suited for tabular data, users should recognize that if their information strains to fit the table structure, the RDBMS may not be the ideal solution. The theoretical nature of RDBMS can pose drawbacks, often manifesting as a large initial learning curve and a perception of confusing complexity. This intimidating nature is identified as a common reason why some users opt for alternative database models.

The curriculum structure provides specific insights into RDBMS application and enhancement. Topic 5, titled Advanced RDBMS topics, covers methods for speeding up query efficiency. This includes a dedicated video on analyzing join-based queries and a module on denormalization. Denormalization is introduced as a strategy for removing safety nets and improving speed.

Beyond the immediate topic, the course structure points to future study on alternative and advanced database architectures. Weeks 11 and 12 will cover distributed databases and other alternative database models. Semantic databases are explored in Weeks 13 and 14, followed by Linked Data in Weeks 15 and 16. Later modules address Multimedia and retrieval (Weeks 17-18) and general Applications (Weeks 19-20). Technical interface details include navigation shortcuts such as CTRL + S to save notes, and the use of H J K L keys for screen reader compatibility. The overall study moves from foundational data handling (Weeks 1-2) to data integrity and security (Weeks 5-6).

---

