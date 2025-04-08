# Efficiency – merge sort Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/SSaWD/efficiency-merge-sort)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The merge sort algorithm splits a list of integers into two halves until each sublist contains only one item, then merges them level by level. The time complexity of merge sort has the same asymptotic bound for its worst-case and best-case scenarios. In the best case, where the list is already sorted, the algorithm spends O(n log n) time, which is worse than other sorting algorithms like bubble sort or insertion sort. However, in the average case, the algorithm's time complexity is still O(n log n), as it splits the list into two halves and merges them recursively. The master theorem is used to analyze the recurrence relation of merge sort, which has a value of d = 1 for its best-case scenario. Using the master theorem, we can conclude that T(n) is proportional to n times log n. Specifically, if the input list has one element, it returns immediately (O(1) time), and otherwise, it recursively sorts the first half and second half of the list before merging them, resulting in a total time complexity of O(n log n). The average case time complexity of merge sort is indeed O(n log n), making it suitable for large datasets.

