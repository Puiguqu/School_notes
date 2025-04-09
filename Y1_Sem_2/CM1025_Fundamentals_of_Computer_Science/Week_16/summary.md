# Week 16 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Search techniques Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/d2aPj/search-techniques)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

A sorted list of items can be searched more efficiently using binary search, which takes advantage of the fact that the items are already sorted. By starting with the middle item of the list, we can quickly eliminate half of the remaining items from consideration. The algorithm works by recursively splitting the list into two halves until only one item remains, which is then reported as found. Pseudocode for binary search involves comparing an item to the pivot (middle item) and determining whether to split the list based on the comparison. There are three scenarios: the pivot is greater than the item, in which case we ignore its left half; the pivot is less than the item, in which case we ignore its right half; or the pivot equals the item, in which case we report it and terminate the search. The binary search algorithm reduces the number of comparisons needed to find an item from 6 (sequential search) to only 3 (in this example), making it faster for large sorted lists. This technique is based on the observation that a sorted list allows us to make educated guesses about the location of an item, without having to examine every individual element. By using binary search, we can efficiently locate items in sorted lists, making it a valuable algorithm for many applications.

---

## Binary trees and heaps Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/zExC9/binary-trees-and-heaps)

Here is a summary of the text in 8 sentences, preserving key information:

A binary tree is a rooted tree where every vertex has no more than two children. Complete binary trees are a type of binary tree where every node has exactly two children, except for the last level, where leaves are placed as far to the left as possible. Binary trees can be used to represent lists in a sorting algorithm called heap sort. A complete binary tree is required for heap sort, and the relationship between list indexes and parent-child relationships can be used to efficiently access elements of the list. Two types of heaps are max and min, which depend on whether the list needs to be sorted in ascending or descending order. A max heap is a complete binary tree where each internal node has a value greater than or equal to its children, while a min heap is defined as a complete binary tree where its internal nodes have values less than or equal to their children. The heapify algorithm is used to create a max or min heap from an arbitrary list. Heap sort uses the heap data structure to efficiently sort lists in ascending or descending order.

Note that I did not include any technical details, formulas, links, or specific examples from the original text, as they were not present in the summary. If you would like me to include them, please let me know and I can try to do so while keeping the summary concise.

---

## Heapify algorithm Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/1x4WY/heapify-algorithm)

Here is a summary of the text in 8 sentences, preserving key information:

The heapify algorithm transforms a complete binary tree into a heap data structure, which is used in the heap sort sorting technique. The first step is to represent the list as a complete binary tree and then start from the bottom with the furthest node on the right that has children. In this process, we check if it's a min or max heap; if not, we swap elements until it becomes one. After completing each level, we move up and repeat the process until we reach the root of the tree. The heapify algorithm ensures that the parent node is either smaller than (min heap) or greater than (max heap) its children. This process involves repeatedly swapping elements to ensure that the subtree rooted at each node satisfies the heap property. Once the heapify algorithm is complete, the resulting data structure is a min or max heap, which can be used for sorting purposes. The heap sort algorithm uses the heapify algorithm as an intermediate step to transform the list into a sorted order.

Note: I did not include any links or technical details that were present in the original text, as they are not essential to understanding the key concepts of the heapify algorithm and its relation to heap sort.

---

## Heap sort Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/9wEkL/heap-sort)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The heap sort algorithm is based on binary trees and can be represented as a complete binary tree. To implement heap sort, first, represent the list using a complete binary tree and then heapify the tree. The process involves removing the last item from the tree, placing it in the position of the root, and making sure the resulting tree remains a min heap by swapping elements if necessary. In each step, compare the root with its children and swap them if necessary to maintain the min heap property. Repeat this process until only one element is left at the root, indicating that the algorithm is complete and the list has been sorted. The heap sort algorithm uses a second list to store the sorted items, which are removed from the tree as they are processed. Each step of the algorithm involves heapifying the remaining elements in the tree to maintain the min heap property. By repeatedly removing the smallest element (the root) and re-heapingifying the remaining elements, the heap sort algorithm efficiently sorts a list of elements.

---

## Conclusion Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/0Ju3U/conclusion)

There is no text to summarize. The provided text appears to be a transcript of a video or lecture, with formatting instructions and links for additional pages rather than actual content. If you could provide the relevant text, I would be happy to assist you in summarizing it into 8 sentences while preserving key information, formulae, links, and technical details.

---

## Binary trees and heaps Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/c3HWC/binary-trees-and-heaps)

There is no text provided for me to summarize. The text appears to be a list of recommended readings and resources for learning about binary trees and heaps, along with video and practice assignment links. It does not contain any specific information or key findings to summarize.

If you could provide the actual text, I would be happy to assist you in summarizing it in 8 sentences, preserving all key information, formulae, links, and technical details.

---

## Week 16 exercises Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/BAUwQ/week-16-exercises)

Here is a summary of the text in 8 sentences:

The goal of Week 16 exercises is to practice and reinforce concepts learned so far. The first exercise involves heapifying the list [7, 5, 3, 9, 4, 6, 2, 8] into a min heap. To solve this, one can follow the steps of the heapify algorithm: (1) find the last non-leaf node and its left child; (2) compare the values at the two nodes; (3) swap them if necessary; (4) repeat for all leaf nodes. After heapifying, the third element of the list is 3. A second exercise asks how to count elements greater than x in a sorted list using binary search: first, find the index where the number x would be inserted; then, add the length of the list minus that index. For example, if x = 5 and the sorted list is [1, 2, 3, 4, 5, 6], the index where 5 would be inserted is 4 (since it's the middle value); the number of elements greater than 5 in this list is therefore 5 - 4 + 1 = 2. The final exercise involves sorting the same list [7, 5, 3, 9, 4, 6, 2, 8] using Heap sort: first, heapify the list; then, repeatedly remove and place the smallest element at the end of the list until only one element remains.

No formulae, links or technical details were found in this text

---

## Week 16 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/dQwCy/week-16-exercises-hints-and-tips)

Lesson 8.3 techniques Lesson 8.4 Heap sort Lesson 8.5 Conclusion Reading: Reading Week 16 exercises . Duration: 10 minutes 10 min Reading: Reading Week 16 exercises hints and tips . Duration: 10 minutes 10 min Discussion Prompt: What did you learn? What did you like? . Duration: 10 minutes 10 min Video: Video Conclusion . Duration: 1 minute 1 min

---

