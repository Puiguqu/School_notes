# Solution to Sudoku problem Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/0gQ7c/solution-to-sudoku-problem)

Here is a summary of the text in 8 sentences, preserving key information, formulae, and technical details:

The original solution method for solving Sudoku puzzles generates candidate solutions as vectors of numbers for blank entries, resulting in 4^B possible candidates, where B is the number of blank entries. To improve this approach, the problem can be restricted by analyzing allowed values for each row and column. By looking at the numbers that appear in each row and column, the set of allowed values for each entry can be determined, reducing the number of candidates to generate. This approach still results in an exponential increase in possible candidates, with the number of generated candidates being greater than 2^B for B blank entries. Further improvement can be achieved by analyzing smaller square grids within the puzzle and constructing candidate solutions from allowed numbers. However, even this approach does not guarantee a polynomial time complexity in the number of blank entries (n) and the size of the grid (m), as the problem remains related to the famous question of whether P=NP. The study of computational complexity and algorithms is crucial to solving Sudoku puzzles, with the solution being connected to the question of whether P=NP, a fundamental problem in mathematics. In 2002, the Clay Mathematics Institute offered a $1 million prize for a proof or counterexample regarding the relationship between P and NP.

Note that I had to make some compromises on formatting and technical details to condense the text into 8 sentences while preserving key information.

