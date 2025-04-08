# Week 12 - CM1035 Algorithms and Data Structures I - Problems, algorithms and flowcharts, Part 1 - Week 1

## Worst-case time complexity Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/Mh8XT/worst-case-time-complexity)

The text discusses the concept of worst-case time complexity in algorithms, which refers to the maximum number of operations required by an algorithm for a given input size.

To analyze an algorithm's time complexity, it is essential to consider the worst-case scenario, where the input size is maximal. For example, in linear search, the worst-case input is when the target value is not present in the array or vector, requiring the inspection of all n elements.

Bubble sort has a best-case time complexity of O(n), as only one pass is needed to sort an already sorted array. However, the worst-case scenario occurs when the array is sorted with the largest value first and the smallest value last, requiring n-1 passes, each with O(n) operations, resulting in a worst-case time complexity of O(n^2).

Similarly, insertion sort also has a worst-case time complexity of O(n^2), as it requires n-1 passes to sort an array.

The key takeaway is that analyzing worst-case time complexity helps identify the maximum resources required by an algorithm for a given input size. This understanding enables developers to choose the most efficient algorithms for specific problems.

Note: There are no formulas, links, or technical details in this summary as it is focused on preserving the main concepts and findings of the text.

---

## Input size Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/yKACg/input-size)

Here is a summary of the text in 8 sentences, preserving key information:

The video discusses the distinction between complexity and its impact on algorithm efficiency, highlighting that an algorithm's time complexity can change depending on how resources are counted. In the RAM model, it was assumed that each memory unit could store an arbitrarily large integer, but digital computers have limited space per register due to storing bytes. To accurately count resources, we standardize storage as an array of bits or a string with the possibility of storing nothing. This leads to problems where the input is stored in an array of length Big O log n, and the time complexity changes from Big O of n to Big O 2^m, where m is the size of the input. The number of operations required grows exponentially in the size of the input, rendering previously efficient algorithms less effective. This emphasizes the importance of carefully counting resources when analyzing algorithms. The video also mentions the need for standardizing resource counting and storing numbers as arrays or strings of bits to accurately assess algorithm efficiency. The findings suggest that how we count resources can have significant consequences for our claims about algorithm efficiency.

---

## Summary Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/F4PCi/summary)

Unfortunately, there is no text provided for me to summarize. The text you shared appears to be a video transcript with links and technical details, but it does not contain any actual content that I can summarize.

However, I can provide an overview of the key concepts and findings presented in the video transcript:

The video transcript discusses algorithms and their performance analysis using the RAM model. It explains how to count operations implemented for a particular algorithm in the RAM model and introduces big O notation to analyze the asymptotic growth of functions. The worst-case time complexity, which is the maximum time complexity for all possible inputs, is discussed as a measure of an algorithm's performance.

The transcript also mentions examples of algorithms with different worst-case time complexities, such as linear search (O(n)), bubble sort and insertion sort (O(n^2)), and another algorithm with O(log n) worst-case time complexity. However, without more information about the specific algorithm mentioned in the link "Lesson 6.4 Summary Video: [link]", I cannot provide further details.

If you could provide the actual text or content to be summarized, I would be happy to assist you further.

---

## The Pizza Problem Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/olmE3/the-pizza-problem)

There is no text to summarize in this conversation, only a blank space. Please provide the text you'd like me to summarize, and I'll be happy to assist you.

---

## Analysis of algorithms Reading• . Duration: 1 hour 25 minutes 1h 25m

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/supplement/z0vGY/analysis-of-algorithms)

Here is a summary of the text in 8 sentences:

The provided text references Section 2.2 of Cormen's "Introduction to Algorithms" textbook, which discusses the RAM model and time complexity. The section reviews insertion sort, with a detailed analysis that covers various notions of complexity beyond the scope of this module. This information is considered essential reading for future study. Access to the ebook is available through E-Book Central (ProQuest) via the provided links. The video "Worst-case time complexity" and practice assignment are also mentioned as part of Lesson 6.3. However, no further details or summaries of these resources are provided in the text snippet.

---

