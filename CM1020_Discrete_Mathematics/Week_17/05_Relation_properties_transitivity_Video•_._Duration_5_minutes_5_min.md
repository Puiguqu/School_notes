# Relation properties: transitivity Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/vd0Yf/relation-properties-transitivity)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A relation R on a set S is transitive if for all a, b, c in S, if a is related to b and b is related to c, then a must be related to c. This concept is essential in graph theory, where the digraph of a relation represents the pairs (a, b) such that a is related to b. The transitive closure of a relation R on S is the smallest transitive relation that contains R.

To determine if a relation is transitive, one can examine its digraph and add edges as necessary to ensure that the resulting graph is transitive. For example, in the case of the relation defined by x ≤ y on N, we can see that it is indeed transitive since x ≤ y and y ≤ z imply x ≤ z.

In contrast, the relation R = {(2, 3), (3, 2), (2, 2)} is not transitive because three is related to two, but two is related to three, while three is not related to three. This implies that adding edges to the digraph will make it transitive.

To find the minimum number of edges needed to add to a relation to make it transitive, we can analyze the digraph and identify any missing connections. For instance, in the case of the relation R on S with the given digraph, we need to add edges (a, c), (b, d), and (a, d) to make it transitive.

The enhanced relation obtained by adding these edges is called the transitive closure of the original relation. This concept is crucial in graph theory, as it allows us to analyze and understand the behavior of relations on graphs.

In conclusion, transitivity is a fundamental property of relations that ensures that if two elements are related through an intermediate element, then they are also directly related. Understanding transitivity is essential for analyzing and manipulating relations in various contexts.

The process of finding the transitive closure of a relation involves examining its digraph and adding edges as necessary to ensure transitivity. This can be a complex task, but it provides valuable insights into the structure and behavior of relations on graphs.

Overall, the concept of transitivity is a key aspect of graph theory, and understanding it is essential for analyzing and manipulating relations in various contexts.

