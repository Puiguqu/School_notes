# 07_Text_processing_summary_Video_4_min

# Text processing summary
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/zP0Nf/text-processing-summary

This summary focuses on Topic 2: Basic Text Processing, covering the fundamentals of manipulating unstructured data in NLP.

The course objectives for text processing were defined as understanding fundamentals, applying techniques, and manipulating unstructured data. A primary task in processing natural language is resolving the considerable ambiguity present in human language. Before intent or structure can be determined, ambiguity must be addressed at various linguistic levels. The basic level of analysis begins with lexical analysis, essentially known as tokenization. Various approaches to tokenization and whitespace exist, but they require smarter techniques to identify appropriate tokens.

Stemming is a crude process of chopping word endings to reduce them to a common root, though this root may not always be a genuine word. Lemmatization solves this issue by analyzing the process in a more linguistically principled manner. Lemmatization considers the syntactic context to identify the correct lemma or root for each input word. Morphology refers to the shape of words; English is less morphologically complex than languages like German, which exhibits complex compounding behavior.

The next stage involves syntax, which analyzes the syntactic role of each word to interpret the sentence structure. Syntax also presents ambiguity, exemplified by the phrase, "I saw the man on the hill with a telescope." Solving this requires utilizing contextual information rather than syntax alone. Sentence boundary detection is another challenging task; while simple rules based on punctuation help, exceptions are common in linguistic data.

Regular expressions offer a highly flexible tool, enabling diverse text processing tasks. These expressions are used effectively to extract specific data points, such as URLs, email addresses, and dates. Furthermore, stop word removal is a necessary step, but there is no definitive universal list for English or any language. The selection of a stop word list must depend entirely on the specific application or goal being pursued.

Finally, text corpora—large samples of textual data—allow for various linguistic and stylistic analyses. Four types of corpora were briefly examined: isolated, categorized, overlapping, and temporal. The entire process of text data handling moves toward advanced topics like language modeling. The associated coursework includes dedicated modules on Regular Expressions (Parts 1 & 2), Stop Words, and Text Corpora. The curriculum progresses through these stages, leading eventually to advanced treatments of language and NLP in practice.

