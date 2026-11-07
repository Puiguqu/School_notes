# Week 19 - CM3010 Databases and Advanced Data Techniques - Topic 1: Working with Data - part 1 - Week 1

## 01_Exploring_practical_considerations_through_examples_Video_2_min

# Exploring practical considerations through examples
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/fEMVE/exploring-practical-considerations-through-examples

This curriculum covers database management, beginning with foundational concepts in Weeks 1 and 2 ("Working with Data - part 1" and "part 2"). Weeks 3 and 4 focus on Relational Databases, establishing the core structure for data organization. Subsequently, Weeks 5 and 6 delve into data reliability, emphasizing critical concepts of Data Integrity and Security. The application of these concepts starts in Week 7 and Week 8 ("Using Databases: libraries and templating - part 1" and "part 2").

The study expands into advanced database theory, covering "Advanced RDBMS topics" in Week 9, followed by a Mid-term assignment in Week 10. The focus broadens significantly in Week 11 and Week 12, exploring Distributed databases and alternative database models. Weeks 13 and 14 introduce Semantic databases, followed by a deep dive into Linked Data in Weeks 15 and 16.

The curriculum then transitions to multimedia management, covering "Multimedia and retrieval" in Weeks 17 and 18. The final major topic block, Week 19 and Week 20 ("Applications - part 1" and "part 2"), uses practical examples to demonstrate real-world database use. Specifically, the course details projects such as mapping medieval manuscript migrations across three databases. Further technical examples include using The collector: Schoenberg Database of manuscripts, the Bibale research institute database, and the Medieval manuscripts in Oxford Libraries database. These practical case studies are supplemented by quizzes, practice assignments, and discussion prompts, preparing students for the final exam in Week 21.

---

## 02_Mapping_manuscript_migrations_a_tale_of_3_databases_Video_18_min

# Mapping manuscript migrations: a tale of 3 databases
Video • 18 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/SecSD/mapping-manuscript-migrations-a-tale-of-3-databases

Different stakeholders require different data views for the same object, such as a book or manuscript, leading to diverse data models and organizational requirements. This video examines how three distinct groups created three different databases based on their unique interests, demonstrating how different views shape database design

---

## 03_The_collector_Schoenberg_Database_of_anuscripts_Video_8_min

# The collector: Schoenberg Database of anuscripts
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/h7urs/the-collector-schoenberg-database-of-anuscripts

This course systematically covers fundamental to advanced concepts in database systems across twenty-two weeks. Initial modules introduce working with data, followed by an in-depth study of Relational Databases (Weeks 3 and 4). Reliable database operation is addressed in Weeks 5 and 6, focusing on critical concepts of Data Integrity and Security. Subsequently, the course explores practical implementation by detailing how databases are used through libraries and templating (Weeks 7 and 8).

Advanced database theory is covered in Week 9, before transitioning to more complex architectures in Weeks 11 and 12, specifically focusing on Distributed databases and alternative database models. Topics then progress to specialized database types, including Semantic databases (Weeks 13 and 14) and the integration of Linked Data (Weeks 15 and 16).

Further specialized topics include Multimedia and retrieval (Weeks 17 and 18), culminating in an exploration of real-world Applications in Weeks 19 and 20. Practical applications are illustrated through examples, such as mapping manuscript migrations, and case studies featuring specific systems like The collector: Schoenberg Database of Manuscripts and the research institute Bibale.

The curriculum utilizes various resources, including videos and quizzes, to reinforce learning, demonstrated by assignments associated with topics such as medieval manuscripts in Oxford Libraries. The course structure ensures a thorough understanding of database architecture, moving from standard relational models to cutting-edge concepts like semantic and distributed systems. Week 10 marks the mid-term assessment, while Week 21 prepares students for the final examination, which takes place in Week 22.

---

## 04_The_collector_Schoenberg_Database_of_Manuscripts_Reading_1h

# The collector: Schoenberg Database of Manuscripts
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/rPkzI/the-collector-schoenberg-database-of-manuscripts

The Schoenberg Database of Manuscripts (SDBM) is accessible at the following link: https://sdbm.library.upenn.edu/. For a high-level understanding of the data model, slides detailing the structure are available directly on the site. The accompanying user manual provides crucial insight into how the data is structured, specifically addressing the degree of explicitness in both the database itself and the data entry documentation. The core functions and structure of the SDBM, managed by The collector: Schoenberg Database of Manuscripts, can be learned through these resources. If any of the provided links are found to be broken, users are instructed to notify the appropriate party via the Student Portal.

---

## 05_The_research_institute_Bibale_Video_9_min

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

## 06_Bibale_and_IRHT_Reading_1h

# Bibale and IRHT
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/6Aope/bibale-and-irht

Bibale is a digital tool utilized by the IRHT for researching manuscript provenance; a comprehensive introduction to its data model and role is found in H. Wijsman’s article, 'The Bibale database at the IRHT: A digital tool for researching manuscript provenance,' published in *Manuscript Studies* 1(2) 2017, pp.328–341. For technical maintenance, users are instructed to report any broken link related to this resource via the Student Portal.

---

## 07_The_library_Medieval_manuscripts_in_Oxford_Libraries_Video_17_min

# The library: Medieval manuscripts in Oxford Libraries
Video • 17 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/LR5Yd/the-library-medieval-manuscripts-in-oxford-libraries

This course progresses through fundamental database concepts, beginning with introductory work with data (Week 1 & 2). The curriculum moves into Relational Databases (Week 3 & 4), establishing the core principles of structured data management. Subsequently, Weeks 5 and 6 address the critical need for reliable databases by focusing on Data Integrity and Security. The course then delves into practical application using databases via libraries and templating (Week 7 & 8).

Advanced RDBMS topics are covered in Week 9, preparing students for the Mid-term assignment in Week 10. The focus shifts dramatically in Weeks 11 and 12, exploring Distributed databases and alternative database models. Subsequent sections cover specialized conceptual models, starting with Semantic databases (Week 13 & 14). Weeks 15 and 16 are dedicated to understanding Linked Data, a key component of modern information systems.

The curriculum also includes Multimedia and retrieval techniques (Week 17 & 18), followed by practical applications in Week 19. Topic 10, Applications, introduces practical considerations through examples, including case studies like databases of medieval manuscripts. Specific examples are detailed, such as mapping manuscript migrations, The collector: Schoenberg Database of Manuscripts, Bibale, and Medieval manuscripts in Oxford Libraries. These final weeks reinforce learning with the completion of Part 2 of Applications (Week 20) and preparation for the final exam (Week 21 & 22).

---

## 08_Mapping_manuscript_migrations_Putting_it_together_Video_5_min

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

