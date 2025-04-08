# Worst-case time complexity Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/Mh8XT/worst-case-time-complexity)

The text discusses the concept of worst-case time complexity in algorithms, which refers to the maximum number of operations required by an algorithm for a given input size.

To analyze an algorithm's time complexity, it is essential to consider the worst-case scenario, where the input size is maximal. For example, in linear search, the worst-case input is when the target value is not present in the array or vector, requiring the inspection of all n elements.

Bubble sort has a best-case time complexity of O(n), as only one pass is needed to sort an already sorted array. However, the worst-case scenario occurs when the array is sorted with the largest value first and the smallest value last, requiring n-1 passes, each with O(n) operations, resulting in a worst-case time complexity of O(n^2).

Similarly, insertion sort also has a worst-case time complexity of O(n^2), as it requires n-1 passes to sort an array.

The key takeaway is that analyzing worst-case time complexity helps identify the maximum resources required by an algorithm for a given input size. This understanding enables developers to choose the most efficient algorithms for specific problems.

Note: There are no formulas, links, or technical details in this summary as it is focused on preserving the main concepts and findings of the text.

