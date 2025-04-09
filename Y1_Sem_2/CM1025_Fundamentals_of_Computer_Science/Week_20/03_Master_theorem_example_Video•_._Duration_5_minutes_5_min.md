# Master theorem example Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/PYqGC/master-theorem-example)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The video transcript discusses the application of master theorem to find time complexity of recursive algorithms. The first example is binary search, with a recursion relation T(n) = T(n/2) + 1, resulting in O(log n). Another algorithm to sum up all elements has a recursion relation T(n) = 2T(n/2) + 1, leading to O(n). A recursive function Find_max to find the largest element in an unsorted list also has a time complexity of O(n), as shown by the equation T(n) = 2T(n/2) + 1. The master theorem is applied to another recursive function f(n), with T(n) = T(n/2) + n, resulting in O(n^d). Since d > log2(1), the time complexity is O(n^d), and as d = 1, the final answer is O(n). Additionally, videos on master theorem example, efficiency of quicksort and mergesort, and reading materials on solving recurrences are listed.

