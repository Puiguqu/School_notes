# Master theorem Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/SMAjd/master-theorem)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The master theorem is a useful theory for finding time complexity of recursive relations that can't be solved using recursion trees. It provides a formula to determine the final form of T(n) based on the relationship between d and log A in base b. If d is smaller than log A in base b, then T(n) is O(log n). If d is equal to log A in base b, then T(n) is O(n^d * log n). If d is greater than log A in base b, then T(n) is O(n^d). The master theorem states that if the recurrence T(n) is 8 times T(n/2) + p of n to the power of d divided by b plus other terms, then the relationship between d and log A in base b can be used to determine the final form of t of n. For example, with a=1, B=2, and d=0, T(n) is O(log n), while with d=1, T(n) is O(n^d). The master theorem provides a simple and efficient way to analyze the time complexity of recursive relations without having to build trees or guess.

