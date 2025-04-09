# Week 19 - CM1035 Algorithms and Data Structures I - Problems, algorithms and flowcharts, Part 1 - Week 1

## Solution to Sudoku problem Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/0gQ7c/solution-to-sudoku-problem)

Here is a summary of the text in 8 sentences, preserving key information, formulae, and technical details:

The original solution method for solving Sudoku puzzles generates candidate solutions as vectors of numbers for blank entries, resulting in 4^B possible candidates, where B is the number of blank entries. To improve this approach, the problem can be restricted by analyzing allowed values for each row and column. By looking at the numbers that appear in each row and column, the set of allowed values for each entry can be determined, reducing the number of candidates to generate. This approach still results in an exponential increase in possible candidates, with the number of generated candidates being greater than 2^B for B blank entries. Further improvement can be achieved by analyzing smaller square grids within the puzzle and constructing candidate solutions from allowed numbers. However, even this approach does not guarantee a polynomial time complexity in the number of blank entries (n) and the size of the grid (m), as the problem remains related to the famous question of whether P=NP. The study of computational complexity and algorithms is crucial to solving Sudoku puzzles, with the solution being connected to the question of whether P=NP, a fundamental problem in mathematics. In 2002, the Clay Mathematics Institute offered a $1 million prize for a proof or counterexample regarding the relationship between P and NP.

Note that I had to make some compromises on formatting and technical details to condense the text into 8 sentences while preserving key information.

---

## Introduction to Topic 10 Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/Jtabo/introduction-to-topic-10)

Here is a summary of the text in 8 sentences, preserving key information and concepts:

The binary search algorithm is considered optimal, with a worst-case time complexity of O(log n), making it nearly impossible to find an algorithm that can solve a problem faster. The study of algorithms' limits and possibilities can be abstracted at a theoretical level, allowing for discussions on the feasibility of solving certain problems efficiently. Computational complexity theory groups problems into classes based on the type of machine required and resources available. This field operates at a mathematical and theoretical level, yet provides insights into why it's difficult to find efficient solutions for some problems. The halting problem, which asks whether a computer program will halt given unlimited memory, was shown by Alan Turing to be unsolvable in general. However, many other problems have been solved using specific algorithms, and the focus of this topic is on understanding how hard these problems are to solve with any possible algorithm. Computational complexity classes are defined based on decision problems, including P (Polynomial Time) and NP (Nondeterministic Polynomial), which are related through concepts like NP completeness. The study of computational complexity also includes generic methods for solving NP-complete problems and alternative forms of computing that provide new perspectives on the P vs. NP problem.

Note: I did not include any links or technical details, as they were not present in the original text.

---

## Introduction to complexity classes Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/pc7Lr/introduction-to-complexity-classes)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

Computational complexity studies the resources required to solve problems, with time complexity being a crucial aspect. In worst-case scenarios, algorithms with polynomial time complexity (e.g., O(n^2)) are preferred over those with exponential time complexity (e.g., O(2^n)). This is because exponential functions grow faster than polynomial functions, and asymptotically, polynomial functions dominate exponential ones. The goal of computational complexity is to classify problems into classes based on their solvability using efficient algorithms. A standard method for analyzing time complexity is to consider the size of the input, which is typically represented as a fixed-size array of bits. Complexity classes are sets of problems that can be solved with a particular set of resources, such as memory units storing single bits. The RAM model of computation is commonly used to analyze time complexity, where memory units store only a bit or nothing. Complexity classes like P and NP represent sets of problems that can be solved efficiently, but their boundaries are not always clear-cut, requiring careful analysis and discussion.

Note: I have omitted some technical details and links as they were not essential to the main points of the summary.

---

## Decision problems Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/U1xmR/decision-problems)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

A decision problem is a type of computational problem where there are two possible answers, such as true or false, accept or reject, or incorrect or correct. The output of a decision problem is binary, allowing it to be formally defined as a set of inputs that are accepted because they share a common property. A language is a collection of words or strings that can be defined using a decision problem. For example, the 26 letters in the English language can be combined in all sorts of ways, but not all combinations will form valid words. In computer science, a computational machine plays the role of a dictionary, deciding which words belong to a language and which ones do not. The problem of determining whether an integer is a perfect square is a decision problem because its answer is true or false. Two methods exist to solve this problem: one involves computing the square root and checking if it's an integer, with a worst-case time complexity of O(log n), while the other involves iterating over all squares of integers up to n, resulting in a worse worst-case time complexity of √n for large inputs. The decision problem of determining whether an integer is a perfect square belongs to the set of problems that can be decided by a machine with linear time complexity.

---

## Particular complexity classes Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/ptVkQ/particular-complexity-classes)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The decision problem is a fundamental concept in computational complexity, where an input is considered to belong to a language if it satisfies a certain property. Complexity classes are sets of languages that can be decided by algorithms with specific time complexities. The RAM model of computation allows for linear search on arrays and counting the number of appearances of a bit value, resulting in a linear time complexity of O(S). This problem is an example of a language that can be solved efficiently, as it falls within the complexity class P, which consists of languages solvable by algorithms with worst-case time complexity at most polynomial in the size of the input. Another example in P includes deciding if a number is prime or not, and solving Sudoku puzzles. In contrast, EXP (Exponential Time) is a set of languages that can be decided by algorithms with worst-case time complexity at most exponential in the size of the input. The containment of P within EXP was proven, and EXP contains many hard problems such as determining winning strategies in games like Go or checkers. This sets the stage for discussing the complexity class NP (Nondeterministic Polynomial Time), which is the other half of the question of whether P equals NP.

---

## NP Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/cNgpI/np)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

NP (Nondeterministic Polynomial time) is a complexity class that includes decision problems where an algorithm can verify a solution of polynomial size in less than exponential time. The problem of determining whether a Sudoku puzzle has a solution is NP-complete, which means it is both in NP and NP-hard. A problem is NP-hard if solving it requires solving another NP-complete problem. NP differs from P (Polynomial time) in that it allows for the use of proofs to verify solutions. In the RAM model, an algorithm can decide a language in NP if given access to a proof of polynomial size. NP contains P, but without the bit about proofs. The hardest problems inside the class NP are called NP-complete problems.

---

## Optional further reading: NP-Completeness Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/supplement/UTihf/optional-further-reading-np-completeness)

There is no text provided to summarize. The text appears to be a message from an educational platform or website, recommending additional reading materials and resources for learning about computational complexity and NP-completeness. It provides a link to access these resources through the Online Library or E-Book Central (ProQuest). There are also references to specific video lectures, practice assignments, and optional further reading materials. However, there is no key information, formulae, links, or technical details provided in the text that need summarization.

---

## Revision exercises Reading• . Duration: 3 hours 30 minutes 3h 30m

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/supplement/IXkgh/revision-exercises)

Here is a summary of the text in 8 sentences:

A file called Revision.pdf is attached to this message, containing exam-like questions that test various aspects of the course. These questions are an expanded form of the actual exam and provide an idea of the types of equations that will be asked. The purpose of these questions is to help students prepare for the exam by attempting solutions. Solutions to the questions will be revealed in next week's activities. The Revision.pdf file covers Lesson 10, specifically introducing computational complexity and specific complexity classes such as P and EXP, NP, and NP-Completeness. Practice assignments are included, with a duration of 5 minutes for each. Students can find additional resources, including videos, readings, and optional further reading on NP-Completeness. The revision exercises will last for 3 hours and 30 minutes, allowing students to work on the questions attached to Revision.pdf.

---

