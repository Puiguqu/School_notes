# Binary search is optimal Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/u8Our/binary-search-is-optimal)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The binary search algorithm is considered optimal for searching in an array or vector, assuming no prior knowledge of the stored data. This is proved using the random-access machine model, where the focus is on the control unit's implementation of the algorithm. The basic operations (addition) are ignored, while decisions with two possible outcomes (0 and 1) are considered. The algorithm can be represented as a tree-like structure, where each decision node corresponds to a bit string tracing the path through the computation. There are n+1 possible outputs, and the number of time-steps (T) must be at least the length of the bit string describing the steps in the computation. Using the pigeonhole principle, it can be shown that 2^T ≥ n+1, which implies T = O(log n). This result proves that binary search is optimal, as it achieves a worst-case complexity of O(log n), which is already achievable by the algorithm. The use of abstraction and mathematical modeling in this proof highlights the interplay between computer science and mathematics.

