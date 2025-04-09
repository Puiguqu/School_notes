# Sleuth case by case 802 Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-1/lecture/9lCLy/sleuth-case-by-case-802)

Here is a summary of the text in 8 sentences, preserving key information and details:

The video transcript discusses Case 802, "Case of Montecarlo," where the speaker uses R programming to analyze data from a poker game against statisticians. The goal is to identify cards that are either diamonds or Aces and mark them accordingly. The speaker creates a function called `cardPicker` to iterate through an array of 52 cards, checking for these specific properties. If a card matches, it sets the `marked` property to true. To test the function, the speaker calls it from within the `setup` function and observes that diamonds are not marked yet, indicating a need to call the function before running the simulation. The speaker then modifies the code to include an additional condition for Aces, setting the `marked` property to true when the card's number equals 1 (for Ace). Running the updated simulation results in the correct marking of both diamond and Ace cards.

