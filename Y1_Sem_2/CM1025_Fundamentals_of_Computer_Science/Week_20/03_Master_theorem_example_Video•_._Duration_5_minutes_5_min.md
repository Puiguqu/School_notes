# Master theorem example Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/PYqGC/master-theorem-example)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The master theorem is used to analyze the time complexity of recursive algorithms. The first example analyzed is binary search, where the time complexity T(n) is O(log n) due to its algorithmic structure (T(n/2)+1). The next example involves a function to sum up all elements in an array, with a recursion relation T(n) = 2T(n/2) + 1, resulting in a time complexity of O(n^log_b(a)), where 'b' is the base and 'a' is the element being summed. A third algorithm finds the largest element in an unsorted list recursively, leading to a time complexity of O(n). The master theorem is applied to these examples with specific values for 'a', 'b', and 'd' (base, exponent, and logarithmic part), yielding consistent results. In one of the examples, a loop with a time complexity of O(n) is added to the recursion, leading to an overall time complexity of O(n^d). The master theorem is also used in another example to determine the time complexity of a function that recursively calls itself twice (T(n/2)) and contains a loop with time complexity O(n), resulting in an overall time complexity of O(n^d).

