# Designing Turing machines Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/o0boU/designing-turing-machines)

Here is a summary of the text in 8 sentences, preserving key information, formulas, links, and technical details:

The language of nA's followed by nB's is context-free but not regular. The Turing machine for this language starts with state q1 and reads 'a' to delete it and then moves to the end of the input, where it checks if there is a corresponding 'b'. If so, it deletes the 'b', otherwise it rejects. To process strings of nA's followed by nB's followed by nC's, the Turing machine needs to verify that the number of C's and A's are equal and replace C's with D's. It also needs to count B's and D's and move left if there is a blank at the end of the input. The Turing machine has two phases: one for counting C's and A's, and another for counting B's and D's. To achieve this, it adds new transitions in state q1 and uses loops to read and delete specific letters. By modifying these transitions, we can design a Turing machine that accepts strings of nA's followed by nB's and nC's.

