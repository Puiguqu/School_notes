# Week 19 - CM1005 Introduction to Programming I - Topic 1. Your development environment (cont.) - Week 2

## The factory pattern Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/p1Edo/the-factory-pattern)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The factory pattern is a design pattern used to create objects without specifying the exact class of object that will be created. In this video, the author creates a single tadpole object with various properties and methods, and then uses the factory pattern to create multiple instances of the same object by encapsulating the creation logic in a separate function called `createTadpole`. The `createTadpole` function takes arguments for the x and y coordinates of the tadpole's initial position, which are randomly generated. The author then creates an array of tadpole objects using a loop and populates it with instances created by the `createTadpole` function. To handle the drawing and mouse click logic, the author modifies the original code to traverse the array of tadpoles instead of working with a single instance. This allows the behavior to be applied to multiple tadpoles simultaneously. The resulting code demonstrates the use of the factory pattern to create objects in bulk without copying and pasting code. By using this pattern, developers can write more efficient and maintainable code by separating object creation from usage logic.

---

## The constructor function and the new keyword Video• . Duration: 16 minutes 16 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/rOd2B/the-constructor-function-and-the-new-keyword)

Based on the transcript, here is a summary of the main points covered in the video:

**Introduction**

* The instructor introduces the concept of constructor functions and the `new` keyword.
* They explain that constructor functions are used to create new objects from scratch.

**Creating a simple object**

* The instructor creates a simple object called "Kitty" using a constructor function.
* They demonstrate how to use the `new` keyword to create a new instance of the Kitty object.

**Adding properties and methods**

* The instructor adds properties (such as color and size) and methods (such as `draw`) to the Kitty object using the `this` keyword.
* They explain that `this` refers to the current instance of the object being created.

**Using a loop to create multiple objects**

* The instructor uses a for loop to create multiple instances of the Kitty object, each with different properties and colors.
* They demonstrate how to use random values to generate different colors and locations for each kitten.

**Creating an array of objects**

* The instructor creates an array called `kitties` and populates it with multiple instances of the Kitty object using a loop.
* They explain how to access and manipulate individual elements in the array.

**Using the factory pattern**

* The instructor introduces the concept of the factory pattern, which is used to create objects without specifying their exact type.
* They demonstrate how to use a constructor function as a factory to create multiple instances of an object with different properties and behaviors.

Overall, the video covers the basics of constructor functions, object creation, property management, method overriding, and array manipulation. It also introduces the concept of the factory pattern and how it can be used to create objects without specifying their exact type.

---

## Creating a particle system Video• . Duration: 33 minutes 33 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/l1lur/creating-a-particle-system)

This is a transcript of a video on creating a particle system using JavaScript and the constructor function pattern. Here's a breakdown of the content:

**Introduction**

The instructor introduces themselves and explains that in this lesson, they will be teaching how to create a particle system using JavaScript.

**Creating a new class**

The instructor creates a new class called `Particle` using the constructor function pattern. They explain the benefits of using constructors, including encapsulation, code reuse, and ease of use.

**Properties and methods**

The instructor adds properties (e.g., position, velocity, color) and methods (e.g., update, render) to the `Particle` class. They explain how these properties and methods will be used to control the behavior of individual particles in the system.

**Creating a particle system**

The instructor creates an instance of the `Particle` class and adds it to an array called `particles`. They then define two functions: `updateParticles` and `renderParticles`. The `updateParticles` function updates the position and velocity of each particle based on their properties, while the `renderParticles` function renders each particle on the screen.

**Updating particles**

The instructor explains how the `updateParticles` function works. It iterates over each particle in the array, updates its position and velocity based on gravity (a constant value), and checks if the particle has reached the end of its lifetime. If it has, the particle is removed from the array.

**Rendering particles**

The instructor explains how the `renderParticles` function works. It uses a canvas element to render each particle on the screen, with the color and size determined by the particle's properties.

**Blooming effect**

The instructor introduces a blooming effect that makes particles fade out as they move away from the center of the screen. They add a new property called `lifetime` to the `Particle` class and modify the `updateParticles` function to test against this value instead of a fixed number.

**Final touches**

The instructor adds some final touches to the particle system, including changing the color and size of particles to create a stylized effect. They also encourage viewers to experiment with different values and techniques to create their own unique effects.

Overall, this transcript provides a step-by-step guide to creating a basic particle system using JavaScript and the constructor function pattern. It covers topics such as encapsulation, code reuse, and ease of use, as well as more advanced concepts like gravity, blooming effects, and rendering on the screen.

---

## When to use constructors Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/PugEb/when-to-use-constructors)

The text discusses the decision-making process for choosing between literal objects, factory patterns, and constructor functions in object-oriented programming. The author suggests that identifying the appropriate structure depends on the specific problem and experience with the language.

To decide, ask yourself:

- Do you need multiple objects of the same kind? If yes, a factory pattern or constructor might be suitable.
- How many properties does the object have? More complex objects require a factory pattern or constructor function.
- Will the object expand as development progresses? A factory pattern or constructor function is recommended.

The author presents three case studies:

1. An object to store game play egizer during gameplay, where only one property (lives) is needed and no methods are required, making a literal object suitable.
2. An object to store data for drawing mountains as background objects in the game, where multiple properties are needed and no interaction is required, making a factory pattern suitable.
3. An object for an enemy character with many properties and methods, requiring significant expansion, making a constructor function suitable.

The author concludes that choosing the right structure depends on the specific problem and experience.

---

## Code it from scratch: Robot factory Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/supplement/1uCR4/code-it-from-scratch-robot-factory)

Here is a summary of the text in 8 sentences:

The goal of this exercise is to create a robot factory that can produce multiple robots on the screen at the same time. To achieve this, developers are guided to use the existing robot drawing code from a previous example as a starting point. The program should be extended to display a new robot head at the cursor location each time the canvas is clicked. If struggling with the concept, watching the factory pattern video again is recommended for clarification. Additional ideas for extending the example include reimplementing the factory pattern using a constructor function and animating the robot heads to bounce around the screen. To accomplish these tasks, developers can refer to additional resources such as the lesson 10.1 "Factory Pattern" video and reading materials. The exercise aims to reinforce understanding of the factory pattern in programming and its practical applications. By completing this task, developers will gain hands-on experience with the concept and be able to apply it to future projects.

---

## Hack it: make your own particles Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/supplement/TfBuK/hack-it-make-your-own-particles)

There is no text to summarize. The provided text appears to be a list of links and durations for various video lectures on coding, specifically focusing on the topic of particle systems and constructors in programming. It does not contain any specific information or details that can be summarized.

However, I can provide an outline of what might be included in such a lecture:

* Creating multiple particle emitters with random colors
* Using vectors to construct particles
* Recreating graphics using particle systems

If you could provide the actual text or more context, I would be happy to assist you with summarizing it.

---

