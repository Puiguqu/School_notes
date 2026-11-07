# Week 4 - CM3060 Natural Language Processing - Topic 1: Introduction to NLP (part 1) - Week 1

## 01_Regular_expressions_part_1_Video_8_min

# Regular expressions part 1
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/SMZsu/regular-expressions-part-1

Regular expressions (regex) are a fundamental tool for processing text, providing a formal language to define text strings and character sequences. In practice, regex allows users to express patterns for advanced operations such as matching, replacing, or substitution within textual data. As data scientists frequently handle noisy or unstructured textual data, regex offers a flexible and efficient mechanism for necessary transformations and data cleaning. The transcript focuses on five specific sub-topics within regular expressions: disjunction, negation, optionality, aliases, and anchors, with a deep dive into the former two.

To begin, the Python standard library `re` is imported, allowing manipulation of a variable defined as `text`. The `re.sub()` method is highlighted as the core function, which substitutes a defined `pattern` with a specified replacement string across the `text` variable. An initial example demonstrates finding and replacing all instances of the word "the" with the character 'x'. However, the initial pattern fails to capture all instances because it was case-sensitive, missing the uppercase 'T'.

This leads to the concept of disjunction, which is implemented using square brackets `[]`. Disjunction allows the pattern to match characters preceded by either an uppercase 'T' or a lowercase 't', thereby correcting the initial case-sensitivity error. Other practical applications of disjunction include using character ranges (e.g., `0-9` to match digits or `A-Z` to match all uppercase letters). Disjunction can also be extended to match specific words using the vertical pipe symbol (`|`), allowing a pattern to match "or" or "the" simultaneously.

The next major concept introduced is negation, which enables the inverse operation—matching anything that is *not* a certain type of character. Negation is achieved by placing a caret operator (`^`) immediately before a range definition. For instance, if `[0-9]` matches digits, then `[^0-9]` matches any character that is not a digit. By substituting these non-digit characters with an empty string, the text is effectively reduced to only its digits.

This negation technique is highly adaptable and can be applied to any character range. An example shows using `[^a-z]` to match and eliminate any character that is not a lowercase letter. The combined use of disjunctions and negations provides flexible, low-level tools for powerful textual transformations. Mastery of these simple yet flexible regex tools allows for complex data cleansing and pattern recognition in various NLP applications.

---

## 02_Regular_expressions_part_2_Video_11_min

# Regular expressions part 2
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/AVgt0/regular-expressions-part-2

This curriculum provides a structured progression through various domains of Natural Language Processing (NLP), commencing with foundational concepts in Weeks 1 and 2. The core module on basic text processing (Weeks 3-4) heavily emphasizes practical technical skills, including extensive use of Regular Expressions (Parts 1 & 2) and the application of Stop Words for data cleanup. Subsequent learning focuses on Text Corpora (Week 4), introducing the necessary resources for linguistic analysis and experimentation. The program then delves into advanced linguistic concepts, covering Language Modelling (Weeks 5-6) and Lexical Semantics (Weeks 7-8). Further technical development is achieved through Text Categorization and Sentiment Analysis (Weeks 9-10), bridging basic processing with applied classification. The modules transition into deeper structural analysis, covering Syntax and Parsing (Weeks 11-12) and subsequently focusing on complex Information Extraction (Weeks 13-14). Practical applications are explored via Information Retrieval (Weeks 15-16), followed by specialized systems such as Chatbots and Dialogue Systems (Weeks 17-18). The course culminates by integrating these diverse techniques within broader contexts, addressing NLP in Practice (Week 19) and concluding with a comprehensive course summary and revision week.

---

## 03_Stop_words_Video_4_min

# Stop words
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/zJwBM/stop-words

Stop words are defined as high-frequency words common across different document types and genres. These words offer little lexical content and tend not to contribute significantly to differentiation between texts. For example, common English stop words include "and," "or," "the," and "of." In machine learning tasks, such as document classification, these common words often introduce noise rather than providing meaningful signal. Consequently, they are typically filtered out during the preprocessing phase of text analysis.

However, it is crucial to recognize that stop words are highly language-specific, meaning the English list differs fundamentally from those in French or German. Furthermore, there is no universal list of stop words; the selection must depend entirely on the specific goal of the application. To begin processing, the Natural Language Toolkit (NLTK) is imported to access built-in stop word lists.

The procedure involves importing the NLTK stop word list and printing the extensive list available. To practically use these words, the English stop word list is first stored in a variable named `stopwords`. This list is then cast to a set type to ensure subsequent computational operations execute faster.

Text tokens are extracted from the document using NLTK’s tokenization function. Subsequently, a simple list comprehension is utilized to iterate through the tokenized words. This comprehension filters out any word that exists within the defined `stopwords` set. This process effectively transforms the text by removing high-frequency common phrases, for example, changing "most of the time" to "most time use white space."

A critical caution must be applied when implementing stop word removal. Over-applying the filter can be detrimental to specialized texts. For instance, if filtering Shakespeare's plays, the removal of words like "to" and "be" could result in an empty list, which is clearly inappropriate for that literary corpus.

Beyond English, NLTK provides available lists for other languages. The transcript demonstrated accessing and reviewing the stop words provided for German and also noted the availability of French stop word lists. This basic technique is fundamental to text processing applications, but it must be used with extreme caution. Users must carefully consider which words should definitively be included in their specific stop word list.

---

## 04_Regular_expressions_Reading_1h

# Regular expressions
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/SP5HV/regular-expressions

Please read the following extract on regular expressions: Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 2, Section 2.6 In the event that the draft of the 3rd edition does not contain the chapter reference you require, please refer to the second edition, Chapter 2, pp.17-26. If this link is broken, please let us know via the Student Portal . Regular expressions Please read the following extract on regular expressions: Jurafsky, D. and J.H....

---

## 05_Text_corpora_Video_10_min

# Text corpora
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/ldPwQ/text-corpora

This comprehensive course provides a structured exploration of Natural Language Processing (NLP), starting with introductory concepts in Week 1 and Week 2. The foundational stage then transitions into Basic Text Processing (Weeks 3 and 4), covering critical technical details like Regular expressions, the handling of Stop words, and the utilization of Text corpora. Subsequent modules deepen linguistic understanding through Language Modelling (Weeks 5 and 6) and the principles of Lexical Semantics (Weeks 7 and 8).

The course progresses to analyzing the structure of language by covering Syntax and Parsing in Weeks 11 and 12. Key applications begin with Text Categorisation and Sentiment Analysis (Weeks 9 and 10), followed by modules focused on Information Extraction (Weeks 13 and 14) and Information Retrieval (Weeks 15 and 16).

The final thematic blocks address interactive and practical NLP systems. Weeks 17 and 18 are dedicated to Chatbots and Dialogue Systems, while Week 19 focuses on applying NLP in real-world practice. The curriculum concludes with a comprehensive Course Summary in Week 20, followed by a Revision Week (Week 21) and Exam Week (Week 22).

---

## 06_Accessing_text_corpora_Reading_1h

# Accessing text corpora
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/tf9TE/accessing-text-corpora

Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2009). Section 2.1, pp.39-51. If this link is broken, please let us know via the Student Portal . Accessing text corpora Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2009). Section 2.1, pp.39-51. If this link is broken, please let us know via the Student Portal ....

---

## 07_Text_processing_summary_Video_4_min

# Text processing summary
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/zP0Nf/text-processing-summary

This summary focuses on Topic 2: Basic Text Processing, covering the fundamentals of manipulating unstructured data in NLP.

The course objectives for text processing were defined as understanding fundamentals, applying techniques, and manipulating unstructured data. A primary task in processing natural language is resolving the considerable ambiguity present in human language. Before intent or structure can be determined, ambiguity must be addressed at various linguistic levels. The basic level of analysis begins with lexical analysis, essentially known as tokenization. Various approaches to tokenization and whitespace exist, but they require smarter techniques to identify appropriate tokens.

Stemming is a crude process of chopping word endings to reduce them to a common root, though this root may not always be a genuine word. Lemmatization solves this issue by analyzing the process in a more linguistically principled manner. Lemmatization considers the syntactic context to identify the correct lemma or root for each input word. Morphology refers to the shape of words; English is less morphologically complex than languages like German, which exhibits complex compounding behavior.

The next stage involves syntax, which analyzes the syntactic role of each word to interpret the sentence structure. Syntax also presents ambiguity, exemplified by the phrase, "I saw the man on the hill with a telescope." Solving this requires utilizing contextual information rather than syntax alone. Sentence boundary detection is another challenging task; while simple rules based on punctuation help, exceptions are common in linguistic data.

Regular expressions offer a highly flexible tool, enabling diverse text processing tasks. These expressions are used effectively to extract specific data points, such as URLs, email addresses, and dates. Furthermore, stop word removal is a necessary step, but there is no definitive universal list for English or any language. The selection of a stop word list must depend entirely on the specific application or goal being pursued.

Finally, text corpora—large samples of textual data—allow for various linguistic and stylistic analyses. Four types of corpora were briefly examined: isolated, categorized, overlapping, and temporal. The entire process of text data handling moves toward advanced topics like language modeling. The associated coursework includes dedicated modules on Regular Expressions (Parts 1 & 2), Stop Words, and Text Corpora. The curriculum progresses through these stages, leading eventually to advanced treatments of language and NLP in practice.

---

