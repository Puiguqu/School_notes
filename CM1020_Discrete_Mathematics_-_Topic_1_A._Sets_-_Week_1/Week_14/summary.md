# Week 14 - CM1020 Discrete Mathematics - Topic 1 A. Sets - Week 1

## Isomorphic graphs Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/xShxj/isomorphic-graphs)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Two graphs, G1 and G2, are isomorphic if there exists a bijection (invertible function) F that maps all vertices of G1 to vertices of G2 while preserving adjacency and non-adjacency. This means that for any two vertices U and V in G1, if uv is an edge, then f(U)f(V) is an edge in G2, and vice versa. The concept of isomorphism aims to show that two graphs may appear different but are actually the same. An example of this can be seen with the graphs G1 and G2, where a mapping function f can be defined to establish isomorphism between them. A bijective function preserves adjacency and non-adjacency, as shown in the example of graph G1 mapped onto graph G2 using the function f. Two graphs cannot be isomorphic if they have different degree sequences. For instance, two 3-regular simple connected graphs with four vertices cannot be isomorphic due to their differing degree sequences. However, two graphs can have the same degree sequence and still not be isomorphic. This can be proven by showing that a one-to-one correspondence between the vertex sets of these graphs preserves adjacency but does not exist. The three graphs shown in the example are 2-regular simple connected with four vertices and exhibit isomorphism among themselves through bijection. Similarly, the two graphs shown in another example are 3-regular simple connected with six vertices and can be proven to be isomorphic through a bijective mapping function. In contrast, the final pair of graphs are 2-regular simple connected with five vertices but lack an identifiable bijection, hence cannot be proven to be isomorphic based on given criteria. The concept of isomorphism in graph theory highlights that similarity between graphs may imply underlying structural equivalence despite surface-level dissimilarities. Understanding this relationship between graph structure and adjacency through mapping functions can aid in identifying distinct patterns across various types of connected networks.

---

## Bipartite graphs Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/VYQ8F/bipartite-graphs)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A bipartite graph is a special type of graph where the set of vertices can be divided into two sets, V1 and V2, such that each edge connects one vertex from V1 to one vertex from V2. A bipartite graph is two-colorable, meaning it can be represented using two colors, which are used to represent vertices in V1 (e.g., orange) and vertices in V2 (e.g., yellow). One important property of bipartite graphs is that they have no cycles of odd length.

A matching in a bipartite graph is a set of pairwise non-adjacent edges with no shared endpoints. A vertex is matched or saturated if it's an endpoint of one of the edges, otherwise it's unmatched. The maximum matching is the largest possible number of edges that can still form a matching when adding any edge would break it.

The Hopcroft-Karp algorithm is used to find the maximum matching in a bipartite graph. It uses two other algorithms: breadth-first search (BFS) and depth-first search (DFS). The algorithm starts with all nodes in each side of the graph where C and J have no pairings and iterates through BFS and DFS to find augmenting paths.

An augmenting path is an alternating sequence of unmatched edges ending on a free node, which augments the cardinality of the current machine. In the first iteration, BFS finds three trees connecting nodes in C to nodes in J. The maximum matching is found when an augmenting path is discovered from node J2 up to C1.

The second iteration starts with DFS and finds an augmenting path from node J3 up to C3. This results in a semi-matched graph. After the second iteration, every job seeker is matched to a job.

---

## The adjacency matrix of a graph Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/GbYw5/the-adjacency-matrix-of-a-graph)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A graph can be represented by a set of vertices and a set of edges or connections. The adjacency list represents a graph as a list of vertices and their corresponding individual adjacent vertices. For example, the adjacency list of the graph shown below is as follows: vertex A has B and C as its adjacent vertices, vertex B has A, C, and D as its adjacent vertices, and so on.

A graph can also be represented by its corresponding adjacency matrix. The adjacency matrix represents a graph as a set of entries m_ij, where i and j represent the vertices of the graph. The values in the leading diagonal are loops, which means there is an edge between a vertex and itself.

The number of edges in an undirected graph is equal to half the sum of all the elements m_ij of its corresponding adjacency matrix. This can be expressed as m = (1/2) * ∑m_ij. The sum of all the elements of the adjacency matrix is equal to the sum of the degree sequences of the graph.

For example, given the graph with vertices v_1, v_2, and v_3, the degree sequence is [4, 5, 3], and the sum of the degree sequences is 12. The corresponding adjacency matrix has a sum of elements equal to 12, which matches the number of edges in the graph (6).

The adjacency matrix of a directed graph represents the direction of each edge. In this case, each entry m_ij represents the number of paths from vertex i to vertex j.

For instance, in the given directed graph, the first row of M^2 shows that there is one path of length 2 from v_1 to v_1, four paths of length 2 from v_1 to v_1, and so on for other vertices.

---

## Dijkstra's algorithm Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/72JIm/dijkstras-algorithm)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

1. Dijkstra's algorithm is used to compute the shortest path between two vertices in a weighted graph.
2. A weighted graph is a graph where each edge has a numerical value assigned to it, representing the distance or cost between nodes.
3. In 1956, Edsger Dijkstra introduced an algorithm to find the shortest path between any two nodes in a graph.
4. The algorithm works by iteratively selecting the unvisited vertex with the smallest known distance from the starting node and updating its neighbors' distances.
5. The first step of the algorithm is initialization, where the distance from the starting node to itself is set to zero, and all other distances are initialized to infinity.
6. The second step is the update step, where the algorithm visits each unvisited vertex with a known distance, updates its neighbors' distances if necessary, and marks it as visited.
7. This process continues until all vertices have been visited, resulting in a complete table of shortest distances from the starting node to any other node.

The final answer is: $\boxed{6}$

---

## Webinar on graphs Video• . Duration: 1 hour 24 minutes 1h 24m

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/7ys5z/webinar-on-graphs)

This is a transcript of a lecture on graph theory, specifically on Dijkstra's algorithm for finding the shortest path in weighted graphs. Here's a breakdown of the content:

**Introduction to Graph Theory**

The lecture starts by revisiting what is a graph, its properties, and terminology.

**Degree Sequence of a Graph**

The degree sequence of a graph refers to the number of edges connected to each vertex.

**Adjacency Matrix**

An adjacency matrix is a square matrix used to represent a graph. Each entry in the matrix indicates whether there is an edge between two vertices or not.

**Weighted Graphs**

The lecture then moves on to weighted graphs, where each edge has a weight associated with it.

**Dijkstra's Algorithm**

Dijkstra's algorithm is introduced as a method for finding the shortest path in a weighted graph. The algorithm works by:

1. Initializing the distance to all vertices apart from the starting point to 0 and all others to infinity.
2. Starting from the starting point, visiting each node and updating the distances and previous nodes if shorter paths are found.

**Example Walkthrough**

The lecture provides an example walkthrough of Dijkstra's algorithm using a sample weighted graph. The example shows how the algorithm is applied to find the shortest path from vertex A to all other vertices in the graph.

**Key Takeaways**

The key takeaways from the lecture are:

* Understanding what a graph, adjacency matrix, and weighted graphs are.
* Knowing how Dijkstra's algorithm works for finding the shortest path in weighted graphs.
* Being able to apply Dijkstra's algorithm using an example walkthrough.

**Additional Resources**

The lecture concludes with suggestions for additional resources, including video lectures, webinars, reading materials, and practice problems.

Overall, this transcript provides a comprehensive introduction to graph theory, including the concept of weighted graphs and Dijkstra's algorithm. The example walkthrough helps illustrate how the algorithm works in practice.

---

## Topic 7 essential reading Reading• . Duration: 2 hours 15 minutes 2h 15m

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/4zFdG/topic-7-essential-reading)

There is no text to summarize. The provided content appears to be a list of resources and assignments for a computer science or graph theory course, including topics such as adjacency matrices, isomorphic graphs, bipartite graphs, Dijkstra's algorithm, and exercises. It does not contain any specific text or data that needs summarization.

If you could provide the actual text you would like me to summarize, I would be happy to assist you in breaking it down into 15 sentences while preserving key information, formulae, and technical details.

---

## Dijkstra's algorithm simulation Reading• . Duration: 20 minutes 20 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/XcN8d/dijkstras-algorithm-simulation)

Here are 15 sentences summarizing the text, preserving key information, formulae, and technical details:

1. The next exercise will teach users more about Dijkstra's algorithm and its application to real-world scenarios.
2. Users will be responsible for running Dijkstra's algorithm step-by-step to find the shortest route between two stations in an underground network.
3. Dijkstra's algorithm can be executed on weighted graphs, where each vertex represents a station, each edge represents a route, and the distance between two stations represents the cost or weight of that route.
4. The simulation consists of a weighted graph representing the London underground network, with weights representing real distances in kilometers.
5. Users will be prompted to select a starting and ending point for their journey on the graph.
6. The Dijkstra's algorithm table displays possible next steps based on the shortest distance from the current station.
7. To find the shortest distance between two stations, users must click on all directly connected stations to update the table.
8. The table shows that [BS] Bond Street has two direct neighbors: [OC] Oxford Street and [GP] Green Park, with distances of 0.6 km and 1.4 km respectively.
9. The distance between [BS] Bond Street and itself is 0 km, making it an impossible route.
10. Users must select the station with the shortest distance from [BS] Bond Street as their next step.
11. In this case, users should select [OC] Oxford Street, which updates the table and sets [OC] Oxford Street as the current station to analyze.
12. The process is repeated until the entire table is filled in, allowing users to find the shortest route between two stations.
13. The final answer can be visualized on either the graph or Dijkstra's algorithm table, with the shortest route highlighted in red.
14. Users can submit their answers by listing the shortest journey from the start station to the end station.
15. The simulation also offers options for resetting the current underground network, selecting a new one, and accessing additional resources to test Dijkstra's algorithm knowledge.

---

## Topic 7 summary Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/yH7PG/topic-7-summary)

Here are the 15 key points summarizing the text:

1. Graph theory is a fundamental area of mathematics and computer science that focuses on the study of graphs, which are structures made up of vertices connected by edges.
2. The main concepts covered in this topic include graph representation methods, special graphs, properties, metrics, significant algorithms, and practical applications.
3. Basic concepts include recognizing the primary components of graphs (vertices and edges), differentiating between directed and undirected graphs, weighted and unweighted graphs, regular graphs, simple graphs, and multigraphs.
4. Special graphs include complete graphs, bipartite graphs, and trees, which are used to understand graph properties and analysis.
5. Bipartite graphs can be divided into two disjoint sets such that every edge connects a vertex in one set to a vertex in the other.
6. Graph representation methods include adjacency matrices, adjacency lists, and degree sequences, each with its own advantages and applications.
7. The sum of degrees of all vertices in an undirected graph is twice the number of edges (∑ degree(v) = 2|E|), where v represents vertices and |E| represents the number of edges.
8. Graph isomorphism refers to the conditions under which two graphs are structurally identical, allowing for comparison and analysis of graphs with different structures.
9. Significant algorithms include Dijkstra's algorithm for finding the shortest path in a weighted graph, and maximum matching for finding the largest possible set of edges without common vertices.
10. The topic will equip students with the basics to understand and analyze various types of graphs and their properties, develop algorithms for graph-related problems, and apply graph theory concepts to practical scenarios in diverse fields.
11. Regular self-assessment is crucial as students progress through the course to identify areas where they need to deepen their knowledge or skills.
12. The exercise provides a reflection on learning journey, identifying areas for improvement, and developing an action plan to address these gaps.
13. Strategies for improvement include reviewing course materials and textbooks, seeking additional resources, practicing problems and exercises, seeking help from instructors or peers, and scheduling additional study sessions.
14. The process of implementing the action plan and regularly reviewing progress allows students to adjust their strategies as needed based on ongoing self-assessment and new feedback.
15. Learning is a continuous process, and it's okay to revise one's plan to better suit one's needs.

These key points summarize the main concepts and strategies for improvement covered in the text.

---

## Graph theory problem sheet Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/zywLI/graph-theory-problem-sheet)

Lesson 7.2 Isomorphic graphs adjacency matrix 7.3 Extra resources Video: Video Webinar on graphs . Duration: 1 hour 24 minutes 1h 24m Reading: Reading Graph theory problem sheet . Duration: 10 minutes 10 min Reading: Reading Graph theory problem sheet solutions . Duration: 10 minutes 10 min Graph theory problem sheet tutorial-topic7-graphs.pdf PDF File Mark as completed Dislike Report an issue

---

## Graph theory problem sheet solutions Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/GADLi/graph-theory-problem-sheet-solutions)

There is no text provided to summarize. The given text appears to be a list of resources and study materials related to graph theory, but it does not contain any specific information or concepts to summarize. If you could provide the relevant text, I would be happy to help you summarize it in 4 sentences, preserving key information, formulae, and technical details.

---

