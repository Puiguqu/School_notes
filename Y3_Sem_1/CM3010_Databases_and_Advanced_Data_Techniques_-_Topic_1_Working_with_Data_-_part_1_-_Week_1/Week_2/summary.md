# Week 2 - CM3010 Databases and Advanced Data Techniques - Topic 1: Working with Data - part 1 - Week 1

## 01_What_shape_is_your_data_Introduction_Video_4_min

# What shape is your data? Introduction
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/OmmBF/what-shape-is-your-data-introduction

Data structures are fundamental when designing database applications, requiring careful consideration of how data is organized. These structures exist at a higher level of abstraction than basic programming types like arrays, objects, and floats. Data modeling focuses on representing how data should be brought together and what relationships exist between different pieces of information. Structuring data is critical for successful serialization, which is the process of writing data out to a file or a network connection for reading elsewhere. Serialization is closely related to exchange protocols, which require data structures optimized for inter-application data transmission over connections like sockets. Furthermore, data structure choices must account for human communication, as users have preferences regarding how complex information is presented. If data contains inherent complexity, the presentation structure should be altered to maximize user comprehension and clarity. While low-level operations are handled by algorithms and data structures, this module focuses on high-level data modeling concepts. Specific data shapes, such as tables, trees, and graphs, will be examined in detail. Tables are presented as one of the most intuitive and general-purpose methods for structuring data. Trees are employed to introduce hierarchical relationships into the data structure. Graphs are excellent structures for representing highly interconnected datasets. Briefly, the concepts of objects and documents are also mentioned, though the database itself does not deeply understand their internal workings. The selection of an appropriate data shape will critically inform the underlying database paradigm that is ultimately used. The course begins in Week 1, covering foundational topics such as "Working with Data." Week 1 focuses specifically on the introduction to data structures and includes videos on tables, trees, and other structures. Week 2 delves further into data structure concepts, including assignments and quizzes to reinforce learning. Topic 2, Relational Databases, begins in Week 3 and continues through Week 4. Week 5 introduces Topic 3, covering Data Integrity and Security within reliable databases. The practical application of databases is covered in Weeks 7 and 8, focusing on libraries and templating. Advanced Relational Database Management Systems (RDBMS) topics are addressed in Week 9. A mid-term assignment is scheduled for Week 10, acting as a key assessment point. Topic 6, Distributed databases and alternative models, is covered in Weeks 11 and 12. Weeks 13 and 14 focus on Semantic databases, a specialized area of data storage. Topics 8 and 9 cover Linked Data and Multimedia and Retrieval, respectively, in Weeks 15 through 18. The final two topics, Applications (Weeks 19 and 20), and preparation (Week 21) lead into the comprehensive exam in Week 22.

---

## 02_What_shape_is_your_data_Tables_Video_8_min

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

## 03_What_shape_is_your_data_Trees_Video_7_min

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

## 04_What_shape_is_your_data_Other_Video_11_min

# What shape is your data? Other
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/x2RHO/what-shape-is-your-data-other

### Week 1 Topic 1: Working with Data - part 1 ### Week 2 Topic 1: Working with Data - part 2 #### 1.3 Data structures - What shape is your data? Introduction Video . Duration: 4 minutes 4 min - What shape is your data? Tables Video . Duration: 8 minutes 8 min - What shape is your data? Tables quiz Practice Assignment . Duration: 5 minutes 5 min - What shape is your data? Trees Video . Duration: 7 minutes 7 min - What shape is your data? Trees quiz Practice Assignment ....

---

## 05_Worksheet_Working_with_Data_(Topic_1,_Part_2)_Reading_10_min

# Worksheet: Working with Data (Topic 1, Part 2)
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/S2rJH/worksheet-working-with-data-topic-1-part-2

This worksheet introduces the fundamental concepts regarding the shape and organization of data. The focus shifts from low-level programming types, such as arrays, objects, and numbers. Instead, the emphasis is placed on higher-level data shapes. These shapes are crucial for various technical functions. Specifically, they support data modelling and serialisation processes. They are also essential for implementing exchange protocols and ensuring human-readable presentation of data. The estimated time commitment for this material is approximately 60 minutes.

A core learning objective is the ability to distinguish various data shapes. These include tables, trees, graphs, media files, raw data, and simple unindexed lists. Students will learn to explain the specific utility of each data shape. They will also be able to ask critical questions about data origins and future usage.

Several key terms are defined to aid understanding. A data structure is defined as a shape or organization used to hold and relate data. A Table is a specific grid configuration. In this grid, each row represents a single entity, or "thing." A Row is the horizontal line of cells within the grid, and it represents a thing. Conversely, a Column is the vertical line of cells, and it represents a specific type of information. The Cell is the defined value found at the intersection of a given row and column.

Regarding data handling processes, Serialisation is the method of writing data to a file or network connection. This process ensures the data can be subsequently read elsewhere. An Exchange protocol is established as an agreed way for various applications to pass data over a network connection.

The text also introduces the concepts of hierarchical data, represented by a Tree. A Tree is characterized as a hierarchical structure possessing a single root node. The Root node functions as the top element and has no parent. Any node positioned directly above a specific node is identified as the Parent node. A Child node is defined as any node located directly below a parent node. A Leaf node is distinguished as a node that contains absolutely no children. An Ancestor is defined as any node that is positioned above a given node. Finally, a Descendant is defined as any node that exists below a given node.

---

## 06_Employability_beyond_this_module_and_beyond_the_BSc_Reading_10_min

# Employability: beyond this module and beyond the BSc
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/T9Kit/employability-beyond-this-module-and-beyond-the-bsc

This reading and the accompanying video are designed to help students reflect critically on the value gained from the degree program and how this knowledge will make them valuable to potential employers. A primary focus is exploring workplace trends, specifically how the professional environment has been affected by advancements in AI and Large Language Models (LLMs). The video provides insights from industry professionals who reflect on what skills and attributes are most valued in the current workplace. For further technical insights, students can access the UoL Careers Service webinar recording library. This extensive resource library is also accessible through the centralized CareersConnect portal. Specifically, the November 2025 panel on Careers in Data Science is highlighted as a topic of particular interest for prospective students. Students interested in exploring specific career pathways can review industry briefings, such as "Career Options in Web & Mobile Development." Additionally, a comprehensive collection of career option briefings is available within the Computer Science, Cybersecurity, and Data Science Careers Resources. All these specialized resources can be found through the dedicated CareersConnect portal. Ultimately, the module aims to bolster employability beyond the completion of the BSc.

---

## 07_Employer_voices_on_AI_trends_Video_11_min

# Employer voices on AI trends
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/e3lB0/employer-voices-on-ai-trends

The modern technological landscape is defined by Hyperautomation, which significantly transcends simple Robotic Process Automation (RPA). Hyperautomation integrates advanced technologies such as Artificial Intelligence (AI), machine learning, and process mining to automate, augment, and expand human work capabilities. This integration leads toward near autonomy as systems are designed to observe, learn, and optimize themselves, sometimes without requiring human triggers. Consequently, job design is shifting toward emphasizing human-machine collaboration, leveraging distinctly human traits like creativity, ethical oversight, judgment, and emotional intelligence.

The World Economic Forum's Future of Jobs report (2025) highlights this shift, suggesting that 40% of current professional skills will change by 2027. While traditional roles persist, new specializations are emerging, such as AI security, technology governance, and responsible innovation designers. The demand for roles involving "framing an intelligent problem" has risen, requiring translators who bridge technology and business end-users.

To prepare for this evolving market, students must become T-shaped professionals, possessing both deep core knowledge and broad horizontal facets. Furthermore, business fluency

---

## 08_Topic_1_summary_Video_2_min

# Topic 1 summary
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/s5nGi/topic-1-summary

This course provides an intensive study of data structures and database management systems across 22 weeks. The initial phase (Weeks 1-2) focuses on data structures, specifically exploring the differing shapes of data through tables, trees, and other complex models. Following this foundation, Weeks 3 and 4 introduce core concepts of Relational Databases. A significant focus is placed on data trustworthiness in Weeks 5 and 6, addressing essential topics of Data Integrity and Security.

Weeks 7 and 8 transition into practical implementation, covering the use of databases via specific libraries and templating techniques. The curriculum then deepens its technical scope in Week 9 with an exploration of Advanced RDBMS topics. A major thematic shift occurs in Weeks 11 and 12, detailing Distributed databases and various alternative database models.

The study of knowledge representation begins in Weeks 13 and 14 by analyzing Semantic databases. This is followed by a dedicated focus on Linked Data in Weeks 15 and 16, which addresses interconnected data sets. Weeks 17 and 18 tackle the specialized areas of Multimedia and retrieval.

The final phases of the course (Weeks 19-20) apply these concepts through various Applications, culminating in exam preparation during Weeks 21 and 22. Key professional considerations are integrated throughout, highlighted by sessions on Employability and AI trends. An important mid-term assignment is scheduled for Week 10. The module structure maintains a consistent review cycle, utilizing quizzes and extensive readings for continuous knowledge reinforcement.

---

## 09_Further_reading_Reading_50_min

# Further reading
Reading • 50 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/oBuB1/further-reading

This text details a specific example of a digital humanities dataset concerning menus. The dataset, focusing on menus, has been released as Open Data by the New York Public Library. Trevor Munoz, the Interim Head of the Maryland Institute for Technology in the Humanities, introduced and explored this dataset in two blog posts. These posts are titled "What IS on the menu" and "Refining the problem." The project maintains a dedicated full website. This website allows users to explore the menus. Furthermore, it provides the functionality to download the transcribed data. Contributors are also invited to contribute to the dataset. The official project link is cited as New York Public Library ’What’s on the menu’ (2025). However, the approach to data handling employed in this project is not universally accepted. There is academic debate regarding this methodology. For a discussion on data cleaning related to the ‘What’s on the menu?’ project, a specific resource is provided. This resource is the article, "Against cleaning," authored by Rawson, K. and T. Muñoz. This article appears in the publication "Debates in the Digital Humanities," Volume 5. The publication is associated with the University of Minnesota Press, dated 2019. The text also includes a functional disclaimer regarding potential link breakage. Users are instructed to report broken links via the Student Portal. (Total sentences: 15)

---

