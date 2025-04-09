# Week 1 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Module introduction video Video• . Duration: 2 minutes 2 min Get started . Click to get started

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/3vEXY/module-introduction-video)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

This course introduces the fundamentals of computer science, covering core concepts that underpin modern computer systems. The learning objectives include understanding proof techniques, such as propositional logic and tautology, as well as combinatorial principles, theory of languages, automata, and algorithms. By the end of the course, students should be able to describe the syntax of computer languages through grammar and explain the role of Turing machines in computer science. Understanding why Turing machines are needed and where they fit into computer science is crucial before delving deeper. The course also covers sorting and searching algorithms, including linear and binary search, as well as insertion sort, quick sort, merge, and heap sort. Time complexity and big O notation will be covered to help design efficient algorithms. The course aims to equip students with a solid foundation in computer science principles, enabling them to tackle the challenges of developing their own systems. Throughout the course, students will engage with various materials, including videos, readings, discussions, and interactive prompts, to reinforce their understanding of key concepts.

---

## Careers video Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/hUizJ/careers-video)

## NOTE: VIDEO CONTENT WITHOUT EXTRACTABLE TRANSCRIPT ##

Title: Careers video | Coursera

Lesson 1.0 Introduction Video: Video Module introduction video . Duration: 2 minutes 2 min Reading: Reading Course syllabus . Duration: 20 minutes 20 min Discussion Prompt: About you – introduce yourself in the forum . Duration: 20 minutes 20 min Reading: Reading Getting started in this module . Duration: 10 minutes 10 min Video: Video Careers video ....

---

## Introduction to propositional logic Video• . Duration: 58 seconds 58 sec

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/cWM1h/introduction-to-propositional-logic)

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

## Building blocks of logic Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/wt4Ui/building-blocks-of-logic)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

A proposition or statement is a declarative sentence that can be either true or false but not both or neither. For example, "Two is a prime number" and "Five is an even number" are propositions with truth values of T (true) and F (false), respectively. Not all sentences are propositions, such as questions ("Are you going to school?"), orders ("Do your homework now!"), and sentences whose true value depends on variables. Propositions can be represented by capital letters (P, Q, R) or lowercase letters (p, q, r), with specific statements denoted by capital letters and general statements denoted by lowercase letters. Logical connectives include NOT (negation), OR (disjunction), AND (conjunction), IF-THEN (implication), and XOR (exclusive disjunction). These connectives transform atomic propositions into compound propositions, and their truth values depend on the truth values of the atomic propositions. The formula "P or Q then R and S" can be translated to English as "If I study 20 hours a week or I will attend all the lectures, then I will pass the exam and I will be happy." To translate from English to a well-formed formula, we use logical connectives such as NOT, OR, AND, IF-THEN, and XOR to represent the statements.

---

## Truth table – examples Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/nFxA8/truth-table-examples)

Here is a summary of the text in 8 sentences, preserving key information and concepts:

Truth tables are a set of all possible outcomes of propositions and connectives. The truth value of a proposition can be either true or false, and a variable can signify a hypothetical container that holds any statement whose truth value is not specified. There are four basic connectives: negation (not p), conjunction (∧p ∧q), disjunction (∨p ∨q), and implication (→p →q). The truth table for each connective shows the stable true values, which depend on the number of propositions in the formula. For example, a truth table with two propositions has 2^N rows, where N is the number of propositions. The connectives can be combined to form more complex formulas, and it's essential to understand which connective takes precedence over others when constructing truth tables. Implication (→p →q) is equivalent to "if p then q," and its truth table shows that the implication is always true unless the premise is false. The exclusive or (∧/¬p ∨ ¬q) is different from disjunction in that it outputs false when both propositions are true, and its truth table can be constructed by comparing it to the bi-conditional (→p ∧q).

---

## Tautology and consistency (part 1) Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/L4gxt/tautology-and-consistency-part-1)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The video transcript discusses classes of formulas in propositional logic, starting with tautology. A tautology is a formula that is always true, regardless of the truth values of its propositions. The examples given include p or not p and p and q, which are not tautologies because their output depends on the truth values of p and q. On the other hand, formulas like "p then q" are not tautologies because they can be false even if one of the propositions is true. Consistent formulas, on the other hand, are true for at least one scenario, while inconsistent formulas are never true. The video also introduces a special case called biconditionals, which are defined as "if and only if" statements with two propositions. To analyze biconditionals, the transcript uses truth tables to evaluate their output based on different truth values of the propositions involved. Ultimately, the formula "naught p and q, if and only if p or naught q" is determined to be an inconsistent formula because it never evaluates to true regardless of the truth values of p and q.

---

## Tautology and consistency (part 2) Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/TeY2U/tautology-and-consistency-part-2)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The video transcript discusses useful formulas for detecting tautologies and contradictions in propositional logic. A tautology is a formula that is always true, while a contradiction is a formula that is always false. The given formula "p or not-p or p and not-p" can be simplified by replacing "p or not-p" with "true" and "p and not-p" with "false", resulting in the expression "true". This implies that the original formula is a tautology. Another example, "(if p then p) or (q and r)" can also be simplified to "true", demonstrating that it is also a tautology. The transcript reviews several useful relations for determining if a formula is a tautology, consistent, or contradiction, including the results of combining tautologies and contradictions with other logical operators. These formulas and relations are essential for analyzing and evaluating propositional logic statements.

Note: There are no links or technical details provided in the original text that need to be preserved.

---

## Tautology and consistency – examples Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/cdOzt/tautology-and-consistency-examples)

There is no text provided to summarize. The provided content appears to be a video transcript with timestamps, links, and formatting information, but it does not contain any specific text or formulae that can be summarized.

If you could provide the actual text or questions related to propositional logic, tautologies, consistent, or contradictions, I would be happy to help summarize the key concepts and findings for you.

---

## Course syllabus Reading• . Duration: 20 minutes 20 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/ojoCv/course-syllabus)

I'll provide a response in the format you requested.

## Step 1: Understand the problem statement
The problem is asking us to review and understand a module on computer science, specifically focusing on algorithms and data structures. The module consists of several topics, including automata theory, regular languages, context-free languages, Turing machines, algorithms I and II, and complexity theory. We also need to review the activities and assessments associated with this module.

## Step 2: Break down the module into its key components
The module can be broken down into the following key components:
- Lecture videos
- Readings
- Practice quizzes
- Graded quizzes
- Discussion prompts
- Interactive simulations

## Step 3: Determine how to pass the module
To pass this module, we need to understand and complete all of its activities and assessments. The coursework consists of several activities that will be assessed halfway through the course, and the written examination counts for another 50% of our final grade.

The final answer is: $\boxed{0}$

---

## Getting started in this module Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/kGBzX/getting-started-in-this-module)

There is no text provided for me to summarize. The given text appears to be a welcome message from a module instructor, outlining the course structure, communication tools, and resources available to students. It does not contain any specific information about key concepts, formulae, links, or technical details.

If you provide the actual text related to the module, I would be happy to assist you in summarizing it in 8 sentences, preserving all key information, formulae, links, and technical details.

---

## Propositions and logical equivalences Reading• . Duration: 2 hours 55 minutes 2h 55m

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/t9WgG/propositions-and-logical-equivalences)

Unfortunately, this text does not provide any concrete information or key findings about propositions and logical equivalencies. It appears to be a course outline or learning module on discrete mathematics with applications, specifically on the topic of propositions and logical equivalencies.

However, I can summarize the main points as follows:

* Propositions are basic building blocks of logical reasoning and can be either true or false.
* Understanding propositions is essential for constructing and analyzing more complex logical expressions.
* Logical equivalencies allow for simplification of logical expressions by transforming complex expressions into simpler forms.
* The topic can be studied in more detail through a reading, specifically Chapter 1.1 and 1.2 of Koshy's book "Discrete mathematics with applications" (Academic Press, 2004).

There are no formulas, links, or technical details mentioned in the text, as it appears to be a general introduction to the topic rather than a specific mathematical concept or proof.

---

## Week 1 exercises Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/7mWBi/week-1-exercises)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The exercises for Week 1 are optional but recommended to test knowledge and identify areas for additional study. The first exercise involves determining the truth value of p given two statements: p ≡ q and q is not true. The second statement involves three variables: p ≡ q, q ≡ r, and r is true. These exercises aim to determine whether the given statements are tautologies, contradictions, or consistent/consistent. Additionally, the following formulae require truth tables to be constructed and compared for equivalence: (p → q) ∧ (q → r), (p ∧ ¬¬q) → r, and (p ∨ q) → r ≡ (p → q) ∧ (q → r). The final exercise involves showing that two given formulae are equivalent using truth tables.

---

## Week 1 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/VIJzL/week-1-exercises-hints-and-tips)

Lesson 1.0 Introduction Lesson 1.1 Propositional logic Lesson 1.2 Tautology Discussion Prompt: True or false . Duration: 30 minutes 30 min Video: Video Tautology and consistency (part 1) . Duration: 3 minutes 3 min Video: Video Tautology and consistency (part 2) . Duration: 3 minutes 3 min Reading: Reading Propositions and logical equivalences . Duration: 2 hours 55 minutes 2h 55m Video: Video Tautology and consistency – examples ....

---

