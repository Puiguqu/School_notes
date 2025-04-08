# Week 5 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Introduction Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/83Qw9/introduction)

There is no text to summarize. The provided text appears to be a transcript of a video introduction to a lesson on counting principles in computer science, specifically CM1025 Fundamentals of Computer Science. It does not contain any key information, formulae, links, or technical details that can be summarized.

However, I can suggest some possible topics and concepts that could be covered in this lesson:

1. Counting rules: The lesson may cover the rules of sum and product, which are fundamental principles in combinatorics.
2. Inclusion-Exclusion Principle: This principle is used to count the number of elements in the union of multiple sets while avoiding double counting.
3. Pigeonhole Principle: This principle states that if n items are put into m containers, with n > m, then at least one container must contain more than one item.
4. Permutations and Combinations: The lesson may also cover formulas for permutations and combinations, which can help break down complex problems into simpler ones.

If you could provide the actual text to summarize, I would be happy to assist you further.

---

## Counting Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/2nruS/counting)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The product rule states that if a job can be split into two tasks, there are m ways to complete Task 1 and n ways to complete Task 2, resulting in m*n total ways to complete the job. This concept is applied to counting outfits from a selection of five pairs of trousers and seven shirts, where the number of outfits is 5*7 = 35 using the product rule. The generalized version of the product rule applies to k tasks, stating that if a job can be divided into k tasks with n_i ways of completing task i, then the total number of ways to complete the job is the product of n_1, n_2, ..., n_k. The sum rule states that if a job can be done in n ways or m ways, then it can also be completed in m+n ways, where there is no distinction between two sets of choices. For example, choosing an item to donate to a charity from five pairs of trousers and seven shirts results in 5+7 = 12 possible choices using the sum rule. The teacher's task of choosing an assistant from five classes with different student counts (28, 21, 24, 25, and 27) can be solved by applying the product rule to find the total number of ways to pick an assistant. In this case, the total number of students is 125, which represents the sum of the students in each class. To solve counting problems, techniques such as the product rule and sum rule are used to calculate the total number of possible outcomes or choices.

Note that some information was omitted from the summary, including video transcripts and links, as they were not essential to understanding the main concepts and findings presented in the text.

---

## Complex counting Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/bneMC/complex-counting)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The problem of generating passwords that meet certain criteria requires considering different cases based on password length. For a password length of 5 to 7 characters, each character can be either an uppercase letter or a digit, with at least one uppercase letter required. The total number of possible passwords for this range is 80,590,312,608, calculated using the formulae 36^length - 10^length, where length ranges from 5 to 7. In combinatorial problems, the sum rule can be used when items exclusively belong to one list, but the subtraction rule (inclusion-exclusion principle) must be applied when lists have items in common. This principle states that the number of choices is n + m - k, where n and m are the sizes of the two lists, and k is the number of items in common between them. To find positive integers less than 100 that are divisible by either 2 or 3, one can calculate the number of multiples of 2 (49) and 3 (33), and then subtract the number of multiples of 6 (16). This results in a total of 66 numbers that meet the criteria. The inclusion-exclusion principle is a general technique for solving combinatorial problems with overlapping sets, and it is essential to accurately apply it to avoid overcounting or undercounting solutions.

Note: I did not include any links or technical details as they are not relevant to summarizing the key concepts and findings of the text.

---

## The Pigeonhole Principle Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/e4akZ/the-pigeonhole-principle)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The pigeonhole principle states that if there are k+1 or more objects to be placed in only k boxes, then there will be at least one box containing two or more objects. This principle can be applied to various scenarios, such as drawing five cards from a standard deck of 52 cards, where at least two of them must be of the same suit. Another example is selecting seven countries at random, where at least two are in the same continent. The generalized pigeonhole principle states that if there are n objects to be placed in k boxes, then at least one box contains n/k objects. To prove this, a proof by contradiction can be used, but it goes beyond the scope of this topic. A further example demonstrates how the generalized pigeonhole principle works: selecting 16 cards from a standard deck of 52 cards guarantees that five cards are from the same suit. The number of cards needed to guarantee this result is at least 17, as n/4 = 5. By applying the pigeonhole principle and its generalization, we can solve problems involving distribution and probability.

---

## The Pigeonhole Principle – examples part 1 Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/ULr4l/the-pigeonhole-principle-examples-part-1)

Here is a summary of the text in 8 sentences, preserving key information:

The pigeonhole principle states that if there are n objects placed into m containers with the condition that n > m, then at least one container must contain more than one object. This principle can be applied to various scenarios, such as selecting integers from a set and finding at least two with the same remainder when divided by 3 (Example 1). In this example, we have four integers (n=4) placed into three boxes (m=3), ensuring that at least two integers share the same remainder. The generalized pigeonhole principle states that for n = k*2 + 1 integers, divided by k, there will be at least one box with more than one object (Example 2). For this example, we need to select five balls from a bag containing seven blue and four red balls to guarantee three of the same color are selected. This is equivalent to solving the equation x/2 = 3 for x, which yields x = 5 as the minimum number of balls required. In a third scenario (Example 3), we demonstrate that selecting five integers from 1-8 will ensure at least two of those integers add up to 9 by categorizing pairs into four boxes. Finally, in Example 4, we show that if there are n people in a room where every two individuals are friends or not, then there will be at least two people with the same number of friends (0, 1, 2, 3, or n-2).

---

## The Pigeonhole Principle – examples part 2 Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/5hRxb/the-pigeonhole-principle-examples-part-2)

Here is a summary of the text in 8 sentences, preserving key information:

The pigeonhole principle states that if there are n containers (pigeonholes) and n + 1 items (pigeons), then at least one container must contain more than one item. In this video, we will explore examples of this principle using a set containing numbers from 1 to 11. When selecting seven distinct numbers from the set, we can prove that there are two numbers whose sum is equal to 12 by dividing the range into six pairs (pigeonholes) and assigning each number to a pair based on its value. The video provides an example where selecting 11 integers from the set containing 1-20 results in two numbers with a difference of 2, demonstrating that there are at least two numbers whose sum is equal to 12. Another example demonstrates that among 100 people, there must be at least 9 who were born in the same month using the generalized pigeonhole principle. The number of boxes (months) is 12, and the ceiling of 100 divided by 12 is 9, indicating that at least one box contains at least 9 people. These examples illustrate the application of the pigeonhole principle to various problems, including finding pairs with specific sums or differences.

---

## The Pigeonhole Principle Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/SxwDd/the-pigeonhole-principle)

There is no text provided for me to summarize. The text appears to be a list of resources and instructions related to learning about the Pigeonhole Principle and counting principles, but it does not contain any substantive information or key concepts to summarize. If you provide the actual text, I would be happy to assist you in summarizing it in 8 sentences, preserving all relevant details and technical information.

---

## Week 5 exercises Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/Ds7Eu/week-5-exercises)

Here is a summary of the text in 8 sentences, preserving all key information, formulae, links, and technical details:

The Pigeonhole Principle states that if you have n pigeonholes (or containers) and more than n pigeons (or items), then at least one pigeonhole must contain more than one item. The principle can be applied to various scenarios, such as selecting balls from a bowl or students in a class. In the first scenario, a woman selects balls at random without looking at them from a bowl containing 10 red balls and 10 blue balls. To guarantee having at least three balls of the same color, she needs to select at least 4 balls (2 red + 1 blue or 3 blue). Similarly, to ensure getting at least three blue balls, she must select at least 5 balls (3 blue + 1 red or 4 blue and 1 more blue). The principle can also be applied to finding pairs of integers with a sum of 11 when selecting seven integers from the first 10 positive integers. With this scenario, there must be at least two pairs of integers that sum up to 11 (e.g., 3 + 8 = 11 or 5 + 6 = 11). Additionally, applying the principle to a class of 30 students shows that at least two have last names starting with the same letter. Finally, when there are nine students in a small college class, it is guaranteed that the class has at least five male students or at least five female students using the principle.

---

## Week 5 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/vl0qo/week-5-exercises-hints-and-tips)

Unfortunately, the provided text does not contain any actual information or key concepts about a specific topic. It appears to be a list of lesson titles, video durations, practice assignments, discussion prompts, and reading materials for an educational course.

If you could provide more context or clarify what topic this text is related to (e.g., mathematics, computer science), I would be happy to assist you in summarizing the key information and findings.

---

