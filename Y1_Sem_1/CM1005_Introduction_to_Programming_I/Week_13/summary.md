# Week 13 - CM1005 Introduction to Programming I - Topic 1. Your development environment (cont.) - Week 2

## User defined functions Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/JE7Wd/user-defined-functions)

Here is a summary of the text in 8 sentences, preserving key information, formulas, links, and technical details:

Functions are blocks of code that perform specific tasks, allowing coders to organize their code into discrete sections and reuse it in different contexts. The basic syntax for declaring a function includes the "function" keyword, a function name, two round parentheses, and two curly braces containing the function body. To call a function, one must type the function name followed by two round parentheses. Functions can be used to refactor code, making it more modular and easier to maintain. In this lesson, we learned how to define and call our own functions using P5 JS, separating code into discrete sections and reusing them as needed. By writing high-level programming code on top of pre-existing dependencies (libraries), we create a software stack with different layers interacting with each other. The concept of functions allows us to build upon the work of others, creating a tiered structure of dependencies that is essential for large-scale coding projects. By understanding how functions work and when to use them effectively, coders can write more efficient and maintainable code.

---

## Returning early and the call stack Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/yIZo3/returning-early-and-the-call-stack)

This text is a transcript of a video lesson on programming functions, specifically in the context of coding in a platform that appears to be focused on game development or interactive projects.

The lesson covers several key topics related to functions:

1. **Defining User-Defined Functions**: The instructor explains how to define a function using the `function` keyword and provides an example of a simple game character drawing function.
2. **Returning Early from a Function**: The instructor shows how to use the `return` keyword to stop execution of a function early, using this technique to implement a game mechanic where the character disappears when lives reach zero.
3. **Call Stack Representation**: The instructor demonstrates how the Call Stack represents the sequence of function calls and explains its significance in understanding code flow.

The lesson also mentions additional topics:

1. **Function Input and Output**: Not explicitly covered, but implied as part of broader lessons on variables and scope (Lesson 7.3).
2. **Variables and Scope**: Covers how variables are scoped within functions and when they become accessible to other parts of the program.
3. **Debugging Techniques**: Mentions techniques for debugging code, although specific methods or strategies are not detailed.

**Key Takeaways**

- User-defined functions can be used to organize code into reusable blocks.
- The `return` keyword allows early termination from a function, useful in game mechanics and other scenarios where certain conditions need to be met before continuing execution.
- Understanding the Call Stack is crucial for grasping how functions interact and build upon each other in a program.

**Contextual Information**

- The video lesson appears to be part of a larger curriculum or course focused on teaching programming concepts, likely targeting beginners or those with some programming experience looking to expand their skills.
- The specific platform used for coding isn't named, but the examples suggest it might be a game development engine like Unity or Unreal Engine.

---

## Function arguments Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/osYr3/function-arguments)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

In this video, the creator demonstrates how to use arguments in p5.js functions to control the exposition, y-position, and height of a flower. The creator creates an argument list with variables for x-position, y-position, and stem heights, ensuring that variable names differ from existing ones. The creator uses "find and replace" to replace base x, base y, and stem heights with the corresponding arguments in the code. To reuse the code and draw multiple flowers, the creator uses a for loop to iterate through different values of the argument list. In each iteration, the flower's position and height are adjusted using the i index, allowing for spreading out or changing the pattern of the flowers. The creator also adds an argument for the color of the petals and demonstrates how to use it to change the color of the flowers. By combining different patterns and values, the creator showcases the flexibility of passing arguments into functions. Overall, this video provides a comprehensive introduction to using arguments in p5.js functions to create dynamic and customizable graphics.

---

## Recursive cloud Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/KI9Jj/recursive-cloud)

Here is a summary of the text in 8 sentences, preserving key information:

Recursion is a programming technique where a function calls itself within its own definition. An example of recursion can be seen in Russian dolls or the Droste effect, where an image of a woman holds a smaller version of herself. In code, recursion works by calling a function from within itself, with each call creating a new instance of the function. The key to avoiding infinite loops is to include a conditional statement that stops the recursion when certain conditions are met. In this example, the programmer uses a conditional statement to stop the recursive calls when a certain threshold is reached. The recursion creates an exponential growth in the number of function calls, which can lead to performance issues if not handled carefully. By using random offsets and colors, the programmer can create a visually interesting pattern with clouds, chains of movement, and varying colors. Overall, recursion requires careful planning and execution to produce desired results without crashing the program.

---

## Returning values from functions Video• . Duration: 21 minutes 21 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/ACmeq/returning-values-from-functions)

Based on the provided transcript, it appears that this is a JavaScript programming tutorial. The tutorial covers various topics such as functions, variables, and debugging techniques.

The main topic of the transcript is functions, specifically how to return values from functions in JavaScript. The author explains that functions can return simple values like strings and booleans, but also complex objects and arrays.

Here are some key takeaways from the transcript:

1. Functions can return multiple values using object notation.
2. Functions can be used to reverse the direction of a spaceship when it goes off the edge of the screen.
3. The `getSpeed()` function is used to reverse the direction of a spaceship.
4. The `speed` object is returned by the `getSpeed()` function and assigned to the spaceship's properties.

To expand on this example, you could try:

1. Adding laser beams that come out of the spaceships when they collide.
2. Making the spaceships glow or crackle when they collide.
3. Creating multiple types of collisions (e.g., head-on collision, side collision).
4. Adding sound effects for collisions.

Overall, this transcript provides a comprehensive overview of functions in JavaScript and how to use them to create interactive programs.

---

## Scope - global and local with var Video• . Duration: 11 minutes 11 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/2TcvQ/scope-global-and-local-with-var)

This is a transcript of a video lecture on programming concepts, specifically on the topic of scope and global vs local variables.

The lecturer discusses how in programming, variables have different behaviors depending on where they are created. Variables created inside a function (local) only exist within that function's scope and do not affect other parts of the program. On the other hand, variables defined outside of any function (global) persist across the entire program and can be accessed from anywhere.

The lecturer also touches on the importance of using global variables sparingly, as they can lead to code that is not modular and has difficult-to-keep track-of variable names. Instead, the lecturer suggests creating a return value for functions that can store the new values of variables, allowing for more flexibility and better organization of code.

The key takeaways from this video are:

1. Variables created inside a function (local) have scope limited to that function and do not affect other parts of the program.
2. Variables defined outside of any function (global) persist across the entire program and can be accessed from anywhere.
3. Global variables should be used sparingly, as they can lead to code that is not modular and has difficult-to-keep-track-of variable names.
4. Instead of using global variables, it's better to create a return value for functions that can store new values of variables.

Overall, the video provides an introduction to the concept of scope and its implications for programming, as well as some practical advice on how to manage variables effectively in code.

---

## Copying variables Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/kiVWz/copying-variables)

Here is a summary of the text in 8 sentences, preserving key information:

In JavaScript, when assigning one variable to another, the value is copied, but not referenced. For simple types (numbers, strings, booleans), the assignment creates an independent copy. In contrast, for complex types (objects and arrays), the assignment creates a reference to the original object or array.

When objects are assigned to each other, both variables point to the same memory location, meaning changes made to one variable affect the other. To pass simple properties by value, assign them individually to create new values, as seen in the example of `rect2.x` being set to 200.

Arrays and objects are passed by reference by default, which means modifying an array or object through one variable affects all other variables referencing the same instance. To avoid this behavior, assign a copy of the array or object using the spread operator or the `Object.assign()` method, as demonstrated in the example with `myArray2` being assigned a new array.

Overall, understanding how JavaScript handles assignment and reference can help developers write more effective code and avoid common pitfalls.

---

## Common errors with scope and how to debug them Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/r3JLH/common-errors-with-scope-and-how-to-debug-them)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

In the p5.js programming language, scope refers to the region where a variable is defined and can be accessed. The author provides an example of a global variable `rectWidth` that is set to 100, but when used in the `draw` function, it is not updated with the new value of 200. This happens because the `draw` function has its own local scope, which overrides the global scope. To fix this issue, the author introduces a new function called `drawRect` that takes two parameters: `x`, `y`, and `width`. The `drawRect` function uses these parameters to draw a rectangle, but also accesses the built-in `width` variable of p5.js, which can cause conflicts. To avoid this conflict, the author renames the parameter `width` to `rectWidth` and updates its value inside the function. This allows the function to manipulate its own scope independently of the global scope. The author also notes that variables defined within a function are only accessible within that function's scope, and changes made within the function do not persist outside of it.

Please note that I did not include any links or formulae as they were not present in the original text.

---

## Code it from scratch: Lights on! Reading• . Duration: 1 hour 30 minutes 1h 30m

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/supplement/LCnGt/code-it-from-scratch-lights-on)

Unfortunately, you haven't provided any text for me to summarize. Please provide the text you'd like me to summarize, and I'll do my best to preserve all key information, formulae, links, and technical details in 8 sentences.

Once you provide the text, I'll get started!

---

## Debug challenge Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/supplement/dkNPk/debug-challenge)

Unfortunately, you didn't provide any text for me to summarize. The provided text seems to be a summary of a lesson plan with various activities, such as videos, reading assignments, and discussion prompts, related to functions and debugging techniques in programming. If you could provide the actual text you'd like me to summarize, I'd be happy to assist you.

---

