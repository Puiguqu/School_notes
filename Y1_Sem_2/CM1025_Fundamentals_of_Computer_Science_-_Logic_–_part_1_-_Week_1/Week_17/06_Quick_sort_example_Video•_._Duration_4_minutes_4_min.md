# Quick sort example Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/ovHOD/quick-sort-example)

Here is a summary of the text in 8 sentences, preserving key information:

Quicksort is a recursive sorting algorithm that uses the partition algorithm to divide the list into two smaller sub-lists. The algorithm works by selecting a pivot element from the list, partitioning the other elements around it, and recursively sorting the left and right sub-lists. If the list has one or zero elements, it is already sorted, so the algorithm returns immediately. Otherwise, the partition function is called to determine the pivot position, and the algorithm recursively sorts the left and right sub-lists. The Quicksort algorithm is implemented as `Quick_Sort(List)` where `List` is the input list, `n` is its length, and `j` is the index returned by the `Partition` function. The algorithm uses a recursive approach to sort the list, with the base case being an empty or single-element list. In an example walk-through, the Quicksort algorithm is applied to the list `[3, 6, 2, 7, 1, 4, 5]`, resulting in a sorted list `[1, 2, 3, 4, 5, 6, 7]`. The Quicksort algorithm has a time complexity of O(n log n) on average, but can be O(n^2) in the worst case if the pivot is chosen poorly.

