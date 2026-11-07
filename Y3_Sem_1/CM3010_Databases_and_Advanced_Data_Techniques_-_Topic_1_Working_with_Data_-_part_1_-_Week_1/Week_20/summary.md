# Week 20 - CM3010 Databases and Advanced Data Techniques - Topic 1: Working with Data - part 1 - Week 1

## 01_Mapping_manuscript_migrations_Putting_it_together_Video_12_min

# Mapping manuscript migrations: Putting it together
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/e1pZb/mapping-manuscript-migrations-putting-it-together

This course provides a comprehensive curriculum on data management, structured across 22 weeks. The initial weeks focus on foundational topics, starting with "Working with Data - part 1" (Week 1) and "Working with Data - part 2" (Week 2). Following this, the course delves into "Relational Databases - part 1" and "Relational Databases - part 2" (Weeks 3 and 4). Weeks 5 and 6 address the vital concepts of "Reliable databases: Data Integrity and Security - part 1" and "Reliable databases: Data Integrity and Security - part 2."

The module structure continues by exploring practical database use, covering "Using Databases: libraries and templating - part 1" and "Using Databases: libraries and templating - part 2" (Weeks 7 and 8). Week 9 is dedicated to "Advanced RDBMS topics - part 1," preceding the mid-term assignment in Week 10.

A significant portion of the curriculum addresses complex database architectures, beginning with "Distributed databases and alternative database models - part 1" and concluding with "Distributed databases and other database models - part 2" (Weeks 11 and 12). Following this, the focus shifts to specialized paradigms, specifically "Semantic databases - part 1" and "Semantic databases - part 2" (Weeks 13 and 14). These are succeeded by "Linked Data - part 1" and "Linked Data - part 2" (Weeks 15 and 16).

Later topics broaden the scope to include "Multimedia and retrieval - part 1" and "Multimedia and retrieval - part 2" (Weeks 17 and 18), and finally "Applications - part 1" and "Applications - Part 2" (Weeks 19 and 20). Week 10 also features "Practical examples: Combining databases of medieval manuscripts," detailing videos like "Mapping manuscript migrations: Putting it together" (12 min) and "MMM modelling" (29 min), each with associated quizzes and practice assignments.

The curriculum also addresses data structure in Section 10.3, with videos exploring "What shape is my data?" (3 min) and "What shape do I want my data to be?" (2 min). The course culminates with a final preparation week (Week 21) and the exam week (Week 22).

---

## 02_MMM_modelling_Video_29_min

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

## 03_MMM_Data_conversion_Video_10_min

# MMM Data conversion
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/xjsT3/mmm-data-conversion

The curriculum progresses from foundational concepts in data management, starting with an intensive focus on "Working with Data" (Weeks 1 and 2). The core of database theory is established in Weeks 3 and 4, detailing the principles of Relational Databases. Subsequently, Weeks 5 and 6 address the critical topic of "Reliable databases," focusing specifically on Data Integrity and Security mechanisms.

The practical application of these concepts begins in Weeks 7 and 8, covering the use of databases via libraries and templating. This foundational knowledge is advanced in Week 9 with a deep dive into advanced RDBMS topics, leading up to a Mid-term assignment in Week 10.

The course then shifts to modern architectural paradigms, covering Distributed Databases and alternative database models across Weeks 11 and 12, which addresses scalability. Following this, Weeks 13 and 14 introduce Semantic databases, emphasizing knowledge representation and the meaning of data.

The sequence continues with Weeks 15 and 16 dedicated to Linked Data, a vital technique for connecting disparate datasets across the web. Concepts expand further in Weeks 17 and 18 to cover Multimedia and retrieval techniques for complex data types. Weeks 19 and 20 synthesize all prior learning by focusing on real-world Applications.

Week 20 features practical examples, notably the project combining medieval manuscript databases (MMM). This case study reinforces data modeling through sections like "What shape is my data?" and "What shape do I want my data to be?" The material concludes with a final preparation week (Week 21) leading to the comprehensive examination in Week 22.

---

## 04_MMM_user_interfaces_Video_9_min

# MMM user interfaces
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/G9c2T/mmm-user-interfaces

The project was designed to create a sophisticated and rich resource suitable for humanities and manuscript scholars. This effort involved building a complex dataset that significantly surpasses the complexity of the individual sources it incorporates. Although user studies were conducted, limited resources prevented the development of a cutting-edge, highly sophisticated user interface. The primary goal was not to build a single perfect interface, but rather to demonstrate the potential of the merged data itself.

One initial realization was that the data is the core asset, and the interfaces are merely tools for its interrogation. The first created tool was a relatively straightforward web database structure, accessible at `manuscriptmigrations.org`. This database provided a faceted browsing interface, allowing users to track the migrations and locations of resources. For example, it could trace all sources of Josephus copied in France and visualize their subsequent travel. However, this first interface was ultimately limited, slow, and "boxed in" regarding the types of research questions that could be asked.

The project then built a second interface, "Research Space," which was funded by the British Museum and utilizes the C.CRM data model. This alternative interface enabled a more exploratory and browsing-based approach to inquiry. By utilizing a path of exploration, users could build up the size and complexity of their initial research questions. The existence of these two distinct paradigms proved that fundamentally different ways of exploring data can be applied to the same underlying information.

A critical turning point occurred when domain specialists initially criticized the primitive interfaces, viewing the UI limitations as deficiencies in the data itself. The project corrected this perception by teaching researchers to utilize a query language called Sparkle. Sparkle allowed the scholars to directly construct complex queries, revealing the true richness of the merged dataset. This provided an interesting contrast between the intuitive accessibility of a shiny UI and the power and expressiveness achievable programmatically.

Researchers evaluated twenty-five clear and unambiguous research questions against the databases to gauge their feasibility. Of these, eight questions proved impossible to answer using the Bibale Database. Likewise, six questions were impossible to answer solely with the SDBM database. The successful combination of these diverse datasets ensured that no questions remained unanswerable. Ultimately, 17 of the 25 research questions were fully answered using the combined databases (a success rate of 79%). While the combined data was often difficult to navigate via the user interfaces, the process became significantly easier when leveraging Sparkle. This project successfully demonstrated the crucial ability to combine different data models and approaches to create a synergy greater than the sum of its individual parts.

---

## 05_The_mapping_manuscript_migrations_project_Reading_1h

# The mapping manuscript migrations project
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/Hb82v/the-mapping-manuscript-migrations-project

The Manuscript Migrations Project (MMM) is introduced as a major initiative focused on metadata harmonization. The clearest published description of this project is found in the article, ‘Harmonizing and publishing heterogeneous premodern manuscript metadata as linked open data.’ This article was authored by Koho and numerous colleagues and published in the *Journal of the Association for Information Science and Technology* in 2021, spanning pages 1–18. For further information on the MMM project, the resource mappingmanuscriptmigrations.org is provided. Users are directed to explore the interface on this specific website for all coming discussions. Students are expected to utilize the interface on mappingmanuscriptmigrations.org throughout the course. Lastly, any instances where these provided links are broken must be reported via the Student Portal.

---

## 06_What_shape_is_my_data_Video_3_min

# What shape is my data?
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/2JxLy/what-shape-is-my-data

This course provides a comprehensive, 22-week curriculum focused on data management and advanced database systems. The foundational learning begins with Weeks 1 and 2, covering fundamental concepts in "Working with Data - part 1 and part 2." Weeks 3 and 4 transition into structured data management, detailing "Relational Databases - part 1 and part 2."

A significant emphasis is placed on reliability in Weeks 5 and 6, dedicated to "Reliable databases: Data Integrity and Security - part 1 and part 2." Subsequent weeks focus on implementation, with Weeks 7 and 8 exploring "Using Databases: libraries and templating - part 1 and part 2." Week 9 covers "Advanced RDBMS topics - part 1," consolidating deep knowledge of Relational Database Management Systems.

The scope expands in Weeks 11 and 12 to "Distributed databases and alternative database models - part 1 and part 2." Further specialization continues in Weeks 13 and 14, analyzing "Semantic databases - part 1 and part 2," followed by a deep dive into the modern framework of "Linked Data - part 1 and part 2" (Weeks 15 and 16).

Technical applications are explored in Weeks 17 and 18 through "Multimedia and retrieval - part 1 and part 2," leading into practical "Applications" in Weeks 19 and 20. The latter part of the course features a practical project, "10.2 Practical examples: Combining databases of medieval manuscripts," which includes specific exercises such as "Mapping manuscript migrations" (Video, 12 min) and "MMM modelling" (Video, 29 min).

Additional technical concepts addressed include "10.3 What shape does my data want to be?" and "10.4 Summary - Further reading." The structure culminates with Week 21 dedicated to exam preparation, followed by the comprehensive Week 22 examination.

---

## 07_What_shape_do_I_want_my_data_to_be_Video_2_min

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

## 08_Further_reading_Reading_1h

# Further reading
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/iCo6k/further-reading

The discussion centers on the field of linking diverse musical datasets across different academic disciplines. The author of the introduction notes that their own perspective on dataset linkage is rooted in a historical background. Johanna Devaney addresses this question by proposing a contrasting methodological framework. Devaney's approach significantly shifts the focus toward perceptual and analytical aspects of music data. The core of her work utilizes note-level music encodings as a mechanism for analysis. This technical tool is employed to facilitate interdisciplinary research efforts. The overarching objective of this research is to better understand human engagement with music. The study is detailed in the article by Devaney, J. The full citation is: Devaney, J. ‘Using note-level music encodings to facilitate interdisciplinary research on human engagement with music’. This research was published in *Transactions of the International Society for Music Information Retrieval*, specifically in volume 3(1) from 2020. Readers seeking this material are directed to search for the article within the Online Library.

---

