# Week 9 - CM3060 Natural Language Processing - Topic 1: Introduction to NLP (part 1) - Week 1

## 01_Introduction_and_learning_objectives_Video_1_min

# Introduction and learning objectives
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/8EryH/introduction-and-learning-objectives

This course is structured over 22 weeks, beginning with the fundamental concepts of NLP (Week 1-2) and foundational skills like basic text processing (Week 3-4). The curriculum then progresses to crucial modeling techniques, starting with language modelling (Week 5-6) and advancing into lexical semantics (Week 7-8). Next, the focus shifts to applied analysis, covering text categorisation and sentiment analysis (Week 9-10). A major section is dedicated to syntax and parsing (Week 11-12), detailing advanced methods such as Context-free grammars, Constituency parsing, Dependency parsing, and Probabilistic parsing. Subsequently, the study moves into specialized knowledge retrieval, including Information extraction (Week 13-14) and Information retrieval (Week 15-16). The course then examines interactive systems through the study of Chatbots and dialogue systems (Week 17-18). Practical application is reinforced in the final topics, covering NLP in practice and a comprehensive course summary (Week 19-20). The program concludes with a dedicated revision week followed by the final exam week (Week 21-22).

---

## 02_Intro_to_text_classification_Video_8_min

# Intro to text classification
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/3VYBk/intro-to-text-classification

This comprehensive 22-week course introduces the foundational concepts of Natural Language Processing (NLP), starting with introductory topics in Weeks 1 and 2. Early focus areas include Basic Text Processing (Weeks 3 and 4), followed by Language Modelling, which covers probability concepts necessary for understanding text generation (Weeks 5 and 6). The course then delves into Lexical Semantics (Weeks 7 and 8), examining the meaning of words and phrases. A major section focuses on Text Categorisation and Sentiment Analysis (Weeks 9 and 10), introducing crucial classification methods like Bayesian classification and Multinomial Naive Bayes, which heavily utilizes Bayes' theorem. Technical skills are enhanced through extensive practice assignments, such as those dedicated to Naive Bayes and Bayes' theorem. Later topics transition into structural analysis, covering Syntax and Parsing (Weeks 11 and 12), and specialized data manipulation via Information Extraction and Information Retrieval (Weeks 13–16). The curriculum culminates with advanced dialogue systems, exploring Chatbots and Dialogue Systems (Weeks 17 and 18), before concluding with a practical overview of NLP applications (Weeks 19 and 20). The entire learning structure is reinforced by laboratory experiments, discussion prompts, and dedicated revision time. The course ensures students gain both theoretical knowledge and practical experience across the entire NLP pipeline.

---

## 03_Bayes'_theorem_Video_7_min

# Bayes' theorem
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/QNgrV/bayes-theorem

This discussion delves into Naive Bayes and Bayesian classification, beginning with a detailed review of Bayes’ Theorem. The fundamental concept of Bayes’ theorem is that new evidence should be used to update prior beliefs, rather than being treated in isolation to determine them. To illustrate this, the transcript presents a mental puzzle: determining whether a shy, meticulous colleague is more likely a librarian or a farmer. Intuitive judgment often favors a librarian based on stereotypes, neglecting the crucial role of prior probabilities.

In reality, the prior probability heavily favors farmers; for instance, in the UK in 2014, the ratio of farmers to librarians was significantly weighted, often approximated at 9:1. A rational judgment must factor in both the descriptive evidence and these baseline population probabilities. Bayes’ theorem formalizes this update process: the probability of a hypothesis given the evidence is equivalent to the hypothesis probability multiplied by the probability of the evidence given the hypothesis, divided by the probability of the evidence.

To make this concrete, a scenario involving 100 randomly sampled people is analyzed, maintaining the 90 (farmers) to 10 (librarians) prior probability ratio. If 40% of librarians and 10% of farmers fit the description, a mathematical calculation reveals that the probability of the individual being a librarian is approximately 31%. This finding critically demonstrates that the evidence does not outweigh the strong prior probability.

This concept can be generalized to a neutral case, where confidence might be 50%, illustrating that the relative proportions of areas are used to calculate relative probabilities. Mathematically, the probability of the evidence given the hypothesis is calculated as the proportion of the highlighted area divided by the total highlighted area.

Conceptualizing Bayes' theorem using areas, the area corresponding to the probability of Hypothesis (H) multiplied by the probability of Evidence given H defines a specific region. The overall probability of the evidence (the denominator) is the sum of the relevant rectangles. Ultimately, the core takeaway is that evidence serves to update existing beliefs, not establish them from scratch.

The supplementary material outlines the educational structure for this topic, covering NLP from Week 1 through Week 20. Key topics include Basic Text Processing (Weeks 3-4), Language Modelling (Weeks 5-6), Lexical Semantics (Weeks 7-8), and Text Categorisation/Sentiment Analysis (Week 9 and 10). Specific instructional modules dedicated to this subject matter include "Bayes' theorem" (7 min) and "Bayesian classification" (10 min). Furthermore, specialized modules exist for "Multinomial naive Bayes" (7 min) and "Naive Bayes classification." These modules confirm that Naive Bayes and its related classification techniques are central components of the course curriculum.

---

## 04_Bayesian_classification_Video_10_min

# Bayesian classification
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/FG8sn/bayesian-classification

This course provides a comprehensive study of Natural Language Processing, beginning with foundational concepts in Weeks 1 and 2. The curriculum progresses to basic text processing techniques, covering initial data manipulation in Weeks 3 and 4. Key intermediate concepts involve Language Modelling (Weeks 5 and 6) and the analysis of Lexical Semantics (Weeks 7 and 8). A major focus is placed on Text Categorisation and Sentiment Analysis, detailing methods like Bayes’ theorem and its application in Bayesian and Multinomial Naive Bayes classification (Weeks 9 and 10). Subsequent modules delve into structural analysis, introducing Syntax and Parsing (Weeks 11 and 12). The course then transitions into knowledge retrieval, exploring Information Extraction (Weeks 13 and 14) and Information Retrieval (Weeks 15 and 16). Advanced interaction systems are covered through the study of Chatbots and Dialogue Systems (Weeks 17 and 18). The latter phase of the course explores NLP in practice (Week 19), providing real-world application examples. Weeks 20 through 22 conclude the learning journey with a course summary, revision, and examination. The structured progression ensures deep understanding across foundational, statistical, and applied NLP domains.

---

## 05_Multinomial_naive_Bayes_Video_7_min

# Multinomial naive Bayes
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/pL0Q0/multinomial-naive-bayes

This discussion continues the topic of Bayesian classification by introducing a specialized variant: Multinomial Naive Bayes.
The previous Naive Bayes approach was based on a generative model, assuming features are generated by a model.
In that model, classification compares posterior probabilities for each label using Bayes' theorem.
This calculation involves multiplying the likelihood and the prior, then dividing by the probability of the evidence to yield the posterior probability.
Naive Bayes also relies on key assumptions, including feature independence and the equitable treatment of all features, which may not hold true in real-world data.
The Multinomial Naive Bayes variation fundamentally assumes that the features are generated from a multinomial distribution.
This approach focuses on the probability of observing counts across various categories, thus modeling by finding a best-fit multinomial distribution.
This method is highly suited for text classification tasks, such as categorizing a passage or blog post based on a topical scheme.
In this context, categories correspond to word types, meaning the multinomial distribution observes the counts across the entire vocabulary.
Since raw textual data cannot be directly processed, it must first be converted into a numerical form.
The simplest technique for this numerical conversion, reviewed previously, is the use of `TfidfVectorizer`.
For experimentation, the 20 newsgroups corpus is utilized, which is a collection of approximately 20,000 postings across 20 diverse topics.
The workflow involves setting up a data pipeline that integrates the `TfidfVectorizer` object and the `MultinomialNaiveBayes` model.
This pipeline is then fit using the training data and subsequently used to generate labels by calling the `predict` method on the test data.
A critical way to analyze the results of this classification process is through the confusion matrix.
The confusion matrix plots all pairwise possibilities, showing how true labels were classified against their predicted labels.
The diagonal elements of the confusion matrix represent correct classifications, where the predicted label matches the true label.
Off-diagonal elements reveal specific instances of misclassification, highlighting where the model made errors.
The lecture noted that some misclassifications are plausible, for instance, items for sale (`misc.forsale`) being predicted as recreational autos (`rec.autos`).
Another example pointed out that miscellaneous topics could plausibly be misclassified as talking about guns (`talk.politics.guns`).
The principles established allow the construction of a custom classifier function.
This function accepts a category, the trained model, and an arbitrary sentence to return a predicted label name.
Testing the custom function demonstrates accuracy, successfully classifying a sentence about politics as `talk.politics.misc`.
It was noted that classification difficulty increases when testing on categories not adequately covered during the training phase, such as Shakespearean text.

---

## 06_Naive_Bayes_classification_Reading_10_min

# Naive Bayes classification
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/mdsy3/naive-bayes-classification

VanderPlas, J. Python data science handbook: Essential tools for working with data . (California: O'Reilly Media, Inc., 2016), pp.382–390. Naive Bayes classification VanderPlas, J. Python data science handbook: Essential tools for working with data . (California: O'Reilly Media, Inc., 2016), pp.382–390. Mark as completed Dislike Report an issue

---

## 07_Naive_Bayes_and_sentiment_classification_Reading_1h

# Naive Bayes and sentiment classification
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/ZroNC/naive-bayes-and-sentiment-classification

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 4. Also, refer to Appendix B on this online book version. If this link is broken, please let us know via the Student Portal . Naive Bayes and sentiment classification Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 4. Also, refer to Appendix B on this online book version. If this link is broken, please let us know via the Student Portal ....

---

