# Week 6 - CM3060 Natural Language Processing - Topic 1: Introduction to NLP (part 1) - Week 1

## 01_Intro_to_language_modelling_Video_9_min

# Intro to language modelling
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/ALrrl/intro-to-language-modelling

This comprehensive course outlines a progression through advanced Natural Language Processing (NLP), beginning with introductory concepts and basic text processing techniques (Weeks 1–4). The core technical focus is Statistical Language Modelling (Weeks 5–6), which involves detailed study on estimating probabilities and evaluating the performance of language models. A key related technique is Topic Modelling (Section 3.3), dedicated to experiments in understanding and analyzing textual themes. The curriculum then expands into deep linguistic analysis, covering Lexical Semantics (Weeks 7–8) and Syntax and Parsing (Weeks 11–12). Practical applications begin with Text Categorisation and Sentiment Analysis (Weeks 9–10), moving into structured data extraction via Information Extraction (Weeks 13–14) and Information Retrieval (Weeks 15–16). Furthermore, the course addresses complex human-computer interaction through Chatbots and Dialogue Systems (Weeks 17–18). Specialized skills are reinforced by the module on NLP in Practice (Weeks 19–20), synthesizing the diverse techniques learned. The entire course structure is supplemented by video lessons, practice assignments, and peer-graded assessments across all major topics. The final weeks (Week 21 and Week 22) are dedicated to revision and the examination, ensuring full mastery of the covered domain.

---

## 02_Estimating_probabilities_Video_9_min

# Estimating probabilities
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/uwN8g/estimating-probabilities

Language modeling involves estimating the probabilities of word sequences found within a training corpus. Initially, these probabilities are calculated by simply counting the occurrences of specific word patterns in the available data. However, this counting approach is limited because training corpora are finite, leading to the critical problem of sparse data. If a specific utterance or word sequence is not found in the training data, its probability is assigned a zero value. To manage this, the Markov assumption is employed, which dictates conditioning a word's probability on only a shorter, localized fragment of its history, such as bigrams or trigrams.

The starting point for probability estimation is the Maximum Likelihood Estimator (MLE). The MLE calculates the probability of a word $w_i$ given its preceding word $w_{i-1}$ as: $P(w_i | w_{i-1}) = \frac{\text{Count}(w_{i-1} w_i)}{\text{Count}(w_{i-1})}$. Although simple, this method fails when data is sparse, as it assigns a zero probability to any unobserved bigram.

To overcome the sparse data problem, language modelers seek to "smooth" the probability distribution. This involves shifting probability mass from highly likely events to potential, yet unseen, events in the vocabulary.

One simple technique is Laplace smoothing, which adds one to all observed counts. This yields the smoothed probability estimate: $P(w_i | w_{i-1}) = \frac{\text{Count}(w_{i-1} w_i) + 1}{\text{Count}(w_{i-1}) + |\text{V}|}$, where $|\text{V}|$ is the size of the vocabulary. Although effective, Laplace smoothing is considered a crude approach and more advanced schemes are often preferred in statistical language modeling.

Two more robust schemes for dealing with sparse counts are backoff and interpolation. Backoff operates by progressively falling back to a lower-order model if sufficient evidence is lacking in a higher-order model. For example, the system attempts to estimate $P(w_i | \text{history})$ using a trigram; if its count is zero, it "backs off" to the bigram estimate.

This process continues down the hierarchy—from trigram to bigram, and finally to the unigram model—with specific weighting factors applied at each level. Interpolation offers an alternative strategy where all models (trigram, bigram, and unigram) are utilized simultaneously. Instead of backing off, interpolation mixes the estimates by assigning weights, denoted as $\lambda_1, \lambda_2,$ and $\lambda_3$, to each level. These weights must be chosen such that $\lambda_1 + \lambda_2 + \lambda_3 = 1$. In essence, interpolation provides a balanced estimate derived from multiple contextual levels, creating a more robust model than a pure backoff approach.

---

## 03_Evaluating_language_models_Video_6_min

# Evaluating language models
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/DlqVs/evaluating-language-models

This course provides a comprehensive progression through Natural Language Processing (NLP), starting with foundational concepts (Weeks 1-4) and moving into core linguistic modeling techniques. Key early topics include Basic Text Processing (Weeks 3-4) and a deep dive into Language Modelling (Weeks 5-6), covering probability estimation and model evaluation. Subsequent focus shifts to advanced modeling, specifically introducing Topic Modelling (Week 3.3) for discovering abstract themes within text data. The syllabus then tackles linguistic meaning, starting with Lexical Semantics (Weeks 7-8), which concerns the meaning of individual words. The course progresses through complex structural analysis, dedicated to Text Categorisation and Sentiment Analysis (Weeks 9-10), followed by Syntax and Parsing (Weeks 11-12). Further advanced topics include Information Extraction (Weeks 13-14) and Information Retrieval (Weeks 15-16), essential for data mining and searching. Finally, the curriculum addresses applied systems through Chatbots and Dialogue Systems (Weeks 17-18) and culminates in practical applications and course summation (Weeks 19-20). The structure is heavily supported by various multimedia resources, including specialized videos, practice assignments, and peer-graded learning modules.

---

## 04_Language_modelling_Reading

# Language modelling
Reading - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/Alt02/language-modelling

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 3 If this link is broken, please let us know via the Student Portal . Language modelling Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 3 If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

## 05_Topic_modelling_Video_11_min

# Topic modelling
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/70J53/topic-modelling

Topic modeling is an investigation technique similar to language modeling, aiming to find patterns and relationships within vast quantities of text data. However, unlike language modeling which models individual word sequences, topic modeling searches for

---

## 06_Topic_modelling_Reading

# Topic modelling
Reading - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/exW1V/topic-modelling

Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 6, pp.185-201. If this link is broken, please let us know via the Student Portal. Topic modelling Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks ....

---

## 07_Language_modelling_summary_Video_3_min

# Language modelling summary
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/7cMt2/language-modelling-summary

This course provides a comprehensive introduction to Natural Language Processing (NLP), structured across twenty weeks of specialized topics. The early weeks focus on foundational concepts, starting with an introduction to NLP, followed by essential basic text processing techniques. The program then dives deeply into Language Modelling, covering the theory, estimating probabilities, and the crucial evaluation of language models.

A significant module is dedicated to Topic Modelling, teaching methods for experimentation and understanding how abstract themes are derived from large texts. Progression continues with Lexical Semantics, which examines the meaning of words, before moving into Text Categorization and Sentiment Analysis. Technical skills expand further through Syntax and Parsing, which focuses on the structural analysis of language.

The latter half of the course emphasizes advanced applications, starting with Information Extraction and subsequently covering Information Retrieval techniques. The curriculum then addresses interactive NLP systems, introducing Chatbots and Dialogue Systems. Finally, the course concludes by applying these concepts through NLP in Practice and a comprehensive course summary. The structure ensures a complete mastery of core NLP methodologies, culminating in revision and examination periods.

---

