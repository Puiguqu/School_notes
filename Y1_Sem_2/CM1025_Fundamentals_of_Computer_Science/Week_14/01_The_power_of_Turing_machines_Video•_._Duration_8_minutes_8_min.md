# The power of Turing machines Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/kO7V1/the-power-of-turing-machines)

Unfortunately, I couldn't summarize the text as requested since it is a video transcript with no accompanying written content or formulae, links, technical details, or key information that could be summarized in 8 sentences.

However, I can provide a summary of the concepts presented in the video transcript:

A Turing machine is used to sort binary input by manipulating it. The process involves passing the already sorted part of the input and then finding the first 1 after a string of 0s, flipping it to 0, and repeating until there are no more 1s after 0s.

To build this Turing machine, one must:

* Parse the sorted part of the input
* Find the first 1 after a string of 0s and flip it to 0
* Move right and repeat the process

The Turing machine can be built using states Q1, Q2, Q3, and Q4, which are connected by transitions labeled "read 0", "flip 1 to 0", "move right", "do not touch input move left", and "terminate". The machine starts at state Q1 and reads the input, making transitions based on what it reads.

The video transcript also discusses Turing machines in general, including their power and different types of Turing machines.

