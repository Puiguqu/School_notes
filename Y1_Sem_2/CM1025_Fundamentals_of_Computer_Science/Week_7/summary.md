# Week 7 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Introduction Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/Nc4u4/introduction)

There is no text to summarize. The provided text appears to be a video transcript and introductory content for a lesson on finite automata, specifically Lesson 4 of a course on computer science. It discusses the basics of mathematical machines called automata, including prerequisites, building blocks, and the need to design a machine that can verify valid sequences.

The main topics covered in this lesson include:

* Finite automata: A mathematical model for recognizing patterns and processing inputs.
* Deterministic automata: A specific type of finite automaton where the output is uniquely determined by the input.
* A classic problem, the "farmer and the river," to illustrate the need for a machine that can process inputs.

However, there are no key information, formulae, links, or technical details provided in the text. The content appears to be an introduction to the topic of finite automata, with some context and examples used to illustrate the concepts.

If you could provide more text or clarify what specific information you would like summarized, I'd be happy to help.

---

## Basic definitions, letters, strings Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/1Dj9m/basic-definitions-letters-strings)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

An alphabet denoted by capital sigma is a non-empty set of symbols, such as {0, 1} or {a, b, c}. A string or word is a finite sequence of letters drawn from an alphabet. The length of a string is the sum of occurrences of its symbols, denoted by two bars, and can be calculated using the formula: length = n * m, where n is the number of symbols in the alphabet and m is the length of the string. For example, if sigma is {0, 1} and x is "01110101", then the length of x is 8. The collection of all strings over an alphabet sigma is denoted by sigma* (star), which includes the empty word epsilon. To exclude the empty word, we use sigma+ (plus). A language is a collection of strings over an alphabet, and it can be represented as σ^k (sigma to the power of k), where σ is the alphabet and k is the length of the string.

Note that these definitions provide a foundation for understanding the concept of finite automata in computer science.

---

## What is an automaton? Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/Wgh58/what-is-an-automaton)

Here is a summary of the text in 8 sentences, preserving key information:

A finite automaton is an abstract model of a digital computer that represents how computations are performed with limited memory space. It consists of three parts: a tape, a head, and a state, which are connected through transitions. The tape is made up of cells holding single symbols from an alphabet, while the head moves along the tape to read one symbol at a time. The current state determines the next state based on the current input symbol using a transition function. Finite state automata have two types of states: accepting and rejecting states, which output "accept" or "reject," respectively. The formal definition of a finite automaton consists of five tuples: a set of states (Q), an alphabet (σ), transitions (δ), an initial state (q0), and accepting states (F). To design an automaton, one must create a transition table that lists all possible states and input symbols. By tracing the computation of an automaton on a given string, one can determine whether the string is accepted or rejected based on the output of the automaton's final state.

---

## Finite automata – example (part 1) Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/wZAKa/finite-automata-example-part-1)

Here is a summary of the text in 8 sentences, preserving key information:

The video transcript describes the operation of an automaton with five states (A, B, C, D, and E) and a binary alphabet. The automaton starts at state A and reads one letter from the input "10011". Based on the transition labels (0 or 1), it moves to states B, C, and D, respectively, before rejecting the input because it does not end in an accepting state (E). Another input, "11001", is accepted because it ends in an accepting state. The automaton uses loops (transitions that return to a previous state) to move between states. When the input ends in an accepting state, the automaton accepts; otherwise, it rejects. The video transcript provides examples and links to additional resources for learning about finite automata, including videos, discussions, readings, and exercises.

---

## Finite automata – example (part 2) Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/OZCVe/finite-automata-example-part-2)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The language L consists of all strings having an odd number of 'a's and an even number of 'b's. To design an automaton for this language, start with the initial state q0, where the head is in front of the first letter of the input string. In each state, decide which action to choose based on the current letter in the tape, considering all possible letters from the alphabet (a and b). The number of 'a's and 'b's seen so far determines the state: if even, stay in q0; if odd, move to a new state q1 or q2. In q1, accept strings with an odd number of 'a's and even number of 'b's. In q2, reject strings with an even number of 'a's and odd number of 'b's. The automaton accepts strings like "abb" but rejects strings like "baba".

---

## Working with Automata Simulator Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/uqcTy/working-with-automata-simulator)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The Automata Simulator is used to simulate NFA (Nondeterministic Finite Automaton), DFA (Deterministic Finite Automaton), and pushdown automata. The simulator can be used to design and test NFAs, with a focus on finite state machines. To add a new state, users can click the "add" button, while to create transitions, they can drag and drop labels onto each other. In this example, an NFA is designed to accept strings starting with 'a' from alphabets containing both 'a' and 'b'. The simulator allows users to test their designs by inputting strings that should be accepted or rejected. The automaton was initially designed to accept strings starting with 'a', but had a bug in the final state, which caused it to reject some expected inputs. To fix this, the user added an additional state and ensured the correct accept state was designated. By running the simulator, users can test their designs and ensure they are functioning correctly before adding new states or transitions.

---

## Language of the automata Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/VEs40/language-of-the-automata)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The language accepted by an automaton can be determined by analyzing the input strings that are accepted by the automaton. The red curve shows the path from the start state following the input "110", which results in a loop on state B and acceptance of input "1110". To find all accepted inputs, we choose a final state (E) and examine the arrows entering it, finding that accepting inputs terminate with "10". We also identify all states with incoming arrows labeled 0, which is only state C. The remaining final state is D, and its transitions are labeled 1 and come from states E and C. To ensure no string ends in "10" at non-final states, we circle all transitions coming into E or C, labeling them 0. This results in the language of the automaton being accepted by inputs ending with either "01" or "10". The set of all strings accepted by an automaton is called the language of the automaton.

Note: I did not include any links or technical details that were not relevant to summarizing the main concepts and findings.

---

## Recognise a language Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/FdiYc/recognise-a-language)

Here is a summary of the text in 8 sentences, preserving key information:

The problem of designing an automaton that represents a given set of input strings can be solved by studying its final state. The example of building an automaton to accept all binary strings shows that two states are sufficient: A for accepting strings ending with "0" and B for rejecting strings not ending with "0". An alternative design uses only one state with two loops, which is less efficient but demonstrates the concept. Another example illustrates designing an automaton to accept binary strings ending in "1", requiring three states (A, B, and C) with specific transitions. The automaton can be designed for more complex languages like those accepting strings containing both "0" and "1". For instance, a language that accepts any string containing at least one "0" and one "1" can be represented by an automaton with three states (A, B, and C). The process of designing such automata involves analyzing the conditions under which strings are accepted or rejected. By following this approach, it is possible to create an automaton that represents a given language, even if the language is not finite.

---

## Finite automata Reading• . Duration: 1 hour 45 minutes 1h 45m

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/nNemd/finite-automata)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The essential reading material covers topics studied in Week 7, including languages, finite state automata (FSAs), and deterministic finite automata (DFAs). The recommended study approach involves first watching videos related to the topic before studying the accompanying material. Sipser's book "Introduction to the theory of computation" provides a detailed explanation of FSAs on pages 31-46. The reading includes video lessons, such as "Finite automata – example (part 1)" and "Recognise a language", which cover key concepts and provide interactive simulations with the Automata Simulator. Students are also encouraged to design an automaton using the simulator to accept a simple language. The material is accompanied by a discussion prompt for students to think of a binary language, as well as additional exercises and hints. The recommended study resource is Sipser's book, available in PDF format or online. Overall, the essential reading aims to provide a comprehensive understanding of FSAs and DFA concepts, building on previously studied material from Week 7.

---

## Week 7 exercises Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/jdXnA/week-7-exercises)

Here is a summary of the text in 8 sentences, preserving key information and details:

The Week 7 exercises aim to apply concepts learned so far on finite automata. The first exercise involves parsing the input "abaa" using the given automaton with five states (A, B, C, D, E) and finding if it is accepted or rejected. The second exercise requires analyzing an automaton with six states (A, B', C, E, F) to determine example strings that should be accepted and rejected, as well as the language accepted by this automaton. A self-edge from A to A labelled with 1, a transition from A to B labelled with 0, and other transitions are provided. The third exercise asks to design an automaton over {a,b} to accept all strings starting with 'a', while the fourth exercise involves designing an automaton over {1,2,3} to accept all numbers divisible by 3. Additional resources, including videos, discussions, reading materials, and a simulator, are available for further practice and understanding of finite automata concepts. The exercises are optional but strongly recommended to test knowledge and identify areas for additional study. Completing the exercises will help solidify understanding of finite automata and their applications.

---

## Week 7 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/GLo5p/week-7-exercises-hints-and-tips)

Lesson 4.0 Introduction Lesson 4.1 Finite automata Lesson 4.2 Deterministic automata Video: Video Finite automata – example (part 1) . Duration: 3 minutes 3 min Video: Video Finite automata – example (part 2) . Duration: 8 minutes 8 min Video: Video Working with Automata Simulator . Duration: 6 minutes 6 min Discussion Prompt: Design an automata to accept a simple language using Automata Simulator . Duration: 30 minutes 30 min Video: Video Language of the automata ....

---

