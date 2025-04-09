# Using Big O to analyse selection sort Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/K2SJ9/using-big-o-to-analyse-selection-sort)

Here is a summary of the text in 8 sentences, preserving key information:

The time complexity of selection sort can be analyzed by breaking down its algorithm into smaller parts. The first part of the algorithm finds the minimum element in each iteration using a function called Find_Min, which has a time complexity of O(n). This function iterates through two elements in the list, resulting in a time complexity of O(n) for this part. The overall time complexity of selection sort is determined by an outer loop that iterates through all elements of the algorithm, making it O(n^2). However, since the inner loop is always executed, the time complexity remains O(n^2). The best, worst, and average time complexities of selection sort are all O(n^2), indicating that the algorithm's performance degrades quadratically with the size of the input. Understanding the time complexity of selection sort helps in analyzing its efficiency and making informed decisions about its use in different scenarios. By applying Big O notation to analyze the algorithm's performance, developers can predict how efficient or inefficient a sorting algorithm will be for large datasets.

