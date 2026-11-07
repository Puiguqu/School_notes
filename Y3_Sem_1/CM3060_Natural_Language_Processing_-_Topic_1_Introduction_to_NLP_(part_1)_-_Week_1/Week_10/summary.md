# Week 10 - CM3060 Natural Language Processing - Topic 1: Introduction to NLP (part 1) - Week 1

## 01_Intro_to_sentiment_analysis_Video_15_min

# Intro to sentiment analysis
Video • 15 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/ylmC2/intro-to-sentiment-analysis

This comprehensive curriculum covers the evolution of Natural Language Processing (NLP), commencing with foundational knowledge from Weeks 1 through 4, which focus on general introductions and basic text processing techniques. The core theoretical understanding progresses through Weeks 5 and 6 by detailing Language Modelling, followed by Weeks 7 and 8 which explore Lexical Semantics. A major focus area, Weeks 9 and 10 (Topic 5), is dedicated to Text Categorisation and Sentiment Analysis, featuring intensive practical learning. This segment includes specific modules such as "Intro to sentiment analysis" videos, supervised learning assignments, and detailed readings on lexicons and the Reuters Corpus. Subsequent phases delve into structural analysis, starting with Weeks 11 and 12 on Syntax and Parsing, and advancing to Weeks 13 and 14 covering Information Extraction. Weeks 15 and 16 introduce Information Retrieval (IR), while Weeks 17 and 18 address advanced applications in Chatbots and Dialogue Systems. The curriculum culminates in Week 19 and 20, where students apply these concepts in "NLP in practice" and review the course summary. The entire learning sequence is structured over 20 weeks, preparing students for the concluding revision week (Week 21) and the final examination (Week 22).

---

## 02_Sentiment_analysis_using_supervised_learning_Video_10_min

# Sentiment analysis using supervised learning
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/0vwwD/sentiment-analysis-using-supervised-learning

The process discussed focuses on sentiment analysis using supervised machine learning techniques implemented in a Jupyter Notebook environment. The initial step involves utilizing the NLTK `movie reviews` corpus, which contains 2000 movie reviews, providing designated test and training datasets. A list of documents is constructed by iterating through all categories and reviewing every movie review in the corpus. This list includes both positive and negative class labels, which serves as the target variable for classification.

Feature extraction is the core of the sentiment analysis, relying on the frequency distribution of words. All text is converted to lowercase, and an NLTK frequency distribution is instantiated based on the words in the corpus. Crucially, only the top $N$ most common words are selected to form the `word features`. The starting experiments began with a small value, $N=5$, to ensure functions returned in a reasonable time frame.

A specific document feature extraction function is then implemented, which converts the document into a set for faster matching operations. This function generates a dictionary where, for each word within the top $N$ `word features`, it checks for the word's presence in the document, creating a boolean (True/False) pair. For instance, with $N=5$, almost every document contained these common words, leading to many True values.

Initial training used $N=5$ features with a Naive Bayes Classifier, achieving an accuracy of $0

---

## 03_Learning_to_classify_text_Reading_1h

# Learning to classify text
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/jlslf/learning-to-classify-text

Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 6, pp.221-228. Sections 1 to 1.4 in the above online book version If this link is broken, please let us know via the Student Portal . Learning to classify text Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 6, pp.221-228....

---

## 04_Sentiment_analysis_using_lexicons_Video_5_min

# Sentiment analysis using lexicons
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/H2GMD/sentiment-analysis-using-lexicons

This course on Natural Language Processing (NLP) begins with foundational concepts, dedicating Weeks 1 through 4 to introductions and basic text processing techniques. The focus then shifts to semantics, with Weeks 5 and 6 addressing language modelling, followed by a deep dive into lexical semantics during Weeks 7 and 8. A significant module covers text categorization and sentiment analysis (Weeks 9 and 10), which includes specific analyses like "Sentiment analysis using lexicons," supervised learning classification, and the use of corpora such as the Reuters Corpus Volume 1. The technical progression continues into structural NLP, dedicating Weeks 11 and 12 to syntax and parsing. Subsequent weeks introduce advanced information management techniques, specifically information extraction (Weeks 13 and 14) and information retrieval (Weeks 15 and 16). The curriculum culminates with practical applications in conversational AI, covering chatbots and dialogue systems in Weeks 17 and 18. The final weeks (19 and 20) consolidate knowledge through "NLP in practice" and a comprehensive course summary. The schedule also incorporates numerous learning components, including practice assignments, video lectures, and focused readings on specific sub-topics like lexicons for sentiment and affect. The course concludes with a revision and exam period.

---

## 05_Discovering_sentiment_analysis_Reading_1h

# Discovering sentiment analysis
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/opK97/discovering-sentiment-analysis

Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 6 pp.167-169....

---

## 06_Reuters_Corpus_Volume_1_Reading_1h

# Reuters Corpus Volume 1
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/57Bd1/reuters-corpus-volume-1

Lewis, D.D., Y. Yang, T.G. Rose and F. Li ' Rcv1: A new benchmark collection for text categorization research' , Journal of machine learning research 5 2004, pp.361-397. If this link is broken, please let us know via the Student Portal . Reuters Corpus Volume 1 Lewis, D.D., Y. Yang, T.G. Rose and F. Li ' Rcv1: A new benchmark collection for text categorization research' , Journal of machine learning research 5 2004, pp.361-397. If this link is broken, please let us know via the Student Portal ....

---

## 07_Lexicons_for_sentiment,_affect_and_connotation_Reading_1h

# Lexicons for sentiment, affect and connotation
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/czF59/lexicons-for-sentiment-affect-and-connotation

Jurafsky, D. and J.H. Martin Speech and language processing . (2021; 3rd draft ed.). Check chapter 22 in the provided link. If this link is broken, please let us know via the Student Portal . Lexicons for sentiment, affect and connotation Jurafsky, D. and J.H. Martin Speech and language processing . (2021; 3rd draft ed.). Check chapter 22 in the provided link. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

## 08_Text_categorisation_summary_Video_2_min

# Text categorisation summary
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/lfQ1O/text-categorisation-summary

Topic 5 provided a comprehensive review of text categorization and sentiment analysis, building upon prior learning objectives. The core objectives included understanding categorization fundamentals, exploring sentiment analysis techniques, and evaluating classification methodologies. The discussion began by reviewing various text categorization methods from a conceptual perspective. Initially, the rule-based approach was examined, where high accuracy could be achieved. However, a critical limitation of the rule-based method is its extreme difficulty in scaling and maintaining consistency over large datasets.

The focus then shifted to statistical formalisms, specifically highlighting the application of Naive Bayes. Naive Bayes is presented as a valuable baseline classifier, particularly effective for handling high-dimensional datasets. The methodology involves a set of tunable parameters for optimization. Fundamentally, the process relies upon Bayes’ formula, which established specific terminology for Bayesian classification.

The concepts were explored using a generalized model, where outcomes are represented not just by probabilities, but by areas on a grid of possible outcomes. This generalized view allowed for a detailed thought experiment, such as the "Steve librarian" scenario. Sentiment classification represents a specialized application of this Bayesian approach.

To implement sentiment analysis, a four-step process was walked through using a small toy example. A crucial technical detail discussed in this process was the application of Laplace smoothing. This technique aids in preventing zero probabilities during classification. Practical techniques for implementing these models involved utilizing tools like NLTK.

Beyond supervised learning, the discussion addressed scenarios where training data is unavailable or severely limited. In such cases, manually curated word lists or sentiment lexicons can be employed. These lexicons serve as a non-data-driven method for determining sentiment. The Reuters Corpus Volume 1 was referenced as a practical resource for lexical studies.

The course materials further elaborated on these topics, including a "Sentiment analysis using supervised learning" module (10 min video). Furthermore, a segment titled "Sentiment analysis using lexicons" (5 min video) covered the lexical approach. The supplementary reading on "Lexicons for sentiment, affect and connotation" highlighted this aspect of NLP.

In summary, text classification methods range from high-maintenance rule systems to robust statistical approaches like Naive Bayes. Sentiment analysis applies these principles to classify text based on emotional tone. The next topic in the course will pivot from text processing to exploring the structural complexity of syntax and parsing.

---

