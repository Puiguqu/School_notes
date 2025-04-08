# Week 19 - CM1035 Algorithms and Data Structures I - Problems, algorithms and flowcharts, Part 1 - Week 1

## Solution to Sudoku problem Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/0gQ7c/solution-to-sudoku-problem)

Here is a summary of the text in 8 sentences, preserving key information and concepts:

The original solution method for solving Sudoku puzzles generates candidate solutions by iterating through each blank entry and considering all possible numbers. However, this approach results in an exponential number of candidates (4^B) where B is the number of blank entries. To improve this, a more efficient approach can be used by restricting the number of candidates to generate. This can be done by analyzing rows and columns separately, eliminating possibilities that are already present in other rows or columns. By doing so, the number of candidates to generate is reduced, but it may still be exponentially large (2^B). A further improvement can be made by considering smaller square grids within the puzzle, reducing the number of candidates even more. However, even with these improvements, the number of candidates will still grow exponentially with the number of blank entries and the size of the grid. The question of whether there exists an algorithm to solve a general Sudoku puzzle with exponential time complexity that is better than O(n^m), where n is the size of the grid and m is the number of blank entries, is related to one of the millennial prize problems in computer science: P = NP.

Note: I did not include any links or technical details as they were not explicitly mentioned in the text. Also, some minor rephrasing was done to make the summary more concise and readable.

---

## Introduction to Topic 10 Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/Jtabo/introduction-to-topic-10)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The binary search algorithm is considered optimal, with a worst-case time complexity of O(log n), making it difficult to conceive of algorithms that can solve certain problems more efficiently. Computational complexity theory studies the limits of what is possible and impossible for algorithms, grouping problems into complexity classes based on the resources required. The study of computational complexity operates at a theoretical level, but provides insights into why it's challenging to find efficient solutions to certain problems. One such problem is the halting problem, which asks whether a given computer program will halt for a specific input; Alan Turing showed that this problem cannot be solved algorithmically in general. However, many other problems can be solved using particular algorithms, and computational complexity theory helps understand how hard it is to solve these problems for any possible algorithm. The concept of computational complexity classes provides a framework for classifying problems based on their resource requirements. NP completeness, which relates to the relationship between P (problems that can be solved efficiently) and NP (problems that can be verified efficiently), plays a crucial role in understanding computational complexity. Computational complexity theory also touches on generic methods for solving NP complete problems and alternative forms of computing that provide new perspectives on the problem of P versus NP.

---

## Introduction to complexity classes Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/pc7Lr/introduction-to-complexity-classes)

Here is a summary of the text in 8 sentences, preserving key information, formulae, and technical details:

The study of worst-case time complexity is crucial in computational complexity theory, where an algorithm's efficiency is measured by its time complexity relative to the size of its input. In general, exponential functions grow faster than polynomial functions, making exponential algorithms less efficient. To establish whether a problem is hard or not, researchers focus on determining if there exists an efficient algorithm (i.e., one with polynomial time complexity) that can solve it. The standard way of quantifying input size is by assuming the input is stored in an array where each element represents either a bit or nothing, making the input size equal to the number of elements in the array. The worst-case time complexity is typically computed in terms of the size of the input, and problems are grouped into classes based on the resources required to solve them. A complexity class is a set of sets, where each set represents a problem that can be solved with a particular set of resources (e.g., P for problems solvable in polynomial time). The study of computational complexity theory helps researchers understand what problems are feasible and which ones require significant advancements. By analyzing the time complexity of algorithms, researchers can determine whether a problem is part of a complexity class, such as P or NP, which represents sets of decision problems that can be solved with specific efficiency criteria.

---

## Decision problems Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/U1xmR/decision-problems)

Here is a summary of the text in 8 sentences, preserving key information and concepts:

The concept of computational complexity deals with decision problems, where a machine decides whether to accept or reject an input based on a binary output. A problem can be viewed as a set of inputs that share a common property, and languages are collections of words (inputs) that belong to a particular language. The question of what decides whether a word belongs to a language is analogous to the role of a dictionary in determining which words belong to the English language. In computer science, a computational machine plays this role. Decision problems can be rephrased as languages, such as the language of integers that are perfect squares, where the output is binary (true or false). The time complexity of solving these problems can be analyzed using different methods, such as computing the square root or iterating over all squares of integers up to a certain value. In general, the first method has a linear time complexity in the size of the input, while the second method has a worse-case time complexity on the order of the square root of an exponential in S. The problem of deciding the language of perfect squares belongs to the set of problems that can be decided by a machine and the RAM model in at most polynomial time in the size of the inputs.

---

## Particular complexity classes Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/ptVkQ/particular-complexity-classes)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The decision problem is studied in computational complexity, where input is viewed as a word belonging to a language if it's accepted due to having a certain property, or rejected. A new problem involves determining if an element appears X times in an array given a binary form of the number X. An algorithm can solve this problem in linear time using a linear search and count comparison with X, resulting in O(S) time complexity. This problem is added to the set of languages that can be solved in at most linear time in the RAM Model, along with determining if a number is a perfect square. The RAM Model allows for arbitrary integers to be stored, but limitations lead to differences in worst-case time complexity when switching models. The set of all languages solvable in at most polynomial time in the size of input is called P, and contains problems like determining prime numbers or correct Sudoku solutions. In contrast, EXP is a class of languages that can be solved in O(2^n) time complexity, containing problems such as finding a winning strategy in Go or checkers. The containment relationship between P and EXP implies that any algorithm with polynomial time complexity will have exponential time complexity, highlighting the distinction between these two classes.

---

## NP Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/cNgpI/np)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The problem of determining whether an X squared by X squared Sudoku puzzle has a solution can be solved using an algorithm with worst-case time complexity exponential in the size of the input, but if a candidate solution is given, deciding whether it is valid is a problem in NP (Nondeterministic Polynomial). This class NP captures problems where solutions to other problems can be checked efficiently. NP is defined as the set of languages that can be decided by an algorithm with access to a proof of polynomial size. The class NP differs from P (Polynomial) in that it allows for the use of proofs, whereas P only requires a finite number of steps. All problems in P are also in NP, but NP contains additional complexity due to the ability to use proofs. NP is also contained in EXP (Exponential), as checking all possible proofs can be done in exponential time. The notion of NP hardness introduces problems that are as hard as any other problem in NP, and NP complete problems are those that are both NP-Hard and in the class NP. Currently, many problems have been shown to be NP complete, including determining whether a Sudoku puzzle has a solution, which would require an efficient algorithm to solve if it existed.

---

## Optional further reading: NP-Completeness Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/supplement/UTihf/optional-further-reading-np-completeness)

There is no text provided to summarize. The given text appears to be a list of reading materials and links related to computational complexity and NP-completeness, but it does not contain any specific information or concepts to summarize.

However, I can provide a general summary of the key concepts and topics related to NP-completeness and computational complexity:

NP-completeness is a concept in computer science that refers to a class of problems that are considered to be difficult to solve exactly. It is defined as follows: Problem X is NP-complete if it can be reduced to every other problem in NP (nondeterministic polynomial time), which means that if we can solve any problem in NP, then we can also solve Problem X.

The text suggests reading the introduction to algorithms by Cormen et al., which provides an overview of NP-completeness and complexity classes. It also mentions video lectures, practice assignments, and optional readings on NP-completeness, but no specific information or findings are provided.

If you provide the actual text, I can help you summarize it in 8 sentences, preserving all key information, formulae, links, and technical details.

---

## Revision exercises Reading• . Duration: 3 hours 30 minutes 3h 30m

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/supplement/IXkgh/revision-exercises)

Unfortunately, there is no text provided for me to summarize. The text appears to be a message from a course instructor or system, providing information about upcoming revisions and practice assignments for a computer science course.

However, I can provide a summary of the key concepts and findings based on the title "Introduction to computational complexity" (Lesson 10.0) and the provided information:

The course has attached an expanded version of the exam, called Revision.pdf, which includes questions that will test various aspects of the course. This is an optional practice assignment to help students prepare for the actual exam. The revised exam will not require as many answers as this practice assignment.

Key concepts discussed in Lesson 10.1 and 10.2 include:

* Complexity classes
* NP (Nondeterministic Polynomial) complexity

Practice assignments include:

* P (Polynomial time) complexity class
* EXP (Exponential time) complexity class

Additional resources include optional readings on NP-Completeness and revision exercises that will be revealed in the next week's activities.

If you have any further questions or would like me to clarify any of the technical details, please let me know!

---

