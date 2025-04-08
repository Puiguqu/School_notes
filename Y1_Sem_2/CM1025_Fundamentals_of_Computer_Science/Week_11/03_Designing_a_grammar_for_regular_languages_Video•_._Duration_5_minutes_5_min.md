# Designing a grammar for regular languages Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/BVjLW/designing-a-grammar-for-regular-languages)

Here is a summary of the text in 8 sentences, preserving key information:

Designing regular grammars from finite state machines involves several steps. The algorithm starts by drawing a nondeterministic finite automaton (NFA) or deterministic finite automaton (DFA) to accept the language. The DFA for the language L containing all strings starting with "a" and ending with "b" has four states: Q0, Q1, Q2, and Q3. Domino states are removed, and transitions in state Q1 are eliminated. Each state is labeled with a variable, with the initial state Q0 labeled as capital S, and accepting state Q3 labeled as capital B. Rules are generated for each transition, resulting in six rules: Capital S goes to small a capital A, capital A goes to small a capital A or small b capital B, and so on. The final step is to add a rule that states capital B goes to epsilon, making the grammar complete.

