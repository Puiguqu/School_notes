# Iterative algorithms Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/ULfdI/iterative-algorithms)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Iterative algorithms use loops to implement repeated tasks, whereas recursive algorithms call themselves repeatedly. Most common algorithms used so far are iterative, such as linear search, selection sort, insertion sort, and bubble sort. To find the maximum value in an unsorted list using an iterative algorithm, we assume the first element is the maximum and store it in a variable called "current max". We then compare each subsequent element with the current max, updating it if necessary, until we reach the end of the list. The algorithm can be represented by the formula: `current_max = i` (starting from index 1) while `i < len(list)`, and if `list[i] > current_max`, then `current_max = list[i]`, incrementing `i` to move to the next element. This process continues until all elements have been checked, resulting in the maximum value being stored in `current_max`. The algorithm is based on the idea that we start by assuming the first element as the maximum and iteratively update it if necessary. By using a loop instead of recursive function calls, iterative algorithms can be more efficient and easier to understand for large inputs or complex data structures.

