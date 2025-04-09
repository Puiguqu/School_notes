# Dijkstra's algorithm Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/72JIm/dijkstras-algorithm)

Here is a summary of the text in 8 sentences, preserving all key information, formulae, links, and technical details:

Dijkstra's algorithm is used to compute the shortest path between two vertices in a weighted graph. A weighted graph is a graph where each edge is assigned a numerical value, which can be used to model distances, response times, or costs in various applications. The algorithm works by iteratively visiting unvisited vertices and updating their shortest distance and previous vertex information. In the first iteration, the algorithm initializes the distance from the start vertex to all other vertices as infinity, except for itself, which is set to zero. In subsequent iterations, the algorithm visits the unvisited vertex with the smallest known distance from the start vertex, updates its neighbors' distances if necessary, and marks it as visited. The algorithm continues until all vertices have been visited, at which point the shortest path can be constructed by tracing back the previous vertices. Dijkstra's algorithm has a time complexity of O(E + V log V) in the worst case, where E is the number of edges and V is the number of vertices.

