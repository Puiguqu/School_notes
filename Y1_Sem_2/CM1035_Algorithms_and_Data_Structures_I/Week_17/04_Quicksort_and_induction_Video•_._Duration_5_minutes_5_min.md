# Quicksort and induction Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/nyFgb/quicksort-and-induction)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The Quicksort algorithm is a divide-and-conquer algorithm that uses recursion to sort vectors. It works by partitioning vectors into smaller vectors using two variables and comparing values at different elements. The base case for Quicksort is when a vector has a length of zero or one, in which case it is already sorted and does not require further operations. To prove the correctness of Quicksort, mathematical induction can be used to establish that if a particular instance of a problem is assumed to be true, then the next instance is also true. The algorithm works by recursively reducing vectors to smaller and smaller vectors until they reach the base case, using strong mathematical induction. Specifically, if a vector of length n can be sorted, then a vector of length n+1 can also be sorted by partitioning it into three vectors: the pivot (a single element vector), the left vector, and the right vector. The largest of these three vectors will have at most n elements, which can be sorted using the assumption that vectors of length n can be sorted. This induction strategy demonstrates the idea of divide-and-conquer using recursion, making Quicksort a relatively simple algorithm to understand and implement.

