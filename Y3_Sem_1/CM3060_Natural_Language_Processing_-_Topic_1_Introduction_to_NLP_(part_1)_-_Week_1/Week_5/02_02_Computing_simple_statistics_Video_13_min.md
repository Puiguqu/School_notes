# 02_Computing_simple_statistics_Video_13_min

# Computing simple statistics
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/2US9n/computing-simple-statistics

This practical NLP session shifts focus from academic NLP to applied examples using the NLTK library within a Jupyter Notebook environment. The exercise begins by importing NLTK and accessing several introductory example texts, each serving as a unique corpus. These eight texts provide diverse linguistic data, including novels (Moby Dick by Herman Melville, Sense and Sensibility by Jane Austen), religious works (Bible), political writings, and specialized collections like the Chat Corpus and Wall Street Journal articles. A corpus is defined as a body of text, allowing for comparisons between different linguistic sources.

Initial analysis involves checking the sheer size of the texts using the `len()` method, noting, for instance, that Text 1 (Moby Dick) contains approximately 260,000 words, while Text 6 (Monty Python) is much smaller, at 16,967 words. A critical distinction is then drawn between word tokens and word types. Tokenization is the process of breaking a string into individual components, which are called tokens. In contrast, word types represent unique, non-duplicate words within the text.

To find the number of word types, the set operator is applied to the text, which effectively removes all duplicates. The length of this resulting set represents the total vocabulary or number of word types. Text 1, despite having 260,000 tokens, consists of significantly fewer word types, totaling 19,000.

This comparison leads to the calculation of Lexical Diversity, a measure of text variability. This diversity is mathematically defined as the length of the set of the text (word types) divided by the length of the text (word tokens). The function applied to Text 1 yields a lexical diversity figure of 0.074, while Text 8 shows a higher diversity of 0.22, offering insight into linguistic richness across different genres.

The next analytical stage explores frequency distribution, which counts how many times each word type occurs, utilizing the built-in NLTK method `FreqDist`. Applying `FreqDist` to Text 1 reveals that punctuation marks (like the comma) and common function words (like 'the' and 'of') are the most frequent items. The `FreqDist` object can output the most common terms (e.g., the top 10) or confirm the occurrence of a specific term.

Visualization of frequency distributions often reveals a power law curve, which suggests that in natural languages, a few words appear extremely frequently while many others are used sparingly.

The final core concept introduced is collocations, which are groups of words that stick together more frequently than would occur by chance (e.g., "red wine"). Collocations are analogous to bigrams but exhibit a stronger contextual affinity. Analyzing collocations in Text 1 yields characteristic phrases such as "Sperm Whale" and "Moby Dick

