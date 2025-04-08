# Week 20 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Recursion complexity Video• . Duration: 11 minutes 11 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/WW2OU/recursion-complexity)

Here is a summary of the text in 8 sentences, preserving all key information, formulae, links, and technical details:

The concept of recurrence relations is discussed in this video, where the value of a function for an input is given by its value for a smaller input. The Fibonacci sequence is an example of a recursive function. To solve a recurrence relation using recursive trees, start with the root node representing the original function call and divide it into two child nodes, each representing the smaller inputs. In each level, each node has two children, each representing further divisions until reaching the base case (T1). The height of the tree is log(n), where n is the input size. By analyzing the structure of the recursive tree, the time complexity can be determined, which in this example is O(n) for the function sum that calculates the sum of a list of n elements. The Master theorem is also discussed as a tool to solve recurrence relations, but its application is not demonstrated in this video.

---

## Master theorem Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/SMAjd/master-theorem)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The Master Theorem is a solution to find the time complexity of recursive relations without building recursion trees. It states that if T(n) = aT(n/b) + f(n), where a, b, and f are constants, then the relationship between d (the degree of the recurrence) and log_a(b) can determine the final form of T(n). If d < log_a(b), then T(n) is O(f(n)), if d = log_a(b), then T(n) is Θ(f(n) * n^d), and if d > log_a(b), then T(n) is Ω(f(n)^d). The Master Theorem can be applied to solve three common types of recursive relations: those with a constant recurrence (T(n) = cT(n/2)), those with a logarithmic recurrence (T(n) = T(n/2) + O(log n)), and those with a polynomial recurrence (T(n) = T(n/2) + O(n^d)). The theorem has been demonstrated through several examples, including cases where d is less than, equal to, or greater than log_a(b). In each case, the theorem provides a clear formula for determining the time complexity of the recursive relation. By using the Master Theorem, one can avoid having to build recursion trees and guess the solution, making it a useful tool for analyzing recursive relations. Overall, the Master Theorem is a fundamental concept in algorithm analysis that helps to solve some common types of recursive relations.

---

## Master theorem example Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/PYqGC/master-theorem-example)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The master theorem is used to analyze the time complexity of recursive algorithms. The first example analyzed is binary search, where the time complexity T(n) is O(log n) due to its algorithmic structure (T(n/2)+1). The next example involves a function to sum up all elements in an array, with a recursion relation T(n) = 2T(n/2) + 1, resulting in a time complexity of O(n^log_b(a)), where 'b' is the base and 'a' is the element being summed. A third algorithm finds the largest element in an unsorted list recursively, leading to a time complexity of O(n). The master theorem is applied to these examples with specific values for 'a', 'b', and 'd' (base, exponent, and logarithmic part), yielding consistent results. In one of the examples, a loop with a time complexity of O(n) is added to the recursion, leading to an overall time complexity of O(n^d). The master theorem is also used in another example to determine the time complexity of a function that recursively calls itself twice (T(n/2)) and contains a loop with time complexity O(n), resulting in an overall time complexity of O(n^d).

---

## Efficiency – quick sort Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/RSSUu/efficiency-quick-sort)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The quick sort algorithm is a divide-and-conquer approach that selects a pivot element from the list and partitions it into two sublists based on whether they are greater or less than the pivot. The worst-case time complexity of quick sort is O(n^2) when the pivot does not divide the list in half, resulting in n-1 comparisons becoming n*n-1/2. However, for the average case, if the pivot splits the list into two sublists of equal size, the time complexity can be reduced to O(n log n). To solve this recurrence relation, a substitution technique can be used, which leads to t(n) = 2*t(n)/2 + n, and further simplification results in t(n) = n*|log n. The best-case scenario occurs when each comparison is between two elements that are equal to the median of the list, resulting in O(n log n) time complexity. This can be proven using the master theorem, which states that t(n) = O(n^a), where a = 2 and b = 2. The master theorem can also be applied to solve other recurrence relations, and its results can be used to determine the time complexity of different algorithms. Overall, quick sort has an average-case time complexity of O(n log n), making it one of the most efficient sorting algorithms.

---

## Efficiency – merge sort Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/SSaWD/efficiency-merge-sort)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The merge sort algorithm splits a list of integers into two halves until each sublist contains only one item, then merges them level by level. The time complexity of merge sort has the same asymptotic bound for its worst-case and best-case scenarios. In the best case, where the list is already sorted, the algorithm spends O(n log n) time, which is worse than other sorting algorithms like bubble sort or insertion sort. However, in the average case, the algorithm's time complexity is still O(n log n), as it splits the list into two halves and merges them recursively. The master theorem is used to analyze the recurrence relation of merge sort, which has a value of d = 1 for its best-case scenario. Using the master theorem, we can conclude that T(n) is proportional to n times log n. Specifically, if the input list has one element, it returns immediately (O(1) time), and otherwise, it recursively sorts the first half and second half of the list before merging them, resulting in a total time complexity of O(n log n). The average case time complexity of merge sort is indeed O(n log n), making it suitable for large datasets.

---

## Lesson 10.5 Conclusion Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/PRx9l/lesson-10-5-conclusion)

Here is a summary of the text in 8 sentences, preserving key information:

The problem involves finding the maximum floor from which a phone will not break if dropped from that floor, with the goal of minimizing the cost to pay the building manager. A straightforward approach using binary search would be inefficient due to its worst-case scenario of testing floors 1-50 with only one phone left. To mitigate this, a more optimal strategy involves making smaller jumps in floor testing, such as testing every nth floor and then smaller intervals until both phones break. This approach ensures that the total cost is no greater than 10 pounds. The number of tests required can be calculated using the formula n*(n-1)/2 = 100, where n is approximately 14. This results in a maximum cost of 14 pounds for the worst-case scenario when the answer is above 100 floors. In the best case, when the answer is 0, only two tests are needed. The problem can be extended to three phones using recursion, providing another opportunity to apply the concepts learned about asymptotic behavior and time complexity.

---

## Conclusion Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/3wspe/conclusion)

There is no text to summarize. The provided text appears to be a video transcript and does not contain any specific content or information that can be summarized.

However, I can provide an overview of the topics mentioned in the transcript:

The transcript discusses various topics in computer science, including:

1. Proof techniques
2. First-order logic
3. Combinatorial principles
4. Theory of languages and automata
5. Algorithms (sorting and searching)
6. Turing machines
7. Time complexity and Big O notation

Additionally, the transcript mentions specific algorithms, such as linear and binary search, insertion sort, quick sort, merge sort, and heap sort.

If you provide more context or specify which topic you would like me to summarize, I can try to help further.

---

## Solving recurrences and master theorem Reading• . Duration: 2 hours 5 minutes 2h 5m

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/0d8oi/solving-recurrences-and-master-theorem)

Unfortunately, the text you provided does not contain any specific information or key concepts that can be summarized in 8 sentences. The text appears to be a course syllabus or assignment instructions for a computer science class, listing various readings, videos, and assignments related to time complexity and recurrence solving.

However, I can provide a summary of the topics mentioned:

The essential reading covers topics from Week 20, including asymptotic analysis of merge and quick sorts. The material includes explanations and examples on master theorem and recursion tree method for solving recurrences. It is recommended that students first watch the videos before studying the readings. The course materials include assignments and graded assignments related to time complexity.

To provide more specific information, here are some key concepts and formulas related to the topics mentioned:

* Master theorem: T(n) = aT(n/b) + f(n), where a is the growth rate of the input size, b is the growth rate of the output size, and f(n) is the function representing the recurrence relation.
* Recursion tree method: A graphical representation of the recursion tree to solve recurrences.

If you could provide more context or information about the course material, I may be able to provide a more specific summary.

---

## Week 20 exercises Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/Q0y41/week-20-exercises)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The exercises for Week 20 are designed to test knowledge and encourage additional study. The first exercise involves describing a quick sort algorithm that achieves O(n log n) time complexity in the worst case. The second exercise asks to find the time complexity of a recursive algorithm: F(n) = If n < 1: Return Else: Return F(n/3) + n. To solve this, one can apply the master theorem with the recurrence relation T(n) = 3T(n/4) + n. This requires identifying the values of a, b, and c in the master theorem formula to determine the time complexity. The third exercise involves finding the time complexity of another recursive algorithm: F(List) = If List.size < 2: Return Else: Selection_sort(List), where L is the first quarter of the list. To solve this, one can apply the same steps as before, using the master theorem with the correct recurrence relation and identifying the values of a, b, and c. The goal of these exercises is to test knowledge and identify areas for further study.

---

## Week 20 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/fF4dx/week-20-exercises-hints-and-tips)

Lesson 10.4 Master theorem Lesson 10.5 Conclusion Reading: Reading Week 20 exercises . Duration: 10 minutes 10 min Reading: Reading Week 20 exercises hints and tips . Duration: 10 minutes 10 min Discussion Prompt: Final thoughts . Duration: 20 minutes 20 min Video: Video Lesson 10.5 Conclusion . Duration: 6 minutes 6 min Lesson 10.6 Module conclusion

---

