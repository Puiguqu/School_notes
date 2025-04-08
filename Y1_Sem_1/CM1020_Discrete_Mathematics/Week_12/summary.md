# Week 12 - CM1020 Discrete Mathematics - Topic 1 A. Sets - Week 1

## Recursive definitions Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/nmSDR/recursive-definitions)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Recursive definitions are used to define mathematical objects in terms of themselves. A recursively defined function f with domain n has two steps: basis step and recursive step. The basis step specifies an initial value of the function, while the recursive step provides a rule for finding the value of the function at an integer from its values at smaller integers.

For example, the sequence aN can be defined as 4n, 4^n, or 4 with different definitions. A set S can also be defined recursively by specifying initial elements and providing a rule for constructing new elements from those already in the set.

Algorithms are finite sequences of precise instructions for performing computations or solving problems. An algorithm is called recursive if it solves a problem by reducing it to an instance of the same problem with smaller inputs. For example, n factorial can be recursively defined as 0! = 1 and n! = n * (n-1)!, where n is a non-negative integer.

Recursive definitions are used in mathematics to define complex objects such as functions, sequences, and sets. They provide a way to break down problems into smaller instances of the same problem, making it easier to solve them. The key concepts in this lecture include recursive definitions, basis steps, recursive steps, and algorithms with recursion.

The formulas and technical details used in this lecture include:

* aN = 4n (sequence)
* aN = 4^n (sequence)
* aN = 4 (sequence)
* S = {x | x is an integer such that x = 4y for some integer y} (set)

The key concepts and findings of this lecture are:

* Recursive definitions provide a way to define complex objects in terms of themselves.
* Basis steps and recursive steps are used to define recursive functions, sequences, and sets.
* Algorithms with recursion can be used to solve problems by breaking them down into smaller instances of the same problem.

---

## Recurrence relations Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/ml1I7/recurrence-relations)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A recurrence relation defines a sequence based on a rule that gives the next term as a function of previous terms. An infinite sequence is a function from the set of positive integers to the set of real numbers. The Hanoi Tower problem involves transferring n discs from one spoke to another without placing a larger disc on top of a smaller one, with an equation relating the minimum number of moves (an) to n.

A linear recurrence relation has each term as a linear function of earlier terms in the sequence, with two types: homogeneous and non-homogeneous. The Fibonacci sequence is an example of a second-order linear recurrence relation. An arithmetic sequence has a constant difference between consecutive terms, while a geometric sequence has a constant ratio between consecutive terms.

The number of moves required to transfer n discs from one spoke to another can be expressed as the equation an = 2an-1 + 1. A first-order linear recurrence relates the population in N years from now (an+1) to the previous term (an), with initial conditions a0 = 50 million and an+1 = 1.01an + 50,000.

Divide and conquer algorithms solve problems by dividing them into smaller subproblems, solving recursively each subproblem, and combining solutions. The problem of finding the minimum of a sequence can be solved using this approach. Recurrence relations are essential in solving many types of mathematical problems.

In conclusion, recurrence relations are used to define sequences based on rules that give next terms as functions of previous terms. Linear recurrences relate terms by linear functions of earlier terms, while arithmetic and geometric sequences have constant differences or ratios between consecutive terms. Divide and conquer algorithms can be applied to solve many types of mathematical problems.

---

## Solving recurrence relations Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/wKxir/solving-recurrence-relations)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A recurrence relation can be solved using linear homogeneous recurrences and strong induction. A linear homogeneous recurrence has the form $a_n = c_1a_{n-1} + \cdots + c_ka_{n-k}$, where each term is a multiple of the previous term. The characteristic equation is obtained by dividing both sides by $a_{n-k}$, resulting in $r^n = c_1r^{n-1} + \cdots + c_k$. Solving this equation gives a solution to the recurrence relation.

The Fibonacci recurrence relation is an example of a linear homogeneous recurrence with two distinct roots: $r_1 = 1 + \sqrt{5}/2$ and $r_2 = 1 - \sqrt{5}/2$. The general solution to the Fibonacci recurrence relation is given by $F_n = A_1r_1^n + A_2r_2^n$, where $A_1$ and $A_2$ are constants determined using initial conditions.

In a strong induction proof, we prove that a statement $P(n)$ is true for all integers $n \geq k$, given that it holds for $0, 1, 2, ..., k-1$. To do this, we first verify the base case ($P(k)$), and then assume $P(0), P(1), ..., P(k-1)$ are true. We then show that $P(k+1)$ is also true using these assumptions.

In the context of recurrence relations, strong induction can be used to prove that a solution to a linear homogeneous recurrence relation satisfies the given recurrence relation.

---

## Webinar on proofs Video• . Duration: 1 hour 9 minutes 1h 9m

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/3QJ9i/webinar-on-proofs)

This transcript appears to be a lecture or discussion on mathematics, specifically on proof methods. The content includes:

1. Direct Proof: A method of proving a statement by directly showing its truth.
2. Proof by Contrapositive: A method of proving a statement by showing that if the negation of the statement is true, then the original statement must be false.
3. Proof by Contradiction: A method of proving a statement by assuming the negation of the statement and showing that this assumption leads to a contradiction.

The main topic of the lecture is proof methods in mathematics, and it appears to cover various techniques used to prove statements. The examples given include direct proofs, contrapositive proofs, and proof by contradiction.

The lecture also touches on the concept of strong induction, which is necessary when assuming that p is false does not lead to a contradiction.

The content seems to be from an undergraduate mathematics course, possibly in a introductory algebra or discrete mathematics class. 

It's worth noting that there are two additional resources mentioned at the end: "Lesson 6.2 Recursion" and "Lesson 6.3 Extra resources". These resources may include video lectures, readings, or problems for further practice.

---

## Recursive definitions Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/IGlGA/recursive-definitions)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Recursive definitions are used to define objects, functions, sequences, and sets in discrete mathematics. A recursive definition consists of a base case and a recursive step. The base case provides an initial value or set of values for the object being defined. The recursive step defines how to derive new elements from existing ones using the same definition.

In sequences, the recursive step applies to each term based on the previous one. For example, the Fibonacci sequence is defined recursively as F(n) = F(n-1) + F(n-2). In sets, the recursive step specifies a rule for generating new elements from those already in the set.

Recursively defined functions take an integer n and compute its value using smaller integers. The base case provides the starting values. Defining a recursive function f(n) is equivalent to defining a sequence.

Recursive definitions are useful for simplifying and solving complex mathematical problems. They are crucial in both theoretical and practical applications within computer science and mathematics.

The Fibonacci sequence can be defined recursively as F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1. The set of positive integers that are multiples of 6 can also be defined recursively.

Recursion is not syllogism, but a process called recursion, where an object is defined in terms of itself. Recursively defined functions and sets provide a clear and concise way to define complex mathematical objects.

The conclusion is that understanding recursive definitions is crucial for grasping how they are used to simplify and solve complex mathematical problems. This lesson provides a foundational understanding of recursion in defining sequences and sets, which is essential in both theoretical and practical applications within computer science and mathematics.

---

## Topic 6 essential reading Reading• . Duration: 1 hour 45 minutes 1h 45m

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/L9zA7/topic-6-essential-reading)

Here is a summary of the text in 15 sentences:

The textbook by Koshy covers topics such as recursion, recursively defined functions, sets, and algorithms. The definition of recursion is discussed, which states that a function f is recursive if f(f(x)) = f(x) for all x in its domain. Recursively defined functions are functions that can be defined using other instances of the same function. There are three types of recursively defined functions: direct recursion, indirect recursion, and mixed recursion. The textbook also covers recursively defined sets, which are sets that can be defined using recursive formulas. These sets have a similar structure to the set of natural numbers, with each element being represented as a pair of smaller elements. Recursively defined algorithms are used to solve problems efficiently by breaking them down into smaller sub-problems. Examples of such algorithms include merge sort and binary search. The textbook also covers recurrence relations, which are equations that define how a sequence evolves over time. Solving recurrence relations is essential for understanding many algorithmic techniques, including dynamic programming and greedy algorithms. Recurrence relations can be solved using various methods, including substitution and iteration. In addition to these topics, the textbook provides essential reading material on recursion. The Koshy textbook includes video lessons, practice assignments, and peer-reviewed assignments to help students learn about recursion. Students are encouraged to review their peers' work and provide feedback, which helps foster a sense of community among learners. Overall, the Koshy textbook aims to provide comprehensive coverage of recursion and its applications in computer science.

Note that there is limited technical information or formulae provided in the original text, and most of it appears to be general information about a textbook's structure and content.

---

## Recursion Reading• . Duration: 1 hour 45 minutes 1h 45m

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/s8RbG/recursion)

Here is a summary of the text in 15 sentences:

The provided textbook extracts cover topics such as recursion, recursively defined functions, sets, and algorithms. These pages are located between pp.104-106 and pp.261-266 and pp.278-282 in Koshy's textbook (2004). To complete this section, attempt exercises 1-6 from p.283 in the book. The solutions to these exercises can be found at the back of the book under "Solutions to odd-numbered exercises". Consult this section if you need help with your answers. If you got an incorrect answer, review the question and try to arrive at the correct solution. There are no key concepts or technical details mentioned in the provided extracts. However, the topics covered include recursion, recursively defined functions, sets, and algorithms. The textbook also offers practice assignments for these topics, with durations ranging from 15 minutes to 30 minutes. Additionally, there are video lessons and reading materials available for each topic.

---

## Topic 6 summary Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/wMpKI/topic-6-summary)

This text does not provide a specific problem to solve, but rather appears to be a educational resource or assignment that guides students through the process of understanding different proof techniques in mathematics and computer science. If you could provide more context or clarify what specific aspect of this material you are struggling with, I would be happy to try and assist you.

If you're looking for help with a math problem, please feel free to share the problem statement, and I'll do my best to guide you through the solution process step-by-step.

---

## Proofs problem sheet Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/wmbPT/proofs-problem-sheet)

Lesson 6.2 Recursion Lesson 6.3 Extra resources Video: Video Webinar on proofs . Duration: 1 hour 9 minutes 1h 9m Reading: Reading Proofs problem sheet . Duration: 10 minutes 10 min Reading: Reading Proofs problem sheet solution . Duration: 10 minutes 10 min

---

## Proofs problem sheet solution Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/LcseB/proofs-problem-sheet-solution)

Lesson 6.2 Recursion Lesson 6.3 Extra resources Video: Video Webinar on proofs . Duration: 1 hour 9 minutes 1h 9m Reading: Reading Proofs problem sheet . Duration: 10 minutes 10 min Reading: Reading Proofs problem sheet solution . Duration: 10 minutes 10 min Proofs problem sheet solution topic-6-proofs-sol.pdf PDF File Mark as completed Dislike Report an issue

---

