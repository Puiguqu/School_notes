# Week 7 - CM1035 Algorithms and Data Structures I - Problems, algorithms and flowcharts, Part 1 - Week 1

## Solution to the Theseus and Minotaur problem Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/EwUjP/solution-to-the-theseus-and-minotaur-problem)

Here is a summary of the text in 8 sentences, preserving key information:

The problem of searching through data structures is a fundamental concept in computing, with many applications such as internet search engines like Google. To solve this problem, it's essential to understand the structure of the data, which can be a vector, stack, or queue. The Theseus and Minotaur problem illustrates how a solution can be implemented using a stack, where cards are used to mark out the route through the labyrinth. Each card represents a junction and the direction to take, allowing Theseus to backtrack and adjust his path when encountering a dead end. By discarding the top card that led to an incorrect route, Theseus can replace it with a new card indicating the correct direction. This solution demonstrates how stacks can be useful in solving certain problems, particularly those involving sequential data. The problem of searching through data structures is closely related to dynamic arrays and searching algorithms, which are discussed later in the topic. Understanding these concepts is crucial for implementing efficient solutions to search-related problems.

---

## Arrays Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/TwMoJ/arrays)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The topic of searching in Computer Science involves finding a desired value within a collection of data. Abstract data structures, such as Booleans, integers, vectors, queues, and stacks, provide a framework for approaching problem-solving. However, implementing these data structures on a computer requires a more concrete approach, which is where arrays come into play. An array is a method of organizing multiple pieces of data, with each element assigned a location in memory, referred to as an index. The size of an array can be fixed or dynamic, and computers can read, write, and overwrite values within the elements. Arrays can also implement other data structures, such as vectors, by storing additional information, like length. In the context of searching, arrays can be used to implement stacks and queues. This topic is introduced in Lesson 4.1, which covers dynamic arrays, and is further explored in subsequent lessons.

---

## Dynamic arrays Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/TgxE6/dynamic-arrays)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

A dynamic array is an abstract data structure that combines the benefits of vectors and arrays. It is a finite sequential collection of data with operations like length, select[k], store![o,k], removeAt![k], and insertAt![o,k]. The dynamic array has all the operations of a vector but not vice versa. Its length operation can return different values at different points while it's being used. The dynamic array also allows for removing an element at index k and inserting an element at index k with operations removeAt![k] and insertAt! [o,k]. The implementation of a dynamic array uses an array data structure by creating new arrays when the size needs to be increased, copying elements from the old array, and adding new elements. This process allows for efficient growth and manipulation of the dynamic array.

---

## Linear search algorithm Video• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/ihhPi/linear-search-algorithm)

I can help you with the problem. Here's a step-by-step solution:

## Step 1: Define the Problem
The problem is to search for a specific birthday within a given decimal expansion of pi, which is stored in a vector.

## Step 2: Understand the Algorithm
We need to implement a linear search algorithm to find the birthday within the pi decimal expansion. This involves iterating through each digit of the pi decimal expansion and comparing it with the corresponding digit of the birthday.

## Step 3: Initialize Variables
We need to initialize two vectors, one for the pi decimal expansion and another for the birthday. We also need to set a flag to indicate whether the birthday has been found.

## Step 4: Iterate Through Pi Decimal Expansion
We iterate through each digit of the pi decimal expansion using a loop, starting from the first digit (index 0).

## Step 5: Compare with Birthday
For each digit in the pi decimal expansion, we compare it with the corresponding digit of the birthday. If they match, we set the flag to true and break out of the loop.

## Step 6: Return Flag Value
After iterating through all digits, if the flag is still false, it means the birthday was not found, so we return a message indicating that the birthday is not in the pi decimal expansion.

## Step 7: Implement the Algorithm

Here's some sample code to implement the algorithm:
```
function searchBirthday(piDecimalExpansion, birthday) {
  let found = false;
  for (let i = 0; i < len(piDecimalExpansion); i++) {
    if (piDecimalExpansion[i] == birthday[i]) {
      found = true;
      break;
    }
  }
  return found ? "Found in pi decimal expansion" : "Not found in pi decimal expansion";
}
```
Note: This code assumes that the pi decimal expansion is stored in a vector of digits and the birthday is also stored in a vector of digits.

The final answer is: There is no specific numerical answer to this problem, as it involves implementing an algorithm. However, I can provide you with a sample solution in a programming language of your choice.

---

## Searching π Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/8x2jM/searching-p)

This is a transcript of a video lecture on searching algorithms, specifically the linear search algorithm. The lecturer discusses how to implement the linear search algorithm in different data structures, including vectors, stacks, and queues.

The lecturer starts by explaining that the linear search algorithm is used to find an element in a list or array by iterating through each element and checking if it matches the target value.

**Linear Search Algorithm**

The lecturer provides a step-by-step explanation of how to implement the linear search algorithm:

1. Initialize two variables: `i` (index) and `target` (value to be searched).
2. Set `i` to 0, which represents the first element in the list.
3. Loop until `i` is greater than or equal to the length of the list:
	* Compare the value at index `i` with the target value.
	* If they match, return the index `i`.
	* Otherwise, increment `i` by 1 and repeat step 2.

The lecturer provides examples of how to implement the linear search algorithm in different programming languages, including Python, Java, and C++.

**Vectors**

The lecturer explains that vectors are similar to arrays but allow for dynamic resizing. To search a vector using the linear search algorithm, you can use a similar approach as with arrays, but keep track of the current size of the vector and adjust it as needed.

**Stacks and Queues**

The lecturer notes that stacks and queues do not support random access, which means you cannot directly access an element at a specific index. To search a stack or queue using the linear search algorithm, you would need to use a data structure like a linked list or array to store all the elements of the stack or queue initially.

**Discussion Prompt**

The lecturer invites viewers to discuss how they could implement the linear search algorithm in stacks and queues while preserving the initial data structure.

**Additional Page Content**

The transcript includes additional page content, including:

* Lesson 4.0 Introduction to Topic 4
* Lesson 4.1 Dynamic Arrays
* Lesson 4.2 Introduction to searching

The lecturer also provides links to practice assignments and videos on searching π (pi) and searching stacks and queues.

Overall, the lecture aims to provide a comprehensive introduction to linear search algorithms and their applications in different data structures.

---

## Searching stacks and queues Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/ctKfB/searching-stacks-and-queues)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Searching a stack without losing data can be achieved by using two stacks. The first stack represents the original data structure, and the second stack stores elements that are popped off the first stack during the search process. To find an element with value x in the stack, the algorithm checks the top of the initial stack and pushes its value to the second stack if it's not equal to x. Then, it pops the top element off the initial stack and repeats the process until the desired value is found or the stack is empty. If the desired value is found, the algorithm returns true; otherwise, it returns false. Searching a queue without losing data can be achieved by using a similar approach, but with a queue instead of a stack. However, searching a queue introduces an infinite loop problem if the target element is not in the queue. To resolve this issue, an "end of queue" value is introduced and used to break out of the infinite loop, allowing the algorithm to inspect every element of the queue.

Note that there are no links or technical details mentioned in the text, so I have omitted them from the summary.

---

## Implementing stacks and queues with arrays Reading• . Duration: 50 minutes 50 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/supplement/avjqz/implementing-stacks-and-queues-with-arrays)

Here is a summary of the provided text in 8 sentences:

The reading task requires students to understand how stacks and queues are implemented using simple arrays, with a focus on pointers that store indices rather than memory addresses (as discussed in Cormen et al.'s Introduction to Algorithms textbook). The first memory location in an array is indexed by 1, but can be adjusted by subtracting 1 to match the course convention. Vectors have their first index equal to 1 in this course, whereas Cormen et al. assume it's stored in memory elsewhere. When implementing vectors with arrays, the length of the vector is explicitly stored in the element at index 0. The Essential reading for the programme is available online via E-Book Central (ProQuest), and students can access the ebook via this link or by logging into E-Book Central directly. The reading task includes videos on solving the Theseus and Minotaur problem, arrays, stacks and queues with arrays implementation, dynamic arrays lesson, and introduction to searching. Students should complete Section 10.1 of Cormen et al.'s Introduction to Algorithms textbook to gain a good understanding of how stacks and queues are implemented using simple arrays. The reading task aims to provide students with a solid foundation in data structures and algorithms.

---

