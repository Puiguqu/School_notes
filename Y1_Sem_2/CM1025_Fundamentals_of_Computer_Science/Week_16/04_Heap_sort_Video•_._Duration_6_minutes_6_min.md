# Heap sort Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/9wEkL/heap-sort)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Heap sort is an algorithm for sorting a list of elements using a complete binary tree data structure. To implement heap sort, first represent the list as a complete binary tree, then heapify the tree to ensure it remains a min heap. The root of the min heap contains the smallest element in the original list, which should be removed and placed at the end of a second sorted list. Repeat this process with the remaining elements, ensuring each iteration maintains the min heap property by swapping elements as necessary. If the current element has only one child, swap it with that child to maintain the min heap property. Continue this process until all elements have been removed from the tree and added to the sorted list. Heap sort has a time complexity of O(n log n) in the worst case scenario, making it suitable for sorting large datasets. The algorithm concludes when there are no more elements left in the tree, at which point the list is fully sorted.

