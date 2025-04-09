# Case study 1: drawing app Reading• . Duration: 2 hours 2h

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/supplement/iPuwr/case-study-1-drawing-app)

Here is the rewritten text in a format that is easier to read and understand:

**Case Study 1: Drawing App**

To complete this case study, follow these steps:

1. Open the drawing app folder by dragging it into Visual Studio Code or Brackets.
2. Click on the "Live Preview" button to open the application in your browser.
3. Try out all the tools in the drawing application:
	* Freehand tool
	* Line draw tool
	* Spray can tool
	* Mirror draw tool

Notice that the "Clear" and "Save" buttons don't work yet. We'll address those soon.

**Reading the Files**

Before you start altering the application, read through the various files that make up the drawing application template:

1. `index.html`: HTML content of the application
2. `style.css`: Style sheet for the application
3. `sketch.js`: p5.js sketch with setup and draw functions
4. `p5.min.js`: p5 library (don't worry too much about this one)
5. `colourPalette.js` and `toolbox.js`: Container functions that you don't need to fully understand, but might use some properties from

**Tasks**

Complete the following tasks:

1. **Task 1: Documenting lineToTool.js**
	* Open `lineToTool.js` and read it out loud to a friend or family member.
	* Try commenting out two lines of code to see how it affects the program.
2. **Task 2: Turning sprayCan into a constructor function**
	* Cut the spray can object literal from `sketch.js` and paste it into a new file called `sprayCanTool.js`.
	* Rewrite the object literal as a constructor function called `SprayCanTool()`.
	* Don't forget to add properties and methods with `this` (e.g. `this.points = 13`).
3. **Task 3: Completing helperFunctions**
	* Read through `helperFunctions.js` and find the two event handlers for saving and clearing.
	* Replace `???` on line 9 with the p5.js background function to reset the color to white.
	* Replace `???` on line 19 with a function to save the canvas.

**Further Enhancements**

When you've completed these tasks:

1. Take a look at the mirror tool and try to understand how it works.
2. Try writing your own tools, like a rectangle tool or an ellipse tool.
3. When you're done, upload your completed drawing app sketch for peer review.

This will give you feedback on your progress and help you determine if you've fully understood the tasks. The peer review activity is scheduled for next week's content.

