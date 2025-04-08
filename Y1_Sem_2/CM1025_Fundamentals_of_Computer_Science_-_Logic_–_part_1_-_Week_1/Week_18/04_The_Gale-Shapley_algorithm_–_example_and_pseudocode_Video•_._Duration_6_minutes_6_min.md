# The Gale-Shapley algorithm – example and pseudocode Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/9dueE/the-gale-shapley-algorithm-example-and-pseudocode)

Here is a summary of the text in 8 sentences, preserving key information:

The Gale-Shapley algorithm is used to solve stable matching problems, where every hospital and student has preferences and restrictions. The algorithm terminates when all hospitals are matched, returning a set of pairs (hospitals, students). To prove that the algorithm is correct, it must first show that it terminates within at most n^2 rounds, where n is the number of hospitals. Then, it proves that every hospital appears in the match at least once and at most once, or exactly once. The algorithm ensures a perfect match by preventing unstable pairs, where both parties prefer each other over their current match. To prove stability, the algorithm assumes an unstable pair (h, s) exists, but shows that this leads to contradictions, such as the student's preference rank being higher than the hospital's, or the hospital preferring another student with a lower rank. The Gale-Shapley algorithm has been proven to solve any stable matching problem, including variations with unequal numbers of hospitals and students, restrictions on students, multiple vacancies in hospitals, and couples who need to match together.

