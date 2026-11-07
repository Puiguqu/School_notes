# Week 7 - CM3060 Natural Language Processing - Topic 1: Introduction to NLP (part 1) - Week 1

## 01_Introduction_and_learning_outcomes_Video_1_min

# Introduction and learning outcomes
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/TxGmJ/introduction-and-learning-outcomes

This course provides a structured progression through Natural Language Processing (NLP) concepts, spanning 22 weeks. The initial phase establishes the foundations in NLP (Weeks 1-2) and develops skills in basic text processing (Weeks 3-4). Students then delve into statistical techniques through Language Modelling (Weeks 5-6), which introduces probability to text generation. Lexical semantics (Weeks 7-8) follows, focusing on the meaning and relationships between individual words. The curriculum progresses to practical applications, starting with Text Categorisation and Sentiment Analysis (Weeks 9-10).

A critical technical focus is placed on grammar and structure, addressed through Syntax and Parsing (Weeks 11-12). The subsequent topic, Information Extraction (Weeks 13-14), details specific techniques like POS tagging and Relation extraction, often utilizing tools like NLTK. This is followed by Information Retrieval (Weeks 15-16), focusing on efficient search and document retrieval systems. The latter stages examine advanced applications, including Chatbots and Dialogue Systems (Weeks 17-18), which handle natural human interaction. Finally, the course culminates in reviewing NLP in practice, summarizing the entire domain, and dedicating time to revision and the final examination (Weeks 19-22).

---

## 02_Lexical_semantics_Video_7_min

# Lexical semantics
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/AwdkF/lexical-semantics

This course provides a comprehensive 22-week journey through Natural Language Processing (NLP), commencing with introductory modules in Week 1 and Week 2. Basic text processing skills are developed in Weeks 3 and 4, laying the foundation for more advanced language comprehension. The focus then shifts to Language Modelling during Weeks 5 and 6, followed by an intensive study of Lexical Semantics in Weeks 7 and 8. Week 7 is particularly detailed, covering topics such as WordNet, semantic similarity, and associated readings and assignments. Subsequently, the curriculum addresses practical applications in Weeks 9 and 10, focusing on Text Categorisation and Sentiment Analysis. The course progression continues with fundamental linguistic analysis, covering Syntax and Parsing in Weeks 11 and 12. Information processing deepens with dedicated modules on Information Extraction (Weeks 13 and 14) and Information Retrieval (Weeks 15 and 16). Finally, the later stages tackle advanced conversational AI, exploring Chatbots and Dialogue Systems (Weeks 17 and 18), culminating in practical NLP case studies in Weeks 19 and 20. The entire program concludes with a dedicated revision week (Week 21) and final examinations (Week 22).

---

## 03_WordNet_Video_6_min

# WordNet
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/Rr7NY/wordnet

This summary focuses exclusively on the technical concepts and findings presented in the transcript, adhering to the 25-sentence limit while preserving all core information.

1. The discussion introduces WordNet, a lexical resource, utilizing it within a Jupyter Notebook environment by importing it as `WN` from `nltk.corpus`.
2. A fundamental concept in WordNet is the synset, which conceptually groups words into sets of synonyms.
3. Accessing these groups is performed by calling the method `WN.synsets` on a given term, such as "motorcar."
4. The result for "motorcar" is an indexed synset, exemplified by `car.n.01`, signifying the primary noun sense of the word "car."
5. In contrast, the term "spell" is shown to be far more complex, possessing numerous synsets (approximately 10 or 11), illustrating semantic ambiguity.
6. Drilling into a specific synset, like `car.n.01`, reveals its members—five synonyms in this case—which collectively form that synset.
7. WordNet is noted not to be indexed on individual terms, but rather on abstract concepts.
8. This abstract concept can be explicitly defined using a definition method, such as the definition for `car.n.01` ("a motor vehicle four wheels, usually propelled by an internal combustion engine").
9. The set of all individual members belonging to a synset are referred to as its lemmas.
10. Lemmas represent a linguistically principled process, similar to lemmatization, reducing various tokens to a common root.
11. The demonstration of "car" highlights that multiple senses correspond to multiple synsets; for example, five different synsets exist for the word "car."
12. By iterating through these senses, the transcript shows distinct meanings, including "wheeled vehicle," "railway car," "gondola," "elevator car," and "cable car."
13. The text then shifts focus to traversing the hierarchy within WordNet, exploring hyponyms (child terms) and hypernyms (parent terms).
14. By instantiating `motorcar` with the `car.n.01` sense, the hyponyms for that synset (`types_of_motorcar`) can be retrieved.
15. Conversely, retrieving the hypernym allows the user to move upward from the synset to its parent term.
16. The concept of polyhierarchy is introduced, explaining that a single concept can be defined in multiple ways, thus having multiple parents.
17. This complexity is demonstrated by using the `hypernym_paths` method, which reveals two distinct lineage paths for "motorcar."
18. The first parent path runs from `car.n.01` up through "wheeled vehicle" and "container."
19. The second parent path from "car" follows a different lineage, passing through "conveyance vehicle" before reaching the common parent "entity."
20. This illustrates that different ancestral paths lead up to a shared root node.
21. Key concepts introduced include the hierarchy of WordNet, the crucial role of synsets as conceptual representations, and the methods for navigating this structure.
22. The process of walking up and down the hierarchy enables the discovery of parent and child relationships within the lexicon.
23. The provided course outline shows that WordNet usage culminates in calculating semantic similarity in subsequent modules.
24. Further learning paths involve topics like Basic text processing, Language modelling, and Lexical semantics.
25. These tools provide the foundational knowledge necessary for advanced NLP tasks, such as Text categorisation and Information extraction.

---

## 04_Semantic_similarity_using_WordNet_Video_6_min

# Semantic similarity using WordNet
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/jtJOG/semantic-similarity-using-wordnet

This comprehensive 22-week curriculum initiates the study of Natural Language Processing (NLP) with introductory topics (Weeks 1 & 2) and progresses to basic text processing techniques (Weeks 3 & 4). Foundational concepts are built upon in Language Modelling (Weeks 5 & 6), which forms the basis for semantic analysis. Lexical Semantics is covered extensively (Weeks 7 & 8), involving specific study materials such as the WordNet Video (6 min), various assignments (10 min duration), and in-depth readings. Week 7 introduces semantic similarity using WordNet through focused videos and practical assignments, including a 1-hour Reading module. The curriculum then moves to practical application, covering Text Categorisation and Sentiment Analysis (Weeks 9 & 10) and formal language structure via Syntax and Parsing (Weeks 11 & 12). Subsequent advanced stages focus on extracting knowledge, tackling Information Extraction (Weeks 13 & 14) and Information Retrieval (Weeks 15 & 16). The final major concepts address interaction design through Chatbots and Dialogue Systems (Weeks 17 & 18) and practical application in NLP (Weeks 19 & 20). The course culminates in a final revision week (Week 21) and the examination period (Week 22).

---

## 05_WordNet_Reading_1h

# WordNet
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/CDwg5/wordnet

Read the following chapter on categorising and tagging words: Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 2 - Refer to Section 5 If this link is broken, please let us know via the Student Portal . WordNet Read the following chapter on categorising and tagging words: Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019)....

---

## 06_Lexical_semantics_Reading_1h

# Lexical semantics
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/3ePrf/lexical-semantics

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5. In the event that the draft of the 3rd edition does not contain the chapter reference you require, please refer to the second edition, Chapter 19, pp.623-631. If this link is broken, please let us know via the Student Portal . Lexical semantics Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5....

---

## 07_Activity_Exploring_semantic_similarity_Reading_1h

# Activity: Exploring semantic similarity
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/4hJ2a/activity-exploring-semantic-similarity

Task 1 1. Explain what is meant by the following terms and give one example of each from WordNet: Synonym Antonym Hyponym Hypernym Meronym Holonym 2. Pick two of WordNet’s similarity metrics and briefly explain how they calculate the degree of similarity between two concepts. Activity: Exploring semantic similarity Task 1 1. Explain what is meant by the following terms and give one example of each from WordNet: Synonym Antonym Hyponym Hypernym Meronym Holonym 2....

---

