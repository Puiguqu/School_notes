# Ambiguity and parsing Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/jxm6v/ambiguity-and-parsing)

Here is a summary of the text in 8 sentences, preserving key information:

A programming language's grammar can be ambiguous, leading to different meanings for the same derivation path. The example given uses a simple grammar with an ambiguous rule, which results in multiple possible parse trees and interpretations of the expression "3 times 4 plus 5". To resolve this ambiguity, an unambiguous grammar must be created to ensure that parsing always leads to the same meaning. This can be achieved by using specific rules, such as left recursive rules for both terminals and non-terminals, and ensuring that the precedence of operators is consistent. The provided example shows how to rewrite the ambiguous grammar into an unambiguous one, where multiplication has a higher precedence than addition. Additionally, using Chomsky normal form or Greibach normal form can help in resolving ambiguity in parser algorithms. Unambiguous grammars are essential for parsing, as they ensure that the interpretation of expressions is consistent and predictable. By creating and analyzing unambiguous grammars, developers can write more robust and reliable code.

