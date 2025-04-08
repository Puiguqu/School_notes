# 

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/iKLUl/the-powerset-of-a-set)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A power set of a set S is defined as the set whose elements are all the subsets of S. The cardinality of a power set P(S) is equal to 2 raised to the power of the cardinality of S. For example, given a set A with two elements, {a} and {b}, its power set P(A) contains all possible subsets, including the empty set and individual elements.

The elements of a power set are all subsets of S. Therefore, the empty set is an element of a power set, and it is also a subset of any set. The cardinality of a power set of a set with n elements is 2^n.

To find the power set of a given set, we can list all possible subsets or use the rule of inclusion. For example, if S = {1, 2}, its power set P(S) contains 4 subsets: {}, {1}, {2}, and {1, 2}.

The cardinality of a power set is equal to 2 raised to the power of the cardinality of the original set. This means that the number of possible subsets grows exponentially with the size of the original set.

In general, if A is a set containing n elements, then P(A) contains 2^n subsets. If we apply this process again to find the power set of P(A), we get P(P(A)) with 2^(2^n) subsets.

This process can be repeated indefinitely, resulting in an infinite number of power sets. However, the cardinality of each subsequent power set remains a power of 2.

Overall, the concept of a power set provides a way to systematically generate all possible subsets of a given set and understand their relationships with each other.

The relationship between the cardinality of a set S and its corresponding power set P(S) is well-defined: |P(S)| = 2^|S|.

