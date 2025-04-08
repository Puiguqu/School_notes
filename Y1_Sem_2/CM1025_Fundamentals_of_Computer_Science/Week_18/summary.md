# Week 18 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Merging lists Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/16VnD/merging-lists)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The video transcript introduces the concept of merge sort, a sorting technique that explores recursion. To illustrate this, the authors demonstrate how to merge two sorted lists without tampering with their order, starting with the following lists: [3, 20, 28, 32, 35] and [7, 14, 27, 30, 39]. The process involves comparing entries from each list, writing the smallest entry into a new output list, deleting it from its original list, and moving the arrow one position right. This comparison process is repeated until only one item remains in either list. Each comparison performs a certain number of moves for both lists, equal to the sum of their sizes. The authors emphasize the importance of considering every step in writing pseudocode, including terminating conditions for when one of the lists becomes empty. By merging two sorted lists, it's possible to sort an unsorted list by first splitting it and then magically sorting each part. This technique will be further explored in a subsequent video.

---

## Merge sort Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/IMm4K/merge-sort)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The video transcript describes a powerful technique to merge two sorted lists by splitting them into individual entries and then merging them level by level. This technique can be used to sort an unordered list by repeatedly applying it to smaller sublists until only one entry is left. The process involves using the ceiling function to handle odd-length lists, where the first item in the right sublist has one more entry than the corresponding item in the left sublist. By merging two sorted lists level by level, a complete and sorted unordered list can be produced. The pseudocode for this technique begins with a list of size N and returns the sorted list if it has only one element. Otherwise, the list is split into two halves using the ceiling function to handle odd-length lists, and the merge sort algorithm is applied to each sublist. The merged sublists are then combined using the merge function, which compares corresponding elements and places them in a new list. This process repeats until only one entry remains, at which point it can be returned as the sorted list.

---

## The algorithm of happiness Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/G0ZeI/the-algorithm-of-happiness)

The Gale-Shapley algorithm is a well-known algorithm for stable matching problems, also known as the algorithm of happiness. It was developed by Lloyd Shapley and Alvin Roth, who won the 2012 Nobel Prize in Economics together. The algorithm's goal is to pair hospitals and medical students such that no unstable pair exists.

In this problem, there are n hospitals and n medical students, each with a list of preferences for the other party. A stable match is one where no hospital prefers a student from another hospital, and no student prefers a hospital that already has them assigned to it. The algorithm's objective is to find a perfect matching, where every hospital and student are paired.

The Gale-Shapley algorithm works as follows:

1. Each unmatched hospital offers the top-ranked student on its list.
2. Students with one offer accept the offer.
3. Students with more than one offer accept the highest-ranked hospital that made them an offer.
4. Repeat steps 1-3 until all hospitals are matched.

In the given example, the algorithm produces a stable match where Whittington is paired with Mohammed, UCLH is paired with Elena, and Royal Free is paired with Sara.

The stability of the algorithm can be proven using the concept of unstable pairs. An unstable pair exists when a student prefers a hospital that already has them assigned to it, and the hospital prefers the student. The Gale-Shapley algorithm ensures that no such pair exists in the resulting match.

The time complexity of the algorithm is O(n^2), where n is the number of hospitals and students. This makes it efficient for solving large-scale matching problems.

In conclusion, the Gale-Shapley algorithm is a powerful tool for stable matching problems, offering a systematic approach to pairing individuals based on their preferences. Its stability guarantee and efficiency make it an essential algorithm in various fields, including economics, computer science, and operations research.

---

## The Gale-Shapley algorithm – example and pseudocode Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/9dueE/the-gale-shapley-algorithm-example-and-pseudocode)

Here is a summary of the text in 8 sentences, preserving key information:

The Gale-Shapley algorithm is used to solve stable matching problems, where every hospital and student has preferences and restrictions. The algorithm terminates when all hospitals are matched, returning a set of pairs (hospitals, students). To prove that the algorithm is correct, it must first show that it terminates within at most n^2 rounds, where n is the number of hospitals. Then, it proves that every hospital appears in the match at least once and at most once, or exactly once. The algorithm ensures a perfect match by preventing unstable pairs, where both parties prefer each other over their current match. To prove stability, the algorithm assumes an unstable pair (h, s) exists, but shows that this leads to contradictions, such as the student's preference rank being higher than the hospital's, or the hospital preferring another student with a lower rank. The Gale-Shapley algorithm has been proven to solve any stable matching problem, including variations with unequal numbers of hospitals and students, restrictions on students, multiple vacancies in hospitals, and couples who need to match together.

---

## Conclusion Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/Uj4Py/conclusion)

Here is a summary of the text in 8 sentences, preserving key information, formulae, and technical details:

The video transcript discusses sorting algorithms that use the divide and conquer technique, as well as the Gale-Shapley algorithm for stable matching. The problem presented involves climbing a staircase with 10 stairs, where one can take either one step or two steps at a time, and asks for the number of ways to reach the top step. The solution is based on recursion, where the number of ways to reach step i (Ni) is defined as Ni = Ni-1 + Ni-2. This recursive formula is derived from the observation that the number of ways to reach a step depends on the number of ways to reach the previous two steps. The sequence generated by this formula is recognized as the Fibonacci sequence, with each term being the sum of the previous two terms. To compute the ith Fibonacci number, pseudocode can be written using the recursive formula Ni = Ni-1 + Ni-2, starting with initial values N1 = 1 and N2 = 2. The video transcript also mentions related topics, including merge sort algorithm, the Gale-Shapley algorithm, and discussion prompts for further learning.

---

## Model answer for How does this magic work? Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/VAKgm/model-answer-for-how-does-this-magic-work)

Unfortunately, you didn't provide the text to be summarized. Please share the original text, and I'll do my best to preserve all key information, formulae, links, and technical details in a concise summary of 6 sentences.

---

## Merge and merge sort algorithm Reading• . Duration: 1 hour 30 minutes 1h 30m

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/O1LDW/merge-and-merge-sort-algorithm)

There is no text to summarize. The provided text appears to be a summary of a course or educational material, listing recommended readings, lessons, and discussion prompts. It does not contain any specific information or technical details that can be summarized in 8 sentences.

However, I can provide a general outline of the content:

The essential reading covers topics studied in Week 18, including merge and merge sort algorithms. The text recommends watching videos and then studying the readings, specifically chapters from Cormen et al. on designing algorithms and the stable-marriage problem. The lessons cover merging and the Gale-Shapley algorithm. The discussion prompt asks students to reflect on what they learned and what they liked about the material.

---

## Week 18 exercises Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/i0bCh/week-18-exercises)

Here is a summary of the text in 8 sentences, preserving key information and concepts:

The course now moves on to practical exercises based on concepts learned earlier. The first exercise involves sorting a list using merge sort with steps shown for reference. Most programming languages have built-in sorting functions, making it unnecessary to implement algorithms. To explore this further, try finding the algorithm used in Java or Python. In another exercise, students are asked to apply the Gale-Shapley algorithm to find stable matches between nurses and hospitals. The initial list of preferences is provided for one set of nurses and hospitals, followed by a second list with different preferences. The Gale-Shapley algorithm is used to determine the most stable match based on the given lists. Students are encouraged to engage with these exercises as they provide an opportunity to test their knowledge and identify areas that require further study.

---

## Week 18 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/uvEst/week-18-exercises-hints-and-tips)

Lesson 9.2 Merging Lesson 9.3 The Gale-Shapley alogrithm Lesson 9.4 Conclusion Reading: Reading Merge and merge sort algorithm . Duration: 1 hour 30 minutes 1h 30m Reading: Reading Week 18 exercises . Duration: 10 minutes 10 min Reading: Reading Week 18 exercises hints and tips . Duration: 10 minutes 10 min Discussion Prompt: What did you learn? What did you like? . Duration: 10 minutes 10 min Video: Video Conclusion . Duration: 2 minutes 2 min

---

