# 05_The_research_institute_Bibale_Video_9_min

# The research institute: Bibale
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/5jYjh/the-research-institute-bibale

The Bible database contrasts significantly in design, purpose, and history compared to the Schoenberg database. Its origins trace back to the Card catalogues of Yazdi, a research institute founded in the 1930s. This institution accumulated increasingly complex data without imposing limitations on vocabulary or structure. The resulting data source is exceptionally rich and complex, dealing with the messy nature of humanities research.

The major design challenge was modeling this highly unstructured richness within a rigid relational database framework. The resulting database utilizes a specialized, slightly unconventional relational structure. It is fundamentally built around generic structures, specifically the concept of an object possessing a defined type and a name. Objects, such as persons or books, are stored in a primary table, each having a type, a name, and an ID.

A separate mechanism handles elements, which are attached to these objects and possess a type value (e.g., 'death date' or 'sex'). This structure deviates from conventional relational design, which typically allocates a column for every attribute. Instead, the database structure uses a row for each extra attribute or element. This decision renders the tables dense rather than sparse. The rationale for this design choice is crucial: it enables the easy addition of new attributes and relationships without requiring complex database structure redesigns.

By bypassing explicit database structure enforcement, the designers shifted the responsibility for maintaining data structures onto the end-users. This trade-off provides greater flexibility but introduces slightly riskier code execution. Consequently, the data modeling is straightforward from the database builder's perspective, yet complex for those tasked with processing or displaying the data.

A critical finding is that this architecture empowers scholars, allowing them to enrich the data model without being constrained by a rigid schema. The model itself resides primarily in documentation, not in the SQL schema, which presents a challenge for developers. The logic and enforcement of rules are often informal, communicated directly to the catalogers.

Practically, the system's limitations mean catalogers frequently adopt shortcuts because the database does not enforce documented rules. Researchers, therefore, must model not only the prescribed structures but also the practical, informal usage patterns of the database. These project characteristics are typical of large humanities database initiatives. Contextually, related topics include Weeks 3 and 6 concerning Relational Databases and Data Integrity. Advanced concepts such as Semantic Databases (Weeks 13/14) and Linked Data (Weeks 15/16) are also relevant to these historical data projects. The module structure includes detailed examples such as "Mapping manuscript migrations: a tale of 3 databases."

