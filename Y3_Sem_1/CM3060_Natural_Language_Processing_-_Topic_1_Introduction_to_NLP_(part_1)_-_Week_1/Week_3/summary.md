# Week 3 - CM3060 Natural Language Processing - Topic 1: Introduction to NLP (part 1) - Week 1

## 01_Introduction_and_learning_objectives_Video_11_min

# Introduction and learning objectives
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/ZjNpC/introduction-and-learning-objectives

This text provides a foundational introduction to basic text processing and Natural Language Processing (NLP). The course objectives include differentiating between rule-based and statistical approaches to NLP, exploring appropriate statistical language analysis techniques, and utilizing software tools like corpus readers and stemmers. Furthermore, the curriculum involves studying text corpora and introducing various NLP software libraries. The specific learning goals for this topic center on text processing fundamentals, applying these techniques, and manipulating unstructured data.

Unstructured data is globally pervasive and constitutes a significant volume in enterprise studies. This data exists in many forms, including printed paper documents, emails, social media posts, and customer feedback. Critical textual information is often found in open-ended survey responses, web pages, and transcripts of

---

## 02_Text_processing_fundamentals_(part_1)_Video_10_min

# Text processing fundamentals (part 1)
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/khiZb/text-processing-fundamentals-part-1

This course provides a comprehensive, modular introduction to Natural Language Processing (NLP) over a 22-week period, beginning with foundational concepts in Week 1 and 2. The learning immediately transitions into Basic Text Processing in Weeks 3 and 4, focusing on fundamentals like sentence segmentation, word tokenization, and text normalization, which are crucial for handling unstructured data. Following preprocessing, Weeks 5 and 6 introduce Language Modelling, exploring how systems predict sequences of words. The curriculum then delves into Lexical Semantics in Weeks 7 and 8, examining the meaning and relationships between individual words.

A major application focus begins in Weeks 9 and 10 with Text Categorization and Sentiment Analysis, techniques used to classify text and determine emotional tone. The focus shifts structurally in Weeks 11 and 12 to Syntax and Parsing, detailing the grammatical structure of sentences. Subsequently, Weeks 13 and 14 cover Information Extraction, the process of pulling specific, meaningful data points from text.

The advanced topics continue with Information Retrieval in Weeks 15 and 16, a key mechanism for searching and retrieving relevant documents. Weeks 17 and 18 introduce Chatbots and Dialogue Systems, demonstrating how NLP enables conversational interaction. The practical culmination of the course occurs in Weeks 19 and 20, where NLP is explored in real-world applications and the course is summarized. The final weeks, 21 and 22, are dedicated to revision and examination.

---

## 03_Text_processing_fundamentals_(part_2)_Video_7_min

# Text processing fundamentals (part 2)
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/OL4vH/text-processing-fundamentals-part-2

This text provides a detailed look into the fundamentals of text processing, specifically focusing on the higher-level challenges of linguistic ambiguity. Building upon the discussion of lexical ambiguity from previous materials, this segment focuses on ambiguities encountered at the sentence and discourse levels. At an elementary level of analysis, words within a sentence are classified by different syntactic categories, such as nouns, verbs, adjectives, pronouns, determiners, prepositions, and conjunctions. For instance, the word "book" demonstrates ambiguity because it can function as a noun ("I read the book") or as a verb ("I booked a flight").

Syntactic analysis attempts to determine the correct sequence of these categories for a string of words, often resolving ambiguities, such as tagging the string "book that flight" as verb, determiner, noun. However, determining the correct sequence is often impossible, leading to various forms of ambiguity. Structural ambiguities arise when syntactically similar sentences have distinct meanings, such as comparing "time flies like an arrow" to "fruit flies like a banana."

Moving beyond elementary syntactic thinking, a more structured approach analyzes the grammar of sentences using formal methods. A major challenge is resolving Prepositional Phrase Attachment, where it is unclear which preceding element modifies the attached phrase. For example, in the phrase "the man on the hill with a telescope," it is uncertain whether the man or the observer is holding the telescope. Parsing aims to construct a tree structure that indicates how various elements combine to form the composite meaning of the utterance.

Furthermore, a significant technical hurdle in text processing is sentence segmentation: accurately determining where a sentence begins and where it ends. While punctuation marks like periods or exclamation marks might indicate boundaries, language data presents numerous exceptions to simple rule-based separation. This lack of consistent rules is a core reason why statistical techniques are often considered more robust in Natural Language Processing (NLP) than purely rule-based methods.

The broader course content outlines a comprehensive curriculum covering foundational NLP skills and advanced concepts. The curriculum begins with fundamental text processing topics, including sentence segmentation, word tokenization, and text normalization. Following these fundamentals, the course progresses to Language Modelling and Lexical Semantics. Specialized topics include Text Categorisation and Sentiment Analysis, alongside detailed studies of Syntax and Parsing. The later stages cover practical NLP applications such as Information Extraction, Information Retrieval, and Chatbots and Dialogue Systems. The entire curriculum spans various weeks, leading to a course summary and final examinations, ensuring a deep dive into the technical aspects of processing natural language data.

---

## 04_Reading_Representing_text_Reading_1h

# Reading: Representing text
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/tlGXH/reading-representing-text

Provost, F. and T. Fawcett Data science for business: what you need to know about data mining and data-analytic thinking . (California: O'Reilly Media, Inc., 2013). Pages 251-277. Reading: Representing text Provost, F. and T. Fawcett Data science for business: what you need to know about data mining and data-analytic thinking . (California: O'Reilly Media, Inc., 2013). Pages 251-277. Mark as completed Dislike Report an issue

---

## 05_Sentence_segmentation_Video_5_min

# Sentence segmentation
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/DkElp/sentence-segmentation

This course structure spans 22 weeks, systematically progressing through the fundamental concepts of Natural Language Processing (NLP). The initial phase, Weeks 1 and 2, provides the foundational Introduction to NLP (part 1 and part 2). Basic text processing is covered intensively in Week 3, focusing on essential techniques like Sentence Segmentation, Word Tokenization, and Text Normalisation. Week 4 deepens the understanding of basic text processing fundamentals before the course transitions into language modelling in Weeks 5 and 6.

The focus then shifts to meaning and structure, starting with Lexical Semantics in Weeks 7 and 8. These topics prepare students for Text Categorisation and Sentiment Analysis, which are covered comprehensively in Weeks 9 and 10. The study moves into grammatical structure with Syntax and Parsing in Weeks 11 and 12. Subsequent major modules address complex data extraction and management.

Information Extraction is introduced in Weeks 13 and 14, followed by Information Retrieval in Weeks 15 and 16. The course then explores interactive AI with Chatbots and Dialogue Systems across Weeks 17 and 18. The curriculum culminates in practical application, dedicated to NLP in Practice in Week 19 and a course summary in Week 20. The final weeks allocate time for revision and examination.

---

## 06_Word_tokenization_Video_4_min

# Word tokenization
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/pBuFT/word-tokenization

The provided material details the process and application of word tokenization within the field of Natural Language Processing (NLP). Tokenization is a critical step in basic text processing, serving to segment a character string into its constituent words or tokens. While English generally relies heavily on whitespace as a reliable delimiter between words, this simplicity often masks numerous linguistic exceptions.

To investigate these complexities, the demonstration utilizes the `nltk` (Natural Language Toolkit) library within a Jupyter Notebook environment. The video first discusses the necessity of robust tokenizers because simple whitespace splitting fails in specific cases. The initial setup involves importing `nltk` and preparing sample text designed to showcase various challenging structures.

Initially, the text is subjected to sentence tokenization to correctly segment the input into distinct sentences. This preparatory step confirms that standard methods can reasonably divide sentences using appropriate delimiters. Subsequently, the word tokenizer is applied, executing a list comprehension across each segmented sentence.

The analysis of the first sentence, which is the simplest, reveals that only the punctuation, such as the full stop, is tokenized as a separate unit. The second sentence is used to examine special characters, notably an email address. `nltk` correctly splits the email address based on the `@` character, which is considered a reasonable tokenization approach. Furthermore, the tokenizer successfully keeps complex date formats intact as a single cohesive token, which is the desired outcome.

The third sentence highlights the handling of possessive and contracted forms. The possessive `'s` is treated distinctly; for example, in a possessive form, the word segment is kept, but the possessive apostrophe and letter are separated into individual tokens. Similarly, contractions like "aren't" are split into two separate tokens: "are" and the possessive marker "n't."

The fourth sentence demonstrates the handling of contractions like "it's," which are also split into multiple tokens (e.g., "it" and "'s"). Conversely, the tokenizer successfully keeps hyphenated words together, treating them as a single, meaningful unit.

A second, more complex test case involving specialized text elements is then introduced. This text includes a URL, various company names, and proper names for further evaluation. The tokenizer splits the URL at the colon, showing its ability to handle technical separators. Importantly, both company names are retained as single tokens, preserving their integrity. Proper names are also tokenized accurately, consistent with the findings from the simpler test.

In conclusion, the out-of-the-box `nltk` word tokenize function demonstrates high accuracy for English text across diverse challenging scenarios. However, the presentation strongly cautions that the choice of a "correct" tokenization method is not absolute. The ultimate definition of a valid tokenization strategy must be derived from a heuristic approach dictated by the researcher's specific primary goal. This goal determines whether a contraction must be treated as one token or multiple tokens.

---

## 07_Text_normalisation_Video_6_min

# Text normalisation
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/VyAuw/text-normalisation

This extensive course systematically introduces Natural Language Processing (NLP), beginning with foundational concepts in Week 1 and 2. Week 3 focuses on basic text processing, detailing crucial techniques such as sentence segmentation (5 min video), word tokenization (4 min video), and text normalization (6 min video), with corresponding practice assignments. These fundamentals address representing unstructured data, moving the learner from initial concepts to practical processing techniques.

The curriculum then advances into Language Modelling (Weeks 5 and 6), establishing how linguistic structure predicts and understands language patterns. Following this, Lexical Semantics is introduced in Weeks 7 and 8, focusing on the meaning and relationships of words within text.

Weeks 9 and 10 cover Text Categorization and Sentiment Analysis, teaching how to classify texts and determine emotional tone. The discussion then shifts to deep linguistic analysis, dedicating Weeks 11 and 12 to Syntax and Parsing. This phase emphasizes understanding the grammatical structure of sentences.

Subsequently, the course explores applied knowledge through Information Extraction (Weeks 13 and 14), extracting specific data points from documents. This is followed by Information Retrieval (Weeks 15 and 16), focusing on finding relevant information from large datasets.

Weeks 17 and 18 focus on the specialized area of Chatbots and Dialogue Systems, covering the complex interaction mechanisms of conversational AI. The learning culminates in Weeks 19 and 20, which address NLP in practice and provide a comprehensive course summary. Finally, Weeks 21 and 22 are designated for revision and exam preparation, reinforcing all technical concepts learned.

---

## 08_Tokenization_and_more_Reading_1h

# Tokenization and more
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/Cr4lD/tokenization-and-more

Schütze, H., C.D. Manning and P. Raghavan Introduction to information retrieval . (Cambridge: Cambridge University Press, 2008). Chapter 2, pp.21-22. If this link is broken, please let us know via the Student Portal . Tokenization and more Schütze, H., C.D. Manning and P. Raghavan Introduction to information retrieval . (Cambridge: Cambridge University Press, 2008). Chapter 2, pp.21-22. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

