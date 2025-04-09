# Week 17 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Introduction Video• . Duration: 59 seconds 59 sec

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/xnsna/introduction)

There is no text to summarize beyond the initial VIDEO TRANSCRIPT section and ADDITIONAL PAGE CONTENT section. The provided text only includes the VIDEO TRANSCRIPT with a riddle about climbing stairs and the introduction to Lesson 9.0, which does not contain any technical details or formulas.

However, I can provide some context about recursion in general:

Recursion is a programming concept where a function calls itself repeatedly until it reaches a base case that stops the recursion. It's commonly used to solve problems that have a recursive structure, such as tree or graph traversals, and has many applications in computer science.

The staircase problem mentioned earlier can be solved using recursion. The idea is to break down the problem into smaller sub-problems: climbing 1 step, 2 steps, or recursively solving the same problem for a smaller number of stairs. This process continues until reaching the base case (reaching the top stair), at which point the results are combined to form the final answer.

Unfortunately, without more information about the Lesson 9.0 content and CM1025 Fundamentals of Computer Science course, I couldn't provide a summary with key formulas or technical details.

---

## Recursion Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/ruUO2/recursion)

Here is a summary of the text in 8 sentences, preserving key information:

The video transcript discusses recursion, a process where a function calls itself repeatedly. The "LessThan" pseudocode example illustrates this concept, where the function recursively checks if the input value minus a decreasing number is greater than zero until it reaches one. Another example, Euclid's algorithm, computes the greatest common divisor (GCD) of two non-zero integers by repeatedly dividing the larger number by the smaller one and updating the remainder. This process continues until the remainder becomes zero, at which point the GCD is determined to be the last non-zero remainder. The pseudocode for Euclid's algorithm uses a loop or recursion, with the recursive version calling itself with updated values until the terminating condition is met (b = 0). In both cases, the algorithm terminates after a finite time and produces a result. To apply Euclid's algorithm in practice, one must ensure that it does so by checking for the zero termination condition and using an auxiliary variable to keep track of intermediate results. By understanding recursion and Euclid's algorithm, developers can solve problems efficiently, such as finding the GCD of two numbers or implementing sorting algorithms like quicksort.

---

## Iterative algorithms Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/ULfdI/iterative-algorithms)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Iterative algorithms use loops to implement repetitive tasks, whereas recursive algorithms call themselves repeatedly. Most common algorithms, such as linear search, selection sort, insertion sort, and bubble sort, are iterative. An example of an iterative algorithm is the algorithm to find the maximum value in an unsorted list, which iterates through each element and updates the "current max" variable if necessary. The algorithm works by comparing each element with the current maximum and updating it if the new element is greater. For instance, given a list [14, 27, 15, 5, 1, 3, 29, 7, 10, 8], the algorithm starts with the first element as the current max (14) and iterates through the rest of the list, updating the current max if necessary. The final result is the maximum value in the list, which is 29. This process can be formalized into a simple formula: `current_max = list[index_i]` where `i < list.len`.

---

## Recursive algorithms example Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/tdXMx/recursive-algorithms-example)

Unfortunately, the provided text is a transcript of a video on recursion in algorithms, but it doesn't contain any explicit mathematical formulae or technical details that can be summarized in a concise manner. The text mainly focuses on explaining recursive algorithms using examples, such as the functions F and G.

However, I can summarize the main concepts and findings:

* Recursive algorithms are a way to solve problems by breaking them down into smaller sub-problems of the same type.
* Recursive trees are a visual representation of recursive algorithms, where each node represents a call and its children represent the results of the recursive calls.
* The functions F and G illustrate different types of recursive algorithms, with F calculating 2^m and G calculating a^n.
* The examples demonstrate how to build recursive trees for these functions and use them to calculate their values.

There are no explicit formulae or technical details mentioned in the text that can be summarized in a concise manner. However, I can provide some general information on recursion:

Recursion is a fundamental concept in computer science that involves breaking down problems into smaller sub-problems of the same type. Recursion is often used to solve problems that have a recursive structure, such as sorting algorithms like quicksort.

If you're looking for more information on recursion and its applications, I'd be happy to help you find some resources or provide further explanations.

---

## Quick sort Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/yPkzK/quick-sort)

Here is a summary of the text in 8 sentences, preserving key information:

The partition algorithm is an iterative algorithm used in the Quick Sort sorting algorithm. The idea behind this algorithm is to select a pivot element and reorder the list such that all elements smaller than the pivot are placed on its left side and all elements greater than the pivot are placed on its right side. Two indices, i and j, are defined: i starts from the beginning of the list and moves to the right to find the first element greater than the pivot, while j starts at the last element and moves towards the left to find the first element smaller than the pivot. The algorithm swaps elements at indices i and j if i is smaller than j, otherwise it swaps the pivot with index j. This process continues until all elements are placed on either side of the pivot. Once the partitioning is complete, the algorithm returns the position of the pivot in the list. The initial state of the list after calling the partition is initialized by setting i to 1 (the first element) and j to List.length (the last element), with the pivot set to the first element.

---

## Quick sort example Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/ovHOD/quick-sort-example)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Quicksort is a recursive sorting algorithm that uses the partition algorithm to divide the list into two smaller sub-lists. The Quicksort algorithm takes a list as input and checks if it has one or zero elements; if so, it returns immediately since the list is already sorted. Otherwise, it calls the partition function, which rearranges the list such that all elements less than the pivot are on its left and all elements greater are on its right. The Quicksort algorithm then recursively sorts each sub-list, with the pivot element being placed in its final sorted position. An example of how Quicksort works is provided, showing how the algorithm iteratively partitions the list and recursively sorts the sub-lists until the entire list is sorted. In this example, the list [3, 6, 2, 7, 1, 4, 5] is sorted using Quicksort, with the pivot elements being placed in their final positions after each recursive call. The final sorted list is [1, 2, 3, 4, 5, 6, 7]. Quicksort has a time complexity of O(n log n) on average, making it one of the most efficient sorting algorithms.

---

## Partition and quick sort algorithms Reading• . Duration: 1 hour 25 minutes 1h 25m

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/VKpIQ/partition-and-quick-sort-algorithms)

There is no text provided for me to summarize. The provided text appears to be a resource list or table of contents for learning materials, covering topics such as partition and quicksort algorithms, recursion, and iteration. It includes references to videos, readings, and practice assignments, but does not contain any specific information that can be summarized in 8 sentences.

If you provide the actual text you would like me to summarize, I will be happy to assist you.

---

## Week 17 exercises Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/LPqME/week-17-exercises)

There are no technical details, formulas, or key information provided in the text that can be summarized. The text appears to be a list of exercises and resources for learning algorithms, specifically quick sort and recursion. 

However, here's a summary of the main points:

- The text provides exercises and resources for practicing concepts learned in Week 17, including quick sort and recursion.
- There are two lists provided: one for quick sort exercises and another for a partition algorithm exercise.
- The first list contains numbers that need to be sorted using quick sort, while the second list requires partitioning the list around a pivot element.
- The text also includes resources such as video lectures, practice assignments, and reading materials to help students learn and practice algorithms.

There are no links or technical details mentioned in the text.

---

## Week 17 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/WJyP1/week-17-exercises-hints-and-tips)

Lesson 9.0 Introduction Lesson 9.1 Recursive and iterative alogrithms Video: Video Recursion . Duration: 7 minutes 7 min Video: Video Iterative algorithms . Duration: 4 minutes 4 min Video: Video Recursive algorithms example . Duration: 5 minutes 5 min Discussion Prompt: Recursion vs iteration . Duration: 30 minutes 30 min Practice Assignment: Recursive and iterative algorithms . Duration: 25 minutes 25 min Video: Video Quick sort . Duration: 6 minutes 6 min Video: Video Quick sort example ....

---

