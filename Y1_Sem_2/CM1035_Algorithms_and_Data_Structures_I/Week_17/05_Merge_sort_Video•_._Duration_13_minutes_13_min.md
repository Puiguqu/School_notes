# Merge sort Video• . Duration: 13 minutes 13 min

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

