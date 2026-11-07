# 03_Text_processing_fundamentals_(part_2)_Video_7_min

# Text processing fundamentals (part 2)
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/OL4vH/text-processing-fundamentals-part-2

This text provides a detailed look into the fundamentals of text processing, specifically focusing on the higher-level challenges of linguistic ambiguity. Building upon the discussion of lexical ambiguity from previous materials, this segment focuses on ambiguities encountered at the sentence and discourse levels. At an elementary level of analysis, words within a sentence are classified by different syntactic categories, such as nouns, verbs, adjectives, pronouns, determiners, prepositions, and conjunctions. For instance, the word "book" demonstrates ambiguity because it can function as a noun ("I read the book") or as a verb ("I booked a flight").

Syntactic analysis attempts to determine the correct sequence of these categories for a string of words, often resolving ambiguities, such as tagging the string "book that flight" as verb, determiner, noun. However, determining the correct sequence is often impossible, leading to various forms of ambiguity. Structural ambiguities arise when syntactically similar sentences have distinct meanings, such as comparing "time flies like an arrow" to "fruit flies like a banana."

Moving beyond elementary syntactic thinking, a more structured approach analyzes the grammar of sentences using formal methods. A major challenge is resolving Prepositional Phrase Attachment, where it is unclear which preceding element modifies the attached phrase. For example, in the phrase "the man on the hill with a telescope," it is uncertain whether the man or the observer is holding the telescope. Parsing aims to construct a tree structure that indicates how various elements combine to form the composite meaning of the utterance.

Furthermore, a significant technical hurdle in text processing is sentence segmentation: accurately determining where a sentence begins and where it ends. While punctuation marks like periods or exclamation marks might indicate boundaries, language data presents numerous exceptions to simple rule-based separation. This lack of consistent rules is a core reason why statistical techniques are often considered more robust in Natural Language Processing (NLP) than purely rule-based methods.

The broader course content outlines a comprehensive curriculum covering foundational NLP skills and advanced concepts. The curriculum begins with fundamental text processing topics, including sentence segmentation, word tokenization, and text normalization. Following these fundamentals, the course progresses to Language Modelling and Lexical Semantics. Specialized topics include Text Categorisation and Sentiment Analysis, alongside detailed studies of Syntax and Parsing. The later stages cover practical NLP applications such as Information Extraction, Information Retrieval, and Chatbots and Dialogue Systems. The entire curriculum spans various weeks, leading to a course summary and final examinations, ensuring a deep dive into the technical aspects of processing natural language data.

