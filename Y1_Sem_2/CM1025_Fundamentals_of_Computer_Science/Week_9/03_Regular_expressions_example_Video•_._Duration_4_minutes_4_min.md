# Regular expressions example Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/JbkLo/regular-expressions-example)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The language of σ* (sigma star) generates all strings over alphabet σ, where σ = {a, b}. A regular expression σ* represents the union of σ and itself, denoted as σ + σ. The regular expression (b*a+)* can generate strings like "bbaa" by considering the last star as one expression, but it cannot generate strings like "abb" since the last letter must always be "a". Another regular expression, (ab* + ba+)*, can generate strings like "abba" and "aaba", but not "bba". Regular expressions allow for different ways to generate a string, as seen in examples. The process of generating a string involves choosing parts from each expression in the union, using the symbols "+" or "*". Regular expressions are a fundamental concept in formal language theory and have applications in computer science and software design. Understanding regular expressions is essential for working with formal languages and designing efficient algorithms for pattern matching and text processing tasks.

