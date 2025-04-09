# Week 6 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Permutations Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/M1Qlb/permutations)

Here is a summary of the text in 8 sentences, preserving key information, formulas, and technical details:

Permutation refers to an ordered arrangement of distinct objects. The number of permutations of n objects is denoted by n! (n factorial), which is the product of all numbers from 1 to n. For r-permutations of a set of size n, the formula P(n,r) = n × (n-1) × ... × (n-r+1) is used. In the context of photo arrangements, if we have four pets and want to take a side-by-side photo with two pets, there are 12 possible arrangements using the r-permutation formula with n=4 and r=2. When allocating three roles to 20 actors, the number of ways can be calculated using P(20,3) = 20! / (17!), resulting in 6840 possibilities. To count permutations containing a specific word "bad", we consider the reduced set {c, e, f, g, bad} and calculate permutations as 5!, then extend to all possible lengths by inserting "bad" into gaps, yielding 120 possibilities for length seven. The r-permutation formula is useful in calculating the number of ways for different scenarios involving distinct objects and slots.

---

## Combinations Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/K7G9i/combinations)

Here is a summary of the text in 8 sentences, preserving all key information, formulae, links, and technical details:

The problem of taking a photo of two pets from a group of four (mouse, cat, dog, and rabbit) illustrates the concept of combinations. A combination is an unordered arrangement of objects, and there are n!/(r!(n-r)!) ways to choose r elements from a set of n distinct elements. The formula for combinations, C(n, r), can be simplified by canceling out identical terms in the numerator and denominator. For example, to calculate the number of hands of 7 cards that can be dealt from a standard deck of 52 cards, we use the combination formula: C(52, 7) = 52!/(7!(52-7)!). The same calculation applies when choosing 45 cards per hand, as shown by the identity C(n, r) = C(n, n-r), which allows us to simplify the calculation. In a team of 11 players chosen from 16 footballers, the number of combinations is C(16, 11), which evaluates to 4368. The concept of combinations also applies to binary words with equal numbers of zeros and ones, as seen in the example of finding strings of length 8 with exactly four ones.

---

## Conclusion Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/9EuHK/conclusion)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The video transcript discusses counting techniques for breaking down complex problems into simpler ones. Permutation and combination differ from each other, and understanding these concepts is fundamental to computer science. The transcript presents a problem involving a person playing at least one round of a video game per day for 30 days, with a total of 40 rounds played over the same consecutive days. Two sequences, gI and fI, are defined: gI represents the number of games played up until and including day I, while fI = gI + 19. By combining the two sequences, we get 60 unique numbers, all less than 59, which implies that at least two of them must be equal by the pigeonhole principle. Assuming fj = gi, we substitute gj + 19 for fi to find gi - gi = 9, indicating that there are 10 consecutive days with the same number of games played (i.e., j+1, j+2, ..., I). This finding reveals a key insight into how order matters when dealing with combinatorial problems.

---

## Model answer for permutations Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/rl5pO/model-answer-for-permutations)

Lesson 3.3 Order matters Video: Video Permutations . Duration: 6 minutes 6 min Practice Assignment: Permutations . Duration: 20 minutes 20 min Discussion Prompt: Permutations . Duration: 20 minutes 20 min Reading: Reading Model answer for permutations . Duration: 10 minutes 10 min Video: Video Combinations . Duration: 10 minutes 10 min Reading: Reading Combinatorics . Duration: 1 hour 1h Practice Assignment: No order/combinations ....

---

## Combinatorics Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/PHAYM/combinatorics)

There is no text provided for me to summarize. The text appears to be a course syllabus or instructional guide that provides recommendations for studying topics related to combinations and permutations in mathematics. It includes links to specific videos, readings, and practice assignments, but does not contain any original content or findings.

If you provide the actual text, I would be happy to assist you with summarizing it into 8 sentences, preserving key information, formulae, links, and technical details.

---

## Week 6 exercises Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/3kCId/week-6-exercises)

Here is a summary of the text in 8 sentences, preserving key information:

In Week 6, students are encouraged to attempt exercises to practice concepts learned earlier. A zip code in Canada consists of three letters and three digits that alternate between letters and digits (e.g., A1B2C3). The number of possible zip codes can be calculated using combinatorial formulas. For instance, the number of zip codes that end with 6 and begin with A is 26^2 * 10 = 6760. Similarly, the number of bytes that begin with 101 and end with 110 is 8^4 * 2 * (1/8) = 128. Passwords for a computer system consist of eight distinct alphabetic characters, and various combinations can be calculated using combinatorial formulas. The number of possible passwords that end in MATH or contain the word COMPUTER as a substring is 26^7 * 6 = 2085064. Finally, three-digit numerals can be formed using the digits 2, 3, 5, 6, and 9 without repetition, resulting in 120 possible combinations.

---

## Week 6 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/78oRF/week-6-exercises-hints-and-tips)

There is no text provided for me to summarize. The given text appears to be a list of lesson plans and durations, but it does not contain any specific information or content that needs summarization.

If you provide the actual text, I would be happy to assist you in condensing it into 6 sentences while preserving key concepts, formulae, links, and technical details.

---

