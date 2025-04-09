# Call stack Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/n3Yau/call-stack)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The call stack is a data structure that manages function calls in programming languages, storing the relevant data and value returned by each function call. When a function is called, its variables and arguments are pushed onto the call stack to form a stack frame, which is cleared and popped when the function returns. The call stack plays a crucial role in recursive algorithms, where functions call themselves repeatedly until reaching a base case. Recursive binary search is an example of such an algorithm, where the function recursively divides the search space until finding a target value. In this case, the call stack grows as each recursive call is made, but eventually pops when the base case is reached. However, if the recursion becomes infinite or the stack size exceeds its capacity, a "stack overflow" occurs, causing the program to terminate. The call stack needs to be stored in memory, which is finite, and exceeding its capacity can lead to performance issues. Understanding how the call stack works is essential for implementing efficient recursive algorithms and avoiding common pitfalls like stack overflows.

