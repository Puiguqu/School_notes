# Week 17 - CM1005 Introduction to Programming I - Topic 1. Your development environment (cont.) - Week 2

## Methods: Objects which can do things Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/32PCx/methods-objects-which-can-do-things)

Here is a summary of the text in 8 sentences, preserving key information:

The video transcript discusses building upon knowledge of functions and objects to bring them together by creating objects that contain both properties and functions, referred to as methods. Methods are used to perform actions or behaviors within an object, such as drawing or updating values. To create a method, the syntax is: `method_name : function()` where `function` contains parameters in parentheses. The body of the method is enclosed in curly brackets `{}`. When calling a method on an object, the same data operator is used as with properties, followed by parentheses to set any required arguments. The video example demonstrates creating a "kitty" object with a method called "meow" that outputs the text "meow" to the screen at a specified position. Parameters are added to make the meow function more flexible and reusable. By using parameters, the function can be called multiple times with different positions and values.

---

## This: making objects refer to themselves Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/z6HHH/this-making-objects-refer-to-themselves)

Here is a summary of the text in 8 sentences, preserving key information:

In JavaScript, objects can access their own properties using the `this` keyword. This allows developers to encapsulate code within objects, making it easier to manage complex data structures. The example demonstrates how to create an object with methods (functions) that operate on its own properties. In the first example, a `MyRect` object is created with properties for position and size, and a method `draw()` that uses `this` to access these properties. The second example creates a `RocketShip` object with methods `draw()` and `moveRockets()`, where `moveRockets()` uses `this` to access the rocket's properties. To make `moveRockets()` work, the developer must use `find and replace` to update all instances of `rocket` with `this`. This approach allows developers to create modular, organized code by encapsulating related functionality within objects. By using methods to operate on an object's properties, developers can write more efficient and maintainable code.

---

## Exploring a p5 object: Vector Video• . Duration: 18 minutes 18 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/M747L/exploring-a-p5-object-vector)

Here is a written summary of the transcript:

The video explores the p5 vector object, which is used to represent points in space. The author introduces several key concepts and methods related to vectors.

First, the author discusses how to manipulate vectors using basic arithmetic operations such as addition, subtraction, multiplication, and division. They also explain how to use the dot product method to calculate the angle between two vectors.

Next, the author delves into the details of the p5 vector object's methods, including:

* `mult`: multiplies a vector by a scalar value
* `mult()`: returns a new vector with the original vector multiplied by the specified scalar value
* `div`: divides a vector by a scalar value
* `mag`: calculates the magnitude (length) of a vector
* `angle()`: calculates the angle between two vectors using the dot product method
* `normalize()`: normalizes a vector to have a length of 1

The author provides examples and explanations for each of these methods, including code snippets in JavaScript.

Finally, the video touches on how to use these methods to create something interesting, such as creating a Tamagotchi game. However, this section is not fully explored in the transcript, leaving it for further explanation in another video.

Throughout the video, the author emphasizes the importance of understanding and mastering vector operations and methods in p5.js development.

---

## Bringing it all together: Tamagotchi Video• . Duration: 29 minutes 29 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/uE1tV/bringing-it-all-together-tamagotchi)

The transcript provided appears to be a teaching script for an introductory programming course, likely in Python, that uses the p5.js library. The script is used to demonstrate how to create a simple animation of a "tamagotchi" using p5.js.

Here's a breakdown of what the script does:

1. **Initialization**: The script initializes a new p5.js sketch and sets up some basic variables.
2. **Creating the Tamagotchi**: The script creates the tamagotchi by drawing its body, head, eyes, and mouth using various shapes and colors.
3. **Adding Interactivity**: The script adds interactivity to the tamagotchi by responding to mouse movements and key presses. When the mouse is moved over the tamagotchi's head, it changes color; when a key is pressed, it makes the tamagotchi "happy" or "sad".
4. **Adding Animation**: The script adds animation to the tamagotchi by rotating its points around a central axis as it grows.

The transcript also provides additional information about p5.js and its built-in features, such as vectors and their static and non-static methods.

Some key concepts covered in this transcript include:

* Working with p5.js
* Understanding vectors and their methods
* Creating simple animations using p5.js
* Adding interactivity to a sketch

Overall, the script provides a solid foundation for learning how to create interactive sketches using p5.js and covers some of the basics of vector manipulation and animation.

---

## Hack it: Rocket Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/supplement/Ob49J/hack-it-rocket)

There is no text provided for me to summarize. The text appears to be a lesson plan or instructional guide, outlining extensions and activities for a programming exercise on rockets. It mentions various methods and topics, such as using vectors, adding sounds, and implementing a fire method, but does not provide specific details or information that can be summarized.

If you could provide the actual text or context, I would be happy to assist you in summarizing it into 8 sentences, preserving key information, formulae, links, and technical details.

---

