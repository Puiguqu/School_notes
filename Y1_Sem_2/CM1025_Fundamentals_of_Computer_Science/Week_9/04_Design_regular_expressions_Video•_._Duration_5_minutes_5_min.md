# Design regular expressions Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/SukqX/design-regular-expressions)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The language consists of binary words containing "bb" with at least one occurrence of "bb". This can be represented by the regular expression Σ*bbΣ*. Another example is the language of all binary words ending with either "ab" or "ba", which can be represented as Σ*ab Σ*ba. The language of all binary words with at most one "a" can be represented as b*ab*b*. This includes binary strings of length 0 (ε), 1 (Σ), and 2 (ΣΣ). For binary strings of length 3, the regular expression is ΣΣΣ. To represent languages with constraints on word length, we can use Σ³ or Σ³+ for "at least three" and ε ∪ Σ ∪ ΣΣ for "at most three". The language of all binary words of length exactly three can be represented as ΣΣΣ.

