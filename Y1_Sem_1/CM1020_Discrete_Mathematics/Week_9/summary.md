# Week 9 - CM1020 Discrete Mathematics - Topic 1 A. Sets - Week 1

## Midterm preparation Video• . Duration: 14 minutes 14 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/IA5MI/midterm-preparation)

Here is the reformatted text:

**Midterm Assessment Preparation**

The midterm assessment will cover five topics: Functions, Propositional Logic, Predicate Logic, and Boolean Algebra.

**Topic 1: Functions**

* Domain, co-domain, and range of a function
* Properties of functions (one-to-one, onto, bijective)
* Inverse functions
* Rules for working with inverse functions

**Topic 2: Propositional Logic**

* Definition of a proposition
* Compound propositions using AND, OR, NOT, IMPLIES, EQUVALENT
* Truth tables and truth sets for compound propositions
* Laws of propositional logic (idempotent law, commutative law, associative law, distributive law)
* De Morgan's laws

**Topic 3: Predicate Logic**

* Difference between a predicate and a proposition
* Quantifiers (universal quantifier, existential quantifier, uniqueness quantifier)
* Nested quantifiers
* Rules of inference (Modus ponens, Modus tollens, conjunctions, disjunctive syllogism)
* Combining rules of inference for propositions and quantified statements

**Topic 4: Boolean Algebra**

* Laws of Boolean algebra (distributive law, commutative law, associative law)
* Building blocks and logic gates
* Converting Boolean expressions to logical circuits
* Simplifying Boolean expressions using Karnaugh maps

**Study Resources**

* Video: "Midterm Preparation" (14 minutes)
* Video: "Introduction to Boolean Algebra" (5 minutes)
* Discussion Prompt: "What do you know about Boolean algebra?" (20 minutes)
* Reading: "Postulates of Boolean Algebra" (15 minutes)
* Practice Assignment: "Postulates of Boolean Algebra" (25 minutes)
* Video: "Boolean Functions" (5 minutes)
* Practice Assignment: "Boolean Functions" (30 minutes)

**Additional Study Resources**

* Reading: Essential reading for Topic 5 (2 hours)

---

## Introduction to Boolean algebra Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/e0vBy/introduction-to-boolean-algebra)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Boolean algebra is a new topic that will be introduced in this lecture. The history of Boolean algebra dates back to Aristotle's work on logic between 384 and 322 BC. George Boole published an investigation of the laws of thought in 1854, developing a system of logical algebra for mathematical expression of reasoning. Claude Shannon wrote a thesis in 1938, investigating Boolean algebra as a tool for analyzing relay switching circuits.

Today, Boolean algebra is the foundation of computer circuit analysis and design of transistors, which are the basic elements in building processors. A two-valued Boolean algebra system is used, where variables can only have values of zero or one. The operators "+" and "." are used instead of "and" and "or". The most well-known form of Boolean algebra is a two-valued system.

Boolean algebra is based on three fundamental operations: the logical product (AND), represented as x.y; the logical sum (OR), represented as x+y; and the logic complement (NOT), represented as x'. The truth tables for these operators are provided. When parentheses are not used, these operators have a specific order of precedence.

The two-valued Boolean algebra system can be used to describe and design digital circuits. It is also the basis for designing transistors in building processors. For example, an IoT system can be designed using a Boolean algebra equation, such as w = h and a, where w represents the spray in water, h represents high heat detected, and a represents the system being activated.

Overall, this lecture introduces Boolean algebra, its history, applications, and basic operations, providing a foundation for computer circuit analysis.

---

## Postulates of Boolean algebra Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/mUmjb/postulates-of-boolean-algebra)

Here is a summary of the text in 15 sentences, preserving all key information, formulae, and technical details:

Boolean algebra is a branch of mathematics that deals with logical operations. The six axioms of Boolean algebra, known as Huntington's postulates, are: closure, identity, commutativity, complements, distributivity, and uniqueness of complements. These axioms define the properties of Boolean operations such as AND (dot) and OR (plus). The Boolean operation satisfies the following laws: idempotent law (x + x = x and x.x = x), tautology (x + 1 is always true), contradiction (x * 0 is always false), involution (x complemented twice equals x), associative law (x + y + z = x + y + z), absorption law (x + xy = x and x.x + y = x), and uniqueness of complements. De Morgan's theorems state that the complement of a product is equal to the sum of the complements, and the complement of a sum is equal to the product of the complements. The principle of duality states that every theorem in Boolean algebra remains valid if we interchange all ANDs and ORs and interchange all zeros and ones. There are four ways to prove the equivalence of Boolean relations: perfect induction (showing identical truth tables), axiomatic proof (applying Huntington's postulates or other rules), duality principle, and contradiction. The absorption rule can be proved by writing a true table or using the rules earlier seen as x + xy = x and x.x + y = x. Boolean algebra has many applications in digital electronics and computer science, including circuit design and analysis. Understanding Boolean algebra is essential for designing and analyzing digital circuits, which are used in computers, communication systems, and other electronic devices.

---

## Boolean functions Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/DsDb9/boolean-functions)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A Boolean function defines a mapping from one or multiple Boolean input values to a Boolean output value. For n Boolean input values, there are 2^n possible combinations. A truth table can be used to represent a Boolean function, but it is not the only form of representation. The algebraic form of a Boolean function can be expressed in various ways, including the sum of products form and the product of sums form.

The sum of products form is more convenient for simplification purposes. To build a function in this form, focus on the values of the variable that make the output equal to 1, then express it as the sum of products of all the terms for which f equals 1. If an input equals 0, its complement is used.

The exclusive or function can be expressed as x or y = x'y + xy'. The implies function can be expressed as x → y = x' + y. Two useful Boolean functions are the exclusive or function and the implies function. These functions have specific truth tables that illustrate their behavior. 

The sum of products form is used in this lecture for building Boolean functions. It allows for easier simplification of complex expressions.

---

## Postulates of Boolean algebra Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/07fgj/postulates-of-boolean-algebra)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Boolean algebra is a mathematical structure that captures the essentials of logic operations and set operations. The primary postulates of Boolean algebra are: closure with respect to binary operations, identity, complement, commutativity, associativity, distributivity, absorption, idempotent law, De Morgan's laws. These postulates provide a formal framework for manipulating and reasoning about logical expressions and digital circuits using addition (+) for OR and multiplication (⋅) for AND. The set S={0,1} is closed under the operations of addition and multiplication, meaning that for all a,b∈S, a+b∈S and a.b∈S. For all a∈S, we have a+0=a and a.1=a, which represent the identity element for OR and AND operations, respectively. Every element a∈S has a complement a’∈S such that a+a’=1 and a.a’=0, representing the complement operation. The commutative law states that a+b=b+a and a,b=b.a, indicating that the order of elements does not change the result. Associativity holds for all a,b,c∈S, meaning that (a+b)+c=a+(b+c) and (a.b).c=a.(b.c), showing that the order in which elements are combined does not affect the result. Distributivity states that a.(b+c)=a.b+a.c and a+(b+c)=(a+b)+c, demonstrating the relationship between addition and multiplication operations. The absorption law states that a+(a.b)=a and a.(a+b)b=a, showing that certain combinations can be simplified. De Morgan's laws state that (a+b)’=a’.b’ and (a.b)’=a’+b’, which provide a way to simplify complex logical expressions. These principles are foundational to computer science, digital logic design, and various fields involving binary decision processes. The postulates of Boolean algebra provide a mathematical structure for analyzing and designing digital circuits and computer algorithms. By understanding these fundamental concepts, one can better appreciate the power of Boolean algebra in solving problems related to logic and computation.

---

## Topic 5 essential reading Reading• . Duration: 2 hours 2h

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/4rQcO/topic-5-essential-reading)

Here is a summary of the text in 15 sentences:

The provided text appears to be a table of contents for a study guide or textbook on Boolean algebra, with references to specific pages, exercises, and videos.

The table of contents covers various topics related to Boolean algebra, including its definition, Huntington's postulates, De Morgan's theorems, the principle of duality, and algebraic forms.

There are multiple video tutorials available for each topic, ranging from 5-30 minutes in duration.

Exercises are also provided, with solutions available at the back of the book or online.

---

