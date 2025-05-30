# Minimum spanning tree Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/ktfeY/minimum-spanning-tree)

Here is a summary of the text in 15 sentences, preserving all key information, formulae, and technical details:

A minimum cost spanning tree is a subgraph that connects all vertices in a connected undirected graph with the minimum total edge weight. The weight of a spanning tree is the sum of the weights of its edges. Two algorithms are used to find minimum cost spanning trees: Kruskal's algorithm and Prim's algorithm.

Kruskal's algorithm starts by selecting the cheapest edge in the graph that is not part of the current spanning tree. If adding this edge would form a cycle, it is skipped. Otherwise, it is added to the spanning tree. This process is repeated until all vertices are connected.

Prim's algorithm also starts with an arbitrary node and adds the smallest edge incident to that node to the spanning tree. The node is then removed from consideration, and the next smallest edge incident to the remaining nodes is selected. This process continues until all vertices are connected.

A key concept in both algorithms is the use of disjoint sets (also known as union-find data structures) to detect cycles and ensure that the resulting graph is a minimum spanning tree.

In Kruskal's algorithm, the edges are sorted by weight, and the cheapest edge that does not form a cycle is selected. In Prim's algorithm, the smallest edge incident to each node is chosen until all nodes are connected.

Both algorithms have time complexity of O(E log E) or O(E + V), where E is the number of edges and V is the number of vertices in the graph. The algorithms also use a disjoint set data structure to keep track of the connected components and detect cycles.

The minimum cost spanning tree has the lowest total edge weight among all possible spanning trees of the graph.

