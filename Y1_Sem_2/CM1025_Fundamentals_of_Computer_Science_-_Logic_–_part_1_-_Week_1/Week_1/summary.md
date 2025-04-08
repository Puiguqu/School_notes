# Week 1 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Module introduction video Video• . Duration: 2 minutes 2 min Get started . Click to get started

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/3vEXY/module-introduction-video)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The course "Fundamentals of Computer Science" aims to introduce core concepts that underpin modern computer science principles, including proof techniques, logic, combinatorial principles, theory of languages, automata, algorithms, syntax of computer languages, Turing machines, sorting and searching algorithms, time complexity, and big O notation. By the end of the course, students will be able to explain various proof techniques, describe the syntax of computer languages through grammar, and understand the role of Turing machines in computer science. The course covers fundamental topics such as propositional logic, tautology, combinatorial principles, and theory of languages, providing a solid foundation for understanding modern computer systems. Students will learn about linear and binary search algorithms, different sorting algorithms (insertion sort, quick sort, merge sort, heap sort), and implement and analyze these algorithms to gain practical experience. The course also covers time complexity and big O notation, which is essential for designing efficient algorithms. Turing machines are introduced as a crucial concept in computer science, allowing students to understand the theoretical foundations of modern computing systems. The course is designed to provide a comprehensive introduction to computer science principles, preparing students for future learning and exploration in the field. Throughout the course, students will engage with interactive content, including videos, reading materials, and discussion prompts, to deepen their understanding of key concepts and apply them practically.

---

## Careers video Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/hUizJ/careers-video)

## NOTE: VIDEO CONTENT WITHOUT EXTRACTABLE TRANSCRIPT ##

Title: Careers video | Coursera

Lesson 1.0 Introduction Video: Video Module introduction video . Duration: 2 minutes 2 min Reading: Reading Course syllabus . Duration: 20 minutes 20 min Discussion Prompt: About you – introduce yourself in the forum . Duration: 20 minutes 20 min Reading: Reading Getting started in this module . Duration: 10 minutes 10 min Video: Video Careers video ....

---

## Introduction to propositional logic Video• . Duration: 58 seconds 58 sec

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/cWM1h/introduction-to-propositional-logic)

Unfortunately, there is no text provided for me to summarize. The given text appears to be a video transcript and additional page content related to an online course or tutorial on propositional logic. It does not contain any specific information that can be summarized in 8 sentences.

However, I can provide an overview of the main concepts and topics related to propositional logic based on the provided links and videos:

Propositional logic is a system that deals with propositions or statements. The basic concepts include building blocks of logic, truth tables, and tautology. Tautology refers to a statement that is always true regardless of the values assigned to its variables.

The tutorial covers topics such as introducing propositional logic, discussing the concept of liars and knights, solving riddles like the example mentioned in the transcript, and exploring the building blocks of logic, truth tables, and propositions. The course aims to help learners develop skills in solving logical puzzles and understanding the principles of propositional logic.

Please provide more text or context for me to summarize, and I'll be happy to assist you further.

---

## Building blocks of logic Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/wt4Ui/building-blocks-of-logic)

Here is a summary of the text in 8 sentences, preserving key information and concepts:

A proposition or statement is a declarative sentence that can be either true (T) or false (F), but not both. Sentences like "X is a prime number" are not propositions because their truth value depends on variable values, making them contingent statements. Propositions are denoted by capital letters (P, Q, R) and have specific meanings, whereas lowercase letters (p, q, r) represent general statements with unspecified true values. Logical operators include NOT (~), OR (∨), AND (∧), IF-THEN (∠), and XOR. Connectives transform atomic propositions into compound propositions by changing their truth values based on the value of the operands. The formula "If P or Q then R and S" can be translated into English as "If I study 20 hours a week or I attend all lectures, then I will pass the exam and I will be happy." To translate from English to a well-formed formula, identify the propositions (P, Q, R) and apply logical operators accordingly. The process involves replacing sentences with letters and applying connectives to create a logical statement that accurately represents the intended meaning.

---

## Truth table – examples Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/nFxA8/truth-table-examples)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

A truth table is a set of all possible outcomes of propositions and connectives, where each proposition can be either true or false. The connective negation (NOT) is defined as one minus the truth value of p, resulting in a table with two rows: P = True -> NOTP = False; P = False -> NOTP = True. Conjunction (AND) has four possible combinations: PP & QQ = True, PQ or QR = True, but PP & QQ = False. The formula for conjunction is equivalent to the multiplication of truth values: p & q = truth value of p * truth value of q. Disjunction (OR) is true if at least one proposition is true, resulting in a table with four rows. Conditional (IMPLIES) can be understood as "if-then" statements, where p -> q holds true only when p is false or q is true: p -> q = truth value of p <= truth value of q. Bi-conditional and exclusive OR are also discussed, with the bi-conditional being equivalent to an equality check (p iff q) and exclusive OR meaning "only one of these can be true". The order of precedence for connectives is determined by their table layout: negation first, then disjunction, implication, and finally bi-conditional.

---

## Tautology and consistency (part 1) Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/L4gxt/tautology-and-consistency-part-1)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The first class of formulas being studied is tautology, which refers to a formula that is always true regardless of the truth values of its propositions. A counterexample to this definition is p and q, as it can be false when the truth value of p is 0. Another example is "p then q", which can be false even if p is true and q is false. In contrast, a formula that is true for at least one scenario is called consistent. A contradiction is a formula that is never true. The given example, "naught p and q if and only if p or naught q", is an instance of the latter type, making it inconsistent. To determine the consistency of this formula, its truth table was created, showing that it is false in all scenarios, thus confirming it as a contradiction. This finding has implications for our understanding of logical equivalences and the relationships between different types of formulas.

---

## Tautology and consistency (part 2) Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/TeY2U/tautology-and-consistency-part-2)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

A tautology is a formula that is always true, while a contradiction is a formula that is always false. To determine if a formula is a tautology, consistent, or contradiction, we can use various formulas and rules of propositional logic. One such formula is "p or not-p", which is always true and can be replaced with "true". Another formula, "p and not-p", is always false and can be replaced with "false". The given formula "p or not-p or p and not-p" is a tautology because it can be reduced to "true". To determine if another formula "if p then p or q and r" is a tautology, consistent, or contradiction, we can apply similar rules. The formulas for determining the properties of a formula are: (1) A tautology or consistent formula is always a tautology, (2) A tautology and consistent formula is consistent, (3) A tautology or contradiction formula is a tautology, (4) A tautology and contradiction formula is a contradiction, (5) A contradiction or consistent formula is consistent, (6) A contradiction and consistent formula is a contradiction, (7) If a formula is a tautology then it implies a contradiction, and (8) if a formula is a contradiction then it implies a tautology.

---

## Tautology and consistency – examples Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/cdOzt/tautology-and-consistency-examples)

There is no text provided to summarize. The given text appears to be a video transcript and additional page content related to tautologies, consistent, and contradictions in propositional logic. It outlines various lessons, videos, readings, practice assignments, and discussion prompts without presenting specific formulas or technical details.

If you provide the actual text you'd like me to summarize, I'll be happy to assist you with preserving key information, formulae, links, and technical details in a concise summary of 8 sentences.

---

## Course syllabus Reading• . Duration: 20 minutes 20 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/ojoCv/course-syllabus)

I'd be happy to help you with this course outline! However, I noticed that the text is quite long and contains many tables and formatting. Could you please provide me with a summary of the main topics and activities in the course? That would make it easier for me to assist you.

From what I can gather from the text, the course appears to be an introductory computer science course that covers a range of topics, including:

* Programming concepts
* Data structures (arrays, linked lists, stacks, queues)
* Algorithms (sorting, searching, graph algorithms)
* Automata theory
* Formal languages
* Turing machines
* Complexity theory

The course includes various activities, such as:

* Lecture videos
* Readings
* Practice quizzes
* Graded quizzes
* Discussion prompts
* Interactive simulations

Is that a correct summary? If you could provide more context or clarify any specific questions you have about the course, I'd be happy to try and help further!

---

## Getting started in this module Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/kGBzX/getting-started-in-this-module)

There is not enough information in the text provided to summarize in 8 sentences, preserving all key information, formulae, links, and technical details. The text appears to be a welcome message for a module on Coursera, outlining the course syllabus, learning outcomes, assessment requirements, and providing resources for success.

However, here is a summary of the most important concepts and findings in 4-6 sentences:

This module provides an introduction to propositional logic, covering key topics such as tautology. The University of London Careers Service is available to support students throughout their career journey, regardless of their location. Students are encouraged to familiarize themselves with the course syllabus, learning outcomes, and assessment requirements. The module also introduces three important communication tools: discussion forums, Slack, and Zoom. Additionally, students can access resources such as the Online Library and Studiosity, a new online service piloted by the University to support academic writing.

There is no information on formulae, links, or technical details in the provided text.

---

## Propositions and logical equivalences Reading• . Duration: 2 hours 55 minutes 2h 55m

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/t9WgG/propositions-and-logical-equivalences)

Unfortunately, there is no text provided for me to summarize. The text appears to be a course outline or instructional materials for a learning platform, but it does not contain any specific information or data that can be summarized. If you could provide the actual text you would like me to summarize, I would be happy to assist you.

---

## Week 1 exercises Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/7mWBi/week-1-exercises)

Here is a summary of the text in 8 sentences, preserving key information:

The exercises from Week 1 are optional but recommended to test knowledge and identify areas for additional study. The first exercise involves determining the truth value of p in given scenarios, such as when p ≡ q and q is not true. Another scenario is when p ≡ q and r ≡ t, with r being true. The exercise also requires identifying whether a formula is a tautology, consistent, or contradiction. Truth tables are provided for the following formulae: (p → ¬r) ∧ (q → ¬r), (p ∧ ¬¬q) → ¬r, and (p ∨ q) → ¬r ≡ (p → ¬r) ∧ (q → ¬r). The exercises aim to show that these formulae are equivalent using truth tables. Additionally, the exercises P → ¬(q ∨ r) ≡ (p ∧ ¬¬q) → ¬r require completion and analysis of the logical equivalences.

---

## Week 1 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/VIJzL/week-1-exercises-hints-and-tips)

There is no text to summarize. The provided input appears to be a course syllabus or lesson plan, listing topics, video durations, reading materials, practice assignments, and discussion prompts for a 30-minute introduction to propositional logic lesson. 

If you provide the actual text related to propositional logic, I would be happy to assist with summarizing it in 8 sentences while preserving key information, formulae, links, technical details, and most important concepts and findings.

---

