# Week 15 - CM3010 Databases and Advanced Data Techniques - Topic 1: Working with Data - part 1 - Week 1

## 01_Introduction_to_Linked_Data_and_the_Semantic_Web_Video_9_min

# Introduction to Linked Data and the Semantic Web
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/MWlQe/introduction-to-linked-data-and-the-semantic-web

This course provides a comprehensive exploration of data management, beginning with foundational concepts in working with data (Weeks 1-2) and progressing through the structure of Relational Databases (Weeks 3-4). Key security and robustness concepts are covered in Topic 3, focusing on Data Integrity and Security within reliable databases (Weeks 5-6). The curriculum transitions into practical application, addressing how databases are used via libraries and templating (Weeks 7-8) and delves into Advanced RDBMS topics (Week 9).

A major shift occurs with the study of modern infrastructure, covering Distributed databases and alternative database models (Weeks 11-12). The focus then pivots to highly abstract structures with the study of Semantic databases (Weeks 13-14).

Topics 8 and 16 specifically introduce Linked Data and the Semantic Web, initiating the deep dive into graph-based data models. This section emphasizes RDF (Resource Description Framework) as the foundational model and its various serializations, facilitating thinking in graphs. To achieve semantic meaning in Linked Data, the course utilizes Web ontologies, providing modules on choosing, designing, and evaluating these complex models.

The later stages continue this theme by covering Linked Data in depth (Week 16) and expanding into broader applications, including Multimedia and retrieval (Weeks 17-18) and various real-world Applications (Weeks 19-20). The course culminates in preparatory phases and the final Examination.

---

## 02_Open,_Linked_and_Data_Video_6_min

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

## 03_Tim_Berners-Lee's_Proposal_inventing_the_web_Reading_1h

# Tim Berners-Lee's Proposal – inventing the web
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/Dkq8p/tim-berners-lees-proposal-inventing-the-web

Tim Berners-Lee's original proposal for the Web was submitted to his managers at the CERN particle physics laboratories. This document, titled 'Information management: A proposal', is described as fascinating and highly accessible. The text provides insight into how the burgeoning Web fit into the context of existing hypertext systems. Most critically, the proposal shows that Berners-Lee was thinking beyond the constraints of mere HTML. He advocated for a more comprehensive Web that utilized the power of Linked Data. The official source material is cited as: Berners-Lee, T. 'Information management: A proposal', CERN 1989, converted and republished by W3C. Users can access the material under the heading "Tim Berners-Lee's Proposal – inventing the web." Furthermore, users are advised to contact the Student Portal if the associated link is found to be broken.

---

## 04_RDF_the_model_and_its_serialisations_Video_26_min

# RDF: the model and its serialisations
Video • 26 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/OJCTr/rdf-the-model-and-its-serialisations

This course comprehensively covers database management, beginning with foundational skills in data handling (Weeks 1-2) and advancing into the structure of relational databases (Weeks 3-4). Key early topics include ensuring reliable database operations through detailed study of data integrity and security principles (Weeks 5-6). The curriculum then shifts to practical application, exploring how databases are utilized through libraries and templating, alongside advanced Real-World Database Management System (RDBMS) topics (Weeks 7-9). Subsequent modules tackle system architecture by introducing the concepts of distributed databases and alternative database models (Weeks 11-12). A major conceptual transition occurs with the study of semantic databases (Weeks 13-14), which lays the groundwork for modern interconnected data systems. The course dedicates significant time to Linked Data (Weeks 15-16), focusing on how information can be interconnected across the Semantic Web. Technical details are explored in depth through RDF: the model and its various serialisations, emphasizing the importance of thinking in graphs. Furthermore, the material delves into Web ontologies (Weeks 8.2), covering the design, evaluation, and utilization of structured knowledge representations. The syllabus also addresses multimedia and retrieval methods (Weeks 17-18), preparing students for diverse modern data applications (Weeks 19-20). The final segments involve preparation for the comprehensive exam (Week 21) and a dedicated focus on the underlying principles of RDF (Week 22). This progression moves from basic data manipulation through relational systems to advanced conceptual models like distributed and semantic data structures.

---

## 05_Thinking_in_graphs_Video_5_min

# Thinking in graphs
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/WeWqh/thinking-in-graphs

The discussion centers on the nature and complexity of working with graphs and graph diagrams in modeling abstract concepts. Some individuals find this abstract modeling liberating, while others find it intimidating due to its lack of concrete structure. Modeling begins by selecting a point in a semantic space, which is typically marked with a circle and a name. Initial simple relationships, such as "Film has cast member actor," are often oversimplified for complex real-world data. For instance, merely attaching a role to an actor's URI only provides a list of roles without connecting them to the specific film. A more complex structure is required, such as "Film has a role which is a character" and "That character is played by an actor." Furthermore, complex systems require even greater intricacy, such as differentiating between a young and an old version of the same character. A general rule advises utilizing existing structures developed by others, provided they are adopted critically.

Graphs differ fundamentally from structures like JSON and XML, which inherently possess a hierarchical tree structure. Crucially, graphs lack an inherent, fixed order. This lack of order is especially important in a web environment where graph components may arrive unpredictably from different servers or URLs. In graph theory, any combination of a circle, an arrow, and another circle constitutes exactly one triple. Once a graph is drawn, it can be easily translated into RDF serialization, which effectively stores all data. Extracting data involves counting the cycles and areas within the finalized graph structure.

Beyond the graph concept, the course structure details a comprehensive exploration of database models. Topics progress from Week 1 (Working with Data - part 1) through Week 6 (Reliable databases: Data Integrity and Security - part 2). This leads into Week 11 and Week 12, which focus on Distributed databases and alternative database models. A major shift occurs in Weeks 13 through 15, dedicated to Semantic databases and Linked Data.

Specifically, Section 8.0 introduces Linked Data and the Semantic Web, referencing Tim Berners-Lee's foundational proposal. Section 8.1 focuses on RDF, detailing the model and its various serializations, reinforced by activities like "Thinking in graphs." Finally, Section 8.2 delves into Semantics in Linked Data via Web ontologies. This area includes practical assignments on choosing, designing, and drawing ontologies, demonstrating the technical application of semantic web concepts.

---

## 06_Introduction_to_web_ontologies_Video_27_min

# Introduction to web ontologies
Video • 27 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/o7rgD/introduction-to-web-ontologies

This curriculum outlines a comprehensive study of data management, progressing from basic data operations to advanced semantic web technologies. The initial weeks focus on fundamental data handling, covering both data processing and the structure of traditional relational databases (RDBMS). Following this foundation, subsequent weeks address data robustness through topics in Data Integrity and Security within reliable databases.

The course then transitions to the practical application of databases, exploring how libraries and templating mechanisms facilitate database interaction. Advanced RDBMS concepts are covered, before introducing more modern architectures such as distributed databases and alternative database models. The focus shifts further toward semantic data management, starting with an introduction to Semantic Databases.

Central to the later modules is the concept of Linked Data and the Semantic Web, which aims to connect data across the internet. A key technical element introduced is RDF (Resource Description Framework), the model and its various serializations, often visualized as graphs. The utilization of Web Ontologies is crucial, providing the semantic framework necessary for machines to interpret data relationships.

Finally, the course covers practical applications and the retrieval of multimedia data. The curriculum concludes by exploring the integration of these sophisticated data models, culminating in specialized topics like Linked Data application, multimedia retrieval, and a comprehensive exam.

---

## 07_Choosing_ontologies_Linked_Jazz_and_other_performance-related_Linked_Data_Reading_1h

# Choosing ontologies: Linked Jazz and other performance-related Linked Data
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/uHnJG/choosing-ontologies-linked-jazz-and-other-performance-related-linked-data

This article explores the intricate process of choosing, combining, and extending ontologies, framing this complicated yet enjoyable endeavor. The research specifically details the stages involved in creating prototypes that aggregate musicological datasets on the semantic web. A key focus is placed on utilizing Linked Jazz and other performance-related Linked Data for these semantic implementations. The work provides helpful illustrations and graphs to walk through the complex stages of ontological development. The full technical findings are presented in the paper titled ' Building prototypes aggregating musicological datasets on the semantic web '. This research was conducted by Nurmikko-Fuller T., D. Bangert, A. Dix, D. Weigl, and K. Page. The article is published in *Bibliothek Forschung und Praxis*, Volume 42, Issue 2, in 2018, spanning pages 206-221.

---

## 08_Designing_an_ontology_Video_6_min

# Designing an ontology
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/T6XIA/designing-an-ontology

Designing a Web Ontology shares similarities with creating a relational database schema, often starting with an Entity Relationship model (ER model). However, Web Ontologies require extra care because they are highly exposed and can accidentally create industry standards. When utilizing external concepts, it is crucial to ensure the ontology is used in the manner it was originally intended. Ontology design and modeling must be undertaken with the foresight that other parties will utilize the resulting structures and data. Web Ontologies are significantly more explicit about various aspects than a simple database schema, requiring more nuanced decision-making. A fundamental best practice is to always review existing, external ontologies, as they represent a significant amount of prior expert effort. For collaborative projects, joining forces with others working on similar initiatives helps move towards generally useful outcomes. It is vital to test the ontology design using real data and workshop specific scenarios to validate functionality. A key principle is to avoid excessive detail, adhering to the rule: do not add detail you will not need fairly immediately. It is preferable to prioritize getting something done over achieving absolute completeness in the initial stages. Furthermore, it is better to be slightly over-general than to publish completely inaccurate data on the Web of Knowledge. Good ontologies require substantial time, often taking days of collaborative workshopping even within a small project. It is essential to gather multiple viewpoints and allocate sufficient time for thorough review of the completed structure. Visual aids, such as big whiteboards and large flip pads, are highly recommended to help nail down and formalize the concepts. The process demands explicitness to determine precise statements, enabling stakeholders to raise questions like, "We can't have that," or "We will have an exception." Once the basic design is complete, specialized tools can be used to formalize the structure. Protege is a notable free and open-source software tool designed by Stanford for specifying ontologies. A web-based version, WebProtege, allows users to register with Stanford and construct an ontology in a user-friendly manner. The final ontology is then exported in the OWL format. It is not generally necessary to construct a gigantic ontology entirely from scratch. Most practical projects involve a small amount of new ontology development combined with a large amount of selecting and importing established terms. The primary effort in implementation involves reviewing and integrating these pre-existing ontologies, not building them de novo. These practices support the broader goals of Semantic Databases and Linked Data, fundamental concepts in the Semantic Web.

---

