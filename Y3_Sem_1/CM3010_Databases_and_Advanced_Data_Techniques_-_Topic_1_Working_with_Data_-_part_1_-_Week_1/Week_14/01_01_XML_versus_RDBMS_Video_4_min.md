# 01_XML_versus_RDBMS_Video_4_min

# XML versus RDBMS
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/jLQt8/xml-versus-rdbms

The text primarily contrasts XML-based database technologies with Relational Database Systems (RDBMS), asserting that the comparison is "unfair" because the systems fulfill fundamentally different functions. The core difference lies in their data structure: XML organizes data as a tree that is characterized by a looser and less structured format. Processing XML requires traversing this tree, relying on external processing mechanisms rather than a predefined tabular schema. This inherent lack of rigid, upfront structure makes indexing more complex compared to RDBMS, often necessitating third-party indexing tools like Lucene applied to a transformed version of the data.

Despite indexing challenges, XML is highly amenable to parallelization from the beginning. Individual XML documents can be processed separately, allowing for heavy parallelization, even if a single file must be processed in a strict, left-to-right order. Crucially, the operations examined are side-effect free, enabling multiple operations to run simultaneously and the resulting data to be compiled linearly. Furthermore, XML files possess the capability of being directly shared and functioning as web links, something a typical relational database cannot inherently do.

The philosophical foundation of RDBMS, as introduced by Codd, aims to be a general-purpose, guaranteed, and effective system. Codd designed RDBMS in reaction to existing specialized and deductive databases, advocating for a simpler, more repeatable structure that maintains less prior knowledge about the data, believing this simplicity was more intuitive and provable.

The academic schedule details a comprehensive study of database models. Topics range from basic concepts (Week 1) through advanced RDBMS features (Week 9). The curriculum heavily covers distributed and alternative database models (Week 11 and 12). Specific technical modules include semantic databases (Weeks 13 and 14) and Linked Data (Weeks 15 and 16).

Practical application is emphasized through modules like "Transforming XML: XML Pipelines" (16 min video) and dedicated studies on XML Schemata (26 min video). The course includes numerous practice opportunities, such as the "XML versus RDBMS quiz" and "Transforming concert data Lab." The structure is cumulative, leading to a major Mid-term assignment in Week 10 and culminating in the final examination in Week 22.

