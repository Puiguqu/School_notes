# Solution to the conversion problem Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/EIQQt/solution-to-the-conversion-problem)

Here is a summary of the text in 8 sentences, preserving key information:

The problem of converting an integer in decimal to binary can be solved using a stack, where each element in the stack represents a power of two. The central idea is to divide the number by two and push the remainder into the stack until there are no more remainders. This process simulates the way binary numbers are constructed from powers of two. The pseudocode for this solution involves creating an empty stack and repeatedly dividing the number by two, pushing the remainder onto the stack, and updating the number. If the floor of the number divided by 2 is not equal to 0, the remainder is pushed onto the stack; otherwise, the floor value is used as the new number. The process continues until there are no more remainders, at which point the stack represents the binary representation of the original number. The flowchart for this solution illustrates the steps involved in converting a decimal number to binary using a stack. By simulating the construction of binary numbers from powers of two using a stack, we can efficiently convert decimal integers to their binary equivalents.

