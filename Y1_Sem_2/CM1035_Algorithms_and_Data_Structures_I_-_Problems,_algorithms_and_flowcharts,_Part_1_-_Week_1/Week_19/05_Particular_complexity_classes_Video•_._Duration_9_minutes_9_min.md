# Particular complexity classes Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/ptVkQ/particular-complexity-classes)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The decision problem is studied in computational complexity, where input is viewed as a word belonging to a language if it's accepted due to having a certain property, or rejected. A new problem involves determining if an element appears X times in an array given a binary form of the number X. An algorithm can solve this problem in linear time using a linear search and count comparison with X, resulting in O(S) time complexity. This problem is added to the set of languages that can be solved in at most linear time in the RAM Model, along with determining if a number is a perfect square. The RAM Model allows for arbitrary integers to be stored, but limitations lead to differences in worst-case time complexity when switching models. The set of all languages solvable in at most polynomial time in the size of input is called P, and contains problems like determining prime numbers or correct Sudoku solutions. In contrast, EXP is a class of languages that can be solved in O(2^n) time complexity, containing problems such as finding a winning strategy in Go or checkers. The containment relationship between P and EXP implies that any algorithm with polynomial time complexity will have exponential time complexity, highlighting the distinction between these two classes.

