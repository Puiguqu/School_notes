# The power of Turing machines Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/kO7V1/the-power-of-turing-machines)

Unfortunately, the text you provided is a transcript and does not contain any mathematical formulae or technical details that can be extracted and preserved in a summary. The transcript appears to be a video explanation of how Turing machines can be used to sort binary inputs (zeros and ones) into a specific format.

However, I can summarize the key concepts and findings presented in the transcript:

The video discusses how Turing machines can be used to sort binary inputs by reading the input from left to right and using transitions between states to manipulate the tape. The machine first reads the sorted part of the input and then finds the first one and flips it to 0. It then goes back to the left most 0 and flips it to 1, repeating this process until there is no 1 after 0s.

The Turing machine uses several states (Q1, Q2, Q3, and Q4) to perform this sorting operation. The transition from state Q3 to state Q4 flips the first one after 0s to 0. If the input starts with runoff zeros, a new transition is added to handle this case.

The video also discusses how to build such a Turing machine, which involves creating a set of transitions between states that implement the sorting algorithm. The machine terminates when it reads a blank symbol (representing the start of the input) and enters an accepting state.

Overall, the transcript provides a step-by-step explanation of how Turing machines can be used to sort binary inputs into a specific format using transitions between states.

