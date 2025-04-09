# Week 17 - CM1035 Algorithms and Data Structures I - Problems, algorithms and flowcharts, Part 1 - Week 1

## Revisiting the substitution cipher problem Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/YCXza/revisiting-the-substitution-cipher-problem)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

Frequency analysis is a technique used to break substitution ciphers by comparing the frequency of letters in the ciphertext to their frequency in English. This approach assumes that the encoded message or plaintext is in English and that some letters appear more often than others. The most frequently appearing letter in the ciphertext can be compared to the most frequently appearing letter in English, such as 'e', to assume the original letter is 'x'. A sorting algorithm is used to compare these permutations, with the goal of finding the correct mapping between ciphertext and plaintext. However, traditional sorting algorithms like bubble sort and insertion sort have a time complexity of around 10^53 operations for large amounts of data, making them inefficient. This lesson will explore alternative sorting algorithms, such as Quicksort and Merge sort, which can be more efficient for handling large datasets. These algorithms are being introduced as part of a new topic to discuss faster methods for solving the substitution cipher problem. The goal is to develop algorithms with fewer steps or operations to improve efficiency when dealing with large amounts of data like this.

---

## Introduction to Topic 9 Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/9fGH9/introduction-to-topic-9)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

This topic introduces divide and conquer algorithms, which reduce a problem into smaller and simpler problems that can be easily solved recursively. The goal of these algorithms is to combine the solutions of each smaller problem to solve the initial problem. Two examples of divide and conquer algorithms are quicksort and merge sort. Quicksort reduces the input vector by partitioning it according to a specific element's value, while merge sort divides the input into halves multiple times and runs merge sort on these halves. The worst-case time complexity of quicksort is O(n^2), compared to O(n log n) for merge sort and other sorting algorithms like bubble sort and insertion sort. Merge sort has a higher space complexity due to its recursive nature, but it is generally more efficient than quicksort in practice. Quicksort's performance degrades significantly in the worst case when the pivot element is chosen poorly, whereas merge sort is less affected by the choice of pivot. Understanding the time and space complexities of these algorithms is crucial for choosing effective sorting solutions in various applications.

---

## Quicksort Video• . Duration: 11 minutes 11 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/CkWRD/quicksort)

It appears that the provided text is a transcript of a video or lecture on computer science, specifically on the topic of sorting algorithms. The main algorithm being discussed is Quicksort.

Here's an excerpt from the transcript:

**Excerpt**

"So we can see the vector at the top which is unsorted. We're going to do the same trick as before, initialise two variables i and j. One's going to start with the leftmost element. One is going to start with the rightmost element. We're going to see if the value stored there are larger than the value stored at the pivot. Four is less than nine, so it's on the correct side of the pivot. So we're going to increase the value of i. Five is smaller than nine, so we're going to have to move that to the left of the pivot. So we're going to keep j where it is for the time being."

The transcript explains how the Quicksort algorithm works by using two variables, `i` and `j`, to partition the elements in an array around a pivot element.

**Key concepts:**

*   Partitioning: The process of dividing the elements in an array into two parts, based on their values relative to the pivot.
*   Pivot: A selected element from the array that serves as the reference point for partitioning.
*   Quicksort algorithm: An efficient sorting algorithm that uses recursive calls and partitioning to arrange elements in ascending order.

**Implementation:**

The implementation of the Quicksort algorithm is not provided in the transcript, but it typically involves:

1.  Selecting a pivot element from the array.
2.  Partitioning the remaining elements around the pivot using two pointers (`i` and `j`).
3.  Recursively applying the same process to the sub-arrays on either side of the pivot until the entire array is sorted.

**Practice Assignments:**

The transcript mentions a practice assignment for Quicksort, which might include:

1.  Implementing the Quicksort algorithm in a programming language (e.g., JavaScript).
2.  Testing and verifying the correctness of the implementation.
3.  Analyzing the time complexity and space complexity of the algorithm.

**Further Resources:**

Additional resources mentioned in the transcript include video lectures, practice assignments, and reading materials on pseudocode for Quicksort partitioning. These resources can provide further insight into understanding the Quicksort algorithm and its implementation.

---

## Quicksort and induction Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/nyFgb/quicksort-and-induction)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The Quicksort algorithm is a divide-and-conquer algorithm that uses recursion to sort vectors. It works by partitioning vectors into smaller vectors using two variables and comparing values at different elements. The base case for Quicksort is when a vector has a length of zero or one, in which case it is already sorted and does not require further operations. To prove the correctness of Quicksort, mathematical induction can be used to establish that if a particular instance of a problem is assumed to be true, then the next instance is also true. The algorithm works by recursively reducing vectors to smaller and smaller vectors until they reach the base case, using strong mathematical induction. Specifically, if a vector of length n can be sorted, then a vector of length n+1 can also be sorted by partitioning it into three vectors: the pivot (a single element vector), the left vector, and the right vector. The largest of these three vectors will have at most n elements, which can be sorted using the assumption that vectors of length n can be sorted. This induction strategy demonstrates the idea of divide-and-conquer using recursion, making Quicksort a relatively simple algorithm to understand and implement.

---

## Merge sort Video• . Duration: 13 minutes 13 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/8DSap/merge-sort)

I can provide a step-by-step explanation of how to implement merge sort.

## Step 1: Understand the merge sort algorithm
Merge sort is a divide-and-conquer algorithm that works by dividing the input array into two halves, sorting each half recursively, and then merging the sorted halves back together.

## Step 2: Define the base case
The base case for merge sort is when the input array has only one element. In this case, the sub-array is already sorted, so we can return it immediately.

## Step 3: Divide the array into two halves
To divide the array into two halves, we need to find the middle index of the array. We can do this by dividing the length of the array by 2 and rounding down to the nearest whole number.

## Step 4: Recursively sort each half
Once we have divided the array into two halves, we recursively call the merge sort function on each half. This will divide each half into even smaller sub-arrays until we reach the base case.

## Step 5: Merge the sorted halves
Once both halves are sorted, we need to merge them back together in a sorted manner. We can do this by comparing the smallest unmerged element from each half and adding the smaller one to our result array.

## Step 6: Implement the merge sort algorithm in code
Here is an example of how you might implement merge sort in Python:
```
def merge_sort(arr):
    # Base case: if the array has only one element, return it
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    merged_arr = []
    while len(left_half) > 0 and len(right_half) > 0:
        if left_half[0] <= right_half[0]:
            merged_arr.append(left_half.pop(0))
        else:
            merged_arr.append(right_half.pop(0))

    # Add any remaining elements from either half
    merged_arr.extend(left_half)
    merged_arr.extend(right_half)

    return merged_arr

# Test the merge sort function
arr = [3, 6, 1, 8, 2, 4]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 6, 8]
```
Note that this is just one possible implementation of merge sort in Python. There are many other ways to implement it, and different languages may have slightly different syntax or requirements for the algorithm.

The final answer is: $\boxed{[1, 2, 3, 4, 6, 8]}$

---

## Setting up the substitution cipher problem Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/LX0xT/setting-up-the-substitution-cipher-problem)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The programming activity involves implementing merge sort on a simplified version of the permutations problem. The goal is to decode an encoded message by permuting letters in the original message. Six letters (w, r, e, s, h, i) are used, with frequencies of appearance in the original message as follows: r (5), w (3), e and s (2), h and i (1). The `permutations` function generates all possible permutations of these six letters, resulting in 6! = 720 permutations. A new function, `frequency_order`, sorts the elements of the permutations array according to how frequently the first element appears in the English language. This is achieved by assigning a number to each letter based on its frequency in English and using this numerical information to sort the permutations. The merge sort algorithm is implemented, taking an array as input and merging it into one big sorted array. However, the implementation requires additional steps to handle the sorting of elements according to their frequency in English.

---

## Pseudocode for Quicksort partitioning Reading• . Duration: 20 minutes 20 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/supplement/64dPg/pseudocode-for-quicksort-partitioning)

The attached brief note presents the pseudocode for the partition function since this is the most important element of Quicksort. Quicksort.pdf PDF File Lesson 9.0 Introduction to Topic 9 Lesson 9.1 Quicksort Video: Video Quicksort . Duration: 11 minutes 11 min Practice Assignment: Quicksort . Duration: 10 minutes 10 min Video: Video Quicksort and induction . Duration: 5 minutes 5 min Reading: Reading Pseudocode for Quicksort partitioning ....

---

