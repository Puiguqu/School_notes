# Solution to Sudoku problem Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/0gQ7c/solution-to-sudoku-problem)

Here is a summary of the text in 8 sentences, preserving key information and concepts:

The original solution method for solving Sudoku puzzles generates candidate solutions by iterating through each blank entry and considering all possible numbers. However, this approach results in an exponential number of candidates (4^B) where B is the number of blank entries. To improve this, a more efficient approach can be used by restricting the number of candidates to generate. This can be done by analyzing rows and columns separately, eliminating possibilities that are already present in other rows or columns. By doing so, the number of candidates to generate is reduced, but it may still be exponentially large (2^B). A further improvement can be made by considering smaller square grids within the puzzle, reducing the number of candidates even more. However, even with these improvements, the number of candidates will still grow exponentially with the number of blank entries and the size of the grid. The question of whether there exists an algorithm to solve a general Sudoku puzzle with exponential time complexity that is better than O(n^m), where n is the size of the grid and m is the number of blank entries, is related to one of the millennial prize problems in computer science: P = NP.

Note: I did not include any links or technical details as they were not explicitly mentioned in the text. Also, some minor rephrasing was done to make the summary more concise and readable.

