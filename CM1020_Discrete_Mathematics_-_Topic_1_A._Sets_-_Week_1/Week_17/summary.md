# Week 17 - CM1020 Discrete Mathematics - Topic 1 A. Sets - Week 1

## Topic 9 introduction Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/9TG9j/topic-9-introduction)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A new topic called relations will be introduced, which will cover relationships between living or nonliving things. In mathematics, a relation refers to a connection between two elements, such as the relationship between a positive integer and an integer it divides. Relations can also be defined between two real numbers or between a real number x and the value of f(x) where f is a function. Mathematically, relations are used to study relationships between sets and their properties. The concept of relations in mathematics was introduced in this video lecture, which will be further discussed in the next lecture. Relations can be defined between two elements of the same set or between two different sets. In mathematics, we can use various methods to represent relations, such as matrices and graphs. The matrix representation of a relation is a square matrix where each entry represents a relationship between two elements. Graph representations of a relation are also used to visualize relationships between sets. There are several properties of relations, including reflexive, symmetric, anti-symmetric, and transitive. Reflexivity means that every element is related to itself, symmetry means that if one element is related to another, then the other element is also related to it, and anti-symmetry means that if one element is related to another, then they cannot be equal. Transitivity means that if two elements are related to a third element, then those two elements must also be related to each other. The properties of relations will be discussed in more detail in future lectures. Relations have various applications in computer science, such as between a computer language and a valid statement in the language. Understanding relations is essential for studying mathematics and its many applications.

---

## Definition of a relation: relation versus function Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/BBp3i/definition-of-a-relation-relation-versus-function)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A relation between elements of two sets A and B can be defined as a link or connection between an element of set A to an element of set B. The relation R linking elements of set A to elements of set B is denoted by xRy, where x is related to y. The Cartesian product of two sets A and B, written as AxB, is a set of pairs (x,y) such that x is an element of set A and y is an element of set B. A binary relation from a set A to a set B is a subset of the Cartesian product AxB. The pair (x,y) is an element of R if and only if x is related to y. When the sets A and B are the same, we talk about a relation on the set A. In this case, a relation R and the set A is denoted by RxA. A relation can be defined between elements of the same set. For example, let R be a relation on the set A given x,y element of the set A, x is related to y if and only if x is strictly less than y. The relation R on the set A can be represented as a set of pairs (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), and (3, 4). A relation is reflexive if every element of the set is related to itself. A relation is symmetric if for every x in the set A, if x is related to y, then y is also related to x. A relation is anti-symmetric if for every x in the set A, if x is related to y and y is related to x, then x = y.

The Cartesian product of two sets A and B can be calculated using the formula: aAxB = {(a,b) | a ∈ A, b ∈ B}. The relation R on the set A can be represented in matrix form as:

```
| 1  2  3
|------------------
| 0  1  0
| 1  0  1
| 0  1  0
```

The relation R on the set A can also be represented graphically using a directed graph, where each element of the set is connected to every other element in the set.

---

## Matrix and graph representations of a relation Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/wiiWm/matrix-and-graph-representations-of-a-relation)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A relation R can be represented using matrices, where the matrix M_r has dimensions n_a x n_b, with element M_ij equal to one if a_i is related to b_j and zero otherwise. The set A contains elements {1, 2, 3, 4} and the set B contains elements {CS100, CS101, CS102, CS103}. The relation R can be represented by a matrix where the element at row i and column j represents the relationship between student i and course j. The union of two relations is a new set that contains all pairs of elements in at least one of the original relations, while the intersection contains only those pairs present in both relations. The union of two relations can be calculated using the joint (i.e., element-wise OR) of the matrices representing R and S, and the intersection can be calculated using the meet (element-wise AND). A relation on a set A can also be represented by a digraph, where an arrow from x to y indicates that x is related to y. The digraph for the relation "divides" on the set {1, 2, 3, 4} shows loops at each vertex indicating self-relations and other edges representing divisibility relations. Similarly, the digraph for the relation "less than or equal to" on the same set shows loops at each vertex and edges representing the relation between elements. In contrast, the digraph for the strictly less than relation has no loops because an element is not related to itself. The properties of a relation, including reflexivity, symmetry, anti-symmetry, transitivity, are also discussed in this lecture.

Overall, the text discusses three ways to represent relations: using matrices, directed graphs (digraphs), and explaining key concepts such as union, intersection, reflexivity, symmetry, and transitivity. The examples provided illustrate how these methods can be used to model different types of relationships between sets and elements.

---

## The properties of a relation: reflexive, symmetric and anti-symmetric Video• . Duration: 14 minutes 14 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/fw5TG/the-properties-of-a-relation-reflexive-symmetric-and-anti-symmetric)

It appears that the provided text is not a complete solution to a problem, but rather a transcript of a lecture or presentation on "Properties of Relations" in mathematics. The text outlines the concepts of reflexivity, symmetry, and anti-symmetry, as well as their graphical representations using matrices and digraphs.

There is no specific problem or question being addressed in the provided text, and it does not contain step-by-step solutions or answers to a particular problem. However, I can provide a summary of the key points discussed in the lecture:

1. Definition of a relation: A relation between two sets is a subset of their Cartesian product.
2. Properties of relations:
	* Reflexivity: A relation R on a set A is reflexive if for all x in A, (x, x) is in R.
	* Symmetry: A relation R on a set A is symmetric if for all x and y in A, if (x, y) is in R, then (y, x) is also in R.
	* Anti-symmetry: A relation R on a set A is anti-symmetric if for all x and y in A, if (x, y) is in R and (y, x) is in R, then x = y.
3. Graphical representations:
	* Matrix representation: A relation R on a set A can be represented as a matrix M, where the entry at row i and column j represents the number of ordered pairs (i, j) in R.
	* Digraph representation: A relation R on a set A can be represented as a digraph, which is a directed graph where each vertex represents an element of A, and there is a directed edge from vertex x to vertex y if (x, y) is in R.

If you could provide more context or clarify what specific problem or question you would like me to help with, I'll be happy to assist you further.

---

## Relation properties: transitivity Video• . Duration: 5 minutes 5 min

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

---

## The properties of a relation: reflexive, symmetric and anti-symmetric Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/iElEF/the-properties-of-a-relation-reflexive-symmetric-and-anti-symmetric)

Here is a summary of the text in 15 sentences, preserving all key information, formulae, and technical details:

1. In discrete mathematics, particularly in the study of relations, there are several key properties that a relation can possess.
2. Understanding these properties helps in analyzing the nature of relationships between elements in a set.
3. Three important properties of a relation are reflexivity, symmetry, and anti-symmetry.
4. A reflexive relation is one where every element in a set is related to itself.
5. The formal definition of a reflexive relation is: ∀a∈A, aRa
6. An example of a reflexive relation is R={(1,1),(2,2),(3,3)} on the set A={1,2,3}.
7. On the other hand, an example of a non-reflexive relation is R={(1,1),(2,2)} on the same set.
8. A symmetric relation is one where if an element is related to another, then the second element is also related to the first.
9. The formal definition of a symmetric relation is: ∀a,b∈A,(a,b)∈R⟹(b,a)∈R
10. An example of a symmetric relation is R={(1,2),(2,1)} on the set A={1,2}.
11. However, an example of a non-symmetric relation is R={(1,2)} on the same set.
12. An anti-symmetric relation is one where if an element is related to another and vice versa, then they must be the same element.
13. The formal definition of an anti-symmetric relation is: ∀a,b∈A,(a,b)∈R and (b,a)∈R⟹a=b
14. An example of an anti-symmetric relation is R={(1,1),(2,2),(3,3),(1,2)} on the set A={1,2,3}.
15. Understanding these properties is crucial for analyzing relations in sets, which is a foundational concept in discrete mathematics with applications in computer science, particularly in database theory and graph theory.

Note: The text also mentions that there will be another important property discussed in the next lesson, which is transitivity.

---

## Relations Reading• . Duration: 2 hours 10 minutes 2h 10m

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/stZ41/relations)

Here is a summary of the text in 15 sentences:

The textbook "Koshy" covers several topics related to relations, including their definition, graph and matrix representations, reflexivity, symmetry, anti-symmetry, transitivity, and other properties.

The student is asked to read extracts from the Koshy textbook, specifically pages 437-41, 443-46, 448, and 454-59.

After completing the reading, students are encouraged to attempt exercises found on pages 448 and 459-60.

Exercises 1-3, 7-9, 23, 25, 27, 30, 31, 34, and others have solutions at the back of the book in a section titled "Solutions to odd-numbered exercises".

Students are advised to consult this section if they get an answer wrong.

The video topic covers the definition of a relation versus function, which is discussed further in the reading material.

The practice assignment on the definition of a relation involves completing a task related to relations.

Another video topic explores matrix and graph representations of a relation.

The practice assignment for matrix and graph representations also involves completing a task.

A third video topic discusses the properties of a relation, specifically reflexivity, symmetry, anti-symmetry, and transitivity.

The reading material on these topics provides additional information on each property.

The practice assignment on the properties of a relation requires students to complete tasks related to reflexive, symmetric, anti-symmetric, and transitive relations.

Finally, there is a video topic on relation properties: transitivity, which summarizes key concepts.

The overall duration for each activity is specified in minutes (2-20 minutes).

The reading material covers the topics of relations, including definition, graph and matrix representations, reflexivity, symmetry, anti-symmetry, and transitivity.

---

