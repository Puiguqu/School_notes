# Regular expressions example Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/JbkLo/regular-expressions-example)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The language generated by σ* (sigma star) includes all strings over the alphabet {a, b}. The syntax of σ* involves concatenation of σ with itself, where each union represents a possible choice. For example, given the regular expression σ = {a, b} in σ* , the string "ab" can be generated by choosing "a" from one union and "b" from another union. Conversely, it is not possible to generate any string that cannot be generated by σ* on the same alphabet. To determine if a specific string belongs to the language generated by a regular expression, it must be possible to break down the string into substrings that can be generated separately. For instance, the string "bbaa" can be broken down into two "bb"s and two "aa"s, which can be generated using the given regular expression σ* . However, the string "abb" cannot be generated by this regular expression because it must start with a character from either {a, b}, but not "ab".

