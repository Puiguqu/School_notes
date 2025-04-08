# Search techniques Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/d2aPj/search-techniques)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

A sorted list can be used to improve the search technique for finding an item in the list. By starting with the middle item, we can reduce the search space by half each time, making it more efficient than sequential search. The process involves comparing the target item with the pivot (middle) item, and then deciding which part of the list to ignore based on the comparison. If the item is less than or equal to the pivot, we look at the left side; otherwise, we look at the right side. This process is repeated until we find the item or determine that it's not in the list. The pseudocode for binary search involves splitting the list into two parts based on the comparison and then repeating the process with the new sublist. Binary search has been shown to be faster than sequential search in this example, reducing the number of comparisons needed from 6 to 3. This highlights the efficiency of binary search, but it's worth noting that this is not always true for all cases, and comparing the speed of two algorithms requires further analysis.

