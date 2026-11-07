# 02_Estimating_probabilities_Video_9_min

# Estimating probabilities
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/uwN8g/estimating-probabilities

Language modeling involves estimating the probabilities of word sequences found within a training corpus. Initially, these probabilities are calculated by simply counting the occurrences of specific word patterns in the available data. However, this counting approach is limited because training corpora are finite, leading to the critical problem of sparse data. If a specific utterance or word sequence is not found in the training data, its probability is assigned a zero value. To manage this, the Markov assumption is employed, which dictates conditioning a word's probability on only a shorter, localized fragment of its history, such as bigrams or trigrams.

The starting point for probability estimation is the Maximum Likelihood Estimator (MLE). The MLE calculates the probability of a word $w_i$ given its preceding word $w_{i-1}$ as: $P(w_i | w_{i-1}) = \frac{\text{Count}(w_{i-1} w_i)}{\text{Count}(w_{i-1})}$. Although simple, this method fails when data is sparse, as it assigns a zero probability to any unobserved bigram.

To overcome the sparse data problem, language modelers seek to "smooth" the probability distribution. This involves shifting probability mass from highly likely events to potential, yet unseen, events in the vocabulary.

One simple technique is Laplace smoothing, which adds one to all observed counts. This yields the smoothed probability estimate: $P(w_i | w_{i-1}) = \frac{\text{Count}(w_{i-1} w_i) + 1}{\text{Count}(w_{i-1}) + |\text{V}|}$, where $|\text{V}|$ is the size of the vocabulary. Although effective, Laplace smoothing is considered a crude approach and more advanced schemes are often preferred in statistical language modeling.

Two more robust schemes for dealing with sparse counts are backoff and interpolation. Backoff operates by progressively falling back to a lower-order model if sufficient evidence is lacking in a higher-order model. For example, the system attempts to estimate $P(w_i | \text{history})$ using a trigram; if its count is zero, it "backs off" to the bigram estimate.

This process continues down the hierarchy—from trigram to bigram, and finally to the unigram model—with specific weighting factors applied at each level. Interpolation offers an alternative strategy where all models (trigram, bigram, and unigram) are utilized simultaneously. Instead of backing off, interpolation mixes the estimates by assigning weights, denoted as $\lambda_1, \lambda_2,$ and $\lambda_3$, to each level. These weights must be chosen such that $\lambda_1 + \lambda_2 + \lambda_3 = 1$. In essence, interpolation provides a balanced estimate derived from multiple contextual levels, creating a more robust model than a pure backoff approach.

