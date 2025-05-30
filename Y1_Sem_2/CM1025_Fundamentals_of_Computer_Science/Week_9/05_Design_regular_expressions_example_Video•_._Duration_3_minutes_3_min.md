# Design regular expressions example Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/JsmIX/design-regular-expressions-example)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Sigma star generates all strings over an alphabet (a, b) by taking the union of all possible strings generated by concatenating the alphabet with itself. To generate all strings containing at least one 'a', the regular expression Σ* a Σ* can be used. Similarly, to generate all strings starting with 'a' or ending with 'a', the regular expressions a Σ* and a Σ* a can be used, respectively. To generate all strings of even length, the concatenation of (a+b) with itself followed by a star (∗) can be used: (a+b)∗. A regular expression to generate odd numbers in an alphabet of 1, 2, and 3 can be created using the union of '1' and '3': 1+3 Σ*. For generating all numbers greater than 200, a regular expression that includes strings with exactly three digits (starting with either '2' or '3') followed by strings with four or more digits: (2+3 Σ*) ∪ Σ*Σ*Σ*. These regular expressions demonstrate the power of Sigma star in generating strings based on specific conditions.

