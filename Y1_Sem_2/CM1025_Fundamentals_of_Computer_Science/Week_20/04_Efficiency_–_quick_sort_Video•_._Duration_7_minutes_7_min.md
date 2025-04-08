# Efficiency – quick sort Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/RSSUu/efficiency-quick-sort)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The quick sort algorithm is a divide-and-conquer approach that selects a pivot element from the list and partitions it into two sublists based on whether they are greater or less than the pivot. The worst-case time complexity of quick sort is O(n^2) when the pivot does not divide the list in half, resulting in n-1 comparisons becoming n*n-1/2. However, for the average case, if the pivot splits the list into two sublists of equal size, the time complexity can be reduced to O(n log n). To solve this recurrence relation, a substitution technique can be used, which leads to t(n) = 2*t(n)/2 + n, and further simplification results in t(n) = n*|log n. The best-case scenario occurs when each comparison is between two elements that are equal to the median of the list, resulting in O(n log n) time complexity. This can be proven using the master theorem, which states that t(n) = O(n^a), where a = 2 and b = 2. The master theorem can also be applied to solve other recurrence relations, and its results can be used to determine the time complexity of different algorithms. Overall, quick sort has an average-case time complexity of O(n log n), making it one of the most efficient sorting algorithms.

