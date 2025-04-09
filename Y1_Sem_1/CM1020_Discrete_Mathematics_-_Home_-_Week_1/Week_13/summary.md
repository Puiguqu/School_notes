# Week 13 - CM1020 Discrete Mathematics - Home - Week 1

## Topic 7 introduction Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/misR3/topic-7-introduction)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Graph theory is an area of discrete mathematics that studies configurations called graphs, consisting of vertices (nodes) and edges connecting them. The first problem in graph theory was the Seven Bridges of Konigsberg problem, solved by Leonhard Euler in 1735, which involved determining whether it was possible to take a walk and cross all seven bridges only once between two islands. Graphs can be used to model real-world problems, such as computer networks, roadmaps, shortest path problems, and assigning jobs to employees. In graph theory, vertices represent dry land and edges represent bridges. The degree sequence of a graph is a measure of the number of edges connected to each vertex. Special graphs include simple graphs (no multiple edges between vertices), r-regular graphs (all vertices have the same degree), and complete graphs (every pair of vertices is connected by an edge). Graph theory can be used to distinguish chemical compound structures, such as modeling molecules using graphs to gain insight into physical properties. The lecture series will continue to explore graph theory in more detail, including walks, paths, circuits, and special types of graphs.

---

## Definition of a graph Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/J5YvL/definition-of-a-graph)

Here is a summary of the text in 8 sentences, preserving key information:

A graph is a discrete structure consisting of vertices and edges that connect them. It can be represented by a pair VE, where V is a set of nodes (vertices) and E is a set of edges (lines or connections). Vertices are the basic elements of a graph, usually drawn as nodes or dots, and are denoted by V(G) or just V. An edge is a link between two vertices, represented by a line connecting them, and is denoted by E(G) or just E. Two vertices are adjacent if they share the same vertex, while two edges are adjacent if they connect the same pair of vertices. Loops occur when an edge connects a vertex to itself, while parallel edges occur when multiple edges connect the same pair of vertices. Directed graphs, also known as digraphs, are graphs where edges have a direction, usually indicated by an arrow on the edge. This lecture covered the definition and basic concepts of graphs, including adjacency, loops, and directed graphs.

---

## Walks and paths in a graph Video• . Duration: 11 minutes 11 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/paqVc/walks-and-paths-in-a-graph)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

A walk in a graph is a sequence of vertices and edges where vertices and edges can be repeated. A trail is a walk with no repeated edges, while a circuit is a closed trail with repeated vertices only. A path is a trail with neither repeated vertices nor edges. The length of a path is the number of edges it contains. An Eulerian path is a path that traverses each edge of a graph once, making the graph traversable. A Hamiltonian path visits each vertex of a graph exactly once, while a Hamiltonian cycle visits each vertex except the start and end vertices. A strongly connected directed graph has a directed path between all pairs of vertices, whereas an undirected graph is connected if there exists a path between any two nodes. The transitive closure of a digraph provides reachability information about the graph by adding directed edges from one vertex to another if there is a directed path between them.

---

## The degree sequence of a graph Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/7KP4a/the-degree-sequence-of-a-graph)

Here is a summary of the text in 8 sentences, preserving all key information:

The degree of a vertex in a graph is defined as the number of edges incident to it, with loops contributing twice to the degree and isolated vertices having a degree of 0. In directed graphs, the out-degree of a vertex is defined as the number of edges that end at the vertex, while the in-degree is the number of edges that start at the vertex. The degree sequence of a graph is a list of the degrees of each vertex in descending order, separated by commas. One property of a graph's degree sequence is that the sum of the degree sequence is always even, as it is impossible to construct a graph with an odd sum of degree sequence. Another property is that the sum of the degree sequence is twice the number of edges in the graph. To verify this, we can use the example of a graph with a degree sequence of 4,3,2,1,1, which has 7 edges. By counting the edges manually, we can confirm that the sum of the degree sequence matches the expected value. This concept is crucial in understanding how graphs can be represented using their degree sequences.

---

## Special graphs: simple, r-regular and complete graphs Video• . Duration: 13 minutes 13 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/vfFhv/special-graphs-simple-r-regular-and-complete-graphs)

This is not a problem to be solved, but rather a transcript of a video lecture on graph theory. However, I can provide some information and answers based on the content of the lecture.

The lecture covers three main topics:

1. Simple graphs: A simple graph is an undirected graph with no multiple edges between any two vertices.
2. Regular graphs: A regular graph is a graph where every vertex has the same degree.
3. Complete graphs: A complete graph is a graph where every pair of vertices are adjacent.

The lecture also introduces some important concepts and formulas, such as:

* The degree sequence of a graph
* The number of edges in a graph
* The properties of simple, r-regular, and complete graphs

If you have specific questions or topics related to graph theory that you'd like me to help with, feel free to ask!

---

## Walks, paths and circuits in graph theory Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/7cUix/walks-paths-and-circuits-in-graph-theory)

The text is a passage about graph theory, specifically explaining the concepts of walks, paths, and circuits.

To answer the question "What are walks, paths, and circuits in graph theory?", here's a summary:

*   **Walks**: A walk is a sequence of vertices and edges that starts at a vertex, traverses to another vertex (or returns to the starting vertex), and ends at another vertex. In the passage, it provides examples of different types of walks, such as walks with repeated vertices or repeated edges.
*   **Paths**: A path is a walk in which all vertices and edges are distinct. It means that a path does not revisit any vertex. The passage provides an example of a path from vertex a to vertex d.
*   **Circuits**: A circuit is a type of walk that starts and ends at the same vertex, with all edges distinct. The passage provides an example of a circuit starting and ending at vertex a.

Understanding walks, paths, and circuits is essential in various applications, such as network routing and social network analysis.

---

## Graphs Reading• . Duration: 2 hours 40 minutes 2h 40m

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/BaYxT/graphs)

Here is a summary of the text in 8 sentences:

The provided text outlines a series of learning materials for graph theory, covering topics such as the definition and application of a graph, degree sequence, simple, regular, and complete graphs, and paths. The materials are based on extracts from Koshy and Levin textbooks (licensed under Creative Commons Attribution- Alike 4.0 International License) and include exercises with solutions provided at the back of the books. Students are encouraged to consult the "Solutions to odd-numbered exercises" section for answers to their questions. The learning materials also include video topics, practice assignments, and reading materials that cover these topics in more depth. A total of 5 hours and 40 minutes of material is available, including a 3-minute introduction video, a 20-minute discussion prompt, and a 2-hour reading assignment on graphs. The specific topics covered include the definition of a graph, walks and paths in a graph, the degree sequence of a graph, special graphs such as simple, regular, and complete graphs. Students can access these materials through links to videos and practice assignments, which are also included in the text. Overall, the learning materials provide a comprehensive introduction to graph theory, covering key concepts and providing students with opportunities to practice their understanding through exercises and assignments.

---

