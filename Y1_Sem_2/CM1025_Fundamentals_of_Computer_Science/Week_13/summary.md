# Week 13 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Introduction Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/jj1fv/introduction)

There is no text provided to summarize. The given text appears to be a transcript of a video introduction to a topic on Turing machines and computer science, but it does not contain any specific information or concepts to summarize.

However, I can provide an outline of the main topics that will be covered in the lesson:

1. Learning outcomes: Describe the process of computation through Turing machines, consider the design and utility of Turing machines, explore the power and language of Turing machines, and discuss non-context-free languages.
2. Introduction to Turing machines: Study the capabilities and limitations of Turing machines, which can recognize vast classes of languages.
3. Comparison with finite automata: Examine the differences between Turing machines and finite automata, highlighting how these differences make Turing machines more powerful.
4. Non-context-free languages: Discuss non-context-free languages, including their characteristics and relationships to Turing machines.

If you provide the actual text or a specific excerpt from the transcript, I can assist with summarizing it in 8 sentences while preserving key information, formulae, links, and technical details.

---

## Non-context free languages Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/dRI8S/non-context-free-languages)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Context-free languages are a superset of regular languages, meaning all regular languages are context-free languages. Context-free languages are closed under concatenation and union, as well as clean restore and unary operators. The Pumping Lemma is used to prove that a language is not context-free, but its application for context-free languages is beyond the scope of this module. An example shows that two given languages, L1 and L2, are context-free, with grammars describing their structures. By applying closure properties, it can be shown that L1 concatenated to L2 and L1 union L2 have context-free grammars. This means that a context-free grammar can be written to describe the resulting language. Context-free languages are distinct from non-context-free languages, which do not have this property. The module does not cover the Pumping Lemma for context-free languages in detail, but instead provides information on their closure properties and relationship to regular languages.

---

## Non-context free languages example Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/2W6cB/non-context-free-languages-example)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

Non-context-free languages are a type of language that cannot be described by a context-free grammar. These languages have a specific structure that requires a certain number of characters to appear before others, making them more complex than context-free languages. Two examples of non-context-free languages are L1 (a* b* c*) and L2 (a* b* c*). The intersection of these two languages results in a language with the same structure, but this language is not context-free. To prove that it's not context-free, one can use the extended version of the pumping lemma. Another example of a non-context-free language is WW, where strings must be symmetric around the middle. This language cannot be described by a context-free grammar because it requires symmetry. The language d^n a^m c^m d^n is context-free because it has a context-free grammar that generates the same number of characters.

Note: I preserved the technical details and formulas mentioned in the text, but condensed the summary to focus on the most important concepts and findings.

---

## Turing machines Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/9v4xh/turing-machines)

Here is a summary of the text in 8 sentences, preserving key information:

A Turing machine is a virtual machine invented by Alan Turing that models computations. It consists of an infinite tape with a finite set of states, a start state, and a transition function delta. The transition function takes one state and one letter from the input alphabet, returning a state, a letter to be written on the current cell, and the direction (L for left or R for right) to move the tape head. Turing machines can process an input many times and may enter an infinite loop if it doesn't terminate at an accept or reject state. The machine terminates when it reaches either an accept or reject state, which is essential for Turing machines but not all finite automata have. Finite state automata are similar to Turing machines in that they describe the transition function in a tabular form and can be used to model computations. However, Turing machines have some key differences: they don't terminate just because the input is parsed and processed, and they may process an input many times before terminating.

---

## Turing machines – examples Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/i3jsV/turing-machines-examples)

Here is a summary of the text in 8 sentences, preserving key information:

A Turing machine is designed to accept the language WW reverse, where W is defined over small a and small b. The language is not regular, with a grammar that generates it: Capital S goes to small a (S → aS), or small b (S → bS) or epsilon (∅). To design the machine for WW reverse, consider the string "abbbba" as an example. Assuming the first letter starts with small a, read a from state q1 and then go to state q2. Delete the small a in each position that must be followed by another small a ( rule S → aS). Parse the input from right to left to remove any remaining small a or b. If a non-expected letter is found during parsing, reject the string; otherwise, accept it when all small a and b have been removed.

---

## Designing Turing machines Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/o0boU/designing-turing-machines)

Here is a summary of the text in 8 sentences, preserving key information, formulas, links, and technical details:

The language of nA's followed by nB's is context-free but not regular. The Turing machine for this language starts with state q1 and reads 'a' to delete it and then moves to the end of the input, where it checks if there is a corresponding 'b'. If so, it deletes the 'b', otherwise it rejects. To process strings of nA's followed by nB's followed by nC's, the Turing machine needs to verify that the number of C's and A's are equal and replace C's with D's. It also needs to count B's and D's and move left if there is a blank at the end of the input. The Turing machine has two phases: one for counting C's and A's, and another for counting B's and D's. To achieve this, it adds new transitions in state q1 and uses loops to read and delete specific letters. By modifying these transitions, we can design a Turing machine that accepts strings of nA's followed by nB's and nC's.

---

## Designing Turing machines example Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/dPobr/designing-turing-machines-example)

Here is a summary of the text in 8 sentences, preserving key information:

A Turing machine with transitions that change the characters on the tape head was used to analyze a specific example. The machine starts at state q_1 and reads an "a", which takes it back to q_1 but writes "b" over the existing character. It then moves right, reads "b", changes it to "a", and moves left, repeating this process until it reaches an empty cell (q_2). From q_2, the machine can only move to the accept state if the input ends with "ab". This means that any input with a non-empty suffix must be rejected. The machine's behavior is determined by its transitions, which specify what action to take based on the current state and character read from the tape. In this example, the Turing machine accepts inputs that end with "abaab" but rejects those that end with "baabb". The analysis of this Turing machine provides insight into the properties of certain non-context-free languages.

Note: I've omitted some technical details such as links to additional resources and practice assignments, as they are not essential to understanding the main concept.

---

## Conclusion Video• . Duration: 37 seconds 37 sec

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/CQafp/conclusion)

There is no text to summarize. The provided text appears to be a transcript of a video or lecture on computer science, specifically discussing non-context free grammars, Turing machines, and their applications in computation.

However, if you provide the actual text, I can help you summarize it in 8 sentences, preserving key information, formulae, links, and technical details.

---

## Introduction to Turing machines Reading• . Duration: 1 hour 55 minutes 1h 55m

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/l8Y87/introduction-to-turing-machines)

There is no text provided for me to summarize. The text appears to be a list of resources and videos related to Turing machines, along with recommended study materials and exercises, but it does not contain any specific information or concepts to summarize. If you could provide the actual text, I would be happy to assist you in summarizing it in 8 sentences while preserving key information, formulae, links, and technical details.

---

## Week 13 exercises Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/QOsAh/week-13-exercises)

Here is a summary of the text in 8 sentences:

The text provides exercises and prompts for Week 13, which focuses on understanding context-free languages and designing Turing machines. The first exercise asks if a given language L={a i b j c k d i+j+K ∣i,j,k≥0} is context-free, and provides the definition of the language. The second exercise asks if another language L={w 1 w 2 w 3 ∣w 1 ,w 2 ,w 3 ε(a+b) ∗ and w 1 =w 2 } is context-free, with a similar definition provided. To design a Turing machine for the language L={a i b j c i+j ∣i,j≥1}, a transition table must be created to handle the repetition of characters 'a' and the addition of 'j'. For the language L={a(a+b) ∗ b}, a transition table is needed to handle the multiplication of 'a' by '(a+b)' and the subsequent 'b'.

The exercises are optional, but recommended for further practice. They aim to test knowledge and identify areas that need additional study. The text also provides links to videos, reading materials, and practice assignments for Week 13.

---

## Week 13 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/6EYIJ/week-13-exercises-hints-and-tips)

Lesson 7.0 Introduction Lesson 7.1 Non-context free languages Lesson 7.2 Turing machines Video: Video Turing machines . Duration: 8 minutes 8 min Video: Video Turing machines – examples . Duration: 5 minutes 5 min Video: Video Designing Turing machines . Duration: 7 minutes 7 min Video: Video Designing Turing machines example . Duration: 5 minutes 5 min Practice Assignment: Turing machines . Duration: 25 minutes 25 min Reading: Reading Introduction to Turing machines ....

---

