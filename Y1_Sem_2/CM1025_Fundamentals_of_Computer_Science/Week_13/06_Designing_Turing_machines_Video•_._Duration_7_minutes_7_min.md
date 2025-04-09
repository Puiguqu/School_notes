# Designing Turing machines Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/o0boU/designing-turing-machines)

Here is a summary of the text in 8 sentences, preserving key information:

The language "nA's followed by nB's" is not regular but is context-free, with a grammar defined as S → aSb or ε. A Turing machine can be designed to accept this language by parsing the input until a blank is reached, then checking if it ends with a b and deleting it. To handle strings that start with "nA's followed by nB's followed by nC's", a modified Turing machine can verify that the number of c's and a's are equal, replacing c's with d's during processing. The machine then proceeds to count and delete b's and d's, rejecting inputs with a's or c's left in the middle. A new state q7 is added to read and delete only b's and d's, ensuring that any remaining letters will be rejected. The Turing machine also verifies that the number of d's and b's are equal, providing another means of distinguishing between valid and invalid strings. To design such a Turing machine, one must carefully consider the transitions and states required to parse the input and ensure that it produces the correct output. By following these steps, it is possible to design a Turing machine that accepts "nA's followed by nB's" and "nA's followed by nB's followed by nC's" languages.

