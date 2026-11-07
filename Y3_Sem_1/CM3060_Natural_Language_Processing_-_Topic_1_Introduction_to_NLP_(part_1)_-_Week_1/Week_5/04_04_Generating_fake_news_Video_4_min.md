# 04_Generating_fake_news_Video_4_min

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

