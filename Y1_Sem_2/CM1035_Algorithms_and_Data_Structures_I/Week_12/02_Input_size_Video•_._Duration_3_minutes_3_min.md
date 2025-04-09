# Input size Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/yKACg/input-size)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The time complexity of an algorithm can be affected by how resources are counted. In the RAM model, it was assumed that each memory unit or register could store an arbitrarily large integer. However, digital computers typically store a byte in each register or memory unit, limiting space. To accurately count resources, we standardize storage to assume input is an array of bits. A number n can be stored using O(log n) bits. When computing the factorial of n with an algorithm that previously had a time complexity of O(n), it now takes exponential time in terms of the size m of the input (O(2^m)), as the size of the input grows exponentially larger than the original size. This highlights the importance of careful counting when discussing resource usage and algorithm efficiency.

