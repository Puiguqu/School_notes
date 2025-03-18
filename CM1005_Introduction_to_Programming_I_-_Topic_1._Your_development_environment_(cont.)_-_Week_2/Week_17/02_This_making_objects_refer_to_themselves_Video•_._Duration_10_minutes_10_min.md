# This: making objects refer to themselves Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/z6HHH/this-making-objects-refer-to-themselves)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

In JavaScript, objects can have functions called "methods" that allow them to perform actions on themselves. The `this` keyword refers to the current object being executed within a method. When creating an object with properties and functions, the `this` keyword points to the object when its code is running. This allows the object to access its own properties.

In the example provided, an object named "rocket" was created with methods for drawing and moving it on the canvas. The original draw function contained multiple references to "rocket", which were replaced with "this" using Find and Replace in the editor. This ensured that the correct object reference was used within the method.

The moveRocket function was also modified to use "this" instead of referencing the rocket object directly. This allowed the code to work as intended, reducing complexity in the draw function.

By using methods, objects can encapsulate their own behavior and maintain a clean and organized codebase. The example demonstrated how methods can be used to reduce repetition and improve readability.

