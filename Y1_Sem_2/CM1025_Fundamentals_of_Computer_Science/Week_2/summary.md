# Week 2 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Equivalences (part 1) Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/WG11o/equivalences-part-1)

Here is a summary of the text in 8 sentences, preserving key information:

Propositional equivalencies are defined as two formulae being equivalent if they have identical truth tables, denoted by three horizontal lines (∼). De Morgan's Laws state that not (P ∧ Q) is equivalent to (¬P ∨ ¬Q) and not (P ∨ Q) is equivalent to (¬P ∧ ¬Q), which can be used to apply negation to conjunctions. The first law of De Morgan's Law changes the connective "and" to "or" when applying negation, while the second law binds to each proposition separately before changing the connective. Applying De Morgan's Law to the statement "it is Wednesday and it is not sunny" results in "it is not Wednesday or it is sunny". Truth tables can be used to prove equivalence, as demonstrated by the first law of De Morgan's Law. Another important equivalence is P ∧ Q ≡ ¬Q ∨ P, which demonstrates that conjunction is equivalent to disjunction with negation. The contrapositive of P ∧ Q is not Q ∧ ¬P, but it is logically equivalent due to the symmetry property of propositional logic. These equivalencies demonstrate fundamental properties of first-order logic and are essential for applying logical operations to complex statements.

---

## Equivalences (part 2) Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/iTK5b/equivalences-part-2)

Here is a summary of the text in 8 sentences, preserving key information and concepts:

The video discusses equivalences with logical operators, focusing on converting disjunction to negation and conjunction using De Morgan's Law. The law states that p or q can be written as ¬(¬p ∧ ¬q), where ¬ denotes negation. The video also explores the conversion of implication to its equivalent form using De Morgan's Law. For example, "if p then q" is equivalent to "¬p ∨ q", which can be further simplified to "¬p ∧ q". The video provides an example where the formula "p or if q then r" is rewritten using only negation and conjunction. By applying De Morgan's Law and simplifying, the final formula is ¬(¬p ∧ ¬q ∧ ¬r). Additionally, the video discusses converting each conjunction to its equivalent form using disjunction and negation. The speaker also explains how to prove a statement true without using a truth table by breaking it down into simpler logical equivalences.

---

## First-order logic Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/Zweww/first-order-logic)

Here is a summary of the text in 8 sentences, preserving key information and concepts:

First-order logic is a branch of logic that deals with predicates, which describe properties of objects. Predicates can take one or multiple objects as arguments, forming propositions that can be true or false. The existential quantifier (E) denotes "there exists" and the universal quantifier (∃) denotes "for all", where the former requires only one example to make a statement true, while the latter must be true for all elements in the domain. Quantifiers play a crucial role in reasoning about multiple objects, with the first-order logic language allowing for translations from English to formal sentences using these quantifiers. The negation of universally quantified statements can be proven false by finding just one counterexample, whereas the negation of existentially quantified statements requires a positive example to disprove its truth. An alternative presentation of quantifiers using connectives allows for more flexibility in handling formulas and proofs. By applying DeMorgan's law and other logical equivalences, it is possible to negate universally quantified statements by changing them into existential quantifications and vice versa. The understanding of first-order logic, including predicates, quantifiers, and negation, is essential for further study in mathematics and computer science.

---

## Conclusion Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/G4xjT/conclusion)

There is no text to summarize. The provided output appears to be a video transcript with links, instructions, and other metadata, but it does not contain any specific information or content that needs summarization.

However, I can provide a general summary of the topics covered in the video transcript:

The video transcript covers Week 2 of a computer science course, focusing on propositional logic. The learning objectives include explaining propositions, tautology and contradiction, De Morgan's law, first-order logic, and solving problems using formal proof.

A specific riddle is presented, involving two people on an island, where one person (Person A) claims that at least one of them is a liar, while the other person (Person B) says nothing. The transcript guides the viewer through a logical analysis to determine whether Person A is a knight or a liar and conclude that Person A is indeed a knight and Person B is a liar.

The summary includes information on the course material, learning objectives, and key concepts such as propositional logic, tautology, contradiction, De Morgan's law, first-order logic, and formal proof.

---

## Quantifiers Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/BJvom/quantifiers)

This text does not provide any key information, formulae, links, or technical details. It appears to be a summary of a course material that covers various topics in logic, including propositions, tautologies, De Morgan's law, first-order logic, and quantifiers.

However, I can summarize the content as follows:

The text is an introduction to a series of lessons on logic, covering topics such as propositions, tautologies, De Morgan's law, first-order logic, and quantifiers. It provides detailed explanations, examples, and videos to help students understand these concepts. The recommended learning path includes watching video lectures before studying the essential reading. The text also recommends reading specific chapters and practice assignments, including a discussion prompt on negation.

The topics covered in this section include:

* Propositions
* Tautologies
* De Morgan's law
* First-order logic
* Quantifiers

There are no links or technical details provided in the text.

---

## Week 2 exercises Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/tWvoQ/week-2-exercises)

Here is a summary of the text in 8 sentences, preserving all key information, formulae, links, and technical details:

The exercises for Week 2 are optional but recommended to test knowledge and identify areas for additional study. The first exercise involves negating propositions, such as ∀x(x > 0) and ∃x(x^2 = 4x + 2), which can be solved using truth tables or logical reasoning. Another exercise asks students to rewrite sentences symbolically, including the statement "The product of any two real numbers x and y is negative," which can be expressed as ∀x∀y(x*y < 0). A third exercise requires students to prove that (¬¬p → q) ∨ (r → q) ≡ r → (p ∨ q) using logical reasoning. The fourth exercise asks students to show that ((R → S) → R) is a tautology without using truth tables, by analyzing the logical structure of the statement. The exercises cover various topics in logic, including first-order logic and proposition theory. Students are encouraged to refer to hints and tips on the next page for additional support or clarification.

---

## Week 2 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/c4l9Q/week-2-exercises-hints-and-tips)

Lesson 1.3 First-order logic Lesson 1.4 Conclusion Practice Assignment: Logic . Duration: 35 minutes 35 min Reading: Reading Week 2 exercises . Duration: 1 hour 1h Reading: Reading Week 2 exercises hints and tips . Duration: 10 minutes 10 min Discussion Prompt: What did you learn? What did you like? . Duration: 20 minutes 20 min Video: Video Conclusion . Duration: 2 minutes 2 min Lesson 1.5 Summative assessment

---

