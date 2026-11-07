# Week 15 - CM3060 Natural Language Processing - Topic 1: Introduction to NLP (part 1) - Week 1

## 01_Introduction_and_learning_objectives_Video_1_min

# Introduction and learning objectives
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/8EryH/introduction-and-learning-objectives

This course is structured over 22 weeks, beginning with the fundamental concepts of NLP (Week 1-2) and foundational skills like basic text processing (Week 3-4). The curriculum then progresses to crucial modeling techniques, starting with language modelling (Week 5-6) and advancing into lexical semantics (Week 7-8). Next, the focus shifts to applied analysis, covering text categorisation and sentiment analysis (Week 9-10). A major section is dedicated to syntax and parsing (Week 11-12), detailing advanced methods such as Context-free grammars, Constituency parsing, Dependency parsing, and Probabilistic parsing. Subsequently, the study moves into specialized knowledge retrieval, including Information extraction (Week 13-14) and Information retrieval (Week 15-16). The course then examines interactive systems through the study of Chatbots and dialogue systems (Week 17-18). Practical application is reinforced in the final topics, covering NLP in practice and a comprehensive course summary (Week 19-20). The program concludes with a dedicated revision week followed by the final exam week (Week 21-22).

---

## 02_Boolean_retrieval_Video_10_min

# Boolean retrieval
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/1OGCf/boolean-retrieval

This course provides a comprehensive survey of Natural Language Processing (NLP), beginning with introductory concepts and progressing through basic text processing methods. Core theoretical topics include Language Modelling (Weeks 5-6) and Lexical Semantics (Weeks 7-8), which establish foundational principles of word meaning and context. The curriculum then delves into higher-level analysis, covering Text Categorisation and Sentiment Analysis (Weeks 9-10), Syntax and Parsing (Weeks 11-12), and Information Extraction (Weeks 13-14). A significant section focuses on Information Retrieval (Weeks 15-16), detailing mechanisms such as Boolean retrieval, Ranked retrieval + term weighting, and the Vector Space Model. Further topics explore conversational AI, covering Chatbots and Dialogue Systems (Weeks 17-18), while also addressing NLP in practice. The latter part of the course synthesizes these concepts, culminating in a detailed course summary (Week 20). The final weeks are dedicated to Revision (Week 21) and Exam preparation (Week 22).

---

## 03_Ranked_retrieval_+_term_weighting_Video_8_min

# Ranked retrieval + term weighting
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/EEQE7/ranked-retrieval-term-weighting

The discussion introduces information retrieval by contrasting two paradigms: Boolean retrieval and ranked retrieval. Boolean retrieval is a set-based approach utilizing Boolean operators such as AND, OR, and NOT, allowing for complex search strings, exemplified by a recruiter's search for Java developers. This method offers a very high degree of control, allowing users to articulate precise queries, and its transparency allows tracing results back to specific keywords. Furthermore, Boolean retrieval facilitates reproducibility, a crucial requirement in scientific and legal research, ensuring results are demonstrably consistent over time and across users.

However, the modern, commoditized nature of web search changes user behavior, leading to "satisficing," where users only seek the first few results deemed "good enough." To better support this dynamic, the concept of ranked retrieval is introduced, which returns matching documents in a specific order, most commonly by relevance. In ranked retrieval, the query terms are typically unstructured keywords, and the system must calculate a relevance score for each document.

The foundational representation for this scoring is the term-document matrix, where each document is treated as a count vector of length $V$, representing the total vocabulary. This leads to the "bag of words" model, which is a mathematical set ignoring the order of words within a document or query. To assign weight to these terms, the concept of term frequency (TF) is employed. TF measures a document's "aboutness" and is defined as the number of times a term $t$ appears in document $d$.

To damp the effect of highly frequent words, TF is often calculated using the log function, specifically $1 + \log(\text{TF})$, where $\text{TF}$ is the term frequency, and adding one accounts for the mathematical property that $\log(1)$ is zero. Next, the mechanism of inverse document frequency (IDF) is introduced, which accounts for a term's informativeness across the entire collection.

Rare terms are inherently more informative than ubiquitous ones, similar to the function of stop words. Document frequency ($\text{DF}$) is defined as the number of documents that contain term $t$. Since high $\text{DF}$ indicates a common term, IDF is calculated as the logarithmic inverse of document frequency: $\log(N / \text{DF}_t)$, where $N$ is the total number of documents in the collection.

The popular and effective term weighting scheme, TF-IDF, is the product of the two weights: $\text{TF-IDF} = \text{TF} \times \text{IDF}$. This measure balances both how often a term appears in a specific document (TF) and how rare it is across the collection (IDF). Finally, the overall ranking score for a particular query-document pair is the sum of all the TF-IDF weights for the terms intersecting between the query and the document. This method, widely implemented in NLP platforms like NLTK and scikit-learn, determines the final order of returned documents.

---

## 04_Boolean_retrieval_Reading

# Boolean retrieval
Reading - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/1hSYN/boolean-retrieval

Schütze, H., C.D. Manning and P. Raghavan Introduction to information retrieval. (Cambridge: Cambridge University Press, 2008). 'Boolean retrieval' . If this link is broken, please let us know via the Student Portal . Boolean retrieval Schütze, H., C.D. Manning and P. Raghavan Introduction to information retrieval. (Cambridge: Cambridge University Press, 2008). 'Boolean retrieval' . If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

## 05_Vector_space_model_Video_5_min

# Vector space model
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/ukW9Y/vector-space-model

This extensive NLP curriculum is structured into ten major topics, beginning with foundational concepts in Weeks 1-4, introducing the core methodology of NLP and basic text processing. The course progresses through Language Modelling (Weeks 5-6) and deep into Lexical Semantics (Weeks 7-8), covering how meaning is processed in text. Key technical areas include Text Categorisation and Sentiment Analysis (Weeks 9-10), followed by the structural analysis of Syntax and Parsing (Weeks 11-12) and Information Extraction (Weeks 13-14). The later stages focus heavily on Information Retrieval (Weeks 15-16), detailing techniques such as Boolean retrieval, Ranked retrieval with term weighting, and the Vector Space Model. Specific modules also cover practical application domains, including Information Retrieval (Weeks 15-16), Chatbots and Dialogue Systems (Weeks 17-18), and diverse applications in NLP in Practice (Weeks 19-20). Throughout the program, foundational concepts are reinforced by assignments covering Boolean retrieval, Vector Space Model assignments, and activities exploring various IR models. The curriculum concludes with a comprehensive summary, revision week, and examination week, ensuring mastery of all advanced NLP concepts.

---

## 06_Question_answering_Reading_1h

# Question answering
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/TeTUz/question-answering

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Check chapter 11 in the provided link. If this link is broken, please let us know via the Student Portal . Question answering Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Check chapter 11 in the provided link. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

## 07_Activity_Exploring_IR_models_Reading_1h

# Activity: Exploring IR models
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/pVVUK/activity-exploring-ir-models

This activity explores Information Retrieval (IR) models by requiring the computation of TF.IDF values for the document matrix, using the specified IDF values: car=1.75, vehicle=2.18, insurance=1.72, and best=1.60. The subsequent steps involve calculating the TF.IDF values for the query ‘best car insurance’ and finally ranking each document based on the cosine measure.

---

