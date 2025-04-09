# Efficiency – merge sort Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/SSaWD/efficiency-merge-sort)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The merge sort algorithm splits a list of integers into two halves until each sublist contains one item. The time complexity of merge sort is of interest because its worst-case and best-case time complexities have the same asymptotic bound. In the best case, where the input list is already sorted, the dividing step takes constant time, and each level of merging takes O(n) time. Overall, this results in a time complexity of O(n log n). However, in the average case, when the input list has more than one element, merge sort recursively sorts the first half and the second half separately. The base case for merge sort is when the input list has only one element, in which case it returns the list immediately with constant time complexity. For merging two sorted lists, the time complexity is O(n), where n is the number of elements in the merged list. Using the master theorem, we can determine that the time complexity of merge sort is O(n log n).

