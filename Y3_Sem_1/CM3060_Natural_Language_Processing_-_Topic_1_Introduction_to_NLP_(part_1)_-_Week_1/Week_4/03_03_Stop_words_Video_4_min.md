# 03_Stop_words_Video_4_min

# Stop words
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/zJwBM/stop-words

Stop words are defined as high-frequency words common across different document types and genres. These words offer little lexical content and tend not to contribute significantly to differentiation between texts. For example, common English stop words include "and," "or," "the," and "of." In machine learning tasks, such as document classification, these common words often introduce noise rather than providing meaningful signal. Consequently, they are typically filtered out during the preprocessing phase of text analysis.

However, it is crucial to recognize that stop words are highly language-specific, meaning the English list differs fundamentally from those in French or German. Furthermore, there is no universal list of stop words; the selection must depend entirely on the specific goal of the application. To begin processing, the Natural Language Toolkit (NLTK) is imported to access built-in stop word lists.

The procedure involves importing the NLTK stop word list and printing the extensive list available. To practically use these words, the English stop word list is first stored in a variable named `stopwords`. This list is then cast to a set type to ensure subsequent computational operations execute faster.

Text tokens are extracted from the document using NLTK’s tokenization function. Subsequently, a simple list comprehension is utilized to iterate through the tokenized words. This comprehension filters out any word that exists within the defined `stopwords` set. This process effectively transforms the text by removing high-frequency common phrases, for example, changing "most of the time" to "most time use white space."

A critical caution must be applied when implementing stop word removal. Over-applying the filter can be detrimental to specialized texts. For instance, if filtering Shakespeare's plays, the removal of words like "to" and "be" could result in an empty list, which is clearly inappropriate for that literary corpus.

Beyond English, NLTK provides available lists for other languages. The transcript demonstrated accessing and reviewing the stop words provided for German and also noted the availability of French stop word lists. This basic technique is fundamental to text processing applications, but it must be used with extreme caution. Users must carefully consider which words should definitively be included in their specific stop word list.

