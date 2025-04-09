# Week 8 - CM1005 Introduction to Programming I - Topic 1. Your development environment (cont.) - Week 2

## Game project 3a: interaction with the game character Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/SWLES/game-project-3a-interaction-with-the-game-character)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The video transcript focuses on getting started with Game Project Three, specifically interacting with the game character using keystrokes. The author declares variables for interactions such as left, right, and face direction, which are used to animate the game character. To add the game character code, the author copies relevant code from Part Two A and pastes it into their sketch. Conditional statements are added in the draw function to move the character based on the input of left and right arrows. The character's position is updated by modifying its x-coordinate using unchange (gameChar x) or unchange (gameChar y). The author demonstrates how to create movement for the character, including left and right movements, with optional adjustments to speed. The video concludes by emphasizing that there are still stages to complete in Game Project Part Three, leaving them up to individual completion.

---

## Game project 3b: canyons and coins Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/ar1kk/game-project-3b-canyons-and-coins)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The instructor guides students to continue working on Game Project Three, building upon their previous work by adding interaction between the game character and collectables. They copy the `collectable` code from Project Two Part B into the current sketch file for Game Project Three. The instructor explains that they want to add a property called `isFound` to the collectable object and set its value to `false`. They then create an if statement to draw the collectable only when `isFound` is `false`, allowing the character to pick up the collectable. To implement this, they use the `dist` function to calculate the distance between the character's position and the collectable's position, setting the condition for drawing the collectable to be less than 20 pixels. Once the collectable has been found, its `isFound` value is set to `true`, preventing it from being drawn again. The instructor notes that there are additional tasks to complete in Game Project Three, including drawing the canyon and testing falling down the canyon.

---

## Sleuth case by case: 401 Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/PE7OT/sleuth-case-by-case-401)

Here is a summary of the text in 8 sentences, preserving key information, formulas, links, and technical details:

The video transcript discusses implementing conditional statements in a game project to respond to different poison levels. The goal is to save Console City from Norbert Weiner's Stand by adjusting antidote amounts based on specific conditions. The code initializes variables for poison and antidotes (insulin, paracetamol, ethanol) and uses a moving graph to display poison amounts. Conditional statements are written to decrease insulin when snake venom exceeds 0.64, increase insulin when Warfarin falls below 0.46, and adjust other antidote levels accordingly. The code is implemented by copying and pasting the conditional statements into the program, with errors corrected along the way. After submitting the sketch, it appears that some adjustments are needed to correctly implement the antidotes. To correct these mistakes, the transcript suggests reviewing the specific conditional statements for paracetamol and Warfarin. By addressing these issues, the game project should be able to save Console City from Norbert Weiner's Stand.

---

## Sleuth case by case: 402 Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/aluQ4/sleuth-case-by-case-402)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The case "Why Gang Ruby Heist" from the game project involves a detective running through Console City to catch a ruby thief. The script uses an if statement to determine whether the current road equals Huffman Street, giving the detective a direction to travel east. To turn the detective onto Packard Avenue, another if statement is used with a condition checking for Packard Avenue, setting the direction to south. However, without additional code, Matz gets away. Adding an else if clause or an else condition can improve the script's clarity and extend its functionality. The script has successfully turned the detective onto Adele Street, going west, but will run out of steam without a final direction. A larger if statement with multiple conditions can be used to turn the detective onto Reynolds Street as well, allowing them to continue their pursuit. By submitting this solution, Sleuth yields 75% accuracy, indicating that the script has correctly navigated three corners.

---

## Sleuth case by case: 403 Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/J2q8k/sleuth-case-by-case-403)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The speaker guides viewers through solving "Case 403", also known as the Shiffman stakeout. The goal is to sound an alarm when the criminal mastermind, Shiffman, crosses Adele Street from west to east. To achieve this, the viewer must draw a cyan rectangle covering the entire map from Adele Street to the west. A conditional statement is used to check if Shiffman's position (represented by a red dot) has crossed over Adele Street to the left of its current x-coordinate (1721). The code uses a simple if-statement with `mouseX` to determine this. Once the alarm is triggered, a cyan rectangle is drawn using the `rect()` function, covering the entire map from Adele Street to the west. The rectangle's width and height are determined by the map's dimensions and Shiffman's x-coordinate. By following these steps, the viewer can successfully sound the alarm when Shiffman crosses Adele Street.

---

## Code editor: reminder about Visual Studio Code Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/supplement/mh6FI/code-editor-reminder-about-visual-studio-code)

There is no text provided for me to summarize. The given text appears to be a course announcement or schedule, discussing various video lectures, game projects, and coding editors (Brackets and Visual Studio Code). It seems to provide technical details about compatibility and recommendations for code editors, but does not contain any key information, formulae, links, or technical details that would require summarization. If you could provide the actual text, I would be happy to assist you with a summary in 8 sentences.

---

## Sleuth case 401, 402, and 403: Visual Studio Code Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/supplement/nMKKS/sleuth-case-401-402-and-403-visual-studio-code)

There is no text to summarize in this case. The provided text appears to be a list of lessons, videos, and reading materials related to the Sleuth application, but it does not contain any specific information or key concepts that need to be summarized.

However, I can provide a summary of the content:

The text invites users to complete three case series (401, 402, and 403) from the Sleuth application. Users have the option to use either Brackets or Visual Studio Code as their code editor, but are recommended to use Visual Studio Code due to its modernity and support.

The activities include watching videos (7 minutes, 4 minutes, and 5 minutes), reading materials (10 minutes each), and discussing a topic related to Sleuth cases. Users can mark the completion of these tasks, dislike them if needed, or report any issues encountered.

---

## Reflect on your learning Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/supplement/FHqMC/reflect-on-your-learning)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The course has covered the use of if-else blocks to control program flow based on specific test conditions, defining test conditions involving variables and logical operators, and acquiring new debugging techniques such as isolation and printing. Students have completed cases 401, 402, and 403 in the Sleuth module. To evaluate their learning, students should reflect on their skills and knowledge acquired so far, identifying areas that need improvement. They can develop a concrete action plan to improve their understanding by scheduling additional study sessions, seeking out resources, posting on the discussion forum, or setting specific goals for improvement. The course will include an evaluation activity at the end of each topic to review progress. Students should adjust their strategies and goals based on ongoing self-assessment and new feedback received. Learning is a continuous process, and it's okay to revise plans as needed. To continue with the course, students can access Lesson 4.4: Game project 3 - interaction with the game character and Lesson 4.5: Continuing with Sleuth, as well as watch video tutorials and read related materials.

---

