# Abstract data structure: queues Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/6ZEwx/abstract-data-structure-queues)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

A queue is a fundamental data structure that represents a line or a sequence of elements where each element is added to the end (enqueue) and removed from the front (dequeue). A queue can be thought of as a resource that cannot be immediately accessed, and the longer an element has been waiting, the sooner it will be made available. In computing, queues are often referred to as FIFO (first-in, first-out), where the first item added is also the first one to leave. Unlike vectors, which have fixed length and can access any element directly, queues are extensible and have only two privileged elements: the head and tail. Elements in a queue cannot be accessed arbitrarily, but rather must be removed from the front (dequeue) or added to the end (enqueue). The basic operations of a queue include head, dequeue!, enqueue![o], and empty, which allow access to the front element, remove an element, add an element, and check if the queue is empty, respectively. A queue's structure consists of a linear sequence of elements with two pointers: the tail (pointing to the last element) and the head (pointing to the first element). To access an arbitrary element in a queue, one must remove all elements before it from the front.

Note that I did not include any links or formulae as they were not present in the original text. Let me know if you'd like me to add anything else!

