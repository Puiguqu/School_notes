# Recursive algorithms example Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/tdXMx/recursive-algorithms-example)

Here is a summary of the text in 8 sentences, preserving key information:

Recursive trees are a way to trace recursive algorithms. The given function F takes an integer as input, returning 2^m if m is one, 1 if m is zero, and 2*F(m-1) otherwise. To find the value of F(5), a tree is built with the root F(5), then children are added for each recursive call, such as F(4), which calls F(3), which calls F(2), which calls F(1). The result of each call is calculated and returned, ultimately resulting in F(5) = 32. Another function G takes two parameters, a and n, returning a if n is one, 1 if n is zero, and calling itself twice with different parameters otherwise. A recursive tree is built for G(2,5), then the results of each child are multiplied to get the final result, which is 32. The function G calculates and returns a^n. Recursive algorithms can be visualized using recursive trees, providing insight into how they work and how to solve problems involving them.

Note: I have omitted some technical details such as formulas, links, and specific code examples not present in the original text.

