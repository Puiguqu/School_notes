# Week 16 - CM3060 Natural Language Processing - Topic 1: Introduction to NLP (part 1) - Week 1

## 01_Representing_documents_Video_7_min

# Representing documents
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/4ugLx/representing-documents

The text details the practical application of the Bag of Words (BoW) model for document representation in Natural Language Processing (NLP) and information retrieval. The process involves turning unstructured text data into structured, quantifiable features.

The primary tools utilized are `CountVectorizer` from Scikit-learn, which generates vectors based on term counts, and `NLTK`, used for initial text tokenization. The workflow begins by importing these tools and defining helper functions for basic text processing.

For a sample corpus, the vectorizer is instantiated, and the crucial `fit_transform` method is called on the set of input sentences. This fitting step establishes the vocabulary across all documents, generating the feature matrix $X$.

The feature matrix $X$ is initially produced as a sparse matrix, representing the data efficiently. Conceptually, each entry in $X$ is interpreted as a tuple: (Document ID, Term ID, Count). The vocabulary size is determined by the range of Term IDs, which reached 121 in the initial sample.

This sparse representation can be converted into a dense matrix using NumPy. The dense form displays each document on a separate line, with a feature vector of all 121 term occurrences listed for every document.

A key function of the vectorizer is providing `feature_names`, which maps the Term IDs to their corresponding vocabulary words. To apply the vectorizer to new data, such as a new sentence, only the `transform` method is used, utilizing the vocabulary learned during the initial `fit`.

The process demonstrates how to use the BoW model for elementary information processing. However, the vocabulary can be significantly refined using preprocessing techniques.

One critical refinement is the application of stop words. By instructing the vectorizer to remove common terms (e.g., using `stop_words='english'`), the vocabulary size was successfully reduced from 121 to 76. Stop words are generally considered less informative.

Another powerful method is document frequency (DF) filtering, which addresses the concept of Inverse Document Frequency (IDF). This technique eliminates terms that are too ubiquitous.

By setting a maximum document frequency (`max_df`), such as three, the vectorizer removes terms that appear in more than that number of documents. This filtering further reduced the vocabulary size from 121 to 119, and subsequently to 114 when the threshold was lowered.

Ultimately, the text illustrates the complete pipeline for creating a Bag of Words model. This model allows for the translation of linguistic data into numerical vectors.

The combination of `CountVectorizer`, tokenization, stop word removal, and document frequency filtering provides a robust framework for various Information Retrieval and Natural Language Processing tasks. This approach is fundamental for tasks like searching and information sharing.

---

## 02_Term_weighting_using_TF.IDF_Video_5_min

# Term weighting using TF.IDF
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/h4wVF/term-weighting-using-tf-idf

This course provides a comprehensive journey through Natural Language Processing (NLP), beginning with foundational concepts (Weeks 1-2) and progressing through basic text processing techniques (Weeks 3-4). Subsequent modules focus on advanced linguistic understanding, specifically introducing Language Modelling (Weeks 5-6) and Lexical Semantics (Weeks 7-8). The curriculum then shifts to applied NLP, covering Text Categorisation and Sentiment Analysis (Weeks 9-10) and detailed linguistic structure through Syntax and Parsing (Weeks 11-12).

Further specialized topics include Information Extraction (Weeks 13-14) and Information Retrieval (Weeks 15-16), where key technical methodologies are covered. Crucially, Week 16 details "Term weighting using TF.IDF," a core concept for document representation and search. Additional IR topics explored include semantic search, query expansion for professional search, and the practice of Boolean search.

The final stages of the course expand into interactive systems, studying Chatbots and Dialogue Systems (Weeks 17-18), before concluding with application and review. Week 19 and 20 focus on practical NLP implementations and a comprehensive course summary, culminating in a final revision and exam period.

---

## 03_Capturing_semantics_Reading_1h

# Capturing semantics
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/ElvaK/capturing-semantics

Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 3. Capturing semantics Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 3. Mark as completed Dislike Report an issue

---

## 04_Semantic_search_Video_9_min

# Semantic search
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/i43ss/semantic-search

This segment provides an overview of representing documents and implementing various weighting schemes within a conceptual search engine framework. Although real search engines are far more complex, this exercise offers insight into building a functional system in a limited scope. The project utilizes the IMDB dataset, a semi-structured database containing fields such as rank, title, genre, and a free-text description field used for searching. From a search engine perspective, this catalog serves as the corpus being indexed. A critical concept introduced is "Query Term Expansion," which is vital in web search. This expansion directly solves the "vocabulary mismatch problem," where users' keywords may not perfectly match the terminology used in documents, despite a conceptual match. To address this, the process employs Word2Vec via the Gensim library for query term expansion. The setup begins in a Jupiter notebook environment with necessary library imports. Specifically, the Whoosh library is imported to build the open-source search engine. Gensim is also imported, facilitating dense factors and similarity matching with linguistic data. A pre-trained model, `model.bin`, is used, sourced from repositories like vectors.npl.eu. This specific model is trained on an English language corpus using the word2vec continuous skipgram algorithm. Crucially, this model utilizes 100 dimensions and a window size of 10. Variables are set for the dataset path (CSV format) and the index path, which functions like the inverted index (postings lists). The search engine structure is defined, emphasizing the parsing of queries against the title and description fields. After instantiation, the Gensim model is loaded using the defined path. The system features a "Get similar words" method, which calls the model's most similar function to retrieve top matching terms for a given search query. Demonstrating its function, searching for the term "Galactic" yields matching terms such as "intergalactic" and "interstellar." To perform the search, the initial term is joined with these expanded words using a large OR statement, mirroring boolean retrieval. This query expansion process successfully identifies relevant films, such as "Guardians of the Galaxy," demonstrating the semantic search capability. A second test using the query "gigantic" successfully expands to terms like "Colossal," returning the movie "Colossal." Other useful Gensim methods demonstrated include "Doesn't_match" and "Most_similar_to_given" for NLP applications. In summary, Whoosh serves as the robust search engine library, while Gensim augments it with semantic search capability for query expansion. This integration allows for refined search outcomes by addressing vocabulary mismatch effectively.

---

## 05_Query_expansion_for_professional_search_Reading_1h

# Query expansion for professional search
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/lZyOv/query-expansion-for-professional-search

Russell-Rose, T., P. Gooch and U. Kruschwitz ' Interactive query expansion for professional search applications ', Business Information Review, 2021. If this link is broken, please let us know via the Student Portal . Query expansion for professional search Russell-Rose, T., P. Gooch and U. Kruschwitz ' Interactive query expansion for professional search applications ', Business Information Review, 2021. If this link is broken, please let us know via the Student Portal ....

---

## 06_Activity_Exploring_Boolean_search_Reading_10_min

# Activity: Exploring Boolean search
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/waS0C/activity-exploring-boolean-search

the attached pdf file and follow the instructions to work through the exercise. 8.209 Exploring Boolean search.pdf PDF File Activity: Exploring Boolean search the attached pdf file and follow the instructions to work through the exercise. 8.209 Exploring Boolean search.pdf PDF File Mark as completed Dislike Report an issue

---

## 07_IR_summary_Video_3_min

# IR summary
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/PpN9D/ir-summary

This comprehensive course spans 22 weeks, commencing with foundational knowledge in NLP (Weeks 1-2) and moving into essential basic text processing techniques (Weeks 3-4). The curriculum then delves into language modelling (Weeks 5-6) to understand statistical text generation and lexical semantics (Weeks 7-8) to define word meanings. Subsequent topics include text categorisation and sentiment analysis (Weeks 9-10), followed by the structural analysis of syntax and parsing (Weeks 11-12). The focus then shifts to practical data retrieval, covering information extraction (Weeks 13-14) and information retrieval (Weeks 15-16). Topic 8 emphasizes advanced IR practices, detailing document representation, term weighting using TF.IDF, semantic search, and effective query expansion and Boolean search. The advanced application phase introduces chatbots and dialogue systems (Weeks 17-18), showcasing how NLP is applied in real-world scenarios (Week 19). The final weeks consolidate these concepts in a course summary and revision period (Weeks 20-21). The study culminates in the examination week (Week 22).

---

