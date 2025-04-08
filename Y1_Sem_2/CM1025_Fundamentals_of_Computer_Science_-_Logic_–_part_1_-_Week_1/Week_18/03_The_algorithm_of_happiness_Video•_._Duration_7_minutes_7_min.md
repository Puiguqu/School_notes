# The algorithm of happiness Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/G0ZeI/the-algorithm-of-happiness)

The Gale-Shapley algorithm is a well-known algorithm for stable matching problems, also known as the algorithm of happiness. It was developed by Lloyd Shapley and Alvin Roth, who won the 2012 Nobel Prize in Economics together. The algorithm's goal is to pair hospitals and medical students such that no unstable pair exists.

In this problem, there are n hospitals and n medical students, each with a list of preferences for the other party. A stable match is one where no hospital prefers a student from another hospital, and no student prefers a hospital that already has them assigned to it. The algorithm's objective is to find a perfect matching, where every hospital and student are paired.

The Gale-Shapley algorithm works as follows:

1. Each unmatched hospital offers the top-ranked student on its list.
2. Students with one offer accept the offer.
3. Students with more than one offer accept the highest-ranked hospital that made them an offer.
4. Repeat steps 1-3 until all hospitals are matched.

In the given example, the algorithm produces a stable match where Whittington is paired with Mohammed, UCLH is paired with Elena, and Royal Free is paired with Sara.

The stability of the algorithm can be proven using the concept of unstable pairs. An unstable pair exists when a student prefers a hospital that already has them assigned to it, and the hospital prefers the student. The Gale-Shapley algorithm ensures that no such pair exists in the resulting match.

The time complexity of the algorithm is O(n^2), where n is the number of hospitals and students. This makes it efficient for solving large-scale matching problems.

In conclusion, the Gale-Shapley algorithm is a powerful tool for stable matching problems, offering a systematic approach to pairing individuals based on their preferences. Its stability guarantee and efficiency make it an essential algorithm in various fields, including economics, computer science, and operations research.

