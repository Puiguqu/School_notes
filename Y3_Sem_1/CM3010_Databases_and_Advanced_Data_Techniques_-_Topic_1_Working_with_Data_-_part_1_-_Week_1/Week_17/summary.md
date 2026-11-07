# Week 17 - CM3010 Databases and Advanced Data Techniques - Topic 1: Working with Data - part 1 - Week 1

## 01_Introduction_to_multimedia_databases_and_information_retrieval_Video_2_min

# Introduction to multimedia databases and information retrieval
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/DLU1A/introduction-to-multimedia-databases-and-information-retrieval

This curriculum progresses from basic data management principles, starting with fundamental topics on "Working with Data" (Weeks 1-2) before moving into the core concepts of Relational Databases (Weeks 3-4). Essential to robust systems, Weeks 5 and 6 focus on "Reliable databases," detailing critical concepts of Data Integrity and Security. Following the foundation, the course explores practical implementation (Weeks 7-8) and advanced structural topics, including Advanced RDBMS (Week 9) and distributed database models (Weeks 11-12). The curriculum then branches into specialized database paradigms, covering Semantic databases (Weeks 13-14) and Linked Data technologies (Weeks 15-16), emphasizing data meaning and interconnectivity. A significant portion is dedicated to handling complex data through "Multimedia and retrieval" (Weeks 17-18), discussing Information Retrieval and the use of features, exemplified by the functionality of Shazam. This knowledge is then applied in comprehensive "Applications" (Weeks 19-20), synthesizing all acquired technical details. The learning process is punctuated by a Mid-term assignment in Week 10 and preparation leading up to the final Exam in Week 22. Overall, the course provides a comprehensive journey from basic data handling to advanced distributed, semantic, and multimedia database architectures.

---

## 02_Information_retrieval_Querying_rich_data_Video_12_min

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

## 03_What_is_a_feature_Video_13_min

# What is a feature?
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/REYXl/what-is-a-feature

This curriculum systematically covers database management, beginning with foundational concepts in Week 1 and Week 2: "Working with Data." The focus then shifts to structured data models in Weeks 3 and 4, exploring Relational Databases, followed by critical concepts of reliability, integrity, and security in Weeks 5 and 6. Weeks 7 and 8 introduce practical database application using libraries and templating mechanisms.

The advanced stages begin with Week 9, covering sophisticated RDBMS topics, leading into the complex world of data architecture in Weeks 11 and 12, which address Distributed databases and alternative database models. Further specialization occurs in Weeks 13 and 14 with the study of Semantic databases, preceding Week 15 and 16 on Linked Data.

The later weeks transition to complex data types, detailing multimedia and retrieval in Weeks 17 and 18, including features for complex data and information retrieval mechanisms like Shazam. Finally, the course culminates in Weeks 19 and 20, focusing on practical applications before the preparation and final examination period.

---

## 04_Music_information_retrieval_in_practice_How_does_Shazam_work_Reading_1h

# Music information retrieval in practice: How does Shazam work
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/z5Usn/music-information-retrieval-in-practice-how-does-shazam-work

Music Information Retrieval (MIR) is defined as a broad and diverse discipline. It encompasses both industrial research initiatives and university-based studies. MIR occupies a somewhat distinct and atypical niche within the broader field of Information Retrieval generally. To provide context for this field, the text references two notably old but significant research papers. A prime example of MIR challenge is Shazam, which involves searching audio data based on an audio query. This task presented substantial technical difficulties, particularly given the constraints of 2003 hardware. Back then, servers possessed significantly less processing power than today. Furthermore, audio storage was much more costly, making the creation of large audio databases difficult to manage and search.

Shazam’s central selling point was its ability to recognize music captured by a mobile phone in a noisy public setting. This feature introduced several complex challenges to the system design. Key limitations included the poor sound quality inherent in mobile phone recordings. Mobile bandwidth constraints also posed a significant hurdle to effective data transmission. Processing power limitations on the mobile device further compounded the difficulty of the recognition task. The presence of distortions from ambient noise made robust audio detection exceptionally challenging.

For a detailed analysis of how Shazam solved this complex problem, the conference paper by Li-Chun Wang is recommended. This specific paper is titled "An industrial-strength audio search algorithm." It was presented at the 4th International Conference on Music Information Retrieval (ISMIR) in 2003. For researchers interested in user-related aspects of MIR, a later paper offers valuable insights. This paper, "The neglected user in music information retrieval research," was written by M. Schedl, A. Flexer, and J. Urbano. It appeared in the Journal of Intelligent Information Systems, specifically in issue 41/3, pp.523-539, in 2013. Readers may search for these articles using the provided Online Library resource. The text also instructs users to report any broken links via the Student Portal.

---

