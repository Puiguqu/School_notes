# Solution to the Lottery Problem Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/SSDZj/solution-to-the-lottery-problem)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The module "Algorithms and Data Structures Part 1" focuses on sorting algorithms, which can make searching data more efficient. To solve a problem where determining the winner of a lottery based on unique birthdays is required, a linear search algorithm is applied to every other element in a vector containing player numbers and birthdays. The approach involves counting the appearances of each birthday number using a dynamic array to store their counts. A pseudocode function "FindBirthdays(v)" is described, where v is the input vector, which initializes an empty dynamic array and then applies a linear search starting from the second element (i=2) up to the length of the vector. The outer while loop iterates over each element in the vector, and an inner while loop checks if the birthday number appears elsewhere in the vector by comparing it with other elements. If a unique birthday is found, its count is increased by 1, and if the count equals 1, the birthday is recorded in the dynamic array. The dynamic array stores all birthdays that appear only once as input to the function. This approach ensures that the function can efficiently identify unique birthdays from a large dataset.

Note: I didn't include any formulae, links, or technical details not essential to understanding the main concepts and algorithm.

