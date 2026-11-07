# Week 5 - CM3060 Natural Language Processing - Topic 1: Introduction to NLP (part 1) - Week 1

## 01_Introduction_and_Learning_Objectives_Video_2_min

# Introduction and Learning Objectives
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/2RgnI/introduction-and-learning-objectives

This comprehensive course spans 20 weeks, systematically covering the foundational concepts and advanced applications of Natural Language Processing (NLP). The initial phase (Weeks 1-4) establishes core NLP principles and fundamental skills in basic text processing, including accessing and experimenting with large text corpora. The curriculum progresses into Language Modelling (Weeks 5-6), detailing how simple statistics and conditional frequency distributions are used to compute language probabilities and generate realistic text. Lexical semantics and Text Categorization (Weeks 7-10) address the meaning of words, focusing heavily on sentiment analysis and classification techniques.

Further technical depth is achieved through Syntax and Parsing (Weeks 11-12), which provides the framework for analyzing the grammatical structure of text. This is followed by Information Extraction and Information Retrieval (Weeks 13-16), teaching methods for extracting key facts and effectively searching large databases. The study then moves into practical interaction design via Chatbots and Dialogue Systems (Weeks 17-18). The course culminates in Week 19, where NLP is applied to real-world scenarios, followed by a final course summary and subsequent revision and exam periods. These modules ensure a complete understanding of how complex linguistic structures are handled by computational systems.

---

## 02_Computing_simple_statistics_Video_13_min

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

---

## 03_Conditional_frequency_distributions_Video_7_min

# Conditional frequency distributions
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/84iA9/conditional-frequency-distributions

This course is structured across 22 weeks, progressing through fundamental concepts of Natural Language Processing (NLP) and culminating in applied NLP projects. The early weeks establish the foundation with general NLP introductions (Weeks 1-2) and subsequent basic text processing techniques (Weeks 3-4). A major focus is dedicated to Language Modelling (Weeks 5-6), which covers computing simple statistics, conditional frequency distributions, and the generation of fake news. The curriculum then moves into understanding meaning, detailing Lexical Semantics (Weeks 7-8) before advancing to text categorisation and sentiment analysis (Weeks 9-10).

Structural analysis is introduced in Weeks 11-12 through Syntax and Parsing, allowing for the identification of grammatical relationships within text. The field then transitions to advanced information handling, covering Information Extraction (Weeks 13-14) and subsequently Information Retrieval (Weeks 15-16). Further specialization is found in Weeks 17-18, dedicated to developing sophisticated Chatbots and Dialogue Systems.

The final modules wrap up the theoretical knowledge by exploring NLP in Practice (Week 19) and providing a comprehensive course summary (Week 20). The entire progression is supported by theoretical readings, practical assignments, and laboratory exercises, such as those involving Unix for Poets and text generation, leading up to a final revision and examination (Weeks 21-22).

---

## 04_Generating_fake_news_Video_4_min

# Generating fake news
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/MWKD0/generating-fake-news

This series investigates how Natural Language Toolkit (NLTK) can be utilized to generate synthetic, or "fake," news content. The core technique employed involves the generation of bigrams, which are defined as all word pairs within a given sentence. To demonstrate this, the NLTK method `bigrams` is applied to a sentence, such as "the cat sat on the mat," resulting in pairs like "cat sat," "sat on," and "on the."

The generation process begins by acquiring a source of news data, which is sourced from the Brown Corpus. Specifically, the text corpus is filtered using `brown.words`, limiting the data to records where `categories equals news`.

The bigrams extracted from this corpus are then compiled into a Conditional Frequency Distribution (CFD). This CFD holds statistical information about which word is most likely to follow any given word.

A custom algorithm, dubbed `generate text`, is subsequently defined to utilize this CFD for text generation. This method requires three inputs: the CFD, a specified starting word, and the desired number of output words.

The iterative nature of `generate text` is critical to its function. It begins by printing the starting word. It then consults the CFD to identify the most common word that follows the current word. This highly probable word is printed, and the loop repeats, searching for the most common bigram following this newly generated word.

This sequential lookup and printing process allows the system to build a continuous chain of words, effectively generating random, yet statistically probable, text. Testing the CFD trained on the news corpus reveals common patterns, such as the prevalence of "New" being followed by city names like "New York" or "New Orleans."

When the `generate text` method is initiated starting with the word "new," the system successfully produces a simulated news snippet, such as "New York City, and the first time, the President Kennedy, and the first time."

This simulated output demonstrates a sound principle, illustrating how modern fake news generators operate by reproducing crude modeling patterns found within natural language.

However, the simple bigram model exhibits limitations. For instance, the generated text frequently converges and gets stuck in loops, as seen when starting with "the," which results in repetitive phrases like "President Kennedy on the first time."

To improve the model’s quality and variability, two primary methods can be implemented. One technique involves increasing the pattern length beyond strings of length two (bigrams), upgrading to trigrams (strings of length three). The second improvement is introducing randomness. Instead of always selecting the maximum probability word from the CFD, a random selection can be chosen from the list of bigrams associated with the current word.

Despite its simplicity, this custom generator, built using only half a dozen lines of code, provides a fundamental understanding of language modeling. It serves as a basic, demonstrable tool for experimenting with text generation principles in NLP. This entire process highlights how statistical language modeling is the foundational mechanism for large-scale text synthesis.

---

## 05_Accessing_text_corpora_Reading_1h

# Accessing text corpora
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/MGp0Z/accessing-text-corpora

Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 2.2-2.3 (pp.52-59). If this link is broken, please let us know via the Student Portal . Accessing text corpora Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 2.2-2.3 (pp.52-59). If this link is broken, please let us know via the Student Portal ....

---

## 06_Unix_for_Poets_Reading_1h

# Unix for Poets
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/jM6g2/unix-for-poets

Church, K.W. 'Unix™ for poets' , Notes of a course from the European Summer School on Language and Speech Communication, Corpus Based Methods (1994). If this link is broken, please let us know via the Student Portal . Unix for Poets Church, K.W. 'Unix™ for poets' , Notes of a course from the European Summer School on Language and Speech Communication, Corpus Based Methods (1994). If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

