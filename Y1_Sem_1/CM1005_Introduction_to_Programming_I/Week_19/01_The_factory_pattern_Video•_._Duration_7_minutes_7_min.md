# The factory pattern Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/p1Edo/the-factory-pattern)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The factory pattern is a design pattern used to create objects without specifying the exact class of object that will be created. In this video, the author creates a single tadpole object with various properties and methods, and then uses the factory pattern to create multiple instances of the same object by encapsulating the creation logic in a separate function called `createTadpole`. The `createTadpole` function takes arguments for the x and y coordinates of the tadpole's initial position, which are randomly generated. The author then creates an array of tadpole objects using a loop and populates it with instances created by the `createTadpole` function. To handle the drawing and mouse click logic, the author modifies the original code to traverse the array of tadpoles instead of working with a single instance. This allows the behavior to be applied to multiple tadpoles simultaneously. The resulting code demonstrates the use of the factory pattern to create objects in bulk without copying and pasting code. By using this pattern, developers can write more efficient and maintainable code by separating object creation from usage logic.

