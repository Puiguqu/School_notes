# Finite automata – example (part 2) Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/OZCVe/finite-automata-example-part-2)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The language L consists of all strings having an odd number of 'a's and an even number of 'b's. To design an automaton for this language, start with the initial state q0, where the head is in front of the first letter of the input string. In each state, decide which action to choose based on the current letter in the tape, considering all possible letters from the alphabet (a and b). The number of 'a's and 'b's seen so far determines the state: if even, stay in q0; if odd, move to a new state q1 or q2. In q1, accept strings with an odd number of 'a's and even number of 'b's. In q2, reject strings with an even number of 'a's and odd number of 'b's. The automaton accepts strings like "abb" but rejects strings like "baba".

