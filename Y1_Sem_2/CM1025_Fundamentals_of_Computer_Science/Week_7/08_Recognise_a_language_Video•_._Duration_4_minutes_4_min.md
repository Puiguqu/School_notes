# Recognise a language Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/FdiYc/recognise-a-language)

Here is a summary of the text in 8 sentences, preserving key information:

The goal of this exercise is to design an automaton that can represent a given set of input strings. The problem asks whether it's possible to build an automaton that accepts all binary strings, and how to simplify such an automaton. To answer this question, we consider a simple example: building an automaton that accepts binary strings ending in 0. This requires two states: A (the final state) with incoming arrows labeled 0, and B (initial state) connected to A with transition 0. The outgoing transitions from A are labeled 0 as well, allowing the string to end with multiple zeros. Another example is designing an automaton that accepts binary strings ending in either 0 or 1, requiring three states: A, B, and C. The automaton must also accept strings with a single 0 followed by a single 1, which can be achieved using loops over state C. These examples demonstrate how to design automata for various binary languages using the principles of finite automata theory.

