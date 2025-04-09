# Regular expressions and finite automata examples Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/gWIkV/regular-expressions-and-finite-automata-examples)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The video transcript discusses two examples of converting finite automata to regular expressions. In the first example, an initial state D is created, transitions from D to A labeled epsilon are made, a final state E is created, and transitions from old final states to new final states labeled epsilon are added. The states connected to C are B and E, so only transitions from B to C and from E to itself can be removed, resulting in 1*0+1*(epsilon|0). In the second example, a new initial state D is created, transitions from D to A labeled epsilon are made, a final state E is created with two separate transitions labeled epsilon, and transitions from old final states to new final state E labeled epsilon are added. The states connected to C are B and A, so a new transition from B to A with label 00*1 must be added, resulting in A to E = 0 ∪ ε. After removing B, paths between A and E must be established, leading to the expression 01 ∪ 00*1*(epsilon|0). Finally, after removing A, a new transition from D to E with label 0+ε ∪ 0 is added, resulting in the regular expression 01 ∪ 00*1*(epsilon|0).

Note: The provided text does not include any links or technical details that require preservation. If you would like me to extract specific information or formulas from the text, please let me know and I'll be happy to assist you.

