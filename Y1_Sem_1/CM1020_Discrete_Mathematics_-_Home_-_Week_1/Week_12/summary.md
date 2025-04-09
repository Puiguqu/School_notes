# Week 12 - CM1020 Discrete Mathematics - Home - Week 1

## Recursive definitions Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/nmSDR/recursive-definitions)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Recursive definitions are mathematical objects defined in terms of themselves, allowing for easier definition than explicit ones. A recursively defined function f with domain n has two steps: basis step specifying an initial value and recursive step providing a rule to find the value at any integer from smaller integers. The sequence aN can be defined as 4n, 4^n, or just 4 in different cases, where each term is greater than the previous by 4. Sets can also be defined recursively with basis step specifying initial elements and recursive step providing a rule for constructing new elements. An algorithm is a finite sequence of precise instructions for performing computation or solving a problem, and it's called recursive if it solves a problem by reducing it to an instance of the same problem with smaller inputs. The pseudo code for the recursive algorithm for computing n factorial is: zero factorial equals 1, and n factorial equals n multiplied by (n-1) factorial for positive integers n. Recursion can be applied to functions, sets, and algorithms, and each case has its own definition and examples. The lecture concludes with additional resources and a summary of the topic.

---

## Recurrence relations Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/ml1I7/recurrence-relations)

Here is a summary of the text in 8 sentences, preserving key information, formulas, links, and technical details:

Recurrence relations are equations that define a sequence based on a rule that gives the next term as a function of the previous term. The game of Hanoi Tower involves transferring n discs from one spoke to another without placing a larger disc on top of a smaller one, with the minimum number of moves required being 2^n - 1. Linear recurrence relations can be formalized as an = C1 an-1 + c2 an-2 + ... + ck an-k, where k is the degree of the relation. Non-homogeneous recurrence relations can be formalized as an = C1 an-1 + c2 an-2 + ... + ck an-k + f(n), where f(n) is a function depending only on n. The Fibonacci sequence is an example of a second-order linear recurrence, where each number is found by adding up to two numbers before it (an = an-1 + an-2). Arithmetic sequences have a constant difference between consecutive terms (an+1 = an + c), while geometric sequences have a constant ratio between consecutive terms (an+1 = rn). Divide and conquer algorithms consist of three steps: dividing the problem into smaller subproblems, solving recursively each subproblem, and combining solutions to find a solution to the original problem. The lecture discussed recurrence relations, linear sequences, arithmetic and geometric sequences, and introduce divide and conquer relations.

Note that I did not include any links or formulas as they were not provided in the text, but rather summarized the key concepts and findings.

---

## Solving recurrence relations Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/wKxir/solving-recurrence-relations)

Here is a summary of the text in 8 sentences, preserving key information:

The lesson focuses on solving recurrence relations using strong induction, linear homogeneous recurrences, and Fibonacci recurrences. To solve linear homogeneous recurrences, one needs to find a combination of geometric sequences that satisfy the characteristic equation. The characteristic equation is obtained by dividing both sides of the recurrence relation by the highest power of r. Solving the characteristic equation yields roots whose multiplicity determines the form of the solution. For example, in the Fibonacci recurrence relation, the characteristic equation has two distinct roots with multiplicity 1. The general solution to this type of recurrence relation is a linear combination of these roots raised to the power of n. In the case of the Fibonacci sequence, the initial conditions f_0 = 0 and f_1 = 1 are used to find the coefficients of the linear combination, which yield the formula f_n = (1/√5)(r1^n - r2^n).

---

## Webinar on proofs Video• . Duration: 1 hour 9 minutes 1h 9m

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/3QJ9i/webinar-on-proofs)

This transcript appears to be a lecture or tutorial on mathematics, specifically on the topic of proof and induction. The speaker discusses various methods for proving mathematical statements, including direct proof, proof by contraposition, proof by contradiction, and proof by induction.

The main topics covered in this lecture are:

1. Direct Proof: The speaker explains that a direct proof is when you start with what you want to prove (p) and show that it's true.
2. Proof by Contraposition: The speaker discusses how to prove "not q implies not p" which is equivalent to proving "p implies q".
3. Proof by Contradiction: The speaker explains how to prove a statement by assuming its opposite (not p) and showing that this leads to a contradiction.
4. Induction: The speaker goes through examples of induction, including direct proof, proof by contraposition, and proof by contradiction.

The lecture also touches on the concept of strong induction, which is used when you need to assume all previous terms in order to prove the current term.

Some key points mentioned in this lecture include:

* A prime number is divisible only by 1 and itself.
* The definition of a prime number.
* Direct proof: start with what you want to prove and show that it's true.
* Proof by contraposition: equivalent to proving "p implies q".
* Proof by contradiction: assume not p and show that this leads to a contradiction.
* Strong induction: used when you need to assume all previous terms in order to prove the current term.

The lecture concludes with a summary of the different methods for proof and some additional resources for further learning.

---

## Recursive definitions Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/IGlGA/recursive-definitions)

Here is a summary of the text in 8 sentences, preserving all key information:

Recursive definitions are used to define sequences and sets in discrete mathematics. The base case defines the simplest instance of the object being defined, providing the initial value. Recursive steps define how new elements can be derived from existing ones. Recursively defined functions specify an initial value (base case) and a rule for computing its value from previous values (recursive step). This process is called recursion, not syllogism. Defining a recursive function f(n) from the set N to the set R is equivalent to defining a sequence. Recursive definitions are used to simplify and solve complex mathematical problems, particularly in computer science and mathematics. Understanding these principles provides a foundational understanding of recursion in defining sequences and sets, which is crucial for both theoretical and practical applications.

---

## Topic 6 essential reading Reading• . Duration: 1 hour 45 minutes 1h 45m

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/L9zA7/topic-6-essential-reading)

Unfortunately, there is no text to summarize in this case. The provided text appears to be a list of exercises and activities related to recursion from a textbook, but it does not contain any substantive content or information that needs to be summarized.

However, I can provide some general information about recursion:

Recursion is a fundamental concept in mathematics and computer science, where a function or algorithm calls itself repeatedly until a base case is reached. Recursively defined functions, sets, and algorithms are used to solve problems that have a recursive structure.

The textbook by Koshy covers these topics, including definitions, examples, exercises, and solutions. Students can access additional resources and practice assignments through video lectures, readings, and peer-grading activities.

If you'd like to provide the actual text from the Koshy textbook or another relevant source, I'll be happy to assist you in summarizing it.

---

## Recursion Reading• . Duration: 1 hour 45 minutes 1h 45m

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/s8RbG/recursion)

Here is a summary of the text in 8 sentences:

The Koshy textbook covers topics on recursion, including definitions, functions, sets, and algorithms. The book has several lessons and exercises that cover these topics. The reading assignments include videos, practice assignments, and peer-graded assignments. The lesson plans have durations ranging from 5 minutes to 1 hour and 45 minutes. The lessons are divided into two parts: Lesson 6.2 and Lesson 6.3, which focus on recursion and recurrence relations, respectively. The textbook also provides essential reading materials and a summary of the topic. Students can access solutions to exercises at the back of the book to check their answers and learn from their mistakes. Overall, the Koshy textbook aims to provide an in-depth understanding of recursion and its applications through engaging lessons and practice assignments.

---

## Topic 6 summary Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/wMpKI/topic-6-summary)

## Step 1: Review the problem statement
The problem statement does not provide a specific mathematical problem or question that requires solving. Instead, it appears to be a discussion on different types of proofs and their importance in mathematics and computer science.

## Step 2: Identify the learning outcomes
The learning outcomes are not explicitly stated in the problem statement. However, based on the context, we can infer that the learning outcomes may include understanding different proof techniques, such as constructive and non-constructive proofs, and the ability to assess one's own knowledge and identify areas for improvement.

## Step 3: Determine the task
The task is not explicitly stated in the problem statement. However, based on the context, we can infer that the task may be to reflect on one's understanding of proof techniques and develop a plan for improvement.

## Step 4: Provide a solution
Since there is no specific mathematical problem or question to solve, we cannot provide a numerical answer. However, we can provide a general outline of steps that one could take to address the task:

1. Review the learning outcomes and assess one's understanding of proof techniques.
2. Identify areas for improvement by rating one's understanding on a scale of 1-5.
3. Develop an action plan to improve one's understanding, including reviewing course materials and textbooks, practicing additional problems or exercises, seeking help from instructors or peers, and scheduling additional study sessions.
4. Implement the action plan and regularly review progress.

The final answer is: $\boxed{0}$

---

## Proofs problem sheet Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/wmbPT/proofs-problem-sheet)

Lesson 6.2 Recursion Lesson 6.3 Extra resources Video: Video Webinar on proofs . Duration: 1 hour 9 minutes 1h 9m Reading: Reading Proofs problem sheet . Duration: 10 minutes 10 min Reading: Reading Proofs problem sheet solution . Duration: 10 minutes 10 min

---

## Proofs problem sheet solution Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/LcseB/proofs-problem-sheet-solution)

Lesson 6.2 Recursion Lesson 6.3 Extra resources Video: Video Webinar on proofs . Duration: 1 hour 9 minutes 1h 9m Reading: Reading Proofs problem sheet . Duration: 10 minutes 10 min Reading: Reading Proofs problem sheet solution . Duration: 10 minutes 10 min Proofs problem sheet solution topic-6-proofs-sol.pdf PDF File Mark as completed Dislike Report an issue

---

