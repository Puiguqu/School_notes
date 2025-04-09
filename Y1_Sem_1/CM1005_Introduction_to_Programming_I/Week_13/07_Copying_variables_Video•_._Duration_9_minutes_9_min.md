# Copying variables Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/kiVWz/copying-variables)

Here is a summary of the text in 8 sentences, preserving key information:

In JavaScript, when assigning one variable to another, the value is copied, but not referenced. For simple types (numbers, strings, booleans), the assignment creates an independent copy. In contrast, for complex types (objects and arrays), the assignment creates a reference to the original object or array.

When objects are assigned to each other, both variables point to the same memory location, meaning changes made to one variable affect the other. To pass simple properties by value, assign them individually to create new values, as seen in the example of `rect2.x` being set to 200.

Arrays and objects are passed by reference by default, which means modifying an array or object through one variable affects all other variables referencing the same instance. To avoid this behavior, assign a copy of the array or object using the spread operator or the `Object.assign()` method, as demonstrated in the example with `myArray2` being assigned a new array.

Overall, understanding how JavaScript handles assignment and reference can help developers write more effective code and avoid common pitfalls.

