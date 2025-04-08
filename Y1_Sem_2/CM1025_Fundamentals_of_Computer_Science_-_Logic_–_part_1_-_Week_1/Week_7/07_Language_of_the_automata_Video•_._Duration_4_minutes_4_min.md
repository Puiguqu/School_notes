# Language of the automata Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/VEs40/language-of-the-automata)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The problem discusses the set of strings accepted by a given automaton. The example shows that the automaton accepts inputs such as 110, 1010, and 10110, which correspond to paths on the red curve and loops on state B. To find other inputs accepted by this automaton, we analyze the final states (E) with incoming arrows labeled 0, which implies that accepting inputs must end with "10". We then investigate paths ending at non-final states (C) and find that they all have the prefix "00". By symmetry, we can deduce the set of strings accepted by this automaton. The language of an automaton is defined as the set of strings x belonging to Sigma* if M accepts x. Mathematically, this is represented as x ∈ Σ* if M(x). To further explore this concept, the video lesson introduces finite automata and deterministic automata, with examples and practice exercises.

Note: I removed some formatting elements (e.g., links, screen reader shortcuts) to make the summary more concise while preserving the essential content.

