# Week 15 - CM1035 Algorithms and Data Structures I - Problems, algorithms and flowcharts, Part 1 - Week 1

## 8.0.1 Solution to the substitution cipher problem Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/egw5N/8-0-1-solution-to-the-substitution-cipher-problem)

Here is a summary of the text in 8 sentences, preserving key information:

The goal of this problem is to generate all permutations of elements in a vector using dynamic arrays. To simplify the problem, an alphabet of four letters (A, B, C, D) is used instead of the entire English alphabet. A stack is used to store previous permutations of vectors, and a hybrid data structure is employed where stacks store vectors. The process starts with generating permutations for single elements, then moves on to two-letter combinations using a stack S to store these permutations. Once all permutations of two letters are generated, they are pushed into a new stack p containing the permutations of three letters. Then, each permutation in stack p is used as a starting point to generate new permutations of four letters by inserting C before, after, or between A and B. After generating permutations for four letters, stack p is emptied, and its contents are pushed onto a dynamic array along with the remaining elements in stack S. The goal is to use this process to generalize the solution for any number of letters using recursion.

Note that no specific formulae, links, or technical details were provided in the original text, so I did not include them in the summary. However, the main concepts and findings are preserved.

---

## Introduction to Topic 8 Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/iNHz4/introduction-to-topic-8)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Recursion is a fundamental concept in mathematics, language, and computer science that involves self-referential instructions. The idea behind recursion is to start with a small set of instructions that can be repeated infinitely or until a certain condition is met. This process is often compared to cooking a recipe from a cookbook, where the instructions loop back to themselves. In the context of computers, recursion is used to implement algorithms that can solve complex problems by breaking them down into smaller sub-problems. The goal of using recursion in algorithms is to utilize its power while avoiding infinite loops, which can lead to impractical solutions. To understand recursion, it's essential to analyze how algorithms are recast as recursive instructions and implemented when running a program. Recursion can be challenging to grasp initially, but examples and explanations can help clarify its implementation. The topic will explore recursion through various examples, including the substitution cipher problem and decreasing and conquering approaches.

Note that there is no formula or link in the original text, so I did not include any of those in the summary.

---

## Decrease and conquer Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/3UVTm/decrease-and-conquer)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Recursion involves self-reference to tackle problems by reducing them into smaller instances with the same problem type. The "decrease and conquer" algorithm approach uses recursion to solve general problems by breaking them down into smaller sub-problems of the same type. The factorial function is a classic example of recursion, where the result is calculated as the product of all positive integers up to n (n! = n × (n-1) × ... × 1). Another example is the Fibonacci sequence, where each number is the sum of the two preceding ones (F(n) = F(n-1) + F(n-2)) with base cases F(0) = F(1) = 1. The recursive Euclidean algorithm can be used to solve the birthday party problem and other similar problems by breaking them down into smaller sub-problems until the solution is found. Recursion allows for elegant and straightforward algorithm design, especially when combined with divide-and-conquer approaches. However, it's essential to include base cases and checks for incorrect input to prevent infinite recursion. Additionally, while recursion can simplify code and analysis, it can also be less efficient in terms of computational resources compared to iterative solutions.

---

## Recursive Euclidean algorithm Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/2y6PY/recursive-euclidean-algorithm)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The Euclidean algorithm is a method for finding the greatest common divisor (GCD) of two integers A and B. The algorithm uses a while loop to repeatedly subtract the smaller number from the larger one until they are equal, at which point the GCD is returned. The algorithm can also be implemented recursively by applying the same logic to A minus B and B, repeating this process until X and Y are both 1, indicating that the GCD has been found. The recursive implementation requires a base case, where if A equals B, the function returns A. In contrast to iteration, recursion simplifies the expression of solutions to problems by allowing for more compact code. The Euclidean algorithm can also be used as a building block to solve other problems, such as finding the GCD of multiple numbers. The problem of writing algorithms using recursion and combination with iteration is left as an exercise in the next video. The lesson concludes with an introduction to Topic 8 and suggests watching videos on decrease and conquer, recursive Euclidean algorithm, and recursion examples for further learning.

---

## Recursive searching and sorting Video• . Duration: 13 minutes 13 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/BCBbu/recursive-searching-and-sorting)

This is a transcript of a lecture on recursive algorithms, covering three topics: Decrease and Conquer, Recursion Examples, and Practice Assignments.

The lecturer begins by introducing the concept of Decrease and Conquer, which is a common strategy used in algorithm design. They explain that this approach involves breaking down a problem into smaller sub-problems until we reach a trivial solution, and then combining the solutions to solve the original problem.

Next, the lecturer presents several examples of recursive algorithms, including:

1. Recursive Searching: This algorithm uses recursion to find an element in a sorted array.
2. Recursive Sorting: This algorithm uses recursion to sort an array using the Decrease and Conquer strategy.
3. Insertion Sort: This algorithm uses recursion to sort an array by inserting elements into their correct position.

The lecturer provides pseudocode for each of these examples, illustrating how the recursive algorithm works step-by-step.

Finally, the lecturer presents several practice assignments for students to complete, including:

1. Recursive algorithms in JavaScript
2. Permutations revisited (a review of a previous topic)
3. Recursive binary search

The lecturer concludes by emphasizing the importance of understanding recursive algorithms and providing opportunities for students to practice their skills.

Overall, this lecture provides an introduction to recursive algorithms and covers several key topics, including Decrease and Conquer, recursion examples, and practice assignments. The content is suitable for students who have a basic understanding of programming concepts and are looking to learn more about recursive algorithms.

---

## Permutations revisited Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/8K2OG/permutations-revisited)

The text discusses the solution to generating permutations of letters using recursion. The pseudocode for this process is as follows:

```
function permutations(vector):
    if length(vector) ≤ 1:
        return vector
    else:
        s = []
        for i in alphabet:
            v = vector excluding i
            w = permutations(v)
            p = [i] + w
            append p to s
        return s
```

This pseudocode uses recursion to generate permutations of the letters in the input vector. It works by iterating over each letter in the alphabet, creating a new vector `v` that excludes the current letter, and then recursively generating permutations of `v`. The permutations of `v` are then appended to a new vector `p`, which is created by adding the current letter at the beginning of each permutation.

The key idea behind this recursive solution is that we can generate permutations of n letters by using the permutations of (n-1) letters and inserting the new letter in between the letters of the previous permutations. This approach allows us to avoid storing all the permutations of previous cases in a dynamic array or stack, making the implementation more efficient.

The text also mentions the binary search algorithm and asks the viewer to think about how it can be implemented recursively. It provides a practice assignment for implementing recursive algorithms in JavaScript.

Overall, the text emphasizes the importance of recursion in solving problems by breaking them down into smaller sub-problems that can be solved independently, and then combining the solutions to form the final answer.

---

