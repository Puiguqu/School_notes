# Week 3 - CM1005 Introduction to Programming I - Topic 1. Your development environment (cont.) - Week 2

## RGB (red, green and blue) colours Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/sf1qh/rgb-red-green-and-blue-colours)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The RGB (Red, Green, Blue) color model is used to create a wide range of colors on digital devices. In the code example provided, the background command sets the background color using three arguments: red, green, and blue, with values ranging from 0 to 255. These values represent the intensity of each color, with 0 representing no color and 255 representing maximum color intensity. The combination of these values allows for the creation of a vast number of colors, with exactly 16,777,216 possible colors in total (2^8 x 3). This is achieved by using binary arithmetic to calculate the combinations of red, green, and blue values. By experimenting with different values and combinations, users can create their own unique colors. The RGB color model is used in various applications, including graphics and game development. Online tools, such as RapidTables.com, are available for users to experiment with and find perfect shades for their desired colors.

Note: I removed the additional page content as it was not part of the original text and only provided information about lesson plans and practice assignments.

---

## Fill, stroke, noFill Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/CWSls/fill-stroke-nofill)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The video transcript discusses controlling colors in a program using fill, noFill, stroke, and noStroke commands. Fill changes the inside color of shapes, while noFill makes them transparent. The stroke command controls the outline of shapes, similar to fill. To avoid problems with repetitive drawing loops, it's essential to set the color at the beginning of the draw function. Transparency can be achieved by adding a fourth argument to the fill command, which sets the alpha value (0-255). Experimenting with different colors and transparency levels can create interesting effects. The video also touches on setup and program flow, highlighting the importance of setting colors correctly in the draw function. Finally, it recommends practicing exercises such as the Hackett exercise, Robot Parade, and Kandinsky, which can help improve skills in controlling colors and shapes.

---

## Setup, draw and programme flow Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/G9VO3/setup-draw-and-programme-flow)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The video transcript discusses program parts and flow, exploring how a program is executed from beginning to end. The setup function is executed first, before the draw function, which is called repeatedly every frame. A frame refers to a still image played progressively over time to create an illusion of movement in films or animations. The order of lines within the functions matters, as they should be written from top to bottom like text in a book. Incorrect indentation can lead to unexpected behavior. To demonstrate this, the code is modified to show how changes in indentation affect the program's output. Another trick involves setting an alpha channel on a color value, allowing for semi-transparency, such as adding an alpha value of 100 to one of the squares.

---

## Ellipse, rect, line, triangle and point Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/NhMrI/ellipse-rect-line-triangle-and-point)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The video transcript introduces basic shapes in Processing, a programming language for visual design. An ellipse is created with four parts, where the center coordinates (x and y) determine the shape's orientation, and width and height are the same as the diameter. Changing these values can stretch or shrink the ellipse. The line command takes two pairs of x and y coordinates to draw a line between two points, which can be horizontal, vertical, diagonal, or any combination thereof. A triangle is created with three pairs of coordinates for each corner, allowing for various types of triangles to be drawn. Additionally, the point command can be used to create a visible dot on the screen using a stroke weight command, but it may affect other shapes if not reset to 1. The Processing language retains state between drawings, so the stroke weight set earlier will still apply when drawing other shapes unless reset. To practice drawing functions and exercises, there are various videos, assignments, and readings available, including a "Robot parade" exercise and an assignment to create a Kandinsky-inspired abstract art piece from scratch.

---

## How to access and use the console to view errors Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/a8ouR/how-to-access-and-use-the-console-to-view-errors)

Here is a summary of the text in 8 sentences, preserving key information:

The Console is a powerful tool that allows developers to see what their program is doing under the hood. To access the Console, users can navigate to three different browsers: Chrome, Safari, and Firefox. In each browser, users can access the Console by going to the developer menu or using the hotkey for JavaScript Console. The Console displays several tabs, including Elements, Sources, and Console, with the latter being the relevant tab for error messages. When debugging errors, developers should pay close attention to capitalization, as it is crucial in programming languages such as code. In this video, the creator demonstrates how to access the Console in each browser and fixes an error by adding a capital C to the "createCanvas" command. The process of identifying and fixing errors is called debugging, which will be explored in more detail in a future video. By using the Console and debugging syntax errors, developers can improve their coding skills and create more reliable programs.

---

## Debugging syntax errors Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/d9nVz/debugging-syntax-errors)

The concept of bugs in coding is discussed, where mistakes are called "bugs" due to their resemblance to the first computer bug, a moth that caused an error. Debugging is a core skill in programming that takes time to master and is essential for identifying and fixing errors.

Two types of syntax errors are identified: (1) missing brackets or parentheses, which can be easily fixed by adding the correct characters; (2) unexpected identifiers, where the code uses incorrect variable names or function calls. These errors can cause the program to produce unexpected results or crash.

The console is used as a tool to identify and fix syntax errors. It provides information about the line number of the error, which helps in locating the exact spot where the mistake occurred. However, it may not always be able to determine the root cause of the error, requiring the programmer to use their own deduction skills.

Another type of error discussed is argument errors, where the program expects a certain number or data type of arguments but receives an incorrect one. This can cause unexpected results or crashes.

Examples are given to illustrate these concepts, including a simple drawing program that produces unexpected results due to syntax and argument errors. The programmer uses the console to identify the errors, adds the correct characters or arguments, and fixes the code.

The video concludes by emphasizing that debugging is an essential skill in programming and encourages viewers to try the debug challenge that follows the video.

---

## Programming exercise 3. Hack it: Robot parade Reading• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/supplement/Wcfv6/programming-exercise-3-hack-it-robot-parade)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

This hack allows users to customize their own robots for participation in a robot parade. The goal is to transform the existing grey robots into a colorful parade using techniques learned from previous lessons. Users will work with RGB (red, green, and blue) colors, shapes, and programming concepts to achieve this. To get started, open the provided ZIP file and run the sketch to view the initial grey robot parade. The task requires making each robot on the parade unique in terms of body design. Additional learning materials are available for users to explore ellipse, rect, line, triangle, and point shapes, as well as setup, draw, and program flow concepts. Users can also access additional resources such as programming exercises, code examples, and discussion prompts to enhance their learning experience. The hack is designed to be completed within 30 minutes, with optional extensions available for further practice and exploration.

---

## Programming exercise 4. Code it from scratch: Kandinsky Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/supplement/EyNhN/programming-exercise-4-code-it-from-scratch-kandinsky)

Here is a summary of the text in 8 sentences, preserving key information:

Wassily Kandinsky worked at the Bauhaus school in Germany from 1922 to 1933, where he developed theories on geometric relationships between straight lines, curves, and circles. One notable example of his work during this period is "Circles in a Circle" (1923), which demonstrates his exploration of these geometric principles. To learn about Kandinsky's art, students can code their own masterpiece using P5.js, utilizing shapes such as triangles, ellipses, lines, and points. A provided template can be used as a starting point for creating a Kandinsky-inspired composition. The text also provides various video lessons covering topics like RGB colors, fill and stroke styles, setup, draw, and program flow, ellipse, rect, line, triangle, and point shapes. Additionally, there are practice assignments, reading materials, and discussion prompts available to supplement learning about Kandinsky's work. Students can choose to either copy or create their own composition using the provided template. The ultimate goal of these resources is for students to develop their skills in programming and art, inspired by Kandinsky's abstract styles.

---

## Teach it to yourself Reading• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/supplement/8i6cR/teach-it-to-yourself)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The topic focuses on learning to draw more complex shapes using P5.js functions, building upon previously learned primitive shapes (Rectangle, Triangle, points, and lines). To achieve this, students can use the following p5.js functions: `beginShape()`, `endShape()`, and `vertex()` to create more complex polygons. The lesson also covers other essential topics such as RGB colors, fill, stroke, setup, draw, and program flow. Students are encouraged to practice assignments and watch video tutorials on these topics, with durations ranging from 3-30 minutes. In addition, students will work on programming exercises, including "Hack it: Robot parade" and "Code it from scratch: Kandinsky", which require them to write code from scratch and debug their programs. The lesson also emphasizes the importance of debugging and troubleshooting using the console. Students are expected to learn about P5.js functions and apply them to create complex shapes on the canvas. To access additional resources, including a broken link, students can use the Student Portal to report any issues.

---

## Programming exercise 5: Debug challenge Reading• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/supplement/MoI7e/programming-exercise-5-debug-challenge)

There is not enough text provided to summarize and preserve all key information, formulae, links, and technical details. However, I can provide a summary of the context:

The text appears to be related to debugging a code snippet for a programming exercise, specifically "debugChallengeT2 ZIP File". The task involves identifying and fixing bugs in the code using techniques learned from previous lectures. Some of the bugs are syntax errors, while others have logic errors that need to be addressed.

If you provide more context or the actual text of the code, I would be happy to help summarize it in 8 sentences, preserving key information, formulae, links, and technical details.

---

