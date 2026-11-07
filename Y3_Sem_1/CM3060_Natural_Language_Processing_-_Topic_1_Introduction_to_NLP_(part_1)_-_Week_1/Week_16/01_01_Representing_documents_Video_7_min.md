# 01_Representing_documents_Video_7_min

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

