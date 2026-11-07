# 04_POS_tagging_Video_5_min

# POS tagging
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/D0izE/pos-tagging

This transcript introduces Part-of-Speech (POS) tagging, focusing on its role as a vital middle stage in a high-level NLP processing pipeline. Previously, information extraction focused on elementary tags like sentence segmentation and tokenization, followed by sequential processing stages such as POS tagging, Named Entity Recognition (NER), and relation extraction. This lesson specifically drills into the mechanics of POS tagging, which is defined as assigning words to a specific lexical category based on a defined tag set.

To commence the practical demonstration, the speaker utilizes a Jupyter notebook and imports the NLTK library. A sample sentence, sourced from the Reuters corpus, is first tokenized, separating the continuous text into distinct terms. Next, a POS tagger is downloaded from NLTK and applied to the tokenized sentence. The resulting output provides each term alongside its corresponding lexical category tag, such as NNP (proper noun), VBZ (third person singular present tense of a verb), VBN (past participle), and VBG (gerund form).

The core importance of tagging lies in resolving the inherent ambiguity found in human language and syntactic structures. A representative example provided is the ambiguous phrase, "They refuse to permit us to obtain the refuse permit." Although visually identical in spelling, the words "refuse," "permit," and "refuse" (as a noun) are contextually distinct.

The POS tagger successfully navigated this ambiguity, correctly tagging the forms as verbs or nouns based on their usage within the sentence structure. For instance, the instances of "refuse" and "permit" when acting as verbs were correctly categorized, while the noun forms within "the refuse permit" were properly identified as nouns. This demonstrates the tagger's ability to accurately determine lexical categories despite identical spelling.

The transcript further discusses various types of tag sets, noting that they can vary significantly in size, complexity, and level of detail. The default tag set utilized by NLTK is the UPENN tagset. By examining this tagset, the speaker illustrates detailed categories like PRP (personal pronoun), VBP (third person singular present tense of a verb), and DT (determiner).

In summary, POS tagging is a foundational technique for classifying words into predefined categories, enabling more sophisticated NLP operations. The practical demonstration validates its efficacy in resolving lexical ambiguity present in written text. The conclusion sets the stage for subsequent lessons, promising to utilize POS tagging to perform advanced transformations, specifically identifying named entities and extracting relations.

