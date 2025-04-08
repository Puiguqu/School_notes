# Designing Turing machines example Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/dPobr/designing-turing-machines-example)

Here is a summary of the text in 8 sentences, preserving key information:

A Turing machine with transitions that change the characters on the tape head was used to analyze a specific example. The machine starts at state q_1 and reads an "a", which takes it back to q_1 but writes "b" over the existing character. It then moves right, reads "b", changes it to "a", and moves left, repeating this process until it reaches an empty cell (q_2). From q_2, the machine can only move to the accept state if the input ends with "ab". This means that any input with a non-empty suffix must be rejected. The machine's behavior is determined by its transitions, which specify what action to take based on the current state and character read from the tape. In this example, the Turing machine accepts inputs that end with "abaab" but rejects those that end with "baabb". The analysis of this Turing machine provides insight into the properties of certain non-context-free languages.

Note: I've omitted some technical details such as links to additional resources and practice assignments, as they are not essential to understanding the main concept.

