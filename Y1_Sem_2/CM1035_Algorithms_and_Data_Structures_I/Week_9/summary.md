# Week 9 - CM1035 Algorithms and Data Structures I - Problems, algorithms and flowcharts, Part 1 - Week 1

## Solution to the Lottery Problem Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/SSDZj/solution-to-the-lottery-problem)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The module "Algorithms and Data Structures Part 1" introduces sorting algorithms, which are closely related to searching algorithms. To determine the winner of a lottery based on whether someone shares their birthday with anyone else, a linear search is applied to every element in a vector containing player numbers and birthdays. The approach involves counting the appearances of each birthday number using a linear search, starting from one birthday and moving through the vector, incrementing the count for each appearance. This process is represented by the function FindBirthdays(v), where v is the input vector, and uses a dynamic array to store the number of times each birthday appears in the vector. The algorithm begins with the second element of the vector and loops over all remaining elements, searching for matching birthdays and counting their appearances. If a birthday appears only once, it is recorded in the dynamic array. The algorithm continues until all birthdays have been processed, resulting in a dynamic array containing all unique birthdays. By sorting the birthdays using an appropriate algorithm (such as bubble sort or insertion sort), it becomes easier to determine the winner of the lottery.

Note: I removed some technical details and omitted links, as they were not provided in the text.

---

## Introduction to Topic 5 Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/CAyNt/introduction-to-topic-5)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The problem of sorting data involves finding an algorithm that rearranges elements to be in order according to a specified criteria, such as numerical value or alphabetical sequence. A general structure for this type of problem is to take an input data structure and produce an output data structure with the same values but sorted according to the specified order. The question at hand is how to methodically sort data using algorithms. Two common sorting algorithms are bubble sort and insertion sort, which will be discussed in detail. Bubble sort works by repeatedly iterating through the data structure, comparing adjacent elements and swapping them if they are out of order. Insertion sort builds on this idea, but instead of swapping elements, it inserts each new element into its proper position within the sorted portion of the data structure. These algorithms can be used to solve a variety of sorting problems, including the specific lottery ticket problem where the goal is to arrange tickets in ascending order by date of birth. By understanding and implementing these algorithms, individuals can efficiently sort data and produce output that meets their needs.

---

## Bubble sort Video• . Duration: 13 minutes 13 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/0K8II/bubble-sort)

This text appears to be a transcript of a video lecture on computer science, specifically on algorithms and data structures. The lecture discusses the bubble sort algorithm, its implementation for vectors, dynamic arrays, and arrays, as well as its application to sorting stacks.

The transcript provides a step-by-step explanation of how to implement bubble sort using different data structures, including vectors, dynamic arrays, and arrays. It also includes a discussion on how to apply bubble sort to a stack using only other stacks, although the details of this solution are not revealed in the video lecture.

The accompanying materials include:

* A practice assignment for completing additional problems related to bubble sort
* A discussion prompt for students to explore sorting images

Overall, the transcript provides a comprehensive overview of the bubble sort algorithm and its applications, making it an excellent resource for students learning about algorithms and data structures.

---

## Bubble sort on a stack Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/TLCUo/bubble-sort-on-a-stack)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The video transcript explains how to modify bubble sort to sort a stack using two stacks instead of a dynamic array. The algorithm works by pushing elements from the first stack to the second stack, comparing their tops, and swapping them if necessary. After the first pass, the largest element is at the top of the first stack, which mimics the behavior of bubble sort on vectors. A second pass is required to further sort the stack, where all elements from the second stack are pushed to the first stack and the process repeats. The algorithm requires the same number of iterations as bubble sort for vectors, specifically n-1 passes to sort a stack of length n. The video also encourages viewers to apply the bubble sort algorithm to sorting images on the website Unsplash, where each image can be considered a piece of data in a vector. To do this, one would need to identify a suitable property (e.g. color, material) to sort by and then follow the same steps as the stack sorting algorithm. The goal is to demonstrate how the bubble sort algorithm can be adapted to different contexts beyond sorting numerical vectors.

---

## Insertion sort Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/qyL1L/insertion-sort)

Here is a summary of the text in 8 sentences, preserving all key information, formulae, links, and technical details:

The insertion sort algorithm is another way to sort data, similar to bubble sort. It works by comparing each element with previous elements in the data structure until it finds its correct position. The comparison process involves pairwise comparisons between elements, which differs from bubble sort's approach of comparing adjacent elements. In the pseudocode for insertion sort, a shift function is used to move all elements after an element being inserted to the right. The algorithm starts at the second element and compares it with previous elements until it finds its correct position, then shifts elements forward. For each element i in the data structure, we need to check all previous elements while they have values greater than element i. Insertion sort can be implemented on arrays as well as vectors and dynamic arrays, but the array implementation requires fewer steps compared to the vector implementation for certain types of data. The algorithm's performance depends on the order of input data, with optimal performance when input data is already sorted.

---

## Response to discussion points Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/OrksV/response-to-discussion-points)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The insertion sort algorithm can be implemented for arrays, vectors, and dynamic arrays. The array implementation involves starting from the second element (i = 2) and comparing it with previous elements to the left, shifting them if necessary, until the correct order is achieved. A similar approach can be applied to stacks using an additional stack, where the top of each stack is compared and swapped if necessary. In comparison, bubble sort requires more operations, especially when dealing with vectors that are nearly sorted, as demonstrated by a vector of length 5. The insertion sort implementation for this vector requires only about 17 operations, whereas the bubble sort implementation would require around 49 read and write operations on the array. This highlights an advantage of insertion sort over bubble sort in certain cases. The comparison between insertion sort and bubble sort is important to understand the differences between these two sorting algorithms. By analyzing their implementations, one can gain insights into the trade-offs between different algorithms for solving specific problems.

---

