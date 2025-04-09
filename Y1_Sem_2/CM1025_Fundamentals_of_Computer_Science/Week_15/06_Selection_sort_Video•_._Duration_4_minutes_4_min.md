# Selection sort Video• . Duration: 4 minutes 4 min

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

