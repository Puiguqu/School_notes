# Efficiency – bubble sort and binary search Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/PrM5G/efficiency-bubble-sort-and-binary-search)

Here is a summary of the text in 8 sentences, preserving key information on algorithms and formulas:

The video transcript discusses the efficiency of two algorithms: bubble sort and binary search. Bubble sort has an average time complexity of O(n^2), where n is the number of items in the list, which makes it less efficient than other sorting algorithms. Binary search, on the other hand, has a best-case time complexity of O(log n), worst-case time complexity of O(log n), and average time complexity of approximately O(log n). The binary search algorithm works by repeatedly dividing the search space in half until the target item is found. The number of comparisons required to find an item in a list of n items can be calculated using the formula T(n) = 1 + T(n/2), which represents a recursive division of the search space. This formula can be simplified to O(log n) by recognizing that each level of recursion reduces the size of the search space by half, resulting in a logarithmic number of steps. The average time complexity of binary search is approximately log n because it assumes that each element in the list is equally likely to be the target item. Overall, binary search is more efficient than bubble sort and has better worst-case and average time complexities.

