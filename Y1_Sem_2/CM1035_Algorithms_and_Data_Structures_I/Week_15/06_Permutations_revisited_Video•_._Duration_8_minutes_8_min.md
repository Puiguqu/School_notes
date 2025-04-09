# Permutations revisited Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/8K2OG/permutations-revisited)

The text discusses the solution to generating permutations of letters using recursion. The pseudocode for this process is as follows:

```
function permutations(vector):
    if length(vector) ≤ 1:
        return vector
    else:
        s = []
        for i in alphabet:
            v = vector excluding i
            w = permutations(v)
            p = [i] + w
            append p to s
        return s
```

This pseudocode uses recursion to generate permutations of the letters in the input vector. It works by iterating over each letter in the alphabet, creating a new vector `v` that excludes the current letter, and then recursively generating permutations of `v`. The permutations of `v` are then appended to a new vector `p`, which is created by adding the current letter at the beginning of each permutation.

The key idea behind this recursive solution is that we can generate permutations of n letters by using the permutations of (n-1) letters and inserting the new letter in between the letters of the previous permutations. This approach allows us to avoid storing all the permutations of previous cases in a dynamic array or stack, making the implementation more efficient.

The text also mentions the binary search algorithm and asks the viewer to think about how it can be implemented recursively. It provides a practice assignment for implementing recursive algorithms in JavaScript.

Overall, the text emphasizes the importance of recursion in solving problems by breaking them down into smaller sub-problems that can be solved independently, and then combining the solutions to form the final answer.

