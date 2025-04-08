# Input size Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/yKACg/input-size)

Here is a summary of the text in 8 sentences, preserving key information:

The video discusses the distinction between complexity and its impact on algorithm efficiency, highlighting that an algorithm's time complexity can change depending on how resources are counted. In the RAM model, it was assumed that each memory unit could store an arbitrarily large integer, but digital computers have limited space per register due to storing bytes. To accurately count resources, we standardize storage as an array of bits or a string with the possibility of storing nothing. This leads to problems where the input is stored in an array of length Big O log n, and the time complexity changes from Big O of n to Big O 2^m, where m is the size of the input. The number of operations required grows exponentially in the size of the input, rendering previously efficient algorithms less effective. This emphasizes the importance of carefully counting resources when analyzing algorithms. The video also mentions the need for standardizing resource counting and storing numbers as arrays or strings of bits to accurately assess algorithm efficiency. The findings suggest that how we count resources can have significant consequences for our claims about algorithm efficiency.

