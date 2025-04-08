# Week 15 - CM1005 Introduction to Programming I - Topic 1. Your development environment (cont.) - Week 2

## Initialising and accessing 2D arrays Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/Hvda7/initialising-and-accessing-2d-arrays)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Arrays can store elements of any type, including Booleans, strings, numbers, and objects. They can also store other arrays, making them useful for representing grids or matrices of information. To create a 2D array, we nest sets of square brackets to indicate that each element is an array of values.

For example, `my2DArray = [[1, 2, 3], [4, 5, 6]]` creates a 2D array with one element that contains three numbers. We can access elements of the inner arrays using square brackets, just like we would for 1D arrays.

To iterate through all the elements of a 2D array, we need to use a nested loop structure. The outer loop iterates over each row in the array, and the inner loop iterates over each element within that row.

For example, `for (i = 0; i < groups.length; i++) { console.log(groups[i]); }` prints out each row of the `groups` array. To access individual elements within a row, we can use another nested loop: `for (j = 0; j < groups[i].length; j++) { console.log(groups[i][j]); }`

It's essential to keep track of which variable is controlling the outer loop (`i`) and which one controls the inner loop (`j`). Using a consistent naming convention, such as using `i` for the outer loop and `j` for the inner loop, can help avoid confusion.

Two-dimensional arrays are powerful tools for representing complex data structures. With practice, you'll become more comfortable working with them and be able to apply your knowledge to real-world problems.

The text also mentions the importance of discussing patterns and nesting objects and arrays as part of the lesson progression.

---

## Arrays of objects Video• . Duration: 12 minutes 12 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/BLRsK/arrays-of-objects)

It appears that the provided transcript is not a problem to be solved, but rather a tutorial on using arrays and objects in programming, specifically in the context of p5.js.

However, if you'd like, I can try to extract some specific problems or exercises from the transcript and provide solutions. Please let me know which part of the tutorial you'd like me to focus on.

---

## Complex object properties Video• . Duration: 12 minutes 12 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/A7vUR/complex-object-properties)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The speaker demonstrates how to store objects with array properties in JavaScript. They create an object for a bus with various properties, including x position, length, height, wheel diameter, and driver position. The speaker explains that they will use a two-dimensional array of objects to represent the passengers on the bus.

To start, they initialize an empty passengers array and add five passenger objects to it. Each passenger object has an exponential value (x position) and a random height between 40 and 80. They then draw the driver using the original drawing function, passing in the bus.driver object as an argument.

Next, they comment out the code for drawing the passengers and modify it to extract the x position from each passenger object. They pass the passenger objects at each index to the adapted function, which draws a school child with varying heights.

The speaker notes that there is room for variation, such as adjusting the width of the passengers or giving them different colors or haircuts. They leave this to the viewer's discretion.

Throughout the presentation, the speaker uses comments and code snippets to explain their thought process and provide examples.

---

## Find the matching value Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/GAcbs/find-the-matching-value)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The video transcript discusses basic algorithms for searching arrays in JavaScript. A large array with 1,000 numbers is used as an example, and a variable named "meaningOfLife" is created to store the index of the first instance of the number 42. The array is accessed using the property numArray.length, which returns the length of the array. A for loop is written to iterate over the array, starting from index 0 and stopping when it reaches the last element of the array (i.e., when i < numArray.length). Inside the loop, the condition is checked if the value at index i in the array equals 42 using the syntax numArray[i] == 42. If true, the meaningOfLife variable is assigned the current index i.

The transcript highlights an important point: if the loop finishes without finding 42, the last value returned will be the index of the last element in the array. To fix this issue, the for loop is modified to use a break statement when the value equals 42 is found, which causes the loop to exit prematurely.

The corrected code uses a break statement to stop iterating over the array once 42 is found, ensuring that the first instance of 42 is returned as its index. The meaningOfLife variable is then printed in the console output using the syntax console.log("the meaning of life is at index" + i).

Overall, the video emphasizes the importance of using a break statement to exit a loop prematurely when a specific condition is met, ensuring that the correct index is returned.

Key concepts and findings include:

* Using a for loop to iterate over an array
* Accessing array elements using the property numArray[i]
* Checking conditions within the loop using if statements
* Using a break statement to exit a loop prematurely
* Returning the first instance of a specific value in an array

Formulae and technical details are not explicitly mentioned, but they can be inferred from the code examples provided.

---

## Find the highest / lowest value Video• . Duration: 7 minutes 7 min

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

---

## Exclude a set of values Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/LNoIn/exclude-a-set-of-values)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The speaker introduces manipulating arrays using for loops as another technique. They use an array called "circles" with 1,000 random integer values between 0 and 100. In their draw function, they instruct the drawing of circles at a random location, ignoring any circle under 10 pixels in size. Circles are drawn in red if bigger than 50 pixels, otherwise blue.

The speaker uses a for loop to iterate over the array, with `var i = 0` and `i < circles.length`. Inside the loop, they use an if statement to check if a circle's size is less than 10. If true, they skip using the `continue` keyword to move on to the next iteration.

They also use another if statement to determine whether to draw in red or blue based on the circle's size. The `continue` keyword allows them to bypass drawing smaller circles.

The speaker draws ellipses at a random location, using the value from the array as the ellipse's size. They only draw ellipses with a width greater than 10 pixels.

---

## Code it from scratch: Bookcase Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/supplement/bntMa/code-it-from-scratch-bookcase)

Write a program that creates a 2D array for a bookcase, such that each outer array is a shelf and the inner array stores the books. You can make this as big as you want but try to have at least four shelves with a minimum of five books on each. Write a series of functions that print the following to the console. The first book on each shelf. The total number of books. All the books. The books on a particular shelf specified in a parameter....

---

## Hack it: Robot upgrade Reading• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/supplement/17bAq/hack-it-robot-upgrade)

There is no text provided for me to summarize. The text appears to be a prompt or introduction to a coding challenge or game, but it does not contain any relevant information about robots, firmware, or upgrades. Can you provide the actual text you would like me to summarize? I'll do my best to preserve all key information, formulae, and technical details in an 8-sentence summary.

---

