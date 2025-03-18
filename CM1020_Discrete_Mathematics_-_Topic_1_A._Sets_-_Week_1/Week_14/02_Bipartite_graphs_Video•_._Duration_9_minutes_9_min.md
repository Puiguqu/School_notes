# Bipartite graphs Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/VYQ8F/bipartite-graphs)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A bipartite graph is a special type of graph where the set of vertices can be divided into two sets, V1 and V2, such that each edge connects one vertex from V1 to one vertex from V2. A bipartite graph is two-colorable, meaning it can be represented using two colors, which are used to represent vertices in V1 (e.g., orange) and vertices in V2 (e.g., yellow). One important property of bipartite graphs is that they have no cycles of odd length.

A matching in a bipartite graph is a set of pairwise non-adjacent edges with no shared endpoints. A vertex is matched or saturated if it's an endpoint of one of the edges, otherwise it's unmatched. The maximum matching is the largest possible number of edges that can still form a matching when adding any edge would break it.

The Hopcroft-Karp algorithm is used to find the maximum matching in a bipartite graph. It uses two other algorithms: breadth-first search (BFS) and depth-first search (DFS). The algorithm starts with all nodes in each side of the graph where C and J have no pairings and iterates through BFS and DFS to find augmenting paths.

An augmenting path is an alternating sequence of unmatched edges ending on a free node, which augments the cardinality of the current machine. In the first iteration, BFS finds three trees connecting nodes in C to nodes in J. The maximum matching is found when an augmenting path is discovered from node J2 up to C1.

The second iteration starts with DFS and finds an augmenting path from node J3 up to C3. This results in a semi-matched graph. After the second iteration, every job seeker is matched to a job.

