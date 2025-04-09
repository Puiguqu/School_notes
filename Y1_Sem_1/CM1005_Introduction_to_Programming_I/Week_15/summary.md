# Week 15 - CM1005 Introduction to Programming I - Topic 1. Your development environment (cont.) - Week 2

## Initialising and accessing 2D arrays Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/Hvda7/initialising-and-accessing-2d-arrays)

Here is a summary of the text in 8 sentences, preserving key information:

In programming, an array can store elements of any type, including Booleans, strings, numbers, or objects. A two-dimensional array (2D array) is an array that stores arrays as its elements. To declare a 2D array, one uses nested square brackets, e.g., `my2DArray = [[1, 2], [3, 4]]`. Each element of the outer array can be accessed using the same syntax used for one-dimensional arrays. For example, to access the first element of the inner array, one would use `console.log(my2DArray[0][0])`. Two-dimensional arrays are useful for representing tables or grids, and they can be iterated over using nested loops. In JavaScript, a 2D array is created by declaring an outer array with square brackets and assigning elements to each index of the inner arrays using bracket notation. Understanding two-dimensional arrays is essential for working with programming concepts such as nested objects and arrays.

---

## Arrays of objects Video• . Duration: 12 minutes 12 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/BLRsK/arrays-of-objects)

Based on the provided transcript, it appears that this is a coding lesson or tutorial on JavaScript, specifically focusing on working with two-dimensional arrays (arrays of arrays) and nesting objects within these arrays.

The instructor begins by introducing the concept of using a `for` loop to create an array of objects, which will represent cars in a traffic simulation. The example code shows how to:

1. Create an empty array called `traffic`.
2. Use a `for` loop to iterate over a range of numbers (from 0 to 9), creating a new object for each iteration.
3. Within the loop, create another object that represents the car, with properties like `exposition`, `height`, and `wheelDiameter`.

The instructor then discusses how to space out the cars evenly across the screen by using a variable called `inc` (increment). They calculate the even spacing between cars based on the total width of the screen plus a fixed gap on each side.

Next, the instructor introduces the concept of introducing variation into the simulation. They suggest changing the colors and other properties of the cars, which is achieved by:

1. Using the `Math.random()` function to generate random values for red, green, and blue components.
2. Randomizing the height of the car between 120 and 200.
3. Randomizing the wheel diameter between 40 and 80.

The final section encourages the learner to experiment with different variations, such as changing the speeds of the cars or introducing traffic lights that control the flow of traffic.

Overall, this lesson seems to aim at teaching developers how to work with two-dimensional arrays of objects in JavaScript, including creating, spacing out, and modifying these arrays to simulate a traffic scenario.

---

## Complex object properties Video• . Duration: 12 minutes 12 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/A7vUR/complex-object-properties)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The speaker demonstrates how to store objects within an array in JavaScript, and vice versa. They create an object representing a bus with properties like x position, length, height, wheel diameter, and driver's position. The speaker introduces the concept of nesting objects and arrays, creating a new driver object with attributes like height. To draw the driver, they modify the `drawPerson` function to accept an object with attributes, passing in the `bus.driver` object as an argument.

The speaker then creates five passengers with different x positions, heights, and random attributes using loops and array methods like `push`. They draw each passenger using a modified version of the `drawPerson` function, accessing their properties from within the array. The resulting bus object has multiple passengers with unique characteristics, demonstrating the power of nested objects and arrays in JavaScript.

The speaker provides additional resources and practice assignments related to nesting objects and arrays, such as two-dimensional arrays and patterns, which can be used to further explore these concepts.

---

## Find the matching value Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/GAcbs/find-the-matching-value)

Here is a summary of the text in 8 sentences, preserving key information:

The video discusses searching for a particular value in an array using a for loop. An example array with 1,000 numbers is used to find the first instance of the number 42. A variable `meaningOfLife` is created to store the index of the found value and initialized to zero. The for loop iterates through the array until it finds the value 42, but the current implementation prints the last found index instead of the first one. To fix this, a break statement is added after finding the value 42, which stops the loop from iterating further. With the break statement in place, the program successfully finds the first instance of the number 42 and prints its index, which is 265. This demonstrates how to use a for loop with a break statement to achieve a specific search outcome.

---

## Find the highest / lowest value Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/L1urY/find-the-highest-lowest-value)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

To find the highest or lowest value from an array, one can use a for loop to iterate through each element. To find the largest value, create variables `highestValue` and `highestIndex`, and initialize them to zero. In the for loop, check if the current value is greater than the previous highest value, and update `highestValue` and `highestIndex` accordingly. Similarly, to find the smallest value, create variables `smallestValue` and `smallestIndex`, and initialize `smallestValue` to null (not zero). In the for loop, check if the current value is less than the previous smallest value, and update `smallestValue` and `smallestIndex` accordingly. A common mistake when finding the largest or smallest value is to assign a value to `smallestValue` or `largestValue`, which can lead to incorrect results. To avoid this, make sure to compare values using comparison operators (e.g., `<`, `>`) rather than assignment operators (e.g., `=`). By following these steps and being mindful of common pitfalls, one can effectively find the highest or lowest value in an array.

Note that I did not include any external links, formulas, or specific programming language details, as they were not explicitly mentioned in the provided text.

---

## Exclude a set of values Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/LNoIn/exclude-a-set-of-values)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The speaker explains how to use for loops with arrays to manipulate data. They demonstrate this by creating an array called "circles" with 1,000 random integers between 0 and 100, and then using a for loop to draw circles on the canvas based on their size and color. The loop uses if statements to skip over circles that are too small (less than 10 pixels) and draws them in red if they are bigger than 50 or blue otherwise. To avoid deeply nested if statements, the speaker uses the continue keyword to skip certain iterations of the loop. They also use this technique to conditionally draw ellipses with random locations and sizes based on their values from the array. The speaker notes that the loop must be closed with parentheses to ensure proper function. Additionally, they mention a trick for stopping the drawing process from repeating frame by frame: using the "noLoop" function within the draw loop. This allows the user to see a single frame of the application and then refresh to get a different pattern due to the random variables involved.

---

## Code it from scratch: Bookcase Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/supplement/bntMa/code-it-from-scratch-bookcase)

Write a program that creates a 2D array for a bookcase, such that each outer array is a shelf and the inner array stores the books. You can make this as big as you want but try to have at least four shelves with a minimum of five books on each. Write a series of functions that print the following to the console. The first book on each shelf. The total number of books. All the books. The books on a particular shelf specified in a parameter....

---

## Hack it: Robot upgrade Reading• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/supplement/17bAq/hack-it-robot-upgrade)

I don't see any text provided for me to summarize. The text appears to be a message or prompt from a coding game or tutorial, asking the user to find and resolve issues with a rogue robot that has been upgraded with new firmware. However, there is no actual content to summarize.

If you provide the actual text, I would be happy to help you summarize it in 8 sentences, preserving key information, formulae, links, and technical details.

---

