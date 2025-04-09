# DFA example in Automata Simulator Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/r7iWQ/dfa-example-in-automata-simulator)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

To design a Deterministic Finite Automaton (DFA) for accepting strings over alphabets 'a' and 'b', where the number of 'as' is even and the number of 'bs' is odd, we follow specific steps. The DFA has three states: S0, S1, and S2. In S0, both 'as' and 'bs' are even, while in S1, only 'as' is odd but 'bs' is even. The transition from S0 to S1 occurs when a 'b' is encountered. Conversely, transitioning from S1 to S2 happens when an 'a' is seen. In S2, both 'as' and 'bs' are odd, leading the way back to S0 upon seeing a 'b'. This logic allows the DFA to accept strings with an even number of 'as' but an odd number of 'bs', as demonstrated through several test cases.

