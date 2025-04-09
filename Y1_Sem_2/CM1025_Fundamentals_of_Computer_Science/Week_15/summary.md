# Week 15 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Introduction Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/Nr4MH/introduction)

There is no text to summarize. The provided text appears to be a video transcript and additional page content for a computer science lesson, specifically Lesson 8 of the CM1025 Fundamentals of Computer Science course. It introduces the topic of algorithms and provides information about how to represent them, as well as techniques to design simple sorting and searching algorithms.

The transcript includes a puzzle where an individual is blindfolded and cannot see 10 unordered numbers, but has access to a wise woman who can answer yes or no questions about the relative sizes of these numbers. The goal is to sort these numbers using this process.

Unfortunately, there are no formulae, links, or technical details presented in the provided text. If you could provide the actual content you would like me to summarize, I would be happy to assist further.

---

## What is an algorithm ? Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/47W2m/what-is-an-algorithm)

Here is a summary of the text in 8 sentences, preserving key information and concepts:

An algorithm is a set of steps required to complete a task or solve a problem, often thought of as a recipe for solving a mathematical problem. The concept of algorithms originated from Al-Khwarizmi's book on algebra, which was widely read in Europe during the Middle Ages. Computer science, as we know it today, was founded by Alan Turing, who posed the question: Can machines think? Algorithms are designed by humans to enable machines to solve problems and achieve a specific outcome. Donald Knuth defined an algorithm as a finite, definite, effective procedure with input and output, stating that algorithms are the life-blood of computer science. To develop an algorithm, one must first understand the problem, design an algorithm, check its correctness, analyze its time and space complexity, implement it using programming languages, and test it. A well-defined algorithm consists of an ordered set of unambiguous executable steps that form a terminating process. Examples of everyday algorithms include sorting numbers, finding the shortest path, search engines, and baking a cake, which can be broken down into smaller, more manageable steps to achieve a specific outcome.

---

## Representing algorithms Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/LKhQA/representing-algorithms)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

Algorithms are written and read by humans, but varying representations can lead to ambiguity and confusion. To address this issue, pseudocode is used as a series of notations that describe ideas and operations, making it more intuitive and informal for humans but not executable by machines. Pseudocode uses primitives such as assignment (=), conditional (if-then-else) statements, loops (while), and functions to convey instructions. Primitives are defined using basic syntax, such as equal signs (=) for assignments and if conditions followed by then-else instructions. Loops describe repeated instructions with a terminating condition, while functions are pre-written procedures that can be recalled and utilized. Algorithm design involves understanding the problem, creating a plan, executing it, and evaluating its accuracy. Three widely used techniques for designing algorithms include divide and conquer, greedy algorithms, and backtracking. These techniques, among others, can be employed to tackle complex problems, such as solving Sudoku puzzles using backtracking or network routing using greedy algorithms.

I omitted the following details:

* The video transcript link
* Additional page content (Lesson 8.0-8.2)
* Technical details about specific formulas and examples

Let me know if you would like me to include any of these details in the summary.

---

## Simple algorithms – insertion sort Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/G9Yt0/simple-algorithms-insertion-sort)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The problem being addressed is sequential search, where an algorithm finds a specific number (in this case, 10) in a list. The algorithm reads each element in sequence until it finds a match or determines that the target value was not found. To improve efficiency, sorting algorithms can be used to organize the list before searching. A simple sorting algorithm is insertion sort, which works by comparing each element with previous ones and moving it to its correct position. Insertion sort can be implemented using a pseudocode loop that iterates through the list, selecting an "pivot" element and comparing it to previous elements until finding the next smallest value. Another approach is sequential search, where the algorithm reads the entire list before reporting the target value. The problem of sorting lists has been studied extensively, with other algorithms such as bubble sort and selection sort also being discussed. These algorithms can be used in different situations depending on their efficiency and complexity.

---

## Simple algorithms – bubble sort Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/4wSSb/simple-algorithms-bubble-sort)

Unfortunately, the text does not provide any mathematical formulas or technical details. However, I can summarize the main concepts of bubble sort in 8 sentences:

Bubble sort is a simple sorting algorithm that works by repeatedly iterating through a list of elements, comparing adjacent elements and swapping them if they are in the wrong order. The process continues until no more swaps are needed, indicating that the list is sorted. In the context of bubble sort, we start from the beginning of the list and compare two consecutive numbers. If one number is larger than the other, they swap places. This process is repeated until the entire list is sorted. The algorithm terminates when no more swaps are needed, which means the list has been fully sorted. Bubble sort has a time complexity of O(n^2), making it less efficient for large datasets compared to other sorting algorithms. Despite its inefficiency, bubble sort can be useful for small datasets or educational purposes due to its simplicity and ease of implementation.

Note: There are no links or specific mathematical formulas mentioned in the text.

---

## Selection sort Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/Nnfiu/selection-sort)

Here is a summary of the text in 8 sentences, preserving key information:

Selection sort is a sorting algorithm that works by repeatedly selecting the smallest element from an unsorted list and swapping it with the first element. The process continues until all elements are sorted. In each iteration, the algorithm starts from the beginning of the list, selects the smallest value, and swaps it with the first element. This process continues until only one element is left in the list, which is already sorted. The algorithm uses a variable "start" to keep track of the starting index of the list, incrementing it by 1 at each step. The algorithm then finds the minimum value between remaining elements and swaps it with the first element, repeating this process until all elements are sorted. The selection sort algorithm can be represented in pseudocode as follows:

```
start = 1
while start < length of list:
    min = List[start]
    index = start
    i = Start + 1
    while i <= length of list:
        if List[i] is smaller than min:
            min = List[i]
            index = i
        i = i + 1
    swap List[index] with List[start]
    start = start + 1
```

This algorithm has a time complexity of O(n^2), making it less efficient than other sorting algorithms like quicksort or mergesort.

---

## Model answer for How else would you sort? Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/wtY26/model-answer-for-how-else-would-you-sort)

Lesson 8.0 Introduction Lesson 8.1 Specifying alogrithms Lesson 8.2 Two simple alogrithms Video: Video Simple algorithms – insertion sort . Duration: 5 minutes 5 min Discussion Prompt: How else would you sort? . Duration: 10 minutes 10 min Reading: Reading Model answer for How else would you sort? . Duration: 10 minutes 10 min Video: Video Simple algorithms – bubble sort . Duration: 5 minutes 5 min Video: Video Selection sort . Duration: 4 minutes 4 min Reading: Reading Algorithms ....

---

## Algorithms Reading• . Duration: 1 hour 55 minutes 1h 55m

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/8G7hr/algorithms)

There is no text provided to summarize. The text appears to be a link list or course materials from an educational platform, listing various video lessons, readings, and practice assignments related to sorting algorithms. It does not contain any specific information that can be summarized into 8 sentences.

However, I can provide a summary of the key concepts and findings if you provide the actual text:

The text appears to cover the topics of sorting algorithms, specifically insertion sort, bubble sort, and selection sort. The recommended reading material is Cormen's "Introduction to Algorithms" (4th edition, pp. 17-34), which provides detailed explanations and examples for understanding different sorting algorithms.

If you provide the actual text, I can help summarize it in 8 sentences while preserving key information, formulae, links, and technical details.

---

## Week 15 exercises Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/MF80e/week-15-exercises)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The exercises for Week 15 focus on practicing concepts learned so far. The question asks which sorting algorithm can sort a list that is almost sorted faster (more than 90% of elements are in the right place). Insertion sort, selection sort, and bubble sort are considered. To answer this, we need to analyze each algorithm's performance. Bubble sort performs poorly on nearly-sorted lists because it repeatedly swaps adjacent elements, which can be inefficient. Selection sort is better but still not optimal for nearly-sorted lists because it needs to find the smallest element in each pass, even if most elements are already in order. Insertion sort, on the other hand, takes advantage of the fact that most elements are already sorted and only needs to insert a few elements at the beginning or end. The exercises also ask us to implement bubble sort and selection sort on a sample list A: 13, 1,16, 8, 2, 9, 4, 5.

---

## Week 15 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/ASW66/week-15-exercises-hints-and-tips)

Lesson 8.0 Introduction Lesson 8.1 Specifying alogrithms Lesson 8.2 Two simple alogrithms Video: Video Simple algorithms – insertion sort . Duration: 5 minutes 5 min Discussion Prompt: How else would you sort? . Duration: 10 minutes 10 min Reading: Reading Model answer for How else would you sort? . Duration: 10 minutes 10 min Video: Video Simple algorithms – bubble sort . Duration: 5 minutes 5 min Video: Video Selection sort . Duration: 4 minutes 4 min Reading: Reading Algorithms ....

---

