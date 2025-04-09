# Recursive binary search Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/mpy3O/recursive-binary-search)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The video transcript discusses the recursive implementation of the binary search algorithm, which was previously described iteratively. The recursive version is implemented using two functions: `search` and `binary_search`. The `search` function takes input parameters `V`, `item`, `L`, and `R`, while the `binary_search` function takes only `V` and `item` as inputs. The recursive implementation follows a similar structure to the iterative version, but without iterations. In the first line of the `search` function, it checks if `L` is greater than `R` and returns `false` if so, indicating that the search has been unsuccessful. If `L` is less than or equal to `R`, it calculates `M` as the floor of `L + R / 2` and proceeds with the search. The function then checks if the `n-th` element of `V` is equal to `item` and returns `true` if so, or updates `L` or `R` based on comparisons. Finally, the `binary_search` function calls `search` recursively with updated values of `L` and `R`, demonstrating how recursion is used to implement binary search without iteration.

Note: The original text does not provide any formulae, links, or technical details, as it appears to be a transcript of a video discussing the implementation of the recursive binary search algorithm.

