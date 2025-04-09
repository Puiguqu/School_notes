# Search techniques Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/d2aPj/search-techniques)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

A sorted list of items can be searched more efficiently using binary search, which takes advantage of the fact that the items are already sorted. By starting with the middle item of the list, we can quickly eliminate half of the remaining items from consideration. The algorithm works by recursively splitting the list into two halves until only one item remains, which is then reported as found. Pseudocode for binary search involves comparing an item to the pivot (middle item) and determining whether to split the list based on the comparison. There are three scenarios: the pivot is greater than the item, in which case we ignore its left half; the pivot is less than the item, in which case we ignore its right half; or the pivot equals the item, in which case we report it and terminate the search. The binary search algorithm reduces the number of comparisons needed to find an item from 6 (sequential search) to only 3 (in this example), making it faster for large sorted lists. This technique is based on the observation that a sorted list allows us to make educated guesses about the location of an item, without having to examine every individual element. By using binary search, we can efficiently locate items in sorted lists, making it a valuable algorithm for many applications.

