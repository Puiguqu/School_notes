# Initialising and accessing 2D arrays Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/Hvda7/initialising-and-accessing-2d-arrays)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Arrays can store elements of any type, including Booleans, strings, numbers, and objects. They can also store other arrays, making them useful for representing grids or matrices of information. To create a 2D array, we nest sets of square brackets to indicate that each element is an array of values.

For example, `my2DArray = [[1, 2, 3], [4, 5, 6]]` creates a 2D array with one element that contains three numbers. We can access elements of the inner arrays using square brackets, just like we would for 1D arrays.

To iterate through all the elements of a 2D array, we need to use a nested loop structure. The outer loop iterates over each row in the array, and the inner loop iterates over each element within that row.

For example, `for (i = 0; i < groups.length; i++) { console.log(groups[i]); }` prints out each row of the `groups` array. To access individual elements within a row, we can use another nested loop: `for (j = 0; j < groups[i].length; j++) { console.log(groups[i][j]); }`

It's essential to keep track of which variable is controlling the outer loop (`i`) and which one controls the inner loop (`j`). Using a consistent naming convention, such as using `i` for the outer loop and `j` for the inner loop, can help avoid confusion.

Two-dimensional arrays are powerful tools for representing complex data structures. With practice, you'll become more comfortable working with them and be able to apply your knowledge to real-world problems.

The text also mentions the importance of discussing patterns and nesting objects and arrays as part of the lesson progression.

