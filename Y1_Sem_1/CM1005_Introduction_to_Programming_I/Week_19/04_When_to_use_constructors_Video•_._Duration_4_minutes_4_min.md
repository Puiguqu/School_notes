# When to use constructors Video• . Duration: 4 minutes 4 min

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

