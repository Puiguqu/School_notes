# This: making objects refer to themselves Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/z6HHH/this-making-objects-refer-to-themselves)

Here is a summary of the text in 8 sentences, preserving key information:

In JavaScript, objects can access their own properties using the `this` keyword. This allows developers to encapsulate code within objects, making it easier to manage complex data structures. The example demonstrates how to create an object with methods (functions) that operate on its own properties. In the first example, a `MyRect` object is created with properties for position and size, and a method `draw()` that uses `this` to access these properties. The second example creates a `RocketShip` object with methods `draw()` and `moveRockets()`, where `moveRockets()` uses `this` to access the rocket's properties. To make `moveRockets()` work, the developer must use `find and replace` to update all instances of `rocket` with `this`. This approach allows developers to create modular, organized code by encapsulating related functionality within objects. By using methods to operate on an object's properties, developers can write more efficient and maintainable code.

