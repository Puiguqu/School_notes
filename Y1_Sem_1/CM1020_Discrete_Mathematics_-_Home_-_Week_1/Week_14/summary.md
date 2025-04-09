# Week 14 - CM1020 Discrete Mathematics - Home - Week 1

## Isomorphic graphs Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/xShxj/isomorphic-graphs)

Here is a summary of the text in 8 sentences, preserving key information:

Two graphs are considered isomorphic if there exists a bijection (an invertible function) that maps all vertices from one graph to another while preserving adjacency and non-adjacency. This means that if two vertices are adjacent in one graph, they will be adjacent in the other graph under the mapping. Isomorphism can help show that two graphs appear different but are actually structurally similar. For example, consider two graphs G1 and G2, where a mapping from each vertex of G1 to a corresponding vertex in G2 establishes an isomorphism. The definition of isomorphic graphs relies on the existence of such a bijection, which preserves adjacency and non-adjacency. In contrast, two graphs with different degree sequences cannot be isomorphic, as they must have distinct arrangements of edges around vertices. On the other hand, having the same degree sequence does not necessarily imply isomorphism, as there can exist bijections between the vertex sets that preserve adjacency without being a one-to-one correspondence. The concept of isomorphism in graphs has several important properties and applications, including the relationship between degree sequences of isomorphic graphs.

Note: I removed all external links, formulae, and technical details not directly related to summarizing the main concepts and findings of the text.

---

## Bipartite graphs Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/VYQ8F/bipartite-graphs)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

A bipartite graph is defined as a graph where the vertices can be divided into two sets, V1 and V2, such that each edge connects one vertex from V1 to one vertex from V2. A matching in a bipartite graph is a set of pairwise non-adjacent edges with no common endpoints. A maximum matching is a matching with the largest possible size, where adding any more edges would violate the matching condition. The Hopcroft-Karp algorithm is used to find a maximum matching in a bipartite graph. The algorithm uses breadth-first search and depth-first search to traverse the graph and find augmenting paths that can be used to increase the size of the matching. An example of how the algorithm works is shown using a job seeker and candidate matching graph, where three candidates are matched with three jobs. The Hopcroft-Karp algorithm produces a maximum cardinality matching where each vertex on each side is connected to exactly one vertex on the other side. The algorithm's pseudocode can be represented as a bipartite graph, and applying it results in a maximum matching where each candidate is matched to a job.

---

## The adjacency matrix of a graph Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/GbYw5/the-adjacency-matrix-of-a-graph)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

A graph can be represented by two different methods: the adjacency list and the adjacency matrix. The adjacency list represents the vertices and their corresponding adjacent vertices, while the adjacency matrix represents the edges between vertices as elements of a matrix. The number of edges in an undirected graph is equal to half the sum of all the elements m_ij of its corresponding adjacency matrix. Additionally, the sum of all the elements of the adjacency matrix is equal to the sum of the degree sequence of the graph. In a directed graph, each edge has a defined direction, and the adjacency matrix represents the edges as pairs of vertices. The number of paths of Length 2 from a vertex can be calculated using the squared adjacency matrix. Finally, the lesson covers properties of the adjacency matrix, including the relationship between the sum of the degree sequence and the adjacency matrix.

---

## Dijkstra's algorithm Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/72JIm/dijkstras-algorithm)

Here is a summary of the text in 8 sentences, preserving all key information, formulae, links, and technical details:

Dijkstra's algorithm is used to compute the shortest path between two vertices in a weighted graph. A weighted graph is a graph where each edge is assigned a numerical value, which can be used to model distances, response times, or costs in various applications. The algorithm works by iteratively visiting unvisited vertices and updating their shortest distance and previous vertex information. In the first iteration, the algorithm initializes the distance from the start vertex to all other vertices as infinity, except for itself, which is set to zero. In subsequent iterations, the algorithm visits the unvisited vertex with the smallest known distance from the start vertex, updates its neighbors' distances if necessary, and marks it as visited. The algorithm continues until all vertices have been visited, at which point the shortest path can be constructed by tracing back the previous vertices. Dijkstra's algorithm has a time complexity of O(E + V log V) in the worst case, where E is the number of edges and V is the number of vertices.

---

## Webinar on graphs Video• . Duration: 1 hour 24 minutes 1h 24m

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/7ys5z/webinar-on-graphs)

This is a transcript of a lecture on graph theory, specifically focusing on Dijkstra's algorithm for finding the shortest path in weighted graphs. Here's a summary of the main points:

1. Introduction to graph theory:
	* Definition of a graph
	* Types of graphs (simple, weighted, undirected, directed)
	* Terminology: nodes, edges, vertices, adjacency matrix
2. Adjacency matrix and its properties:
	* Definition of an adjacency matrix
	* Information encoded in the adjacency matrix
3. Weighted graphs:
	* Definition of a weighted graph
	* Properties of weighted graphs (e.g., shortest path problem)
4. Dijkstra's algorithm:
	* Description of the algorithm for finding the shortest path
	* Initialization: setting distances to all nodes except the starting node to 0, and others to infinity
	* Iteration: visiting each node, updating distances if a shorter path is found
	* Application: using Dijkstra's algorithm to find the shortest path in weighted graphs

The lecture also includes some additional pages with extra resources, including:

* A video on graph theory (1 hour 24 minutes)
* A webinar on graph theory (1 hour 24 minutes)
* A reading list on graph theory problems and solutions (10 minutes each)

Overall, this transcript provides a comprehensive overview of the basics of graph theory, including definitions, terminology, properties, and algorithms for finding shortest paths in weighted graphs.

---

## Topic 7 essential reading Reading• . Duration: 2 hours 15 minutes 2h 15m

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/4zFdG/topic-7-essential-reading)

There is no text provided to summarize. The given text appears to be a table of contents or a course outline for a lesson on graph theory, covering topics such as adjacency matrices, isomorphic graphs, bipartite graphs, and Dijkstra's algorithm. It includes links to relevant videos, practice assignments, reading materials, and extra resources.

If you provide the actual text, I can help summarize it in 8 sentences while preserving key information, formulae, links, and technical details.

---

## Dijkstra's algorithm simulation Reading• . Duration: 20 minutes 20 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/XcN8d/dijkstras-algorithm-simulation)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Dijkstra's algorithm is a graph search algorithm that can be applied to weighted graphs. The algorithm simulates finding the shortest route between two stations in an underground network. Each vertex represents a station, each edge represents a route between two stations, and the distance in kilometres between two stations represents the cost or weight of that route. In the simulation, help text guides the user through each stage of the process, while the current underground network is represented as a weighted graph. The user must select a starting and end point for their journey and click on the graph to find distances between directly connected stations. Once the table row is filled in, it means that all distances from the current station have been found, and the next step is to select the station with the shortest distance. The solution can be visualized on either the graph or the Dijkstra's table, which highlights the shortest route and journey from start to end.

---

## Topic 7 summary Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/yH7PG/topic-7-summary)

Here is a summary of the text in 8 sentences:

Graph theory is a fundamental area of mathematics and computer science that studies graphs, which are structures composed of vertices connected by edges. The module covered basic concepts such as graph representation methods, special graphs, properties, metrics, algorithms, and practical applications. Key concepts include understanding vertices and edges, types of graphs (directed, undirected, weighted, unweighted), special graphs (complete, bipartite, trees), graph representation (adjacency matrix, adjacency list, degree sequence), and significant algorithms (Dijkstra's algorithm, maximum matching). The module will equip students with the basics to understand and analyze various types of graphs and their properties, develop algorithms for graph-related problems, and apply graph theory concepts to practical scenarios. To reflect on learning journey, identify areas for improvement, create an action plan, and implement strategies such as reviewing course materials, seeking additional resources, practicing problems, and seeking help from instructors or peers. Students should regularly assess their understanding against the learning outcomes and adjust their plan as needed. The module is designed to be completed in a specific duration with various videos, practice assignments, reading materials, and peer-graded assignments. By completing this module, students will develop a solid foundation in graph theory and its applications.

---

## Graph theory problem sheet Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/zywLI/graph-theory-problem-sheet)

Lesson 7.2 Isomorphic graphs adjacency matrix 7.3 Extra resources Video: Video Webinar on graphs . Duration: 1 hour 24 minutes 1h 24m Reading: Reading Graph theory problem sheet . Duration: 10 minutes 10 min Reading: Reading Graph theory problem sheet solutions . Duration: 10 minutes 10 min Graph theory problem sheet tutorial-topic7-graphs.pdf PDF File Mark as completed Dislike Report an issue

---

## Graph theory problem sheet solutions Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/GADLi/graph-theory-problem-sheet-solutions)

Lesson 7.2 Isomorphic graphs adjacency matrix 7.3 Extra resources Video: Video Webinar on graphs . Duration: 1 hour 24 minutes 1h 24m Reading: Reading Graph theory problem sheet . Duration: 10 minutes 10 min Reading: Reading Graph theory problem sheet solutions . Duration: 10 minutes 10 min Graph theory problem sheet solutions tutorial-topic7-graphs-sol.pdf PDF File Mark as completed Dislike Report an issue

---

