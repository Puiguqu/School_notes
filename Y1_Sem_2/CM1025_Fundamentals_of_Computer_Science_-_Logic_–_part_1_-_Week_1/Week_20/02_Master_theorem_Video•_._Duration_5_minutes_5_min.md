# Master theorem Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/SMAjd/master-theorem)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The Master Theorem is a solution to find the time complexity of recursive relations without building recursion trees. It states that if T(n) = aT(n/b) + f(n), where a, b, and f are constants, then the relationship between d (the degree of the recurrence) and log_a(b) can determine the final form of T(n). If d < log_a(b), then T(n) is O(f(n)), if d = log_a(b), then T(n) is Θ(f(n) * n^d), and if d > log_a(b), then T(n) is Ω(f(n)^d). The Master Theorem can be applied to solve three common types of recursive relations: those with a constant recurrence (T(n) = cT(n/2)), those with a logarithmic recurrence (T(n) = T(n/2) + O(log n)), and those with a polynomial recurrence (T(n) = T(n/2) + O(n^d)). The theorem has been demonstrated through several examples, including cases where d is less than, equal to, or greater than log_a(b). In each case, the theorem provides a clear formula for determining the time complexity of the recursive relation. By using the Master Theorem, one can avoid having to build recursion trees and guess the solution, making it a useful tool for analyzing recursive relations. Overall, the Master Theorem is a fundamental concept in algorithm analysis that helps to solve some common types of recursive relations.

