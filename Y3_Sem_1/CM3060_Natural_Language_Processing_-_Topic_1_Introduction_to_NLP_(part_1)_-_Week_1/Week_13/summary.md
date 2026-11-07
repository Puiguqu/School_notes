# Week 13 - CM3060 Natural Language Processing - Topic 1: Introduction to NLP (part 1) - Week 1

## 01_Introduction_and_learning_outcomes_Video_1_min

# Introduction and learning outcomes
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/TxGmJ/introduction-and-learning-outcomes

This course provides a structured progression through Natural Language Processing (NLP) concepts, spanning 22 weeks. The initial phase establishes the foundations in NLP (Weeks 1-2) and develops skills in basic text processing (Weeks 3-4). Students then delve into statistical techniques through Language Modelling (Weeks 5-6), which introduces probability to text generation. Lexical semantics (Weeks 7-8) follows, focusing on the meaning and relationships between individual words. The curriculum progresses to practical applications, starting with Text Categorisation and Sentiment Analysis (Weeks 9-10).

A critical technical focus is placed on grammar and structure, addressed through Syntax and Parsing (Weeks 11-12). The subsequent topic, Information Extraction (Weeks 13-14), details specific techniques like POS tagging and Relation extraction, often utilizing tools like NLTK. This is followed by Information Retrieval (Weeks 15-16), focusing on efficient search and document retrieval systems. The latter stages examine advanced applications, including Chatbots and Dialogue Systems (Weeks 17-18), which handle natural human interaction. Finally, the course culminates in reviewing NLP in practice, summarizing the entire domain, and dedicating time to revision and the final examination (Weeks 19-22).

---

## 02_Introduction_to_information_extraction_Video_10_min

# Introduction to information extraction
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/RNy0B/introduction-to-information-extraction

Information Extraction (IE) is a fundamental concept in NLP concerned with converting unstructured natural language data, which possesses implicit structure, into explicitly structured data. This process is essentially a transformation, taking raw input strings and aiming to output formalized database entries. Practically, IE allows the construction of applications designed to extract specific semantic content, such as the who, what, when, and where from text. A basic, formulaic example is the automated markup of text, where algorithms identify patterns like dates, phone numbers, and URLs. This simple extraction provides value by enabling interactive features, such as linking a date to a calendar application. More complex applications include building systems that summarize vast amounts of business news, or curating massive scholarly literature to find subtle, valuable relations.

IE involves several distinct subtasks that address the complexity of extracting meaning. The first is Named Entity Recognition (NER), which identifies proper nouns and objects—like people, places, or companies—and resolves them to unique canonical database identifiers. Next is Relation Extraction, which determines how the identified entities relate to one another. For instance, it identifies if "Person A is employed by Organization B" or "Organization B is based in Location C."

Building upon this, Event Extraction identifies specific episodes or events in which those entities participate, which helps construct a coherent timeline. Event Coreference is necessary because linguistic devices often refer back to events using pronouns, and this task resolves these indirect mentions to a unique event instance. Finally, Temporal Event Expression Extraction addresses the "when" by identifying and resolving various expressions of dates, times, and durations related to the events.

The definition of these relations is not universal; it depends heavily on the problem being solved. One example is the ACE evaluation exercise, which proposes a taxonomy of six top-level categories, including "business/lasting personal," "part-whole relations," and "organization affiliation relations," tailored for Newswire reporting. In contrast, the Unified Medical Language System (UMLS) is highly specialized for medicine, dealing with concepts like bodily locations and injuries. Other systems include DBpedia, which systematizes knowledge derived from Wikipedia infoboxes, and WordNet, which defines relations based on hyponym ("is-a") and instance relationships. Ultimately, researchers often employ bespoke systems of relations created specifically to solve a targeted, problem-centric task.

---

## 03_Relation_extraction_Video_14_min

# Relation extraction
Video • 14 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/l87oQ/relation-extraction

This comprehensive course curriculum spans twenty-two weeks, systematically covering foundational to advanced concepts in Natural Language Processing (NLP). The initial phase focuses on the fundamentals, beginning with an introduction to NLP (Weeks 1-2) followed by mastering basic text processing techniques (Weeks 3-4). The progression then moves into theoretical underpinnings, including language modelling (Weeks 5-6) and the analysis of word meaning through lexical semantics (Weeks 7-8).

Weeks 9 and 10 delve into practical application by covering text categorization and sentiment analysis, while the subsequent weeks (11-12) are dedicated to structural analysis through syntax and parsing. The focus shifts to Information Extraction (Weeks 13-14), which introduces key concepts like relation extraction, POS tagging, and practical implementation using tools such as nltk.

Following information extraction, the course addresses Information Retrieval (Weeks 15-16), a critical aspect of information management. The curriculum culminates in advanced conversational AI, examining Chatbots and Dialogue Systems (Weeks 17-18). The final weeks are dedicated to applying these skills in real-world contexts, covering NLP in practice and a comprehensive course summary (Weeks 19-20). The schedule concludes with a dedicated revision week and the final examination (Weeks 21-22).

---

## 04_POS_tagging_Video_5_min

# POS tagging
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/D0izE/pos-tagging

This transcript introduces Part-of-Speech (POS) tagging, focusing on its role as a vital middle stage in a high-level NLP processing pipeline. Previously, information extraction focused on elementary tags like sentence segmentation and tokenization, followed by sequential processing stages such as POS tagging, Named Entity Recognition (NER), and relation extraction. This lesson specifically drills into the mechanics of POS tagging, which is defined as assigning words to a specific lexical category based on a defined tag set.

To commence the practical demonstration, the speaker utilizes a Jupyter notebook and imports the NLTK library. A sample sentence, sourced from the Reuters corpus, is first tokenized, separating the continuous text into distinct terms. Next, a POS tagger is downloaded from NLTK and applied to the tokenized sentence. The resulting output provides each term alongside its corresponding lexical category tag, such as NNP (proper noun), VBZ (third person singular present tense of a verb), VBN (past participle), and VBG (gerund form).

The core importance of tagging lies in resolving the inherent ambiguity found in human language and syntactic structures. A representative example provided is the ambiguous phrase, "They refuse to permit us to obtain the refuse permit." Although visually identical in spelling, the words "refuse," "permit," and "refuse" (as a noun) are contextually distinct.

The POS tagger successfully navigated this ambiguity, correctly tagging the forms as verbs or nouns based on their usage within the sentence structure. For instance, the instances of "refuse" and "permit" when acting as verbs were correctly categorized, while the noun forms within "the refuse permit" were properly identified as nouns. This demonstrates the tagger's ability to accurately determine lexical categories despite identical spelling.

The transcript further discusses various types of tag sets, noting that they can vary significantly in size, complexity, and level of detail. The default tag set utilized by NLTK is the UPENN tagset. By examining this tagset, the speaker illustrates detailed categories like PRP (personal pronoun), VBP (third person singular present tense of a verb), and DT (determiner).

In summary, POS tagging is a foundational technique for classifying words into predefined categories, enabling more sophisticated NLP operations. The practical demonstration validates its efficacy in resolving lexical ambiguity present in written text. The conclusion sets the stage for subsequent lessons, promising to utilize POS tagging to perform advanced transformations, specifically identifying named entities and extracting relations.

---

## 05_POS_tagging_Reading_1h

# POS tagging
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/9UQ2v/pos-tagging

Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 5. If this link is broken, please let us know via the Student Portal . POS tagging Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 5. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

## 06_Information_extraction_using_nltk_Video_7_min

# Information extraction using nltk
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/okCsP/information-extraction-using-nltk

This course structure provides a comprehensive progression through various disciplines of Natural Language Processing (NLP), spanning introductory concepts through advanced applications. The initial weeks (1-4) establish foundational knowledge, covering general introductions to NLP and fundamental basic text processing techniques. Following this, the curriculum delves into semantic and statistical modeling, focusing on Language Modelling (Weeks 5-6) and Lexical Semantics (Weeks 7-8) to understand word meaning and probability.

The middle section focuses on applied linguistic tasks, starting with Text Categorization and Sentiment Analysis (Weeks 9-10) to classify and gauge emotional content in data. This is followed by a detailed study of Syntax and Parsing (Weeks 11-12), which analyzes the grammatical structure of sentences. A significant portion of the course is dedicated to Information Extraction (Weeks 13-14), covering concepts like Relation Extraction, utilizing tools such as NLTK, and performing Point-of-Sale (POS) tagging.

The technical depth continues with Information Retrieval (Weeks 15-16), which addresses how relevant information is found within large datasets. Advanced interaction methods are explored through Chatbots and Dialogue Systems (Weeks 17-18), focusing on conversational AI design. The latter stages transition to practical usage, examining NLP in practice (Weeks 19-20) and concluding with a course summary and revision period (Week 21). The module structure culminates in the final examination week (Week 22).

---

## 07_Information_extraction_Reading_1h

# Information extraction
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/t7oEl/information-extraction

Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 7. If this link is broken, please let us know via the Student Portal . Information extraction Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 7. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

## 08_Information_extraction_Reading_1h

# Information extraction
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/Yuglz/information-extraction

Jurafsky, D. and J.H. Martin Speech and language processing . (2021; 3rd draft ed.). Chapter 20. If this link is broken, please let us know via the Student Portal . Information extraction Jurafsky, D. and J.H. Martin Speech and language processing . (2021; 3rd draft ed.). Chapter 20. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

