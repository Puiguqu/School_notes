# Week 15 - CM1020 Discrete Mathematics - Home - Week 1

## Topic 8 introduction Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/D6ACT/topic-8-introduction)

Here is a summary of the text in 8 sentences, preserving key information:

Trees are a fundamental data structure in computer science, inspired by their composition in nature. In computer science, trees are represented upside down and have various applications, including organization charts, file systems, and version control systems. Trees can be used to find shortest paths in graphs, locate items in lists, and model procedures with decision sequences. A binary tree is a fundamental data structure in high-level programming, which will be further explored in the next lecture. Trees are employed in a wide range of algorithms, including those for games like checker and chess. They can help determine winning strategies by modeling game trees. The properties of trees will be examined to solve real-world problems, building on the informal definition provided earlier.

Note: I did not include any links or technical details as they were not present in the original text. If you would like me to add them, please provide the necessary information and I'll be happy to help.

---

## Definition of a tree Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/wuiwv/definition-of-a-tree)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

A graph is considered acyclic if it has no cycles, including loops and parallel edges. A tree is defined as an undirected graph that is connected and cycle-free. There exists a unique simple path between any two vertices in a tree, which can be proven by contradiction. The number of edges in a tree with n vertices is exactly n-1. The concept of a rooted tree is introduced, where one vertex is designated as the root and every edge is directed away from it. The definition of trees and roots are formalized through examples and properties. A forest is defined as a cycle-free disconnected graph, which can be distinguished from a tree by its lack of connectivity. Understanding these concepts is essential for tracing graph theory, including acyclic graphs, trees, rooted trees, and spanning/minimum spanning trees.

---

## Spanning trees of a graph Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/3aWwu/spanning-trees-of-a-graph)

Here is a summary of the text in 8 sentences, preserving key information and concepts:

A spanning tree of a graph G is a connected cycle-free subgraph of G that contains all the vertices of G. To construct a spanning tree, one keeps all the vertices of G and breaks all cycles while keeping the graph connected. The number of possible spanning trees of a graph depends on its structure, with graphs having more edges allowing for more spanning trees. For example, graph G1 has four possible spanning trees, graph G2 has eight, and graph G3 has 16. Two spanning trees are isomorphic if there exists a bijection preserving adjacency between the two trees, meaning they represent the same structure but may be drawn differently. When drawing all spanning trees of a graph, it's only necessary to draw non-isomorphic ones to avoid repetition. The definition of a tree in graph theory includes a connected subgraph with no cycles, and understanding spanning trees is crucial in various applications such as Internet multicasting.

---

## Minimum spanning tree Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/ktfeY/minimum-spanning-tree)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Minimum cost spanning trees are useful in situations where a network needs to be connected with minimal cost. The weight or cost of a spanning tree is defined as the sum of the costs of its edges. Two basic algorithms for finding minimum cost spanning trees are Kruskal's algorithm and Prim's algorithm. Kruskal's algorithm starts by selecting the cheapest edge in the graph that does not form a cycle, adding it to the tree, and repeating this process until all vertices are connected. The algorithm ensures the minimum cost spanning tree has the lowest total weight or cost. In contrast, Prim's algorithm begins with an arbitrary node, selects the cheapest edge incident on it, and then adds the cheapest edge leading to nodes not yet in the tree, repeating this process until all vertices are connected. Both algorithms can be used to find a minimum cost spanning tree, with Kruskal's being more suitable for large graphs and Prim's for smaller ones due to its simplicity. The goal of both algorithms is to create a minimum cost spanning tree that connects all nodes in the graph while minimizing the total cost or weight.

Note: Since the text does not provide explicit links, formulae, or technical details beyond what has been paraphrased into this summary, these have not been included here.

---

## Topic 8 essential reading Reading• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/OYVA0/topic-8-essential-reading)

Here is a summary of the text in 8 sentences:

The provided extracts cover topics such as tree definitions, spanning trees, weighed graphs, minimum spanning trees, and Prim's and Kruskal's algorithms. The work is licensed under Creative Commons Attribution- Alike 4.0 International License. To complete this material, one should read Koshy (pp.609–13, pp.614–17, pp.626–28) and Levin (pp.247–54), as well as attempt the provided exercises from the textbooks. The exercises can be found in Koshy: p.613, exercises 1–7 and 9–11, and p.624, exercises 11–13, and Levin: p.255, exercises 1–2 and 12–13. Solutions to these exercises are available at the back of the books under the sections 'Solutions to odd-numbered exercises' (Koshy) and 'Selected solutions' (Levin). There are also video lectures and practice assignments available on topics such as tree definitions, spanning trees, and minimum spanning trees. The material is accompanied by a 20-minute discussion prompt and a 5-minute definition of a tree video lecture. Additionally, there are reading materials covering the essential topics that should be completed after finishing the provided extracts.

---

