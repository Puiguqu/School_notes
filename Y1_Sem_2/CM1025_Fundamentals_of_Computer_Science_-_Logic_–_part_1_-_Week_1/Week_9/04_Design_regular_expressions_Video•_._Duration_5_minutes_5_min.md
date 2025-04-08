# Design regular expressions Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/SukqX/design-regular-expressions)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The language consists of binary words containing "bb" and can be represented by a regular expression that captures this language. The type of strings in this language include any string with at least one occurrence of "bb", preceded or followed by zero or more characters. To represent this language, the regular expression Σ*bbΣ* is used. The language of all binary words ending with either "ab" or "ba" can be represented as Σ*ab ∪ Σ*ba. The language of all binary words with at most one "a" can be represented as b*ab*b*. This example illustrates how to apply regular expressions to languages with constraints on the length and structure of strings. Regular expressions are also used to represent languages with specific lengths, such as binary strings of length 3 (ΣΣΣ) or at least 3 characters (ΣΣΣ*). The language of all binary words of length at most 3 can be represented as ε ∪ Σ ∪ ΣΣ.

