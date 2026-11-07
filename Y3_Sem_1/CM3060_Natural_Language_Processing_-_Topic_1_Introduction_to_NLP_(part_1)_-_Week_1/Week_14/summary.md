# Week 14 - CM3060 Natural Language Processing - Topic 1: Introduction to NLP (part 1) - Week 1

## 01_Chunking_Video_7_min

# Chunking
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/u9RJ9/chunking

Information extraction relies heavily on the process of chunking, which is defined as identifying meaningful chunks within a body of text. For the purposes of this practical example using NLTK, these meaningful chunks are typically conceptualized as noun phrases (NP). To begin, NLTK is utilized, often paired with a sentence that has already been parts-of-speech (POS) tagged. A crucial step involves defining a pattern for the desired noun phrase using a regular expression. The initial grammar definition stipulates an NP consists of an optional determiner, followed by zero or more adjectives, concluding with a noun. This grammar is applied using the `nltk.RegexpParser` class, which is instantiated with the defined grammar. Running the parser successfully identifies the NP structure based on the determiner-adjective-noun pattern. However, the basic grammar is inherently limited; it fails to correctly identify complex examples, such as dropping the word "measures" in "Any new policy measures."

To accommodate complexity, the grammar must be modified significantly. An updated grammar might include an optional determiner, zero or more adjectives (like the comparative form, JJR), and one or more nouns (such as the plural form, NNS). By incorporating these structures, the parser can successfully recognize more intricate NP examples like "earliest stages." Furthermore, grammars can be extended to span multiple lines to handle increasingly complex linguistic structures. When parsing a sentence like "Rapunzel let down her long golden hair," the parser requires a refined grammar to accurately capture the entire phrase. This refinement involves including possessives (a determiner or possessive) in the pattern and correctly defining the sequence of adjectives and nouns.

A key concept in regular expressions is greedy matching, which dictates that if a grammar defines a sequence of two or more nouns, the parser will capture the first match it encounters. This leads to the concept of chinking, which is the inverse of chunking. Chinking involves chunking the entire sequence of text and then specifically removing or ignoring undesired bits. This is achieved by defining negative matching within the grammar, such as targeting sequences of past tense and prepositions.

Finally, a standard method for marking up these labeled sequences is using IOB tags (Beginning, Inside, Outside). The 'B' tag marks the beginning of a chunk, 'I' marks the subsequent words inside the chunk, and 'O' marks text outside any identified chunk. For example, in "the yellow dog," 'the' might be tagged as the beginning of the NP, while 'yellow' and 'dog' would be inside. This IOB system allows for highly flexible notation, enabling the representation of multiple, non-overlapping chunk types for sophisticated information extraction.

---

## 02_Extracting_noun_chunks_with_spaCy_Video_4_min

# Extracting noun chunks with spaCy
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/6sF6U/extracting-noun-chunks-with-spacy

This comprehensive course covers the full spectrum of Natural Language Processing, starting with foundational concepts (Topics 1 and 2) and progressing through structured language understanding. Early modules focus on fundamental processes like basic text processing, followed by the critical development of Language Modelling (Topic 3), which predicts the probability of word sequences. Lexical semantics (Topic 4) is explored in depth, focusing on the meaning and relationships of words, culminating in Text Categorisation and Sentiment Analysis (Topic 5).

Next, the course delves into grammatical structure via Syntax and Parsing (Topic 6), which determines the hierarchy and relationships between words in a sentence. A major focus is Information Extraction (Topic 7), employing specific techniques such as Named Entity Recognition (NER) and noun phrase chunking (e.g., with spaCy) to pull structured data from unstructured text. These concepts build toward Information Retrieval (Topic 8) and the implementation of sophisticated Chatbots and Dialogue Systems (Topic 9).

The later stages apply these theoretical findings to real-world scenarios in NLP practice (Topic 10), integrating all learned skills into functional systems. The final weeks serve as a dedicated Revision week, followed by the culminating Exam week, solidifying the comprehensive knowledge acquired across all topics.

---

## 03_Playing_with_grammar_Reading_1h

# Playing with grammar
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/ztCud/playing-with-grammar

Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 2. Playing with grammar Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 2. Mark as completed Dislike Report an issue

---

## 04_NER_with_spaCy_Video_2_min

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

---

## 05_Named_entity_recognition_Reading_1h

# Named entity recognition
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/kSZbD/named-entity-recognition

Russell-Rose, T. ' Zipf's Law: How can something so simple explain so much ', Information Interaction (2010). If this link is broken, please let us know via the Student Portal . Named entity recognition Russell-Rose, T. ' Zipf's Law: How can something so simple explain so much ', Information Interaction (2010). If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

## 06_Information_extraction_Reading_1h

# Information extraction
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/jLxHI/information-extraction

Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 5. Information extraction Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 5. Mark as completed Dislike Report an issue

---

## 07_Information_extraction_summary_Video_1_min

# Information extraction summary
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/adLwx/information-extraction-summary

This comprehensive course structure progresses through fundamental to advanced concepts in Natural Language Processing (NLP). The initial weeks establish the foundation with an introduction to NLP and basic text processing techniques. Subsequently, the focus shifts to predictive and semantic understanding through Language Modelling, followed by Lexical Semantics to analyze vocabulary meaning. The curriculum then moves into applications, covering Text Categorisation and Sentiment Analysis, before addressing the structural analysis of language via Syntax and Parsing. Information Extraction forms a major section, delving into techniques such as NER (Named Entity Recognition) and specific noun phrase chunking, often utilizing tools like spaCy. Further technical detail is provided through assignments and specific modules on chunking videos and grammar reading. The study extends to Information Retrieval, which focuses on finding relevant data, and advanced systems like Chatbots and Dialogue Systems. The course culminates by exploring NLP in practice, followed by a final course summary, revision, and examination.

---

