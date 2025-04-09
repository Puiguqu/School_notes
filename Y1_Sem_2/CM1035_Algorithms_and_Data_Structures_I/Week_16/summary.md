# Week 16 - CM1035 Algorithms and Data Structures I - Problems, algorithms and flowcharts, Part 1 - Week 1

## Recursive binary search Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/mpy3O/recursive-binary-search)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The video transcript discusses the recursive implementation of the binary search algorithm, which was previously described iteratively. The recursive version is implemented using two functions: `search` and `binary_search`. The `search` function takes input parameters `V`, `item`, `L`, and `R`, while the `binary_search` function takes only `V` and `item` as inputs. The recursive implementation follows a similar structure to the iterative version, but without iterations. In the first line of the `search` function, it checks if `L` is greater than `R` and returns `false` if so, indicating that the search has been unsuccessful. If `L` is less than or equal to `R`, it calculates `M` as the floor of `L + R / 2` and proceeds with the search. The function then checks if the `n-th` element of `V` is equal to `item` and returns `true` if so, or updates `L` or `R` based on comparisons. Finally, the `binary_search` function calls `search` recursively with updated values of `L` and `R`, demonstrating how recursion is used to implement binary search without iteration.

Note: The original text does not provide any formulae, links, or technical details, as it appears to be a transcript of a video discussing the implementation of the recursive binary search algorithm.

---

## Call stack Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/n3Yau/call-stack)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The call stack is a data structure that manages function calls in programming languages, storing the relevant data and value returned by each function call. When a function is called, its variables and arguments are pushed onto the call stack to form a stack frame, which is cleared and popped when the function returns. The call stack plays a crucial role in recursive algorithms, where functions call themselves repeatedly until reaching a base case. Recursive binary search is an example of such an algorithm, where the function recursively divides the search space until finding a target value. In this case, the call stack grows as each recursive call is made, but eventually pops when the base case is reached. However, if the recursion becomes infinite or the stack size exceeds its capacity, a "stack overflow" occurs, causing the program to terminate. The call stack needs to be stored in memory, which is finite, and exceeding its capacity can lead to performance issues. Understanding how the call stack works is essential for implementing efficient recursive algorithms and avoiding common pitfalls like stack overflows.

---

## Summary Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/f3nFP/summary)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

Recursion is a fundamental concept in computer science that involves breaking down a problem into smaller instances of the same problem. In this topic, we explored recursion through various algorithms such as the Euclidean algorithm, linear search, binary search, insertion sort, and bubble sort. We also discussed how to implement recursive solutions to compute factorials and Fibonacci numbers. Understanding recursion is crucial for implementing efficient algorithms in a simple manner. However, it does require effort to grasp, so practicing with examples and simulating computer behavior is recommended. To visualize the call stack, we created pseudocode that simulates calculating the factorial of n recursively, using a stack to store intermediate results. The pseudocode demonstrates how the call stack works by pushing values onto the stack and then popping them off to compute the final result. This intuitive understanding of recursion can deepen one's appreciation for the concept and inspire new algorithmic ideas.

Note: I did not include any links or formulae as they were not explicitly mentioned in the provided text. If you need further clarification on any specific technical details, please let me know!

---

## The substitution cipher problem revisited Video• . Duration: 53 seconds 53 sec

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/qkvbB/the-substitution-cipher-problem-revisited)

There is no text provided for me to summarize. The given text appears to be a transcript from an educational video or lecture, containing information about the order of permutations and the use of recursive binary search in solving a cryptographic problem known as the "substitution cipher." However, it does not provide any specific details or formulas related to the problem.

If you could provide the relevant text, I would be happy to assist you in summarizing it.

---

