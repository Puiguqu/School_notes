# Efficiency – quick sort Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/RSSUu/efficiency-quick-sort)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The quicksort algorithm has three time complexities: best case (O(n log n)), worst case (O(n^2)), and average case (O(n log n)). The best case occurs when the pivot is the median of the list, dividing the list into two halves. In this case, each step reduces the problem size by half, leading to a time complexity of O(n log n). However, if the pivot does not divide the list in half, the worst-case scenario occurs, resulting in a time complexity of O(n^2). The average case is dominated by the best and worst cases, resulting in a time complexity of O(n log n). To solve this recursive equation, we can use substitution or the master theorem. Applying the master theorem with parameters a = 2, b = 2, d = 1, and k = 1 yields a solution of O(n log n) for t(n). This confirms that the best-case time complexity of quicksort is indeed O(n log n).

Note: I removed links as they are not supported in this format.

