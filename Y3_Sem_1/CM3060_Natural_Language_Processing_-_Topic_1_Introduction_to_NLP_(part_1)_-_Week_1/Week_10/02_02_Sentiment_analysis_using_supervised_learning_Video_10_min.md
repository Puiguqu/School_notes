# 02_Sentiment_analysis_using_supervised_learning_Video_10_min

# Sentiment analysis using supervised learning
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/0vwwD/sentiment-analysis-using-supervised-learning

The process discussed focuses on sentiment analysis using supervised machine learning techniques implemented in a Jupyter Notebook environment. The initial step involves utilizing the NLTK `movie reviews` corpus, which contains 2000 movie reviews, providing designated test and training datasets. A list of documents is constructed by iterating through all categories and reviewing every movie review in the corpus. This list includes both positive and negative class labels, which serves as the target variable for classification.

Feature extraction is the core of the sentiment analysis, relying on the frequency distribution of words. All text is converted to lowercase, and an NLTK frequency distribution is instantiated based on the words in the corpus. Crucially, only the top $N$ most common words are selected to form the `word features`. The starting experiments began with a small value, $N=5$, to ensure functions returned in a reasonable time frame.

A specific document feature extraction function is then implemented, which converts the document into a set for faster matching operations. This function generates a dictionary where, for each word within the top $N$ `word features`, it checks for the word's presence in the document, creating a boolean (True/False) pair. For instance, with $N=5$, almost every document contained these common words, leading to many True values.

Initial training used $N=5$ features with a Naive Bayes Classifier, achieving an accuracy of $0

