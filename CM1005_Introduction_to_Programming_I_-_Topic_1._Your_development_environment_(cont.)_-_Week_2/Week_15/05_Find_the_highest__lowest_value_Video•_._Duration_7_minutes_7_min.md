# Find the highest / lowest value Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/L1urY/find-the-highest-lowest-value)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

1. The video discusses finding the highest or lowest value in an array.
2. A sketch is shown with a little for loop to push random values into an array between 0 and 1000.
3. A variable called `highestValue` is created to store the highest value found, while another variable `highestIndex` stores the index of that value.
4. The `for` loop iterates through each value in the array, comparing it with the current `highestValue`.
5. If a value is higher than `highestValue`, it updates `highestValue` and `highestIndex`.
6. To find the smallest value, a similar approach is used, but starting from 0.
7. However, setting `smallestValue` to 0 or -1 does not work for all cases, as it only considers positive values.
8. Instead, `smallestValue` is initialized to null and set equal to the first element of the array if it's less than the current value.
9. This ensures that the smallest value in the array is found correctly, even when dealing with negative numbers.
10. The code includes a console log statement to verify the output and identify any bugs.
11. In this case, the bug is fixed by changing `smallestValue` comparison to be equal to null instead of just not equal to zero.
12. With the corrected code, the smallest value in the array is found correctly at index 65 with a value of 0.
13. The video also touches on how to skip over certain values in the array when applying an operation only to some of them.
14. This will be covered in a future video lesson.
15. The video concludes by mentioning additional lessons, including two-dimensional arrays, nesting objects and arrays, and patterns, which will be covered in subsequent videos.

Note: Some technical details, such as the use of `numArray.length` and `i++`, are not explicitly mentioned in this summary, but are assumed to be present in the original text.

