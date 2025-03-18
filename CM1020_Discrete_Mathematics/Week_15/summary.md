# Week 15 - CM1020 Discrete Mathematics - Topic 1 A. Sets - Week 1

## Topic 8 introduction Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/D6ACT/topic-8-introduction)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A mathematical concept known as "trees" is discussed, with an analogy to nature. In computer science, trees are represented upside down and have various applications. Trees can be used to represent organizational charts, file systems, and centralized version control systems. They are particularly useful in algorithms, such as finding the shortest path in a graph. Binary trees are a fundamental data structure in high-level programming. The lecture will examine the properties of trees and their application to real-world problems. Informal definitions of trees have been provided, with an upcoming lecture covering their properties. Trees can be used to model procedures carried out using a sequence of decisions. They have applications in games like checker and chess to determine winning strategies. A binary tree is defined as a fundamental data structure in high-level programming.

The concept of spanning trees and minimum spanning trees will also be covered. Spanning trees are used to represent a graph, while minimum spanning trees are used to find the shortest path between nodes. The goal of this lecture series is to discuss the properties of trees and their applications in real-world problems. The importance of trees in computer science cannot be overstated, as they have numerous practical uses.

The lecture series will include video lectures, practice assignments, and essential reading materials. This will provide students with a comprehensive understanding of trees and their significance in computer science.

---

## Definition of a tree Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/wuiwv/definition-of-a-tree)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A graph G is considered acyclic if it has no cycles, including loops and parallel edges. The directed graph G1 contains at least one cycle and is therefore not acyclic. In contrast, the directed graph G2 is cycle-free and hence acyclic. An undirected graph G is a tree if and only if it is connected and acyclic. This means that there exists a path between any two vertices of G, and G has no cycles. The graph G1 is connected but not a tree because it contains at least one cycle. On the other hand, the graph G2 is both connected and cycle-free, making it a tree. A forest in graph theory refers to a cycle-free disconnected graph. An undirected graph is considered a tree if there exists a unique simple path between any two of its vertices. This property can be proven by contradiction, where assuming a non-unique path leads to a cycle, contradicting the definition of a tree. By this reasoning, a tree with n vertices has exactly n-1 edges. A rooted tree is defined as a tree in which one vertex is designated as the root, and every edge is directed away from the root. The concept of tracing graph theory introduces the idea of analyzing graphs by identifying cycles and paths. Understanding acyclic graphs, trees, and rooted trees is essential for studying graph theory.

---

## Spanning trees of a graph Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/3aWwu/spanning-trees-of-a-graph)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A spanning tree of a graph G is a connected cycle-free subgraph that contains all the vertices of G. A more formal definition states that a spanning tree T is a subgraph of G such that every vertex of G is in T, and T has no cycles. To construct a spanning tree, one can start with an empty tree and add edges to connect all the vertices while avoiding cycles. The number of possible spanning trees for a graph with n vertices increases exponentially with n. For example, a graph with 4 vertices can have 8 or 16 possible spanning trees, depending on its structure. Two spanning trees are isomorphic if there exists a bijection between them that preserves adjacency. Isomorphic spanning trees represent the same underlying structure. When drawing all spanning trees of a graph, it's only necessary to draw non-isomorphic ones to avoid duplicates. The concept of spanning trees has applications in real-life problems like Internet multicasting. Identifying the trees within a graph is crucial for understanding its properties and behavior. Graphs with many vertices can have an enormous number of possible spanning trees, making analysis and visualization challenging. The definition of a tree is closely related to spanning trees, as any subgraph that includes all vertices and no cycles can be considered a tree. Understanding spanning trees is essential for solving problems in graph theory and computer science.

---

## Minimum spanning tree Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/ktfeY/minimum-spanning-tree)

Here is a summary of the text in 15 sentences, preserving all key information, formulae, and technical details:

A minimum cost spanning tree is a subgraph that connects all vertices in a connected undirected graph with the minimum total edge weight. The weight of a spanning tree is the sum of the weights of its edges. Two algorithms are used to find minimum cost spanning trees: Kruskal's algorithm and Prim's algorithm.

Kruskal's algorithm starts by selecting the cheapest edge in the graph that is not part of the current spanning tree. If adding this edge would form a cycle, it is skipped. Otherwise, it is added to the spanning tree. This process is repeated until all vertices are connected.

Prim's algorithm also starts with an arbitrary node and adds the smallest edge incident to that node to the spanning tree. The node is then removed from consideration, and the next smallest edge incident to the remaining nodes is selected. This process continues until all vertices are connected.

A key concept in both algorithms is the use of disjoint sets (also known as union-find data structures) to detect cycles and ensure that the resulting graph is a minimum spanning tree.

In Kruskal's algorithm, the edges are sorted by weight, and the cheapest edge that does not form a cycle is selected. In Prim's algorithm, the smallest edge incident to each node is chosen until all nodes are connected.

Both algorithms have time complexity of O(E log E) or O(E + V), where E is the number of edges and V is the number of vertices in the graph. The algorithms also use a disjoint set data structure to keep track of the connected components and detect cycles.

The minimum cost spanning tree has the lowest total edge weight among all possible spanning trees of the graph.

---

## Topic 8 essential reading Reading• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/OYVA0/topic-8-essential-reading)

Here is a summary of the text in 15 sentences:

The provided text discusses various topics in graph theory, including trees, spanning trees, weighed graphs, minimum spanning trees, and Prim's and Kruskal's algorithms.

These topics will be covered through extracts from two textbooks: Koshy and Levin.

The definition of a tree is discussed, although the exact content is not specified.

Spanning trees are introduced as subgraphs that connect all vertices in a graph without forming any cycles.

Weighted graphs are also mentioned, which implies that the weights or costs associated with edges will be considered.

Minimum spanning trees (MSTs) are defined as subsets of edges in a weighted graph that connect all vertices without forming any cycles and have the minimum total weight.

Two algorithms for finding MSTs are presented: Prim's algorithm and Kruskal's algorithm.

Prim's algorithm is a greedy algorithm that starts with an arbitrary vertex and grows the tree by adding the smallest-weight edge that does not form a cycle.

Kruskal's algorithm, on the other hand, sorts all edges in non-decreasing order of their weights and then adds them to the tree one by one.

The text also mentions video lectures, practice assignments, and reading topics for further learning and exploration.

There are exercises provided at the end of each chapter or section, which students can attempt to check their understanding and learn from mistakes.

Video lectures cover various aspects of these topics in 2-7 minute segments.

Practice assignments allow students to apply theoretical concepts to practical problems and reinforce their learning.

The text is licensed under Creative Commons Attribution- Alike 4.0 International License, indicating that it is free to use, share, and adapt.

Overall, the provided text aims to introduce these fundamental concepts in graph theory and provide resources for further study and practice.

---

