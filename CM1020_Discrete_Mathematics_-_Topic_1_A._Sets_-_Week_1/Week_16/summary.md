# Week 16 - CM1020 Discrete Mathematics - Topic 1 A. Sets - Week 1

## Rooted trees Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/i1CY9/rooted-trees)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A rooted tree is a directed tree with a distinguished vertex called the root, such that there is a directed path from the root to every other vertex. A rooted tree can be represented as a graph if one vertex has an in-degree of zero, while all other vertices have an in-degree of one. The depth or path length of a node in a tree is the number of edges from the root to that node. The height of a node in a tree is the longest path from that node to a leaf. The depth of a tree, also known as its height, is the maximum path length across all its nodes.

A binary tree is a rooted tree with every vertex having two or fewer children. A ternary tree is a rooted tree with every vertex having three or fewer children. An m-ary tree is a rooted tree with every vertex having m or fewer children. An m-ary tree is regular if every internal node has exactly m children.

The maximum number of vertices at level h in an m-ary tree is m^h, while the maximum number of edges in an m-ary tree of h levels is m_h + 1 - 1 / (m - 1).

Two graphs, trees, or trees with different degree sequences are not isomorphic. Two trees with the same degree sequence may or may not be isomorphic.

An isomorphism between two graphs is a bijection that preserves adjacency and non-adjacency. For rooted trees, an isomorphism also requires mapping the root of one tree to the root of the other tree.

Isomorphic trees as rooted trees have additional properties, such as having the same degree sequence at each level.

---

## Binary search trees Video• . Duration: 14 minutes 14 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/XYlri/binary-search-trees)

It appears that the provided text is a transcript of a lecture or educational material related to computer science and data structures, specifically covering the topics of rooted trees and binary search trees.

The transcript includes various sections, such as:

1. "Definition and uses of binary search trees"
2. "Building a binary search tree" (with an example)
3. "Relationship between the number of stored records and the height of the binary tree"

Additionally, there are mentions of related topics, including:

* "Rooted trees"
* "Binary search algorithms"
* "Linear searches"
* "Trees assignment"
* "Topic 8 summary"

The transcript is divided into various sections, each with a specific duration, indicating that it may be part of an online course or educational resource.

Some notable points from the transcript include:

* Binary search trees are data structures used for efficient searching and storage of data.
* They consist of nodes that contain values and references to child nodes.
* The height of a binary tree is the number of edges between the root node and the farthest leaf node.
* The relationship between the number of stored records and the height of the binary tree can be expressed using the formula: 2^h - 1 ≤ n ≤ 2^h, where h is the height of the tree and n is the number of stored records.

Overall, the transcript appears to provide a comprehensive overview of binary search trees, including their definition, construction, and properties.

---

## Rooted trees Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/1PwaC/rooted-trees)

Here is a summary of the text in 15 sentences:

Rooted trees are a fundamental concept in graph theory with wide-ranging applications in computer science, data structures, and algorithms. Understanding rooted trees is essential for tackling problems involving hierarchical structures and recursive data. A rooted tree is defined as a tree where each node has at most two children. The root of the tree is the topmost node, while parent-child relationships are established between nodes. Siblings are nodes with the same parent, and leaves are nodes with no children. Internal nodes are those that have children. Tree levels and height refer to the depth and distance from the root node. Binary trees are a type of rooted tree where each node has at most two children. Binary search trees (BSTs) facilitate efficient searching, insertion, and deletion operations by maintaining a sorted order. Balanced trees like AVL trees and Red-Black trees maintain balanced heights to ensure optimal performance. Understanding these concepts is crucial for working with hierarchical structures in computer science. The study of rooted trees has wide applications in data structures and algorithms. Rooted trees are used to model real-world hierarchies, such as file systems or organizational structures. Learning about rooted trees equips students with the necessary skills to tackle complex problems involving recursive data and hierarchical structures.

---

## Binary search trees Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/FTdMQ/binary-search-trees)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A binary search tree (BST) is a type of binary tree that maintains a sorted order of elements. Each node in a BST contains a value, pointer to the left child, and pointer to the right child. The BST property states that the left subtree of a node contains only nodes with values less than the node's value. The right subtree of a node contains only nodes with values greater than the node's value. Both the left and right subtrees must also be binary search trees. To build a binary search tree, one can start with an empty tree and recursively add nodes with values that maintain the BST property. The height of a binary search tree is determined by the maximum depth of the tree, which is calculated using the formula H = log2(n), where n is the number of nodes in the tree. Binary trees are used to search for values on a sorted list by traversing the tree from left to right. This type of search is more efficient than linear searches, especially for large datasets. To find the height of a binary search tree, one can use the formula H = log2(n) or recursively traverse the tree and keep track of the depth. The key concept in building a binary search tree is maintaining the BST property, which ensures that all nodes are sorted. Understanding how to build and traverse binary search trees is essential for searching large datasets efficiently.

---

## Rooted and binary search trees Reading• . Duration: 2 hours 10 minutes 2h 10m

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/joTQH/rooted-and-binary-search-trees)

Here is a summary of the text in 15 sentences:

The provided text discusses two topics: rooted trees and binary search trees, which will be covered from Koshy's pp.646-52 and pp.664-68 and Levin's pp.251-53. The work is licensed under Creative Commons Attribution- Alike 4.0 International License. After completing the reading, students are encouraged to attempt exercises from Koshy's textbook, specifically exercises 5, 6, 15, and 16. These exercises have solutions provided at the back of the book for reference. Students can check their answers by consulting the Solutions to odd-numbered exercises section. If incorrect, they should review the question and try again. The topics covered include rooted trees and binary search trees.

The video "Rooted Trees" is available for 8 minutes, while the reading "Rooted Trees" takes approximately 15 minutes. A practice assignment for rooted trees also exists, lasting around 20 minutes. Similarly, a video titled "Binary Search Trees" can be found for 14 minutes, accompanied by a 15-minute reading on the same topic. Another practice assignment for binary search trees is available, also lasting around 20 minutes.

Additionally, there is a 2-hour and 10-minute reading that covers both rooted and binary search trees. There is also a discussion prompt titled "Binary and Linear Searches," which lasts 10 minutes. A peer-graded assignment on trees is scheduled to last an hour, and students are encouraged to review their peers' work as part of the Trees Assignment. Finally, a summary of topic 8 can be found for 15 minutes.

There are no key findings or formulae mentioned in this text, but rather instructions for further reading, exercises, and assignments related to rooted trees and binary search trees.

---

## Topic 8 summary Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/3rT20/topic-8-summary)

Here is a summary of the text in 15 sentences:

Trees are a crucial concept in discrete mathematics and computer science, with applications in hierarchical data representation, efficient data structures, algorithm design, database management, artificial intelligence, computational biology, and network design.

A tree is defined as a connected, acyclic graph with n vertices that has n-1 edges. A rooted tree is a tree with one designated root node, where every node (except the root) has exactly one parent.

There are several components of trees: the root is the topmost node, leaves are nodes with no children, and internal nodes have at least one child. The height of a tree is the length of the longest path from the root to a leaf, while depth or level refers to the number of edges from the root to a node.

Binary trees are characterized by each node having at most two children (left and right). Binary search trees (BSTs) are binary trees with the property that the left child's value is less than the parent's value and the right child's value is greater.

Balanced trees maintain a balanced height to ensure efficient operations. The sum of degrees of all vertices in a tree is 2(n-1), where n is the number of vertices. A tree with n vertices has n-1 edges.

Understanding these concepts allows students to analyze and work with various types of trees, implement efficient algorithms, and apply them to solve real-world problems. Regularly assessing understanding and capabilities against learning outcomes is crucial as the course progresses.

To improve understanding, students should review course materials and textbooks, seek additional resources, practice problems or exercises, seek help from instructors or peers, and schedule additional study sessions. Implementing an action plan and regularly reviewing progress will help adjust strategies as needed based on ongoing self-assessment and new feedback.

---

## Trees problem sheet Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/N16tq/trees-problem-sheet)

Lesson 8.2 Rooted trees and binary search trees. 8.3 Extra resources Reading: Reading Trees problem sheet . Duration: 10 minutes 10 min Reading: Reading Trees problem sheet solutions . Duration: 10 minutes 10 min

---

## Trees problem sheet solutions Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/LOL7f/trees-problem-sheet-solutions)

Lesson 8.2 Rooted trees and binary search trees. 8.3 Extra resources Reading: Reading Trees problem sheet . Duration: 10 minutes 10 min Reading: Reading Trees problem sheet solutions . Duration: 10 minutes 10 min Trees problem sheet solutions problem-sheet-trees-solution.pdf PDF File Mark as completed Dislike Report an issue

---

