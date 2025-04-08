# Quick sort Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/yPkzK/quick-sort)

Here is a summary of the text in 8 sentences, preserving key information:

The Partition algorithm is used in the Quick Sort algorithm to divide the input list into two parts, one containing elements smaller than the pivot and the other containing elements greater than the pivot. The first element of the list is chosen as the pivot. Two indices, i and j, are defined: i starts from the beginning of the list and moves to the right to find the first element greater than the pivot, while j starts at the last element and moves towards the left to find the first element smaller than the pivot. The two elements at indices i and j are swapped if i is less than j. This process continues until i is no longer less than j, indicating that the pivot has been placed in its correct position. The partition algorithm returns j as the position of the pivot in the list, allowing for sorting to occur without moving the pivot. This algorithm can be used iteratively or recursively, with iterative versions being more efficient in practice. By using the Partition algorithm, Quick Sort is able to sort a list in O(n log n) time complexity.

