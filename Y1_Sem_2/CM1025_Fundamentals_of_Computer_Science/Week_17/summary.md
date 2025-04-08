# Week 17 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Introduction Video• . Duration: 59 seconds 59 sec

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/xnsna/introduction)

There is no text to summarize. The provided text appears to be a transcript of a video introduction and lesson notes for a computer science course, specifically Lesson 9.0 on Recursive and Iterative Algorithms.

However, I can provide a summary based on the topic of recursion:

Recursion is a process in which a function calls itself within its own definition. This allows the function to repeat a task multiple times without having to repeat the code for each iteration. The concept of recursion will be explored further, including solving problems that involve finding the number of ways to climb 10 stairs using one or two steps at a time.

No specific formulae, links, or technical details are mentioned in the provided text, but it is likely that recursion and iterative algorithms will be discussed, including examples and solutions to problems such as the staircase problem.

---

## Recursion Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/ruUO2/recursion)

Here is a summary of the text in 8 sentences, preserving key information:

The LessThan function is an example of recursion, where a function calls itself repeatedly until it reaches a base case. The pseudocode for LessThan is demonstrated, showing how n decreases by 1 at each recursive call until n becomes less than or equal to 0. Euclid's algorithm is another example of recursion, used to compute the greatest common divisor (GCD) of two non-zero integers. The algorithm works by repeatedly dividing the larger number by the smaller one and taking the remainder, with the GCD being the last non-zero remainder. In an iterative version of Euclid's algorithm, a loop is used instead of recursive calls to achieve the same result. Both versions of Euclid's algorithm terminate when the remainder becomes zero, producing the final GCD. The pseudocode for both algorithms is provided, highlighting key steps such as checking for termination and updating variables. Understanding recursion and iteration are essential concepts in programming, with applications in solving problems like finding the GCD of two numbers.

---

## Iterative algorithms Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/ULfdI/iterative-algorithms)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Iterative algorithms use loops to implement repeated tasks, whereas recursive algorithms call themselves repeatedly. Most common algorithms used so far are iterative, such as linear search, selection sort, insertion sort, and bubble sort. To find the maximum value in an unsorted list using an iterative algorithm, we assume the first element is the maximum and store it in a variable called "current max". We then compare each subsequent element with the current max, updating it if necessary, until we reach the end of the list. The algorithm can be represented by the formula: `current_max = i` (starting from index 1) while `i < len(list)`, and if `list[i] > current_max`, then `current_max = list[i]`, incrementing `i` to move to the next element. This process continues until all elements have been checked, resulting in the maximum value being stored in `current_max`. The algorithm is based on the idea that we start by assuming the first element as the maximum and iteratively update it if necessary. By using a loop instead of recursive function calls, iterative algorithms can be more efficient and easier to understand for large inputs or complex data structures.

---

## Recursive algorithms example Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/tdXMx/recursive-algorithms-example)

Here is a summary of the text in 8 sentences, preserving key information:

Recursive trees are a way to trace recursive algorithms. The given function F takes an integer as input, returning 2^m if m is one, 1 if m is zero, and 2*F(m-1) otherwise. To find the value of F(5), a tree is built with the root F(5), then children are added for each recursive call, such as F(4), which calls F(3), which calls F(2), which calls F(1). The result of each call is calculated and returned, ultimately resulting in F(5) = 32. Another function G takes two parameters, a and n, returning a if n is one, 1 if n is zero, and calling itself twice with different parameters otherwise. A recursive tree is built for G(2,5), then the results of each child are multiplied to get the final result, which is 32. The function G calculates and returns a^n. Recursive algorithms can be visualized using recursive trees, providing insight into how they work and how to solve problems involving them.

Note: I have omitted some technical details such as formulas, links, and specific code examples not present in the original text.

---

## Quick sort Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/yPkzK/quick-sort)

Here is a summary of the text in 8 sentences, preserving key information:

The Partition algorithm is used in the Quick Sort algorithm to divide the input list into two parts, one containing elements smaller than the pivot and the other containing elements greater than the pivot. The first element of the list is chosen as the pivot. Two indices, i and j, are defined: i starts from the beginning of the list and moves to the right to find the first element greater than the pivot, while j starts at the last element and moves towards the left to find the first element smaller than the pivot. The two elements at indices i and j are swapped if i is less than j. This process continues until i is no longer less than j, indicating that the pivot has been placed in its correct position. The partition algorithm returns j as the position of the pivot in the list, allowing for sorting to occur without moving the pivot. This algorithm can be used iteratively or recursively, with iterative versions being more efficient in practice. By using the Partition algorithm, Quick Sort is able to sort a list in O(n log n) time complexity.

---

## Quick sort example Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/ovHOD/quick-sort-example)

Here is a summary of the text in 8 sentences, preserving key information:

Quicksort is a recursive sorting algorithm that uses the partition algorithm to divide the list into two smaller sub-lists. The algorithm works by selecting a pivot element from the list, partitioning the other elements around it, and recursively sorting the left and right sub-lists. If the list has one or zero elements, it is already sorted, so the algorithm returns immediately. Otherwise, the partition function is called to determine the pivot position, and the algorithm recursively sorts the left and right sub-lists. The Quicksort algorithm is implemented as `Quick_Sort(List)` where `List` is the input list, `n` is its length, and `j` is the index returned by the `Partition` function. The algorithm uses a recursive approach to sort the list, with the base case being an empty or single-element list. In an example walk-through, the Quicksort algorithm is applied to the list `[3, 6, 2, 7, 1, 4, 5]`, resulting in a sorted list `[1, 2, 3, 4, 5, 6, 7]`. The Quicksort algorithm has a time complexity of O(n log n) on average, but can be O(n^2) in the worst case if the pivot is chosen poorly.

---

## Partition and quick sort algorithms Reading• . Duration: 1 hour 25 minutes 1h 25m

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/VKpIQ/partition-and-quick-sort-algorithms)

Unfortunately, there is not enough information in the provided text to summarize in 8 sentences, preserving key details. The text appears to be a course syllabus or reading list, listing various videos, readings, and assignments for Week 17 of a course.

However, I can provide a summary based on general information about the topics mentioned:

The essential reading for Week 17 covers partition and quick sort algorithms, which are fundamental concepts in computer science. The recommended resources include Cormen et al., Chapter 7, up to '7.4 Analysis of quick sort', pp.182–193, and various video lectures and practice assignments on recursion, iteration, and quick sort. Watching the videos first is strongly advised before studying the essential reading. The topics covered in Week 17 are likely to include the analysis of quick sort's time complexity (O(n log n) and space complexity (O(log n)) using mathematical formulas. There may be additional readings or assignments that cover related concepts, such as the partition algorithm and its relationship with quick sort.

---

## Week 17 exercises Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/LPqME/week-17-exercises)

Here is a summary of the text in 8 sentences, preserving key information and details:

The text emphasizes the importance of practicing concepts learned in Week 17 through exercises. The list A = [13, 1, 16, 8, 2, 9, 4, 5] is given for quick sort exercise. After one iteration, the list should be sorted in ascending order. To complete this task, use the partition algorithm to rearrange the elements. The text also explores the role of the pivot element in the partition algorithm and whether considering the first element as the pivot is important. Additionally, a recursive algorithm is provided to reverse a string recursively. The text encourages students to engage with these exercises to test their knowledge and identify areas for further study. The recommended time allocations for each exercise are also listed, ranging from 7 minutes (video) to 1 hour 25 minutes (reading).

---

## Week 17 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/WJyP1/week-17-exercises-hints-and-tips)

Lesson 9.0 Introduction Lesson 9.1 Recursive and iterative alogrithms Video: Video Recursion . Duration: 7 minutes 7 min Video: Video Iterative algorithms . Duration: 4 minutes 4 min Video: Video Recursive algorithms example . Duration: 5 minutes 5 min Discussion Prompt: Recursion vs iteration . Duration: 30 minutes 30 min Practice Assignment: Recursive and iterative algorithms . Duration: 25 minutes 25 min Video: Video Quick sort . Duration: 6 minutes 6 min Video: Video Quick sort example ....

---

