# 01_Chunking_Video_7_min

# Chunking
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/u9RJ9/chunking

Information extraction relies heavily on the process of chunking, which is defined as identifying meaningful chunks within a body of text. For the purposes of this practical example using NLTK, these meaningful chunks are typically conceptualized as noun phrases (NP). To begin, NLTK is utilized, often paired with a sentence that has already been parts-of-speech (POS) tagged. A crucial step involves defining a pattern for the desired noun phrase using a regular expression. The initial grammar definition stipulates an NP consists of an optional determiner, followed by zero or more adjectives, concluding with a noun. This grammar is applied using the `nltk.RegexpParser` class, which is instantiated with the defined grammar. Running the parser successfully identifies the NP structure based on the determiner-adjective-noun pattern. However, the basic grammar is inherently limited; it fails to correctly identify complex examples, such as dropping the word "measures" in "Any new policy measures."

To accommodate complexity, the grammar must be modified significantly. An updated grammar might include an optional determiner, zero or more adjectives (like the comparative form, JJR), and one or more nouns (such as the plural form, NNS). By incorporating these structures, the parser can successfully recognize more intricate NP examples like "earliest stages." Furthermore, grammars can be extended to span multiple lines to handle increasingly complex linguistic structures. When parsing a sentence like "Rapunzel let down her long golden hair," the parser requires a refined grammar to accurately capture the entire phrase. This refinement involves including possessives (a determiner or possessive) in the pattern and correctly defining the sequence of adjectives and nouns.

A key concept in regular expressions is greedy matching, which dictates that if a grammar defines a sequence of two or more nouns, the parser will capture the first match it encounters. This leads to the concept of chinking, which is the inverse of chunking. Chinking involves chunking the entire sequence of text and then specifically removing or ignoring undesired bits. This is achieved by defining negative matching within the grammar, such as targeting sequences of past tense and prepositions.

Finally, a standard method for marking up these labeled sequences is using IOB tags (Beginning, Inside, Outside). The 'B' tag marks the beginning of a chunk, 'I' marks the subsequent words inside the chunk, and 'O' marks text outside any identified chunk. For example, in "the yellow dog," 'the' might be tagged as the beginning of the NP, while 'yellow' and 'dog' would be inside. This IOB system allows for highly flexible notation, enabling the representation of multiple, non-overlapping chunk types for sophisticated information extraction.

