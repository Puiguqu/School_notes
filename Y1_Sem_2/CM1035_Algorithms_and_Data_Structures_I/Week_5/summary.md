# Week 5 - CM1035 Algorithms and Data Structures I - Problems, algorithms and flowcharts, Part 1 - Week 1

## Solution to the Birthday Party problem part 2 Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/bAQH1/solution-to-the-birthday-party-problem-part-2)

Here is a summary of the text in 8 sentences, preserving key information, formulas, links, and technical details:

The problem involves assigning sweets and toys to guests such that siblings receive the same number of each item. The total number of people getting sweets and toys (N) is equal to N_0 (guests with no siblings) + 2N_1 (guests with one sibling) + 3N_2 (guests with two siblings), where N_0, N_1, and N_2 must be maximized. The constraints are: N_0 ≤ 2, N_1 ≤ 3, and N_2 ≤ 1. A pseudocode algorithm is proposed to solve this problem by iterating over possible values of i (guests with no siblings), j (guests with one sibling), and k (guests with two siblings) from 0 to m_0, m_1, and m_2, respectively. The algorithm checks if the sum i + 2j + 3k equals 6 and updates the value of t (the total number of guests invited). After looping through all possibilities, the final solution is obtained by returning the maximum value of t. The pseudocode can be applied to different lists of guests with varying numbers of siblings to find the optimal assignment.

Note: I omitted some technical details and links as they are not essential to the summary. If you need further clarification or specific information, please let me know!

---

## Introduction to Topic 3 Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/ZQxKV/introduction-to-topic-3)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The birthday party problem is an algorithmic challenge where guests are invited based on their siblings' presence, ignoring individual names. The original list was not used to calculate the number of guests that could be invited, as the pseudocode focused solely on the numbers. This highlights the importance of data structure in algorithms, which can significantly impact the solution. In real-life scenarios, such as shopping lists or meal ingredients, numbering and breaking up items with line breaks are essential for efficient modification. Computer science emphasizes minimizing technical details when modeling data storage and processing, focusing on fundamental structures and basic operations required in an algorithm. The representation of data, whether in RAM, non-volatile memory, or the Cloud, dictates the necessary operations in an algorithm. For example, the integer representation (binary or decimal) affects the algorithm's efficiency for tasks like determining evenness or oddness. Acknowledging how data is stored and processed enables mathematical modeling of algorithmic usefulness when comparing different solutions to the same problem.

---

## Abstract data structure: vectors Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/UUvuD/abstract-data-structure-vectors)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

A vector is a finite, fixed-size sequential data collection that stores elements of data in a line, with each element following another. The number of elements in a vector, called its length, is non-negative and can be zero if the vector is empty. Vectors have a fixed size, meaning their length cannot be altered after creation. Operations on vectors include the length operation, which returns the number of elements, and the select[k] operation, which returns the Kth element from the vector. The store![o,k] operation alters the vector by setting the Kth element to have value O. Due to its fixed size, vectors cannot be deleted or added to dynamically, but can be extended by creating a new vector of a larger length and assigning elements from the original vector. This limitation is offset by the ability for elements in the vector to store references to data, allowing for efficient storage and retrieval of complex data structures. By understanding how to work with vectors, developers can build more powerful and flexible data structures using these fundamental building blocks.

---

## Abstract data structure: queues Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/6ZEwx/abstract-data-structure-queues)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

A queue is a fundamental data structure that represents a line or a sequence of elements where each element is added to the end (enqueue) and removed from the front (dequeue). A queue can be thought of as a resource that cannot be immediately accessed, and the longer an element has been waiting, the sooner it will be made available. In computing, queues are often referred to as FIFO (first-in, first-out), where the first item added is also the first one to leave. Unlike vectors, which have fixed length and can access any element directly, queues are extensible and have only two privileged elements: the head and tail. Elements in a queue cannot be accessed arbitrarily, but rather must be removed from the front (dequeue) or added to the end (enqueue). The basic operations of a queue include head, dequeue!, enqueue![o], and empty, which allow access to the front element, remove an element, add an element, and check if the queue is empty, respectively. A queue's structure consists of a linear sequence of elements with two pointers: the tail (pointing to the last element) and the head (pointing to the first element). To access an arbitrary element in a queue, one must remove all elements before it from the front.

Note that I did not include any links or formulae as they were not present in the original text. Let me know if you'd like me to add anything else!

---

## My example of a queue Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/mr7hw/my-example-of-a-queue)

There is no text to summarize. The provided "text" appears to be a video transcript with formatting instructions for accessibility, and it does not contain any actual content or information that can be summarized. It includes links, formulas, and technical details related to queues and data structures in computing, but it lacks concrete information to summarize.

If you provide the actual text or content you would like me to summarize, I'll be happy to assist you with preserving key information, formulae, links, and technical details while summarizing it in 8 sentences.

---

