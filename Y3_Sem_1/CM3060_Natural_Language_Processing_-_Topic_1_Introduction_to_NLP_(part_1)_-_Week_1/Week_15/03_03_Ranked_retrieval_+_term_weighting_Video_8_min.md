# 03_Ranked_retrieval_+_term_weighting_Video_8_min

# Ranked retrieval + term weighting
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/EEQE7/ranked-retrieval-term-weighting

The discussion introduces information retrieval by contrasting two paradigms: Boolean retrieval and ranked retrieval. Boolean retrieval is a set-based approach utilizing Boolean operators such as AND, OR, and NOT, allowing for complex search strings, exemplified by a recruiter's search for Java developers. This method offers a very high degree of control, allowing users to articulate precise queries, and its transparency allows tracing results back to specific keywords. Furthermore, Boolean retrieval facilitates reproducibility, a crucial requirement in scientific and legal research, ensuring results are demonstrably consistent over time and across users.

However, the modern, commoditized nature of web search changes user behavior, leading to "satisficing," where users only seek the first few results deemed "good enough." To better support this dynamic, the concept of ranked retrieval is introduced, which returns matching documents in a specific order, most commonly by relevance. In ranked retrieval, the query terms are typically unstructured keywords, and the system must calculate a relevance score for each document.

The foundational representation for this scoring is the term-document matrix, where each document is treated as a count vector of length $V$, representing the total vocabulary. This leads to the "bag of words" model, which is a mathematical set ignoring the order of words within a document or query. To assign weight to these terms, the concept of term frequency (TF) is employed. TF measures a document's "aboutness" and is defined as the number of times a term $t$ appears in document $d$.

To damp the effect of highly frequent words, TF is often calculated using the log function, specifically $1 + \log(\text{TF})$, where $\text{TF}$ is the term frequency, and adding one accounts for the mathematical property that $\log(1)$ is zero. Next, the mechanism of inverse document frequency (IDF) is introduced, which accounts for a term's informativeness across the entire collection.

Rare terms are inherently more informative than ubiquitous ones, similar to the function of stop words. Document frequency ($\text{DF}$) is defined as the number of documents that contain term $t$. Since high $\text{DF}$ indicates a common term, IDF is calculated as the logarithmic inverse of document frequency: $\log(N / \text{DF}_t)$, where $N$ is the total number of documents in the collection.

The popular and effective term weighting scheme, TF-IDF, is the product of the two weights: $\text{TF-IDF} = \text{TF} \times \text{IDF}$. This measure balances both how often a term appears in a specific document (TF) and how rare it is across the collection (IDF). Finally, the overall ranking score for a particular query-document pair is the sum of all the TF-IDF weights for the terms intersecting between the query and the document. This method, widely implemented in NLP platforms like NLTK and scikit-learn, determines the final order of returned documents.

