# NP problems and searching Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/AGolo/np-problems-and-searching)

Here is a summary of the text in 8 sentences, preserving all key information, formulae, links, and technical details:

NP-complete problems are those that are computationally challenging to solve exactly, but can be solved approximately using search algorithms. One approach to solving NP-complete problems is to enumerate all possible proofs or candidate solutions and check them one at a time to see if they can result in acceptance of the input. This approach requires trying an exponentially large number of possibilities, making it impractical for large inputs. However, by using binary search, which has worst-case time complexity O(log n), we can reduce the number of attempts required to find a solution. Another approach is backtracking, where we start with an initial guess and iteratively update our solution based on whether it leads to a valid or invalid result. Backtracking involves pushing values onto a stack and popping them off when necessary, allowing us to backtrack and try alternative solutions. This approach has been shown to be effective for solving certain NP-complete problems, such as Sudoku puzzles. By understanding these approaches and how they can be used to solve hard problems, we can develop new algorithms and techniques that may lead to more efficient solutions.

