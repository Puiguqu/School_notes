# Binary search Video• . Duration: 11 minutes 11 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/Rx8ue/binary-search)

## Step 1: Understand the problem
The problem asks to convert a flowchart for the binary search algorithm on vectors into a pseudocode description of the algorithm.

## Step 2: Identify the steps in the flowchart
The flowchart for binary search on vectors has the following steps:
- Start
- Get input vector and target value x
- Initialize variables N (length of vector), L (leftmost element), and R (rightmost element)
- Ask if R is less than L
  - If yes, return false (target not found)
  - Else, set M to be the midpoint of L and R
  - Look at the element at index M in the vector
    - If its value is x, return true (target found)
    - If its value is greater than x, set R to M-1
      + This means the target must be to the left of the midpoint
      + Update L to be M+1
  - Repeat steps 4 and 5 until R is less than or equal to L

## Step 3: Convert the flowchart into pseudocode
Based on the steps in the flowchart, the pseudocode for binary search on vectors can be written as follows:

```
Function binarySearch(vector, x):
  Initialize N (length of vector), L (leftmost element), and R (rightmost element)
  
  While R < L:
    M = (L + R) / 2
    If the value at index M is equal to x:
      Return true (target found)
    Else if the value at index M is greater than x:
      R = M - 1
    Else:
      L = M + 1
  
  If the value at index L is not equal to x:
    Return false (target not found)

Return "Target not found" or return true
```

## Step 4: Verify the pseudocode
The pseudocode follows the same logic as the flowchart and should correctly implement the binary search algorithm on vectors.

The final answer is: There is no specific number to solve this problem, but the above pseudocode implements the correct binary search algorithm for vectors.

