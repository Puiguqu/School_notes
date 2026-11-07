# Week 1 - CM3010 Databases and Advanced Data Techniques - Topic 1: Working with Data - part 1 - Week 1

## 01_Welcome_to_the_module_Video_4_min_Get_started

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

## 02_Module_syllabus_Reading_10_min

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

## 03_Getting_started_on_this_module_Reading_10_min

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

## 04_Where_does_data_come_from_Video_6_min

# Where does data come from?
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/VuQgW/where-does-data-come-from

This curriculum outlines a comprehensive module focusing on advanced data techniques and database management, progressing systematically over 22 weeks. The initial segment (Week 1) establishes foundational knowledge through discussions on data sources, analyzing data characteristics, and the practical methods of using and linking diverse data sources. Crucially, this foundation incorporates ethical considerations, specifically covering licensing, sharing, and data ethics. Topics build upon this base, moving into the core structural concepts of Relational Databases (Week 3 and Week 4).

Weeks 5 and 6 introduce the critical concepts of reliable databases, delving deeply into data integrity and security protocols. Following this, the module shifts focus to practical implementation through the study of using databases via libraries and templating (Week 7 and Week 8). The progression then moves into specialized database theory, beginning with Advanced RDBMS topics in Week 9.

The mid-term assessment occurs in Week 10, marking the transition to more complex and modern database architectures. Weeks 11 and 12 tackle Distributed databases and alternative database models, exploring systems that operate across multiple locations. This is followed by an exploration of Semantic databases in Weeks 13 and 14, focusing on knowledge representation.

The module then covers interoperability through Linked Data in Weeks 15 and 16. Further specialization occurs with the examination of Multimedia and retrieval systems (Week 17 and Week 18). The practical application of these concepts is addressed in Weeks 19 and 20, focusing on various system Applications.

The final weeks are dedicated to preparation, with Week 21 focused on exam readiness. The module concludes with the final examination in Week 22, completing the journey from basic data sourcing to advanced database model deployment.

---

## 05_What_does_your_data_look_like_Video_6_min

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

## 06_Bringing_data_sources_together_Reading_30_min

# Bringing data sources together
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/ijIGZ/bringing-data-sources-together

The Linked Jazz project is a resource dedicated to publishing and connecting comprehensive information about jazz musicians. Its primary function is to enrich the historical exploration of jazz by synthesizing data from multiple sources. This methodology specifically utilizes information from various databases, including Wikipedia, to broaden the scope of historical study. The material itself is presented as a short news article located on the official Pratt Institute website. The academic source is cited as The Pratt Institute, published in 2020. The core concept emphasized by the reading is how mapping relationships between jazz musicians elevates unsung histories. Finally, the document includes a technical instruction for users, directing that any broken link should be reported via the Student Portal.

---

## 07_Licenses,_sharing_and_ethics_Video_10_min

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

## 08_Licensing_Reading_1h

# Licensing
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/9PDys/licensing

Decisions about whether your data will be proprietary or open are often taken at an institutional level. Research funding bodies, normally require your data to be open, and many governments and their agencies have similar restrictions. Whichever way these decisions go, the exact nature and terms of the license can have a significant impact on the legal re-use of your data. The Ball article summarises some of the issues, the advantages and the disadvantages of different licenses for open data....

---

## 09_Worksheet_Working_with_Data_(Topic_1,_Part_1)_Reading_10_min

# Worksheet: Working with Data (Topic 1, Part 1)
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/tQkHk/worksheet-working-with-data-topic-1-part-1

This module, Topic 1: Working with Data, provides a practical examination of data management. The module structure encompasses understanding data structure, obtaining and cleaning it, storing and retrieving it, and finally, using and sharing it. This specific worksheet deepens the focus on several critical areas within data handling. Specifically, it addresses the origins of data and how the intended use dictates the structure of the data model. Furthermore, the worksheet investigates the legal and ethical considerations that arise when data is reused or repurposed. A simple example, such as a book, illustrates this dependency effectively. An online retailer, for instance, might prioritize the book’s weight. Conversely, a librarian may be interested only in the book’s shelf height. A historian, however, would likely focus heavily on the book's actual content. By completing this worksheet, the student is expected to achieve several specific competencies. These objectives include the ability to classify various data sources. Students must also be able to select appropriate data fields tailored to different user needs. Another key skill is the capacity to thoroughly evaluate any external data source before use. Finally, the module requires learners to critically weigh the arguments for and against the use of open data. The terminology introduced is crucial for navigating these data processes. A fundamental concept is the definition of a data source itself. A data source refers simply to where the data originates: whether it is new, pre-existing, or external. New data is defined as data created or entered specifically for a new system, whether done incrementally or in a large batch. Pre-existing data is information the organization already holds, often within a legacy database or spreadsheet. Legacy data is a specialized type of pre-existing data, characterized as older information kept from previous systems or past working methods. External data is data provided by an entity outside the immediate organization. This external supply could be sourced, bought, or simply found. The process of bulk data entry involves inputting a substantial volume of data all at once. This is frequently done using methods like crowd sourcing or paid staff input. Extraction describes the method of getting data out of an older system into a more usable format. Conversion is the process of transforming data into a form that successfully meets new system requirements. This content is part of a worksheet estimated to take approximately 60 minutes to complete. The instructional material emphasizes working through the activities sequentially. Learners are encouraged to make a genuine attempt at the activities before consulting the provided answers.

---

