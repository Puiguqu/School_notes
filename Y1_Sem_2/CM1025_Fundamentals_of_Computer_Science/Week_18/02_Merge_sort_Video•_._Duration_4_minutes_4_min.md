# Merge sort Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/IMm4K/merge-sort)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The video transcript describes a powerful technique to merge two sorted lists by splitting them into individual entries and then merging them level by level. This technique can be used to sort an unordered list by repeatedly applying it to smaller sublists until only one entry is left. The process involves using the ceiling function to handle odd-length lists, where the first item in the right sublist has one more entry than the corresponding item in the left sublist. By merging two sorted lists level by level, a complete and sorted unordered list can be produced. The pseudocode for this technique begins with a list of size N and returns the sorted list if it has only one element. Otherwise, the list is split into two halves using the ceiling function to handle odd-length lists, and the merge sort algorithm is applied to each sublist. The merged sublists are then combined using the merge function, which compares corresponding elements and places them in a new list. This process repeats until only one entry remains, at which point it can be returned as the sorted list.

