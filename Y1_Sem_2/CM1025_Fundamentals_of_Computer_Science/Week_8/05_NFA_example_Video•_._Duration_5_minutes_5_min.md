# NFA example Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/5KaQt/nfa-example)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

A non-deterministic finite automaton (NFA) is a type of automaton that can process input strings in a non-deterministic manner. To design an NFA, one starts with the initial state `q0` and defines transitions based on the current letter in the tape. The language `L` consists of all strings starting with `a` and ending with `b`. The NFA is designed to accept only strings that meet these criteria. When processing a string, the NFA reads each character one by one, and if there are multiple possible actions for a given character, it behaves non-deterministically, exploring all possibilities before making a decision. This means that an NFA may have different computations for each string, and acceptance depends on whether at least one computation accepts the string. In contrast to deterministic finite automata (DFA), NFAs do not restrict the number of actions per letter, allowing for more complex languages to be accepted. The behavior of an NFA is determined by its transition function, which defines how it reacts to each character in the input string.

