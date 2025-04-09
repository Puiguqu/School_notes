# Common errors with scope and how to debug them Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/r3JLH/common-errors-with-scope-and-how-to-debug-them)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

In the p5.js programming language, scope refers to the region where a variable is defined and can be accessed. The author provides an example of a global variable `rectWidth` that is set to 100, but when used in the `draw` function, it is not updated with the new value of 200. This happens because the `draw` function has its own local scope, which overrides the global scope. To fix this issue, the author introduces a new function called `drawRect` that takes two parameters: `x`, `y`, and `width`. The `drawRect` function uses these parameters to draw a rectangle, but also accesses the built-in `width` variable of p5.js, which can cause conflicts. To avoid this conflict, the author renames the parameter `width` to `rectWidth` and updates its value inside the function. This allows the function to manipulate its own scope independently of the global scope. The author also notes that variables defined within a function are only accessible within that function's scope, and changes made within the function do not persist outside of it.

Please note that I did not include any links or formulae as they were not present in the original text.

