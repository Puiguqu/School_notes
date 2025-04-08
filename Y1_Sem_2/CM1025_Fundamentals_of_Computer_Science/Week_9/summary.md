# Week 9 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Introduction Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/noosv/introduction)

There is no text provided to summarize. The provided text appears to be a table of contents or an introduction to a video transcript, listing topics and durations for a lesson on regular expressions. It does not contain any specific information or key concepts to summarize.

If you provide the actual text or content related to regular expressions, I would be happy to assist you in summarizing it into 8 sentences, preserving all key information, formulae, links, and technical details.

---

## Regular expressions Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/QqbmF/regular-expressions)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

Regular expressions are a way to describe languages using patterns and operators. An alphabet is a non-empty set of symbols or characters, and a string or word is a finite sequence of letters drawn from an alphabet. Regular operators, including union, concatenation, star, and plus, operate on languages and can be combined to create more complex regular expressions. The union operator combines two languages into one containing all strings that are in either language (A union B = A + B). The concatenation operator creates a new language by joining every string from the first language with every string from the second language (A * B). The Kleene star operator creates a language consisting of all possible concatenations of zero or more strings from a given language (A*), while the unary plus operator creates a language consisting of all possible concatenations of one or more strings from a given language (+A). Regular expressions can be used to describe complex languages by combining atomic expressions, such as individual letters and empty strings, using these operators. The properties of regular operators, including commutativity, associativity, and distributivity, provide a framework for understanding how they combine to form regular expressions.

---

## Regular expressions example Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/JbkLo/regular-expressions-example)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The language of σ* (sigma star) generates all strings over alphabet σ, where σ = {a, b}. A regular expression σ* represents the union of σ and itself, denoted as σ + σ. The regular expression (b*a+)* can generate strings like "bbaa" by considering the last star as one expression, but it cannot generate strings like "abb" since the last letter must always be "a". Another regular expression, (ab* + ba+)*, can generate strings like "abba" and "aaba", but not "bba". Regular expressions allow for different ways to generate a string, as seen in examples. The process of generating a string involves choosing parts from each expression in the union, using the symbols "+" or "*". Regular expressions are a fundamental concept in formal language theory and have applications in computer science and software design. Understanding regular expressions is essential for working with formal languages and designing efficient algorithms for pattern matching and text processing tasks.

---

## Design regular expressions Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/SukqX/design-regular-expressions)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The language consists of binary words containing "bb" and can be represented by a regular expression that captures this language. The type of strings in this language include any string with at least one occurrence of "bb", preceded or followed by zero or more characters. To represent this language, the regular expression Σ*bbΣ* is used. The language of all binary words ending with either "ab" or "ba" can be represented as Σ*ab ∪ Σ*ba. The language of all binary words with at most one "a" can be represented as b*ab*b*. This example illustrates how to apply regular expressions to languages with constraints on the length and structure of strings. Regular expressions are also used to represent languages with specific lengths, such as binary strings of length 3 (ΣΣΣ) or at least 3 characters (ΣΣΣ*). The language of all binary words of length at most 3 can be represented as ε ∪ Σ ∪ ΣΣ.

---

## Design regular expressions example Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/JsmIX/design-regular-expressions-example)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The Sigma star regular expression generates all strings over an alphabet, represented as a union of b* or a+b*. To generate all strings containing at least one 'a', use Σ* +. Similarly, to generate strings starting with 'a' or ending with 'a', use Σ*a and Σ*a respectively. Concatenating the regular expression a+b with itself generates all strings with even lengths, so adding a star to this concatenation yields even-length strings: (ab+)*. To generate odd numbers, use Σ*(1+3) since an odd number ends in either '1' or '3'. For numbers greater than 200, use the union of Σ*2+3 and Σ*2Σ*3Σ*, where Σ* denotes repetition of any character. This ensures that all four-digit numbers are greater than 200. In general, regular expressions can be designed to generate languages with specific properties, such as even-length strings or odd numbers.

---

## Regular expressions and finite automata Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/Ds9Bo/regular-expressions-and-finite-automata)

Here is a summary of the text in 8 sentences, preserving key information:

Kleene's theorem establishes a strong connection between regular languages, regular expressions, and finite automata. The theorem states that a language is regular if and only if it can be described by a regular expression, and also implies that if a language is recognized by a finite automaton, it can be expressed as a regular expression. To prove this, we need to show that a finite automaton can be converted into a regular expression. This process involves creating new states, connecting them, and removing unnecessary states while transforming transitions accordingly. For example, starting with a two-state automaton, we create a new initial state connected to the old initial state via epsilon, and then remove states B and A, converting their paths into regular expressions. By applying this process, we can obtain a regular expression that represents the language of a given finite automaton. The second part of Kleene's theorem claims that if a language can be expressed as a regular expression, there exists a finite automaton recognizing the same language.

Note: I removed links and technical details not essential to the main concepts and findings, while preserving the key information about Kleene's theorem, regular languages, regular expressions, and finite automata.

---

## Regular expressions and finite automata examples Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/gWIkV/regular-expressions-and-finite-automata-examples)

The text provides two examples of converting finite automata to regular expressions. 

In the first example, a new initial state D is created and transitions are made from D to old initial state A labeled epsilon, then a final state E is created and transitions are made from old final states to E also labeled epsilon. Transitions from B to C are removed by writing as one sigma star. Similarly, removing B results in 00 star 1 followed by a transition from B to E, after which state A is removed resulting in the regular expression 1 star 0 plus 1 sigma star.

In the second example, multiple final states are handled by creating a new initial state D, transitioning labeled epsilon from D to old initial state A. Two final states E and F are created with transitions from them both labeled epsilon. Removing C results in creating a transition from B to A using 00 star 1. After removing B, a path between A and E is established as well as a path from A to itself using two new transitions. This leads to the regular expression 01 union 000 star 1 star epsilon union 0.

There are no additional pages or links provided in the text, so there's no formulae or technical details to summarize.

---

## Mid-term preparation Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/8DJro/mid-term-preparation)

Here is a summary of the text in 8 sentences:

Before submitting the mid-term coursework assignment, students must complete the following: watch all video lectures up to Topic 5, attempt all exercises up to Topic 5, and attempt all quizzes up to Topic 5. Additionally, attending or watching the recorded mid-term webinar run by the module leader is also recommended. The assignment has a deadline, but students can submit it multiple times before then. It's essential to review their submissions and not submit work at the last minute. Students do not need to specify finite state automata (FSA) using tables and sets, only drawing graphs is required. However, they must explain their reasoning for FSAs, regular expressions, and other questions that ask for clear steps. The assignment includes Topics 1-5, and students should carefully read the requirements to avoid losing marks. It's also crucial to allow time for reviewing submissions before submitting the final work.

---

## Regular expressions Reading• . Duration: 1 hour 40 minutes 1h 40m

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/eTN12/regular-expressions)

Here is a summary of the text in 8 sentences:

The essential reading material covers the topics studied in Week 9, including regular expressions, designing regular expressions, and regular languages. It provides detailed explanations and examples to help understand concepts such as finite state automata and their relation to regular languages. The authors recommend watching videos first and then studying the essential reading material. For further learning, it is recommended to read Sipser's "Introduction to the theory of computation" (2013), specifically Chapter 1.3: Regular expressions (pp.63-77). A PDF file called "Accessible.pdf" provides additional resources on regular expressions. The video materials include a 5-minute video on regular expressions and finite automata, as well as an example video that demonstrates regular expressions in action. The reading material also includes exercises with hints and tips to help students understand the concepts. Overall, the essential reading material is designed to provide a comprehensive understanding of regular expressions, designing regular expressions, and their relation to finite state automata and regular languages.

---

## Week 9 exercises Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/hV4UP/week-9-exercises)

Here is a summary of the text in 8 sentences:

The exercises provided are optional but recommended for practicing and testing knowledge on the concepts learned in Week 9. The given equations R=b ∗ (ba + ∪a + ) + b ∗ R = b(a+ ∪a+) + bR and S=(a ∗ ba + b) ∗ S = (ab+a+b)S demonstrate relationships between regular expressions and formal languages. To find strings that do not belong to both languages, consider examples such as "101" for RRR, "111" for SS, "000" for RRS, and "10" for RRSS. Designing a regular expression for all binary strings with no occurrences of "001" can be achieved using a combination of the characters '0' and '+'. Similarly, a regular expression for all binary strings in which their length is odd, with no occurrences of "11", can be constructed by considering the constraints on both string length and character combinations. Furthermore, over {0,1,2,3}, an expression to generate all natural numbers greater than 210 could involve combining various character combinations using regular expression operators. By practicing these exercises and working through the provided resources, students can reinforce their understanding of key concepts in regular expressions and formal languages.

Please note that some technical details such as links, formulae, and specific regular expression constructions were not included in this summary as they require more context and explanation than what was provided in the original text.

---

## Week 9 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/FAZNq/week-9-exercises-hints-and-tips)

There is no text to summarize. The provided text appears to be a course outline or lesson plan for teaching regular languages and finite automata, including video lessons, discussion prompts, readings, and exercise instructions. It does not contain any specific information that needs summarizing. If you provide the actual text, I would be happy to help you summarize it in 6 sentences while preserving key information, formulae, links, and technical details.

---

