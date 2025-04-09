# Context-free grammar examples Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/ylqMZ/context-free-grammar-examples)

Here is a summary of the text in 8 sentences, preserving key information:

Context-free grammars are defined as having rules where on the left-hand side, only one variable or non-terminal appears, and there are no restrictions on the right-hand side. Regular languages are a subset of context-free languages. A language with the form a^nb^2n, where n ≥ 0 and b is twice the number of a's, can be represented by a context-free grammar S → aSbb. This grammar guarantees that all a's appear on the left-hand side and all b's on the right-hand side. The smallest string in this language is the empty string ε, so an ε rule must be added to complete the grammar. A similar grammar can be constructed for the language over a and b with equal numbers of a's and b's by adding rules S → aSb and S → bSa, as well as an additional ε rule to shuffle the strings. The language described in the third example is a subset of palindromes and generates palindromes with even lengths by using rules S → aSa or S → bSb and replacing S with ε at the end. These grammars demonstrate how context-free grammars can be used to represent specific languages, including those with complex structure and symmetry.

