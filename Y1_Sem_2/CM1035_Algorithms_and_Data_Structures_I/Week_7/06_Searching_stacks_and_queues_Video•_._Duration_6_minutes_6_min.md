# Searching stacks and queues Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/ctKfB/searching-stacks-and-queues)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Searching a stack without losing data can be achieved by using two stacks. The first stack represents the original data structure, and the second stack stores elements that are popped off the first stack during the search process. To find an element with value x in the stack, the algorithm checks the top of the initial stack and pushes its value to the second stack if it's not equal to x. Then, it pops the top element off the initial stack and repeats the process until the desired value is found or the stack is empty. If the desired value is found, the algorithm returns true; otherwise, it returns false. Searching a queue without losing data can be achieved by using a similar approach, but with a queue instead of a stack. However, searching a queue introduces an infinite loop problem if the target element is not in the queue. To resolve this issue, an "end of queue" value is introduced and used to break out of the infinite loop, allowing the algorithm to inspect every element of the queue.

Note that there are no links or technical details mentioned in the text, so I have omitted them from the summary.

