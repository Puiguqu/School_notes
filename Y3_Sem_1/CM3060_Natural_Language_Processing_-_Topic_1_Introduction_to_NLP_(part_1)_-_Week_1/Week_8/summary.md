# Week 8 - CM3060 Natural Language Processing - Topic 1: Introduction to NLP (part 1) - Week 1

## 01_Intro_to_word_embeddings_Video_16_min

# Intro to word embeddings
Video • 16 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/cUvLX/intro-to-word-embeddings

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

## 02_Vector_semantics_Reading_1h

# Vector semantics
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/BSaa8/vector-semantics

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5 If this link is broken, please let us know via the Student Portal . Vector semantics Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5 If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

## 03_Word_embeddings_in_practice_Video_8_min

# Word embeddings in practice
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/rHypB/word-embeddings-in-practice

This course provides a comprehensive progression through Natural Language Processing (NLP), beginning with introductory concepts and basic text processing techniques (Weeks 1-4). Early instruction transitions into Language Modelling (Weeks 5-6), establishing probabilistic frameworks for understanding language structure. A significant focus is placed on Lexical Semantics (Weeks 7-8), specifically detailing Vector Semantics and introducing word embeddings. The curriculum covers advanced topics like Word2vec and word vector algebra, utilizing practice assignments and experiments to grasp the semantic properties of embeddings and analyze bias. Subsequent modules apply these concepts to Text Categorisation and Sentiment Analysis (Weeks 9-10), moving into supervised learning paradigms. Structural analysis is addressed through Syntax and Parsing (Weeks 11-12), which examines the grammatical rules governing sentence construction. The course then delves into information gathering, covering Information Extraction (Weeks 13-14) and Information Retrieval (Weeks 15-16). These foundational skills are built upon to develop complex systems, notably Chatbots and Dialogue Systems (Weeks 17-18). The study culminates in practical applications in NLP (Week 19), followed by a comprehensive course summary and final revision (Weeks 20-22).

---

## 04_Word2vec_Reading

# Word2vec
Reading - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/jAjR4/word2vec

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5, section 5.5. If this link is broken, please let us know via the Student Portal . Word2vec Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5, section 5.5. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

## 05_Word_vector_algebra_Video_5_min

# Word vector algebra
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/CGpdf/word-vector-algebra

This video and associated material explore the unexpected and powerful capability of word embeddings: their ability to perform vector algebra. Word embeddings are fundamentally dense vectors that encapsulate the context in which words appear. These vectors allow researchers to find conceptual similarities between terms, but their most crucial function is enabling meaningful pattern discovery through vector arithmetic. Historically, verbal reasoning tasks, such as A is to B as C is to ?, rely on human intuition, but these embeddings, trained using word2vec and Gensim, can perform these calculations.

The technique involves treating words as vectors in a high-dimensional space, allowing operations like addition and subtraction to yield conceptually related results. For instance, demonstrating a relational analogy, the process involves taking the target vector, subtracting the source concept, and adding the context concept. If we seek the relationship (woman is to ?) given (man is to king), the calculation approximates: $\text{Vector}(\text{King}) - \text{Vector}(\text{Man}) + \text{Vector}(\text{Woman})$. Using the Google News model, this operation successfully yielded 'queen' as the top result.

This illustrates how the embeddings encode abstract concepts, not just vocabulary. Further examples showcase the power of this semantic encoding. When asked to define the geographic relationship: Berlin is to Germany as Paris is to ?, the model successfully extracted 'France.' This demonstrates that encyclopedic knowledge is effectively encoded within the dense factors of the word2vec models.

The capabilities extend beyond simple factual relationships, touching upon syntactic patterns. Applying vector algebra to inflections, the operation (Have - Be) relative to 'has' correctly identified 'is' as the third-person singular form. Similarly, for adjective transformations, the analogy $\text{Longest} - \text{Short}$ relative to 'longest' resulted in 'shortest.'

Semantic relationships are also found through transformations like antonymy. Using the structure $\text{Dark} - \text{Light}$ relative to 'longest,' the system accurately identified 'short' as the appropriate antonym to 'long.' The model can even handle complex grammatical shifts, such as finding the proper pronoun transformation when $\text{He}$ is to $\text{She}$ as $\text{Him}$ is to ?, successfully outputting 'her.'

Furthermore, the models can perform rudimentary categorization tasks, identifying the odd one out in a list, as demonstrated by correctly classifying 'cereal' among 'Breakfast, Dinner, and Lunch.' This comprehensive application confirms the incredible flexibility of word embeddings for a wide variety of Natural Language Processing (NLP) tasks. The associated course content details these methods under "Vector semantics and embeddings," emphasizing the practical application of word vector algebra. This approach provides a deep insight into how language models capture grammar, knowledge, and context simultaneously within dense vector representations.

---

## 06_Semantic_properties_of_embeddings_Reading_1h

# Semantic properties of embeddings
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/56nOO/semantic-properties-of-embeddings

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5, section 5.7. Semantic properties of embeddings Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5, section 5.7. Mark as completed Dislike Report an issue

---

## 07_Bias_and_embeddings_Reading_1h

# Bias and embeddings
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/3a5q2/bias-and-embeddings

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5, section 5.8 If this link is broken, please let us know via the Student Portal . Bias and embeddings Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5, section 5.8 If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

## 08_Lexical_semantics_summary_Video_4_min

# Lexical semantics summary
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/xPRmE/lexical-semantics-summary

This course provides a comprehensive, 22-week curriculum spanning foundational to advanced Natural Language Processing (NLP) techniques. Initial modules introduce NLP fundamentals (Weeks 1-4), progressing quickly into core language modeling principles (Weeks 5-6). A significant technical focus is dedicated to Lexical Semantics (Weeks 7-8), specifically detailing vector semantics, word embeddings, and the Word2vec algorithm. Key technical deep dives involve understanding the mathematical basis of word vector algebra and analyzing the semantic properties and biases inherent in these embeddings. The curriculum then advances to practical applications, covering Text Categorization and Sentiment Analysis (Weeks 9-10). Further specialized topics include the structural complexity of Syntax and Parsing (Weeks 11-12), followed by Information Extraction and Information Retrieval methodologies (Weeks 13-16). Later weeks apply these concepts to modern conversational AI, exploring Chatbots and Dialogue Systems (Weeks 17-18). The course culminates with an application-based module on NLP in practice (Week 19), concluding with a course summary and revision week. The technical journey moves from basic text processing to complex modeling, from tokenization to deep vector representation and structured language understanding.

---

