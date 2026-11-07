# 04_NER_with_spaCy_Video_2_min

# NER with spaCy
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/kTxjv/ner-with-spacy

This summary provides a comprehensive overview of Named Entity Recognition (NER) as demonstrated through the use of the `spaCy` library, alongside contextual information regarding the NLP curriculum structure.

The core demonstration involves applying `spaCy` to the task of NER within a Jupyter Notebook environment. The process begins by importing and imposing `spaCy`, followed by loading small English language models trained on web data. A simple news article, which contains several interesting entities related to the iPhone 12 launch, is then defined for processing. The loaded model is called on this article, which yields a marked-up document containing identified entities. To analyze the results, the code iterates through the document entities, printing the entity text, the starting character position, the ending character position, and the assigned label.

The initial findings showcase several recognized entities, demonstrating the model's ability to handle various types of data. For instance, the digit "12" is accurately identified as a cardinal, starting at position seven and ending at nine. "Apple" is correctly labeled as an organization, alongside another instance of "Apple" being identified as an organization. The system successfully recognizes "US" as a geopolitical entity, and various dates are identified as cardinals. Specific individuals, such as "Tim Cook" and "Dan Ives," are identified as persons, and "Wedbush Securities" is recognized as an organization.

While generally accurate, the model exhibits minor errors, noting that "iPhones" is misclassified as an organization and "many years" is incorrectly categorized as a person. Experimentation with the API is encouraged using personal content. Further details regarding the sample data set are available in the official `spaCy` documentation.

Crucially, the text defines named entities into two distinct categories for classification. The first category consists of actual named entities, which include people, nationalities, political groups, facilities, organizations, and geopolitical entities. Additionally, this category covers other specific types such as locations, products, events, works of arts, law, and languages.

The second, complementary category includes elements that are not strictly named entities but are commonly recognized during the NER task. These include numerical quantities such as dates, times, percentages, money, and other general numerical data.

The curriculum context provided shows that NER falls within Topic 7: Information extraction, spanning Week 13 (Part 1) and Week 14 (Part 2). This module is supported by various educational resources, including "NER with spaCy Video" (2 minutes duration) and "Information extraction Reading" (1 hour duration).

The broader course structure spans 22 weeks, starting with introductory topics like "Introduction to NLP" in Week 1 and continuing through "Language modelling" (Weeks 5 and 6). Advanced topics include "Syntax and parsing" (Week 11) and culminates in "Information retrieval" (Week 15 and 16) and "Chatbots and dialogue systems" (Week 17 and 18).

Specific practical resources related to Information Extraction include a "Practice Assignment" (10 minutes) and a lab focusing on "Experimenting with noun phrase chunking" (1 hour). Additional material also covers how to extract noun chunks using "spaCy" and playing with grammar reading.

These structured materials emphasize the depth of the information extraction process, providing practical hands-on exercises for students. The content ensures that learners have access to both theoretical understanding and technical application skills related to NLP techniques like NER.

