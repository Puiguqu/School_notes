# Worst-case complexity of binary search Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/qerOE/worst-case-complexity-of-binary-search)

Here is a summary of the text in 8 sentences, preserving key information:

The worst-case time complexity of binary search can be determined by analyzing its operations. The best-case input for binary search is when the target value is at the midpoint of the array, resulting in a time complexity of O(1) or constant time. In contrast, if the target value is at the first element of the array, it requires multiple divisions to reach the midpoint, leading to a worst-case time complexity of O(log n). The same principle applies when the target value is next to the midpoint, requiring multiple divisions to find it. Translating this to pizza slices, we can see that binary search can accommodate log n divisions before reaching the final element. This leads to a worst-case time complexity of O(log n) for binary search on sorted arrays. However, if the array is unsorted, sorting it first using algorithms like bubble or insertion sort would increase the overall time complexity due to their O(n^2) performance. In certain cases, such as searching a dictionary multiple times, it may be more efficient to sort the data initially and use binary search for subsequent searches.

