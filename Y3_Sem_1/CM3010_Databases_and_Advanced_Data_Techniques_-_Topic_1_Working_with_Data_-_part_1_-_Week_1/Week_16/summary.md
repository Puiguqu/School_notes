# Week 16 - CM3010 Databases and Advanced Data Techniques - Topic 1: Working with Data - part 1 - Week 1

## 01_Triplestores_and_SPARQL_Video_22_min

# Triplestores and SPARQL
Video • 22 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/gAiTd/triplestores-and-sparql

This course provides a comprehensive study of database management, beginning with foundational concepts in data handling (Weeks 1-2). It then progresses to detailed analysis of Relational Databases (RDBMS) in Weeks 3-4, followed by critical topics of Data Integrity and Security necessary for reliable database operation (Weeks 5-6). Practical application is introduced through utilizing databases via libraries and templating (Weeks 7-8), leading into an examination of Advanced RDBMS topics and a mid-term assessment (Weeks 9-10). The curriculum then explores complex architectures, covering Distributed databases and various alternative database models (Weeks 11-12). A major technical focus is placed on Semantic databases (Weeks 13-14), which enable complex meaning representation and logical inferencing. The study culminates with Linked Data (Weeks 15-16), specifically addressing Triplestores and the powerful query language, SPARQL. Linked Data techniques involve both internal graph database utilization and external methods, such as Dereferencing URIs and implementing Schema.org for SEO. Detailed resources include dedicated lessons on Triplestores and SPARQL, as well as prompts comparing SPARQL to SQL and exploring DBpedia. The final segments address Multimedia and retrieval (Weeks 17-18) and practical database Applications (Weeks 19-20). The course structure concludes with dedicated preparation time and the final comprehensive examination (Weeks 21-22).

---

## 02_Using_open_linked_data_Reading_1h

# Using open linked data
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/C1Ui2/using-open-linked-data

Carnegie Hall, the notable concert venue situated in New York, has made a significant data initiative public. Their archives have been released as Linked Open Data (LOD), allowing broad data access. Users can interact with this data through the defined endpoint at `http://data.carnegiehall.org/sparql/`. This release facilitates extensive exploration, detailed within the venue's accompanying blog and experimental discussions. One notable project highlighted is "Whose birthday is today?". This specific experiment showcases the power of data aggregation and visualization. The "Whose birthday is today?" feature leverages Wikidata's robust querying capabilities. It utilizes data visualization techniques to map composers and performers associated with Carnegie Hall. The mapping function dynamically plots individuals if the current date matches their birthday. Additional plots and supplementary examples are accessible on the same official site for review. Finally, users are encouraged to report any issues or broken links using the Student Portal mechanism.

---

## 03_Dereferencing_URIs_and_following_your_nose_Video_6_min

# Dereferencing URIs and following your nose
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/sZUtt/dereferencing-uris-and-following-your-nose

Sparkle serves as a powerful tool enabling the treatment of the linked data world as a unified database. It allows users to query a triple store specifically through a Sparkle endpoint. A key feature is the facility for federated queries, which addresses the need to combine information from multiple sources. These queries can simultaneously address various Sparkle endpoints, including those for Wikidata, local libraries, or commercial organizations. This capability allows the construction of worldwide-level queries across disparate datasets. However, the vast majority of linked data does not reside within triple stores. Furthermore, relatively few existing Sparkle endpoints support federated querying of their data. This limitation is often due to the significant costs and dependency risks associated with waiting for external endpoints. The barrier to publishing plain linked data is extremely low, meaning there are far more plain linked data publications than established Sparkle endpoints. Consequently, when dealing with real-world linked data, an alternative strategy must be employed. This alternative strategy is known as "follow your nose." Dereferencing is an extremely useful technique within linked data, though it is not a mandatory component. The concept starts with possessing a URI, which uniquely identifies a specific entity within a triple store. The process of dereferencing involves taking that URI and requesting the document found at the end of that address. The request is made as an HTTP request, allowing the user to specify the desired data types, such as RDF. If successful, the response will contain RDF data, presenting a large set of triples. Within these returned triples, the original URL serves as either the subject or the object, linking to numerous other URLs. To gain more information about these referenced objects, the process must be repeated. The subsequent action is to dereference those secondary URLs. This cycle of requesting the URL and receiving back RDF information is repeated continuously. This recursive iteration allows a local knowledge graph to be built based on the data discovered through traversal. This methodology is analogous to "chaining," which is the term used for the human practice of following links while browsing the web. In the linked data context, this method is termed "following your nose." This agent-based traversal builds local knowledge until the required information needed to resolve a specific query is obtained. This operational paradigm differs fundamentally from using SPARQL to perform an explicit query against a defined dataset. Nonetheless, any information gathered through dereferencing can be easily imported into a triple store for explicit inquiry later.

---

## 04_Schema.org_SEO_and_linked_data_Video_2_min

# Schema.org: SEO and linked data
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/hhRHl/schema-org-seo-and-linked-data

This curriculum is structured in 22 weeks, progressing from fundamental data management to advanced semantic and distributed database technologies. The initial phase covers core topics on Working with Data (Weeks 1 and 2), followed by a detailed study of Relational Databases (Weeks 3 and 4). This foundational knowledge is expanded in Weeks 5 and 6, focusing on critical aspects of Data Integrity and Security within database systems.

Practical usage is introduced in Weeks 7 and 8 via libraries and templating, advancing to specific Advanced RDBMS topics in Week 9. The study then shifts to modern architectures, examining Distributed databases and other alternative models in Weeks 11 and 12. Weeks 13 and 14 are dedicated to the concepts of Semantic databases, a key step toward intelligent data management.

A major focus of the course is Linked Data (Weeks 15 and 16), which is practically explored through Triplestores and querying using SPARQL, juxtaposed against standard SQL (8.3). Further technical detail covers Linked Data outside of a database, detailing Dereferencing URIs and the application of Schema.org for SEO (8.4). The final segments integrate these concepts by covering Multimedia and Retrieval (Weeks 17 and 18) and practical Applications (Weeks 19 and 20). The course concludes with preparation for the final exam in Weeks 21 and 22.

---

## 05_Topic_8_summary_Video_3_min

# Topic 8 summary
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/LZZmR/topic-8-summary

Linked data and semantic web technologies, despite their age, are still evolving and face challenges in scaling public datasets. A primary ongoing effort involves finding the best methods for sharing the fruits of labor, specifically in terms of ontologies and structured data. In 2007, the Linked Open Data Cloud had specific criteria for qualification. To join this graph, participants had to publish a defined amount of data and include external links to other data sources. DBpedia is noted as a significant example of an early adopter of this technology. Other quick participants included music-related projects such as Jamendo, MusicBrainz, and DBTune.

The graph has experienced massive expansion over time, moving beyond early initiatives like the American Census data of 2007. As of later versions, the graph shows major growth into specialized fields like sciences and biosciences, particularly in bioinformatics databases. Linguistics and governmental data represent other very large regional sections of the data graph. The structure has become immensely complex, evident in the 2021 graph which required thematic arrangement to manage the massive connections.

It is crucial to understand the distinction between data participation and data consumption. Many large organizations, such as Google and Facebook, utilize private graph databases but do not participate by publicly sharing their own data. This current representation highlights the public-facing scope of linked data applications. The field has been an incredible success, but significant technical challenges still exist before its potential can be fully realized.

The educational curriculum details this progression through various database models, including Relational, Reliable, and Distributed databases. A core focus is placed on Semantic databases and the specific methodology of Linked Data. The course delves into practical components, such as Triplestores and the query language, SPARQL. A comparison of SPARQL and SQL is presented to highlight the differences between graph-based and relational querying.

Furthermore, the learning structure covers how to work with data both inside and outside of a database environment. This includes understanding Dereferencing URIs and the process of "following your nose" through a data graph. Schema.org is specifically mentioned as a key tool linking linked data with Search Engine Optimization (SEO). These topics are integrated within a larger structure, including dedicated units on advanced RDBMS and multimedia retrieval. The curriculum progresses toward specialized application knowledge, leading up to the final exam preparation.

---

## 06_Further_reading_Reading_1h

# Further reading
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/8bYqN/further-reading

It is often useful to place Linked Open Data in a wider context of good practices for data management and sharing. This article gives a good overview of approaches to sustainable and repeatable science, and the place of Linked Data in that. Bechhofer, S. et al., 'Why linked data is not enough for scientists', Future Generation Computer Systems, 29(2) 2013, pp.599-611. A short, earlier conference paper relates Linked Data technologies to another important web publishing approach – REST....

---

