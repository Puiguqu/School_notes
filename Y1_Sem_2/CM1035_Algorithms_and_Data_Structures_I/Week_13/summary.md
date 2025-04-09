# Week 13 - CM1035 Algorithms and Data Structures I - Problems, algorithms and flowcharts, Part 1 - Week 1

## 7.0.1 Solution to the Pizza Problem Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/jsafW/7-0-1-solution-to-the-pizza-problem)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The problem of dividing pizza among friends can be solved using logarithms to determine the number of times the pizzas need to be divided to leave only one slice. The expression for this is n * (1/2)^k = 1, where n is the initial number of slices and k is the number of times the pizzas are divided. By moving 2^k to the other side, we get n = 2^k. To find k, we take logarithms base 2 of both sides, resulting in k = log2(n). Since the number of friends must be an integer, we take the floor of log2(n) to ensure it's an integer value.

The problem is relevant to algorithms and data structures as it introduces a fundamental concept: when considering something a certain number of times, the number of times can be calculated using logarithms. This idea will be explored further in this new topic, but for now, the key takeaway is that logarithms can help solve problems like the pizza division problem.

---

## Introduction to Topic 7 Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/6NZWn/introduction-to-topic-7)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The main focus of this topic will be on the binary search algorithm, which searches vectors and arrays for values by dividing them into two halves until the target value is found. This algorithm has an advantage over linear search because it can search sorted vectors and arrays much faster. The main goal of this topic is to compare binary search with other search algorithms using a comparison tool. To do so, we will use our acquired tools for algorithm comparison to show why binary search is more efficient. Additionally, this topic will explore the concept of divide-and-conquer and its application in solving problems that seem unrelated to searching arrays and vectors. The reasoning behind search algorithms can be applied to other problems by dividing them into smaller sub-problems and finding solutions recursively. The worst-case time complexity of an algorithm determines whether it is suitable for solving certain types of problems, and binary search has a guaranteed best-case time complexity of O(log n). By analyzing the problem of searching in sorted arrays and vectors, we can gain insights into how to approach similar problems in other contexts.

---

## Binary search Video• . Duration: 11 minutes 11 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/Rx8ue/binary-search)

The provided transcript appears to be a lecture or video on the binary search algorithm, specifically for vectors and arrays. The content includes:

1. An explanation of how the binary search algorithm works.
2. A flowchart illustrating the steps involved in the algorithm.
3. A discussion of the advantages of using binary search over linear search.

The final section mentions converting the flowchart into pseudocode and then turning it into working JavaScript code.

Here is a simplified version of the pseudocode for the binary search algorithm:

**Binary Search Algorithm**

**Input:** `arr` (sorted vector or array), `target`

**Output:** `true` if `target` is found in `arr`, `false` otherwise

1. Set `L` to 1 and `R` to the length of `arr`
2. While `L` <= `R`
3. Calculate `M` = `(L + R) / 2`
4. If `arr[M] == target`
5. Return `true`
6. If `arr[M] < target`
7. Set `L` to `M + 1`
8. Else
9. Set `R` to `M - 1`
10. Repeat steps 3-9 until found or not found

The pseudocode is a concise representation of the algorithm's logic, and it can be used as a starting point for implementing the binary search in JavaScript.

**Note:** This is a simplified version of the pseudocode, and you may want to add additional error handling or input validation depending on your specific use case.

---

## Coding up binary search Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/N896V/coding-up-binary-search)

Here is a summary of the text in 8 sentences, preserving all key information:

The binary search algorithm is implemented in pseudocode as a function that takes a vector V and an item to find, returning true if the item is in the vector and false otherwise. The pseudocode initializes variables n (vector length), R (upper bound), L (lower bound), and m (midpoint) for the while loop, which continues until R >= L. In this video transcript, a JavaScript function binarySearch is developed to implement binary search on an array, requiring a sorted array for proper functionality. The file includes the genRandomArray function to create a random array with n elements, swap function for bubbleSort, and bubbleSort itself. An empty binarySearch function is defined, taking an array and item as inputs and returning true if the item is in the array and false otherwise. The file logs the output of bubbleSort and binarySearch with different input arrays and values to find, resulting in undefined output due to the incomplete implementation. To fix this, the student will complete the binarySearch function by implementing the correct logic for finding an element in a sorted array. By completing the practice assignment, students will gain hands-on experience with implementing binary search in JavaScript.

---

## Worst-case complexity of binary search Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/qerOE/worst-case-complexity-of-binary-search)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The worst-case time complexity of linear search was found to be O(n), while binary search has been computed to have a worst-case time complexity of O(log n). The best-case input for binary search occurs when the value being searched for is at the midpoint of the vector, resulting in a time complexity of O(1) or constant. In contrast, the first element of the vector in linear search results in the best case scenario due to early inspection. Worst-case inputs for binary search include scenarios where the value is stored in the first element of the vector or next to the midpoint, requiring multiple divisions by two until reaching a single-element vector. The key observation here is that each step of inspecting the midpoint and not finding the value results in halving the vector, which translates to O(log n) inspections in total. This principle also applies when considering scenarios with n slices of pizza being divided among friends, illustrating the exponential reduction in operations. Binary search has a significant advantage over linear search for sorted arrays, with a worst-case time complexity that is exponentially smaller (O(log n) vs O(n)). However, using binary search on unsorted arrays may not be effective without sorting first, as the sorting algorithm's time complexity can dominate the overall process, making linear search more suitable in such cases.

---

## Binary search is optimal Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/u8Our/binary-search-is-optimal)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The binary search algorithm is considered optimal for searching in an array or vector, assuming no prior knowledge of the stored data. This is proved using the random-access machine model, where the focus is on the control unit's implementation of the algorithm. The basic operations (addition) are ignored, while decisions with two possible outcomes (0 and 1) are considered. The algorithm can be represented as a tree-like structure, where each decision node corresponds to a bit string tracing the path through the computation. There are n+1 possible outputs, and the number of time-steps (T) must be at least the length of the bit string describing the steps in the computation. Using the pigeonhole principle, it can be shown that 2^T ≥ n+1, which implies T = O(log n). This result proves that binary search is optimal, as it achieves a worst-case complexity of O(log n), which is already achievable by the algorithm. The use of abstraction and mathematical modeling in this proof highlights the interplay between computer science and mathematics.

---

