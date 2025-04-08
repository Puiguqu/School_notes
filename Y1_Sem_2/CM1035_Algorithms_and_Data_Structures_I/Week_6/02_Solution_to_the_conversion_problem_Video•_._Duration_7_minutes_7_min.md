# Solution to the conversion problem Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/EIQQt/solution-to-the-conversion-problem)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The problem of converting an integer from decimal to binary using a stack can be solved by dividing the number by 2 and pushing the remainder onto the stack repeatedly. The process continues until the floor of the remaining number over 2 equals 0. At this point, the final value pushed onto the stack is the most significant digit in the binary representation. The algorithm works by simulating this process using a while loop, where each iteration divides the current value and pushes the remainder onto the stack. If the result of the division is an even number, no new value is added to the stack. If the result is an odd number, a new value is pushed onto the stack. The algorithm terminates when the floor of the remaining number over 2 equals 0, at which point the final value pushed onto the stack is returned as the binary representation of the input number. This process can be implemented using pseudocode, where a while loop iterates through the steps of dividing and pushing remainders onto the stack.

