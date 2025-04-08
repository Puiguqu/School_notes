# NP Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/cNgpI/np)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The problem of determining whether an X squared by X squared Sudoku puzzle has a solution can be solved using an algorithm with worst-case time complexity exponential in the size of the input, but if a candidate solution is given, deciding whether it is valid is a problem in NP (Nondeterministic Polynomial). This class NP captures problems where solutions to other problems can be checked efficiently. NP is defined as the set of languages that can be decided by an algorithm with access to a proof of polynomial size. The class NP differs from P (Polynomial) in that it allows for the use of proofs, whereas P only requires a finite number of steps. All problems in P are also in NP, but NP contains additional complexity due to the ability to use proofs. NP is also contained in EXP (Exponential), as checking all possible proofs can be done in exponential time. The notion of NP hardness introduces problems that are as hard as any other problem in NP, and NP complete problems are those that are both NP-Hard and in the class NP. Currently, many problems have been shown to be NP complete, including determining whether a Sudoku puzzle has a solution, which would require an efficient algorithm to solve if it existed.

