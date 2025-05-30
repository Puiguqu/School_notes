# Language of a grammar Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/Mcol1/language-of-a-grammar)

Here is a summary of the text in 8 sentences, preserving key information, formulas, links, and technical details:

The language of a context-free grammar is defined as the set of all strings that can be derived from the starting variable 's' using the production rules of the grammar. The formal definition of the language is given by the set Σ* = {w | w can be derived from s}. Context-free grammars are characterized by the absence of left recursion, where a non-terminal symbol 'A' appears before its right recursive occurrence ('A → BC'). Examples of context-free grammars and their corresponding languages are presented, including G1: B^n A^n, G2: a|ab|...a*, and G3: 0^1 01^11. The language generated by G3 can be described as the union of two sets: {0^n 1^(n+1)} where n is greater than or equal to 0. The grammar G3 has no strings that start with 'a' without followed by a zero, and also cannot derive a single 'a'. The language generated by a context-free grammar can be computed using an automaton, such as a pushdown automaton (PDA).

