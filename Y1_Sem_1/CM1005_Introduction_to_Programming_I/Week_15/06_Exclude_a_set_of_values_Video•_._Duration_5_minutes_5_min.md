# Exclude a set of values Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/LNoIn/exclude-a-set-of-values)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The speaker explains how to use for loops with arrays to manipulate data. They demonstrate this by creating an array called "circles" with 1,000 random integers between 0 and 100, and then using a for loop to draw circles on the canvas based on their size and color. The loop uses if statements to skip over circles that are too small (less than 10 pixels) and draws them in red if they are bigger than 50 or blue otherwise. To avoid deeply nested if statements, the speaker uses the continue keyword to skip certain iterations of the loop. They also use this technique to conditionally draw ellipses with random locations and sizes based on their values from the array. The speaker notes that the loop must be closed with parentheses to ensure proper function. Additionally, they mention a trick for stopping the drawing process from repeating frame by frame: using the "noLoop" function within the draw loop. This allows the user to see a single frame of the application and then refresh to get a different pattern due to the random variables involved.

