# The algorithm of happiness Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/G0ZeI/the-algorithm-of-happiness)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The Gale-Shapley algorithm, also known as the algorithm of happiness, is a well-known algorithm for solving stable matching problems in game theory and economics. The algorithm was developed by Lloyd Shapley and Alvin Roth, who won the 2012 Nobel Prize in Economics for their work on the theory of stable allocations and market design. In this problem, there are n hospitals and n medical students, each with a list of preferences for the other group. The goal is to pair the hospitals and students such that no unstable pair exists, where an unstable pair occurs when a student prefers one hospital to another and the hospital prefers the student back. The Gale-Shapley algorithm works as follows: each unmatched hospital offers a place to a student on top of its list, and students with one offer accept the offer; students with more than one offer choose the top hospital that made them an offer. In the example given, the algorithm matches Mohammed with Whittington, Elena with UCLH, and Sara with Royal Free, but this match is unstable because Elena prefers UCLH to her current hospital, Royal Free. To prove that the Gale-Shapley algorithm always works, we need to show that it produces a stable matching and that every student and hospital appears in at least one pair of the match. The size of the match is equal to the size of the set of hospitals and students, which means that all students and hospitals are paired.

Note: I have omitted some technical details and formulae to make the summary more concise, but the key information and concepts are preserved.

