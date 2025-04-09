# Week 19 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Introduction Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/GqObB/introduction)

There is no text to summarize beyond the first few sentences of the provided transcript. The content seems to be a series of links and instructions on how to navigate through a video transcript, but it does not contain any specific information about algorithms or time complexity.

However, I can provide a general overview of what might be covered in a lesson on efficiency of algorithms:

Algorithms can be analyzed for their time complexity using various methods. One common approach is asymptotic analysis, which compares the performance of different algorithms based on their worst-case and average-case scenarios. Another method is Big O notation, which provides an upper bound on the number of steps required by an algorithm.

A specific example mentioned in the transcript is the "riddle" about finding the maximum floor from which a phone will not break if dropped from a window. This problem can be approached using a recursive approach or a loop-based approach to estimate the breaking point and minimize the cost of testing.

If you provide more context or text, I would be happy to assist you in summarizing it.

---

## Efficiency – insertion sort (time complexity) Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/KguLk/efficiency-insertion-sort-time-complexity)

Here is a summary of the text in 8 sentences, preserving key information, formulae, and technical details:

The time complexity of an algorithm refers to the amount of time it takes to complete a task as a function of the size of the input. Binary search is faster than sequential search for finding a given number in an ordered list, but its performance depends on the difficulty case (average or worst-case scenario). In the average case, binary search requires 17 comparisons to find a number in a list of 100,000 numbers, which is significantly smaller than the 50,000 required by sequential search. The time complexity of an algorithm can be analyzed using three scenarios: worst-case, average-case, and best-case. The worst-case scenario assumes the input will always lead to the maximum possible number of operations, while the best-case scenario assumes the input will always lead to the minimum possible number of operations. For the insertion sort algorithm, the time complexity is O(n^2) in the worst case, but can be improved to O(n) in the best case when the input is already sorted in ascending order. The average-case analysis takes into account all possible inputs and finds that insertion sort performs better than sequential search, with a time complexity of O(n log n). Big O notation is used to express the upper bound on the number of operations required by an algorithm.

---

## Efficiency – bubble sort and binary search Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/PrM5G/efficiency-bubble-sort-and-binary-search)

Here is a summary of the text in 8 sentences, preserving key information on algorithms and formulas:

The video transcript discusses the efficiency of two algorithms: bubble sort and binary search. Bubble sort has an average time complexity of O(n^2), where n is the number of items in the list, which makes it less efficient than other sorting algorithms. Binary search, on the other hand, has a best-case time complexity of O(log n), worst-case time complexity of O(log n), and average time complexity of approximately O(log n). The binary search algorithm works by repeatedly dividing the search space in half until the target item is found. The number of comparisons required to find an item in a list of n items can be calculated using the formula T(n) = 1 + T(n/2), which represents a recursive division of the search space. This formula can be simplified to O(log n) by recognizing that each level of recursion reduces the size of the search space by half, resulting in a logarithmic number of steps. The average time complexity of binary search is approximately log n because it assumes that each element in the list is equally likely to be the target item. Overall, binary search is more efficient than bubble sort and has better worst-case and average time complexities.

---

## Asymptotic complexity Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/zRERE/asymptotic-complexity)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The video transcript discusses the asymptotic complexity of algorithms, which refers to the time required by an algorithm as a function of input size (n). The efficiency of an algorithm can be compared by looking at its graph, where the shape represents the growth rate. To determine the asymptotic behavior, one must consider the fastest-growing term in the function and strip it from its coefficient. There are five main cases: constant functions (like 2n^2 + 5), linear functions (like n log n), quadratic functions (like 3n^2 + 4n), cubic functions (higher-order polynomials), and exponential functions. Each case has a specific order of asymptotic behavior, with logarithmic functions growing slower than constant functions, which in turn grow slower than linear functions, and so on. The video provides examples to illustrate each case, including the best-case and worst-case scenarios for sorting algorithms like insertion sort. The goal of asymptotic analysis is to estimate how slow an algorithm becomes as input size increases. By identifying the fastest-growing term in a function, one can determine the class of function it belongs to and predict its growth rate.

Note: I removed some technical details and formulas not explicitly mentioned in the original text, but preserved key concepts and ideas.

---

## Big O notation Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/aCIDO/big-o-notation)

Here is a summary of the text in 8 sentences, preserving key information and concepts:

Big O notation is used to describe the growth rate of a function. Two functions f(x) and g(x) are related by f(x) being O(g(x)) if there exist constants c and k such that f(x) ≤ c*g(x) for all x > k. This means that f(x) grows slower than some multiple of g(x) as x increases. The constants c and k are called witnesses to the relation between f(x) and g(x). For example, if g(x) = n^2 and f(x) = 2n^2 + 4n + 40, then the witnesses are c = 3 and k = 9. The concept of Big O notation is similar to asymptotic behavior, which describes how a function grows as the input variable increases. To show that one function is O of another, we need to find constants c and k such that the first function is less than or equal to c times the second function for all x > k. This concept is important in computer science because it allows us to analyze the time complexity of algorithms and make predictions about their performance.

---

## Big O notation example Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/HqHbV/big-o-notation-example)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The video transcript discusses big O notation, focusing on examples that prove functions are bounded above by other functions. The first example proves that f(n) = 10n + log2^n ≤ cgn for all n ≥ n0, where c is 11 and g(n) = n. This is done by selecting a witness value for c that holds true for sufficiently large values of n. A second example attempts to prove that f(n) = 5n + 2^n ≤ c(gn), but fails with c = 2 due to the function 2^n growing faster than 5n. To determine if one function is O another, a table can be used to compare their growth rates. The table shows examples of pairs of functions where f is greater than or equal to g, and those where g is greater than or equal to f. In general, f is O(g) if g grows slower than f. Asymptotic analysis is necessary because it allows us to understand the performance of algorithms as input sizes grow, which is crucial in computer science.

---

## Using Big O to analyse selection sort Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/K2SJ9/using-big-o-to-analyse-selection-sort)

Here is a summary of the text in 8 sentences, preserving key information:

The time complexity of selection sort can be analyzed by breaking down its algorithm into smaller parts. The first part of the algorithm finds the minimum element in each iteration using a function called Find_Min, which has a time complexity of O(n). This function iterates through two elements in the list, resulting in a time complexity of O(n) for this part. The overall time complexity of selection sort is determined by an outer loop that iterates through all elements of the algorithm, making it O(n^2). However, since the inner loop is always executed, the time complexity remains O(n^2). The best, worst, and average time complexities of selection sort are all O(n^2), indicating that the algorithm's performance degrades quadratically with the size of the input. Understanding the time complexity of selection sort helps in analyzing its efficiency and making informed decisions about its use in different scenarios. By applying Big O notation to analyze the algorithm's performance, developers can predict how efficient or inefficient a sorting algorithm will be for large datasets.

---

## Model answer for Average, worst and best case Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/jivZP/model-answer-for-average-worst-and-best-case)

There is no text provided for me to summarize. Please provide the text, and I'll be happy to help you summarize it in 4 sentences, preserving key information, formulae, links, and technical details.

---

## Model answer to Why do we need asymptotic behaviour? Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/9ULr0/model-answer-to-why-do-we-need-asymptotic-behaviour)

There is no text to summarize. The provided text appears to be a lesson plan or a course outline for learning about asymptotic complexity and Big O notation. It includes the following information:

* Lesson topics: Asymptotic analysis of insertion sort, Big O notation, time analysis of algorithms using Big O
* Time complexity: O(n^2) (same for both functions)
* Duration of each lesson: 6 minutes, 25 minutes, 10 minutes, etc.
* Practice assignment: Asymptotic complexity

There is no text to summarize, and the information provided is more of a course outline than a technical document. If you can provide the actual text you'd like me to summarize, I'd be happy to assist you.

---

## Asymptotic analysis and Big O notation Reading• . Duration: 1 hour 40 minutes 1h 40m

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/K7g0j/asymptotic-analysis-and-big-o-notation)

There is no text provided for me to summarize. The text appears to be a summary of learning materials for a course or tutorial, listing videos, reading assignments, and practice exercises related to asymptotic analysis and Big O notation. It does not contain any specific information or data that can be summarized in 8 sentences. If you provide the actual text, I would be happy to assist you.

---

## Week 19 exercises Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/69jGR/week-19-exercises)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The week 19 exercises provide opportunities for students to practice concepts learned earlier. The first exercise involves proving whether f(n)=3n+2 is O(g(n)) or g(n)=n^2 is O(f(n)). To do this, students must compare the growth rates of f(n) and g(n). If f(n)=O(g(n)), then there exists a constant c such that f(n) ≤ cg(n) for all n. Similarly, if g(n)=O(f(n)), then there exists a constant c such that g(n) ≤ cf(n) for all n. The second exercise asks students to analyze the time complexity of pseudocode with a while loop and nested operations on variables i and n. Students must determine whether the total number of operations grows quadratically or polynomially with respect to n. The third exercise involves comparing the growth rates of f(n)=4n+logn, g(n)=n^2 logn, h(n)=n^2, and another function not provided in the text.

---

## Week 19 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/2ilAc/week-19-exercises-hints-and-tips)

Here are the key concepts and findings summarized in 8 sentences:

The Big O notation is used to analyze the time complexity of algorithms, which describes the relationship between the input size (n) and the number of operations performed. The formula for calculating Big O is f(n) = O(g(n)) if f(n) ≤ c*g(n) for some constant c and all n ≥ n0. In this lesson, we are introduced to three functions: f(n) = O(n), g(n) = O(n^2), and h(n) = O(n^0.5). We can see that f(n) = O(n) is equal to O(logn) since each time i is doubled, reducing the number of operations by half. The function g(n) = O(nlogn) has a higher growth rate than g(n) = O(n), as n multiplied by logn grows faster than just n. In contrast, h(n) = O(n^0.5) has a lower growth rate than f(n) = O(n). To analyze the time complexity of an algorithm using Big O notation, we need to trace the algorithm and find the witness that proves our answer.

Note: The text provided does not contain any links or technical details about algorithms or data structures, but rather provides hints and tips for analyzing their time complexity using Big O notation.

---

