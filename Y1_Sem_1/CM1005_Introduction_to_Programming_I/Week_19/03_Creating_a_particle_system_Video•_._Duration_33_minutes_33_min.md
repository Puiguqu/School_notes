# Creating a particle system Video• . Duration: 33 minutes 33 min

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

