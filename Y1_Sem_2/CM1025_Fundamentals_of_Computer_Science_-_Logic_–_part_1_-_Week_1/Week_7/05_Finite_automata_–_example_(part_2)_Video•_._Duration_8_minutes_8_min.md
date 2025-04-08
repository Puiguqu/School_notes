# Finite automata – example (part 2) Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/OZCVe/finite-automata-example-part-2)

The text describes the design of a finite automaton to accept or reject strings based on specific language rules. The language L contains all strings with an odd number of 'a's and an even number of 'b's. To design the automaton, we start with an initial state q0 where both 'a' and 'b' counts are 0 (even). We then consider each letter in the alphabet (a and b) and create new states based on whether the current count is odd or even.

The transition from q0 to q1 occurs when an 'a' is read, as this changes the count of 'a's to an odd number. Similarly, a transition from q0 to q2 occurs when a 'b' is read, changing the count of 'b's to an odd number. We continue this process for each new state, considering how reading different letters affects the counts.

The final states (q3) are accept states because they correspond to having an odd number of 'a's and an even number of 'b's. The last state (q1) is a non-accept state as it represents having an even number of both 'a's and 'b's.

To test the automaton, we input strings such as "abb" which should be accepted due to the odd count of 'a's, or "baba" which should be rejected because it has an even count of 'b's. The simulator can be used to design and simulate different types of automata, including determining whether a string is accepted or rejected by the automaton automatically.

This process demonstrates how finite automata can be used to recognize patterns in strings based on specific language rules, which is crucial in various fields such as computer science, data compression, and text analysis.

