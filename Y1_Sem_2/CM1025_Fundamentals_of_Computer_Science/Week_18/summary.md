# Week 18 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Merging lists Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/16VnD/merging-lists)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The video transcript explains how to merge two sorted lists without tampering with their order, using recursion called merge sort. To do this, we compare the first entries of both lists and write the smallest entry into an output list. We then delete it from its original list and move an arrow to the next position. This process is repeated until one of the lists is empty, at which point only the remaining elements need to be copied into the output list. The merging technique can be applied to sort a list by first splitting it into two sorted parts and then using this method to combine them. To count the number of comparisons performed, we move the sum of the sizes of both lists. However, we must also consider the terminating condition, where one list is empty and the other contains elements that are already sorted. The merging technique can be used recursively to sort a list by first splitting it into two parts and then combining them using this method.

---

## Merge sort Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/IMm4K/merge-sort)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The video transcript explains a powerful technique to merge two sorted lists by splitting them into smaller lists and then merging these smaller lists back together. The process involves recursively splitting the list until it has only one entry, and then merging the smaller lists level by level. This technique is based on the concept of splitting an unordered list into two sorted sublists, merging them, and repeating this process until the list is completely sorted. The pseudocode for this algorithm begins with a list size N, which is split into left and right sublists using the ceiling function to handle odd-sized lists. Each sublist is then recursively sorted using the same technique, resulting in two ordered sublists. These sublists are then merged using a standard merge algorithm, resulting in a single sorted list. The time complexity of this algorithm depends on the number of levels of splitting required and the number of comparisons carried out at every level of merging. The video transcript concludes by explaining how this magic works, including the role of the ceiling function and the merge algorithm.

Note that I did not include any links or technical details as they were not explicitly mentioned in the provided text.

---

## The algorithm of happiness Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/G0ZeI/the-algorithm-of-happiness)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The Gale-Shapley algorithm, also known as the algorithm of happiness, is a well-known algorithm for solving stable matching problems in game theory and economics. The algorithm was developed by Lloyd Shapley and Alvin Roth, who won the 2012 Nobel Prize in Economics for their work on the theory of stable allocations and market design. In this problem, there are n hospitals and n medical students, each with a list of preferences for the other group. The goal is to pair the hospitals and students such that no unstable pair exists, where an unstable pair occurs when a student prefers one hospital to another and the hospital prefers the student back. The Gale-Shapley algorithm works as follows: each unmatched hospital offers a place to a student on top of its list, and students with one offer accept the offer; students with more than one offer choose the top hospital that made them an offer. In the example given, the algorithm matches Mohammed with Whittington, Elena with UCLH, and Sara with Royal Free, but this match is unstable because Elena prefers UCLH to her current hospital, Royal Free. To prove that the Gale-Shapley algorithm always works, we need to show that it produces a stable matching and that every student and hospital appears in at least one pair of the match. The size of the match is equal to the size of the set of hospitals and students, which means that all students and hospitals are paired.

Note: I have omitted some technical details and formulae to make the summary more concise, but the key information and concepts are preserved.

---

## The Gale-Shapley algorithm – example and pseudocode Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/9dueE/the-gale-shapley-algorithm-example-and-pseudocode)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The Gale-Shapley algorithm is used to solve stable matching problems, where each hospital offers a student a place on their list, and the student accepts the best offer. The algorithm terminates when there are no unmatched hospitals, and it returns a set of pairs (m) representing the matches. To prove that the algorithm is correct, we show that it terminates within at most n^2 rounds, where n is the number of hospitals. We then prove that every hospital appears in the match exactly once, which makes the proof more complicated. To prove that there are no unstable pairs, we assume the opposite and show that this leads to a contradiction, using two scenarios: when students reject offers they have not received from another hospital, or when they receive an offer from one hospital but reject it due to a better offer from another hospital. The algorithm is stable because in both cases, the assumption of instability leads to a contradiction. We also prove that if all hospitals are matched, then all students must be matched as well, using proof by contradiction. Finally, we conclude that the Gale-Shapley algorithm solves any stable matching problem and provide examples and pseudocode for further exploration.

---

## Conclusion Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/Uj4Py/conclusion)

Here is a summary of the text in 8 sentences, preserving key information:

The text discusses sorting algorithms using the divide and conquer technique and stable matching by Gale-Shapley. It also introduces recursion and applies it to solve a problem about climbing stairs. The problem involves finding the number of ways to climb 10 stairs, either one step or two steps at a time. The solution uses recursion to calculate the number of ways to reach each step, with the formula Ni = Ni-1 + Ni-2, where Ni is the number of ways to reach step i. The sequence generated by this formula is known as the Fibonacci sequence, which starts with 1, 2, 3, 5, 8, 13, 21, 34, 55, and 89 for steps 1-10, respectively. This sequence can be computed using pseudocode to calculate the ith Fibonacci number. The text also mentions related topics such as merging, merge sort algorithm, Gale-Shapley algorithm, and concludes with a discussion prompt for readers to reflect on what they learned.

---

## Model answer for How does this magic work? Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/VAKgm/model-answer-for-how-does-this-magic-work)

There is no text provided to summarize. The text appears to be a list of lesson titles and durations, without any specific content or information about what the lessons cover. Can you provide more context or the actual text you would like me to summarize? I'll do my best to assist you.

---

## Merge and merge sort algorithm Reading• . Duration: 1 hour 30 minutes 1h 30m

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/O1LDW/merge-and-merge-sort-algorithm)

There is no text to summarize. The provided text appears to be a course schedule or reading assignment list for an online learning platform or university course, specifically Week 18 topics. It outlines the required readings, videos, and exercises for completion, without any detailed content to summarize.

However, I can provide a summary of the most important concepts related to merge and merge sort algorithms based on general knowledge:

The merge and merge sort algorithms are used for sorting data in an efficient manner. Merge sort is a divide-and-conquer algorithm that works by splitting the input into smaller chunks, sorting each chunk recursively, and then merging the sorted chunks back together.

The key steps of merge sort include:

1. Divide: Split the input into smaller subarrays.
2. Sort: Recursively apply the merge sort algorithm to each subarray.
3. Merge: Combine the sorted subarrays into a single sorted array.

Merge is a more general algorithm that can be used for various sorting and merging tasks, including sorting arrays and linked lists.

If you provide the actual text or context, I'd be happy to assist with summarizing key concepts, formulas, links, and technical details.

---

## Week 18 exercises Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/i0bCh/week-18-exercises)

Here is a summary of the text in 8 sentences, preserving key information and concepts:

The week 18 exercises are optional but strongly recommended to test knowledge and identify areas for additional study. The first exercise involves sorting a list using merge sort, with all steps provided. Most programming languages do not require implementing sorting algorithms due to built-in functions; try Java or Python to find the algorithm used. The second exercise requires finding the stable match between nurses and hospitals using the Gale-Shapley algorithm with a given list of preferences. The first list of preferences is: { NKem (N), Elena (E), Fatima (F)} and {Whittington (W), Royal Free (R), Highgate (H)}, with corresponding preferences. The third exercise involves solving the problem again with a different list of preferences. To complete these exercises, allocate 1 hour and 30 minutes to reading, 10 minutes for hints and tips, and another 10 minutes for discussion and video conclusion.

---

## Week 18 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/uvEst/week-18-exercises-hints-and-tips)

Lesson 9.2 Merging Lesson 9.3 The Gale-Shapley alogrithm Lesson 9.4 Conclusion Reading: Reading Merge and merge sort algorithm . Duration: 1 hour 30 minutes 1h 30m Reading: Reading Week 18 exercises . Duration: 10 minutes 10 min Reading: Reading Week 18 exercises hints and tips . Duration: 10 minutes 10 min Discussion Prompt: What did you learn? What did you like? . Duration: 10 minutes 10 min Video: Video Conclusion . Duration: 2 minutes 2 min

---

