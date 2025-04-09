# Week 5 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Introduction Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/83Qw9/introduction)

There is no text to summarize. The provided text appears to be a transcript of a video or lecture on a topic related to counting and computer science, but it does not contain any specific information, formulae, links, or technical details.

However, based on the context and the mention of the pigeonhole principle, counting rules (sum and product), inclusion-exclusion principle, and permutations/combinations, I can provide a general outline of what the text might cover:

The lecture is likely to introduce students to key principles in counting, including:

1. Counting rules: sum and product
2. Inclusion-exclusion principle
3. Pigeonhole principle
4. Permutations and combinations

These concepts will be used to solve problems, such as the given riddle about a person playing video games.

If you provide more text or context from the lecture, I would be happy to summarize it for you.

---

## Counting Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/2nruS/counting)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The product rule states that if a job can be split into two tasks, there are m ways to do Task 1 and n ways to do Task 2, resulting in m*n total ways. This concept was demonstrated with an example of choosing outfits from five pairs of trousers and seven shirts, where the product rule yields 35 possible combinations. The generalized version of the product rule applies to k tasks and states that if each task has ni ways of completion, then the total number of ways is the product of ni for i = 1 to k. This was illustrated with an example of choosing outfits including five shirts, three pairs of trousers, and two pairs of shoes, resulting in 30 possible combinations.

The sum rule states that if a job can be done either in n ways or m ways, then it can be completed in m+n ways, regardless of the distinction between the two sets of choices. This concept was demonstrated with an example of selecting an item to donate to a charity from five pairs of trousers and seven shirts, where the sum rule yields 12 possible choices.

Additionally, the text mentions the inclusion-exclusion principle, which is not explicitly explained in the provided transcript, but it appears to be related to counting principles. The Pigeonhole Principle, discussed later in the lesson, states that if n items are put into m containers, with n > m, then at least one container must contain more than one item.

There is no explicit information about formulas, links, or technical details provided in the transcript.

---

## Complex counting Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/bneMC/complex-counting)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The problem of choosing a password requires counting the number of possible combinations that meet certain criteria, such as length and character type. For passwords of length 5-7 characters long, using uppercase letters or digits, at least one uppercase letter is required. The total number of possible passwords can be calculated using the formula 36^n - 10^n, where n is the length of the password. This calculation yields a total of 80,590,312,608 possible passwords for lengths 5-7. The sum rule and subtraction rule (also known as the inclusion-exclusion principle) are used to count combinations when items appear in both lists. For example, if two menus each have 5 items with some items in common, the number of choices is calculated by adding the total number of items in both lists and subtracting the number of items in common. The formula for this calculation is n + m - k, where n is the number of items in one list, m is the number of items in the other list, and k is the number of items in common. For a specific example, if two menus each have 5 items with 2 in common, the total number of choices is 8 (5 + 5 - 2).

---

## The Pigeonhole Principle Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/e4akZ/the-pigeonhole-principle)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The pigeonhole principle states that if there are k+1 or more objects to be placed in only k boxes, then there will be at least one box containing two or more objects. This principle can be applied to various scenarios, such as drawing cards from a deck, selecting students for a class, or choosing countries randomly. In the context of card selection, if five cards are drawn from a standard 52-card deck, there is at least a 50% chance that two of them share the same suit (k+1 = 5 and k = 4). Similarly, if there are more than 367 students in a class, at least two of them will share a birthday. The generalized pigeonhole principle states that if there are n objects to be placed in k boxes, then at least one box contains n/k objects. To prove this, proof by contradiction can be used. An example demonstrating the application of the generalized pigeonhole principle is selecting cards from a deck to guarantee that five cards share the same suit; it requires at least 17 cards (n = 17 and k = 4). By understanding the pigeonhole principle, one can better grasp various combinatorial concepts and apply them to real-world scenarios.

---

## The Pigeonhole Principle – examples part 1 Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/ULr4l/the-pigeonhole-principle-examples-part-1)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The pigeonhole principle states that if n items are put into m containers with n > m, then at least one container must contain more than one item. In the context of remainders when divided by 3, this can be applied to show that among four integers, there will be at least two with the same remainder when divided by 3. The generalized pigeonhole principle states that for k objects and n boxes, if k > n, then at least one box must contain more than one object. This was demonstrated in an example where seven blue balls and four red balls were selected from a bag, showing that five balls would guarantee three of the same color among the selected balls. The principle can also be applied to finding the minimum number of integers needed to ensure certain conditions are met, such as selecting five integers from 1-8 that will guarantee at least two adding up to 9. In a social context, the pigeonhole principle can be used to demonstrate that in a room with n people, there will be at least two people with the same number of friends. The possibilities for the number of friends an individual can have are limited and can be categorized into six possible values: -1, 0, 1, 2, 3, or n-2. In all cases, the pigeonhole principle ensures that there will be at least one person sharing a box with another person having the same number of friends.

Note: I did not include any technical details, formulae, or links as they were not explicitly mentioned in the summary and were already implied by the text.

---

## The Pigeonhole Principle – examples part 2 Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/5hRxb/the-pigeonhole-principle-examples-part-2)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The pigeonhole principle states that if there are more objects (pigeons) than containers (holes), then at least one container must contain more than one object. To demonstrate this, consider selecting 7 distinct numbers from a set of 1-11. By placing each number in a "pigeonhole" corresponding to its sum with another number equal to 12, we can show that there are two numbers whose sum is 12. Similarly, for a set of 1-20 and selecting 11 integers, we can place each pair of numbers in a "pigeonhole" differing by 2, ensuring at least one pigeonhole contains two pigeons. The generalized pigeonhole principle can be applied to any number of objects and containers, stating that if there are more objects than containers, then at least one container must contain more than one object. For example, among 100 people, we can apply this principle by considering each month as a "box" and dividing the population into 12 boxes, ensuring that at least one box contains at least ⌈100/12⌉ = 9 people born in the same month. This demonstrates that with more objects than containers, there must be overlap or sharing between at least two containers. The pigeonhole principle is a useful tool for solving problems involving partitioning and distribution of objects into distinct groups.

Note: I did not include links as they were not present in the original text. Also, I did not include any calculations or formulae that were not explicitly mentioned in the text.

---

## The Pigeonhole Principle Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/SxwDd/the-pigeonhole-principle)

There is no text provided for me to summarize. The given text appears to be a course syllabus or reading list with recommendations for students to follow in order to understand key concepts related to counting principles, inclusion-exclusion, and the Pigeonhole Principle. However, it does not contain any specific information, formulae, links, or technical details that I can summarize.

If you could provide the actual text, I would be happy to assist you in summarizing it into 8 sentences while preserving all key information, formulae, links, and technical details.

---

## Week 5 exercises Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/Ds7Eu/week-5-exercises)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The Pigeonhole Principle states that if n items are put into m containers, with n > m, then at least one container must contain more than one item. To apply this principle to real-world problems, practice exercises can be attempted to test knowledge and identify areas for additional study. In a bowl containing 10 red balls and 10 blue balls, selecting at least 3 balls guarantees having at least 3 balls of the same color, and selecting at least 6 balls ensures having at least 3 blue balls. When seven integers are selected from the first 10 positive integers, there must be at least two pairs of these integers with a sum of 11. In a class of 30 students, there must be at least two students whose last names begin with the same letter. A class of nine students must have at least five male students or at least five female students to guarantee this condition. Furthermore, a class of nine students must also have at least three male students or at least seven female students to satisfy this requirement. The Pigeonhole Principle can be used to solve various problems involving probability and combinatorics, making it an essential tool for further study and practice.

---

## Week 5 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/vl0qo/week-5-exercises-hints-and-tips)

Lesson 3.0 Introduction Lesson 3.1 Counting Lesson 3.2 The Pigeonhole Principle Video: Video The Pigeonhole Principle . Duration: 3 minutes 3 min Video: Video The Pigeonhole Principle – examples part 1 . Duration: 4 minutes 4 min Video: Video The Pigeonhole Principle – examples part 2 . Duration: 3 minutes 3 min Practice Assignment: Use the Pigeonhole Principle . Duration: 25 minutes 25 min Discussion Prompt: Think of an example ....

---

