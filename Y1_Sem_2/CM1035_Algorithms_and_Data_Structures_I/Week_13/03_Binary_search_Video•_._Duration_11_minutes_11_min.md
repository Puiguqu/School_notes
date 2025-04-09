# Binary search Video• . Duration: 11 minutes 11 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/Rx8ue/binary-search)

The provided transcript appears to be a lecture or video on the binary search algorithm, specifically for vectors and arrays. The content includes:

1. An explanation of how the binary search algorithm works.
2. A flowchart illustrating the steps involved in the algorithm.
3. A discussion of the advantages of using binary search over linear search.

The final section mentions converting the flowchart into pseudocode and then turning it into working JavaScript code.

Here is a simplified version of the pseudocode for the binary search algorithm:

**Binary Search Algorithm**

**Input:** `arr` (sorted vector or array), `target`

**Output:** `true` if `target` is found in `arr`, `false` otherwise

1. Set `L` to 1 and `R` to the length of `arr`
2. While `L` <= `R`
3. Calculate `M` = `(L + R) / 2`
4. If `arr[M] == target`
5. Return `true`
6. If `arr[M] < target`
7. Set `L` to `M + 1`
8. Else
9. Set `R` to `M - 1`
10. Repeat steps 3-9 until found or not found

The pseudocode is a concise representation of the algorithm's logic, and it can be used as a starting point for implementing the binary search in JavaScript.

**Note:** This is a simplified version of the pseudocode, and you may want to add additional error handling or input validation depending on your specific use case.

