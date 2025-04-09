# The Gale-Shapley algorithm – example and pseudocode Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/9dueE/the-gale-shapley-algorithm-example-and-pseudocode)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The Gale-Shapley algorithm is used to solve stable matching problems, where each hospital offers a student a place on their list, and the student accepts the best offer. The algorithm terminates when there are no unmatched hospitals, and it returns a set of pairs (m) representing the matches. To prove that the algorithm is correct, we show that it terminates within at most n^2 rounds, where n is the number of hospitals. We then prove that every hospital appears in the match exactly once, which makes the proof more complicated. To prove that there are no unstable pairs, we assume the opposite and show that this leads to a contradiction, using two scenarios: when students reject offers they have not received from another hospital, or when they receive an offer from one hospital but reject it due to a better offer from another hospital. The algorithm is stable because in both cases, the assumption of instability leads to a contradiction. We also prove that if all hospitals are matched, then all students must be matched as well, using proof by contradiction. Finally, we conclude that the Gale-Shapley algorithm solves any stable matching problem and provide examples and pseudocode for further exploration.

