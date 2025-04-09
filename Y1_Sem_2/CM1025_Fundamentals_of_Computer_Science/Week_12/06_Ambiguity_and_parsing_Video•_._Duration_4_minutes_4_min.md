# Ambiguity and parsing Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/jxm6v/ambiguity-and-parsing)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The video transcript discusses the problem of ambiguity in programming languages and its impact on semantics. An example grammar with an ambiguous derivation path is presented, where different parsing methods result in different meanings. To resolve this ambiguity, a new unambiguous grammar is introduced, where the precedence of multiplication is guaranteed to be higher than addition. This is achieved by rewriting the grammar as follows: Capital E goes to capital E plus T, or capital T, and capital T goes to capital T times No, or No.

This reformulated grammar ensures that left recursion is used for both capital E and capital T, demonstrating left associativity. The Chomsky normal form, a specific format for parser algorithms, also requires unambiguous rules. Ambiguity in grammars can lead to incorrect parsing results, as seen in the example where multiplication is incorrectly evaluated.

The video transcript provides additional resources, including videos on context-free grammar, parsing, and ambiguity, as well as practice assignments and lessons on Chomsky normal form. Understanding the importance of unambiguous grammars is crucial for developing robust parser algorithms and ensuring correct evaluation of expressions in programming languages.

