# Regular expressions and finite automata examples Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/gWIkV/regular-expressions-and-finite-automata-examples)

The text provides two examples of converting finite automata to regular expressions. 

In the first example, a new initial state D is created and transitions are made from D to old initial state A labeled epsilon, then a final state E is created and transitions are made from old final states to E also labeled epsilon. Transitions from B to C are removed by writing as one sigma star. Similarly, removing B results in 00 star 1 followed by a transition from B to E, after which state A is removed resulting in the regular expression 1 star 0 plus 1 sigma star.

In the second example, multiple final states are handled by creating a new initial state D, transitioning labeled epsilon from D to old initial state A. Two final states E and F are created with transitions from them both labeled epsilon. Removing C results in creating a transition from B to A using 00 star 1. After removing B, a path between A and E is established as well as a path from A to itself using two new transitions. This leads to the regular expression 01 union 000 star 1 star epsilon union 0.

There are no additional pages or links provided in the text, so there's no formulae or technical details to summarize.

