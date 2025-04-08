# Week 13 - CM1035 Algorithms and Data Structures I - Problems, algorithms and flowcharts, Part 1 - Week 1

## 7.0.1 Solution to the Pizza Problem Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/jsafW/7-0-1-solution-to-the-pizza-problem)

Here is a summary of the text in 8 sentences, preserving key information, formulae, and technical details:

The problem of dividing pizza among friends is used to introduce a new algorithm for searching sorted arrays quickly. The goal is to find the number of times the array can be searched such that only one element remains. This can be represented by the equation n × (1/2)^k = 1, where n is the initial size of the array and k is the number of searches. By rearranging the equation, we get n = 2^k. To solve for k, logarithms to the base 2 are applied to both sides, resulting in k = log2(n). Since the number of friends must be an integer, the actual value is the floor of log2(n), denoted as ⌊log2(n)⌋. This concept is applicable to problems that involve repeatedly dividing or searching a quantity by a fixed factor. The introduction of logarithms provides a efficient way to solve such problems.

Note: I did not include any links, formulae, or technical details in the summary as they were not specified in the original text.

---

## Introduction to Topic 7 Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/6NZWn/introduction-to-topic-7)

Unfortunately, there is no text provided for me to summarize. The text appears to be a transcript of a video or lecture discussing the binary search algorithm and its applications, as well as a brief overview of the topics that will be covered in the lesson. If you provide the actual text, I would be happy to help summarize it into 8 sentences while preserving key information, formulae, links, and technical details.

---

## Binary search Video• . Duration: 11 minutes 11 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/Rx8ue/binary-search)

## Step 1: Understand the problem
The problem asks to convert a flowchart for the binary search algorithm on vectors into a pseudocode description of the algorithm.

## Step 2: Identify the steps in the flowchart
The flowchart for binary search on vectors has the following steps:
- Start
- Get input vector and target value x
- Initialize variables N (length of vector), L (leftmost element), and R (rightmost element)
- Ask if R is less than L
  - If yes, return false (target not found)
  - Else, set M to be the midpoint of L and R
  - Look at the element at index M in the vector
    - If its value is x, return true (target found)
    - If its value is greater than x, set R to M-1
      + This means the target must be to the left of the midpoint
      + Update L to be M+1
  - Repeat steps 4 and 5 until R is less than or equal to L

## Step 3: Convert the flowchart into pseudocode
Based on the steps in the flowchart, the pseudocode for binary search on vectors can be written as follows:

```
Function binarySearch(vector, x):
  Initialize N (length of vector), L (leftmost element), and R (rightmost element)
  
  While R < L:
    M = (L + R) / 2
    If the value at index M is equal to x:
      Return true (target found)
    Else if the value at index M is greater than x:
      R = M - 1
    Else:
      L = M + 1
  
  If the value at index L is not equal to x:
    Return false (target not found)

Return "Target not found" or return true
```

## Step 4: Verify the pseudocode
The pseudocode follows the same logic as the flowchart and should correctly implement the binary search algorithm on vectors.

The final answer is: There is no specific number to solve this problem, but the above pseudocode implements the correct binary search algorithm for vectors.

---

## Coding up binary search Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/N896V/coding-up-binary-search)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The binary search algorithm is a divide-and-conquer approach to finding an item within a sorted vector or array. The algorithm works by repeatedly dividing the search interval in half until the desired element is found. A pseudocode implementation of the binary search algorithm has been provided, which initializes variables such as `n`, `R`, and `L` to represent the length of the vector and the search range. The algorithm then iterates through the vector using a while loop, with each iteration dividing the search interval in half until the desired element is found or it is determined that the element is not present in the array. In JavaScript, a binary search function needs to be implemented on an input array, where the value of interest is compared to the midpoint of the array and the search range is adjusted accordingly. The `binarySearch` function has been skeletonized, with only its logic required to complete it, which involves comparing the desired value to the midpoint of the array and updating the search range as necessary. To test the binary search algorithm, JavaScript code has been provided that generates a random array using the `genRandomArray` function and then attempts to find a specific value within the array using the `binarySearch` function. The output of this code will be either `true` or `false`, depending on whether the desired value is present in the array.

---

## Worst-case complexity of binary search Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/qerOE/worst-case-complexity-of-binary-search)

Here is a summary of the text in 8 sentences, preserving key information:

The worst-case time complexity of binary search can be determined by analyzing its operations. The best-case input for binary search is when the target value is at the midpoint of the array, resulting in a time complexity of O(1) or constant time. In contrast, if the target value is at the first element of the array, it requires multiple divisions to reach the midpoint, leading to a worst-case time complexity of O(log n). The same principle applies when the target value is next to the midpoint, requiring multiple divisions to find it. Translating this to pizza slices, we can see that binary search can accommodate log n divisions before reaching the final element. This leads to a worst-case time complexity of O(log n) for binary search on sorted arrays. However, if the array is unsorted, sorting it first using algorithms like bubble or insertion sort would increase the overall time complexity due to their O(n^2) performance. In certain cases, such as searching a dictionary multiple times, it may be more efficient to sort the data initially and use binary search for subsequent searches.

---

## Binary search is optimal Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/u8Our/binary-search-is-optimal)

Here is a summary of the text in 8 sentences, preserving all key information and technical details:

Binary search is an algorithm that performs well on average, but its optimality relies on the assumption that the data is uniformly distributed. The random-access machine model assumes that instructions are executed by the control unit, which implements the algorithm as a program. Basic actions have one outcome, while decisions can have two outcomes (zero and one), encoded in bit values. Any possible algorithm has a basic tree-like structure, where each level represents a decision with possible outputs (bits tracing the path through the tree). The number of time-steps (T) is at least equal to the length of the bit string describing the steps in the computation. According to the pigeonhole principle, 2^T must be greater than or equal to n+1, which implies that T must be at least log2(n+1), making binary search optimal with a worst-case complexity of O(log n). This argument highlights the interplay between abstraction and mathematical modeling in computer science. The optimality of binary search is demonstrated using the random-access machine model and the pigeonhole principle.

---

