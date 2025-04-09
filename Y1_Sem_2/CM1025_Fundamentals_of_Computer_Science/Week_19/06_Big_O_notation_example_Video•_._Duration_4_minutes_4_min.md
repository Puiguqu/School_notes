# Big O notation example Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/HqHbV/big-o-notation-example)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The video transcript discusses big O notation, focusing on examples that prove functions are bounded above by other functions. The first example proves that f(n) = 10n + log2^n ≤ cgn for all n ≥ n0, where c is 11 and g(n) = n. This is done by selecting a witness value for c that holds true for sufficiently large values of n. A second example attempts to prove that f(n) = 5n + 2^n ≤ c(gn), but fails with c = 2 due to the function 2^n growing faster than 5n. To determine if one function is O another, a table can be used to compare their growth rates. The table shows examples of pairs of functions where f is greater than or equal to g, and those where g is greater than or equal to f. In general, f is O(g) if g grows slower than f. Asymptotic analysis is necessary because it allows us to understand the performance of algorithms as input sizes grow, which is crucial in computer science.

