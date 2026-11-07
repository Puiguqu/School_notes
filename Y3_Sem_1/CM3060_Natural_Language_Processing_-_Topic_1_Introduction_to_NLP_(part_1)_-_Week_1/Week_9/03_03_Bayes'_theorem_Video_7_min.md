# 03_Bayes'_theorem_Video_7_min

# Bayes' theorem
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/QNgrV/bayes-theorem

This discussion delves into Naive Bayes and Bayesian classification, beginning with a detailed review of Bayes’ Theorem. The fundamental concept of Bayes’ theorem is that new evidence should be used to update prior beliefs, rather than being treated in isolation to determine them. To illustrate this, the transcript presents a mental puzzle: determining whether a shy, meticulous colleague is more likely a librarian or a farmer. Intuitive judgment often favors a librarian based on stereotypes, neglecting the crucial role of prior probabilities.

In reality, the prior probability heavily favors farmers; for instance, in the UK in 2014, the ratio of farmers to librarians was significantly weighted, often approximated at 9:1. A rational judgment must factor in both the descriptive evidence and these baseline population probabilities. Bayes’ theorem formalizes this update process: the probability of a hypothesis given the evidence is equivalent to the hypothesis probability multiplied by the probability of the evidence given the hypothesis, divided by the probability of the evidence.

To make this concrete, a scenario involving 100 randomly sampled people is analyzed, maintaining the 90 (farmers) to 10 (librarians) prior probability ratio. If 40% of librarians and 10% of farmers fit the description, a mathematical calculation reveals that the probability of the individual being a librarian is approximately 31%. This finding critically demonstrates that the evidence does not outweigh the strong prior probability.

This concept can be generalized to a neutral case, where confidence might be 50%, illustrating that the relative proportions of areas are used to calculate relative probabilities. Mathematically, the probability of the evidence given the hypothesis is calculated as the proportion of the highlighted area divided by the total highlighted area.

Conceptualizing Bayes' theorem using areas, the area corresponding to the probability of Hypothesis (H) multiplied by the probability of Evidence given H defines a specific region. The overall probability of the evidence (the denominator) is the sum of the relevant rectangles. Ultimately, the core takeaway is that evidence serves to update existing beliefs, not establish them from scratch.

The supplementary material outlines the educational structure for this topic, covering NLP from Week 1 through Week 20. Key topics include Basic Text Processing (Weeks 3-4), Language Modelling (Weeks 5-6), Lexical Semantics (Weeks 7-8), and Text Categorisation/Sentiment Analysis (Week 9 and 10). Specific instructional modules dedicated to this subject matter include "Bayes' theorem" (7 min) and "Bayesian classification" (10 min). Furthermore, specialized modules exist for "Multinomial naive Bayes" (7 min) and "Naive Bayes classification." These modules confirm that Naive Bayes and its related classification techniques are central components of the course curriculum.

