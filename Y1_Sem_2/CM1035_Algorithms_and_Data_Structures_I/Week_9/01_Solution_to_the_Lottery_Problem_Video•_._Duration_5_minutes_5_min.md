# Solution to the Lottery Problem Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/SSDZj/solution-to-the-lottery-problem)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The module "Algorithms and Data Structures Part 1" introduces sorting algorithms, which are closely related to searching algorithms. To determine the winner of a lottery based on whether someone shares their birthday with anyone else, a linear search is applied to every element in a vector containing player numbers and birthdays. The approach involves counting the appearances of each birthday number using a linear search, starting from one birthday and moving through the vector, incrementing the count for each appearance. This process is represented by the function FindBirthdays(v), where v is the input vector, and uses a dynamic array to store the number of times each birthday appears in the vector. The algorithm begins with the second element of the vector and loops over all remaining elements, searching for matching birthdays and counting their appearances. If a birthday appears only once, it is recorded in the dynamic array. The algorithm continues until all birthdays have been processed, resulting in a dynamic array containing all unique birthdays. By sorting the birthdays using an appropriate algorithm (such as bubble sort or insertion sort), it becomes easier to determine the winner of the lottery.

Note: I removed some technical details and omitted links, as they were not provided in the text.

