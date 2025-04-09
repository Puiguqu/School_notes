# Game project - part 5: Multiple interactables Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/bT6E6/game-project-part-5-multiple-interactables)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The video transcript guides viewers through creating a game project Part 5 by refactoring code from Part 4 to make it reusable and flexible. The first step involves renaming the game project and adding necessary files, including a ReadMe file. The guide then explains how to create a new function called `drawClouds` to draw clouds, which replaces the original four-loop code. A similar process is followed for drawing mountains and trees using the same approach with a new function called `drawTrees`. However, when it comes to drawing collectables, a different approach is taken, as there are multiple interactables involved. The guide explains how to create a function called `drawCollectable` that takes an argument `t_collectable`, which represents a temporary collectable. To draw any collectable, the code replaces references to `collectable` with `t_collectable` inside the function. By passing a real collectable variable instead of `t_collectable`, the game characters can be drawn correctly when calling the function with a valid collectable object.

