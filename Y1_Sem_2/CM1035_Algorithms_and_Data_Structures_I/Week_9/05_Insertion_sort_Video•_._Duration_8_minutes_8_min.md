# Insertion sort Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/qyL1L/insertion-sort)

The insertion sort algorithm is a simple and efficient sorting technique that works by iterating through an array or vector one element at a time, inserting each element into its proper position within the sorted portion of the array. The algorithm compares each element to all previous elements and shifts them forward until it finds the correct position for the new element.

The key concept behind insertion sort is that once an element has been inserted into its correct position, all subsequent elements in the array will be sorted without further comparisons. This property allows the algorithm to terminate early when no more swaps are needed, making it less efficient than bubble sort in some cases.

The pseudocode for insertion sort can be summarized as follows:

1. Start at the second element of the array.
2. Compare each element with all previous elements and shift them forward until it finds the correct position for the new element.
3. Repeat step 2 until the end of the array is reached.

In terms of its implementation, insertion sort can be easily adapted to work on arrays, vectors, or dynamic arrays. The main difference between these implementations is the way in which elements are accessed and manipulated.

The algorithm's time complexity is O(n^2) in the worst case, although it can be improved to O(n) in the best case when the input array is already sorted.

Insertion sort has several advantages over bubble sort, including:

* It does not require any additional space for an auxiliary array.
* It only requires a single pass through the data, whereas bubble sort may require multiple passes.
* It is generally faster than bubble sort for nearly-sorted or partially-sorted data.

However, insertion sort also has some disadvantages, such as:

* It can be slower than bubble sort for very large datasets due to its overhead in shifting elements.
* It requires more memory accesses than bubble sort in some cases.

Overall, insertion sort is a simple and efficient sorting algorithm that is well-suited for many applications, particularly those with relatively small datasets.

