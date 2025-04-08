# Context-free grammar examples Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/ylqMZ/context-free-grammar-examples)

Here is a summary of the text in 8 sentences, preserving key information:

Context-free grammars are defined as having rules where only one variable or non-terminal appears on the left-hand side, with no restrictions on the right-hand side. Regular languages are a subset of context-free languages. A grammar for the language "a^nb^2*n" can be constructed using the rule S → aSbb, ensuring that all 'b's appear after all 'a's. The grammar also includes an Epsilon rule to handle strings with zero length. Another example involves generating strings with equal numbers of 'a' and 'b', requiring two rules (S → aSb or S → bSa) followed by an Epsilon rule. However, this approach can fail for certain strings, such as "abba", which require additional rules to generate palindromes. To construct a grammar for the language of palindromes with even lengths, two initial rules (S → aSa and S → bSb) are used, followed by an Epsilon rule. These examples demonstrate the importance of understanding context-free grammars in linguistics and computer science.

