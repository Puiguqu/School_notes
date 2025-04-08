# Week 4 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Proof by induction Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/NJOxu/proof-by-induction)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Mathematical induction is a form of proof used to show that a statement P is always true for all natural numbers n. The principle of mathematical induction states that if P(0) is true (the basis step), and for all k in N, if P(k) is true then P(k+1) is true (the inductive step), then P(n) is true for all n in N. This technique is used to prove statements where there is a chain, such as natural numbers. The three steps of proof by induction are: 1) proving that P(0) is true (basis), 2) proving that if P(k) is true then P(k+1) is true (inductive step), and 3) concluding that P(n) is true for all n in N (conclusion). The inductive hypothesis states that we assume P(k) is true, and then show P(k+1) is true. In this case, we do not assume the inductive step to be true, but rather prove it by assuming P(k) is true and showing P(k+1) is true. This technique can be used to solve various problems, such as proving statements about natural numbers.

Note: I did not include any additional information or links from the original text, only a summary of the key points and concepts in 8 sentences.

---

## Example of a correct proof Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/ANgoA/example-of-a-correct-proof)

Here is a summary of the text in 8 sentences, preserving all key information, formulae, links, and technical details:

The video discusses proof by induction, a method used to prove statements about natural numbers using mathematical induction. The first example states that the sum of the first n powers of two is equal to 2^n - 1, and attempts to prove this claim mathematically. To do so, it assumes the statement Pk is true for an arbitrary k, where Pk denotes the statement "2^0 + 2^1 + ... + 2^k = 2^k - 1". The inductive step then proves that if Pk is true, then P(k+1) is also true. This involves starting with the left-hand side of P(k+1) and using the inductive hypothesis to simplify it to the right-hand side. In the second example, the statement "n < 3^n" is claimed to be true for all natural numbers n, and a similar proof by induction is attempted. The basis step checks that P1 is true (1 < 3^1), while the inductive step proves that if Pk is true then P(k+1) is also true.

---

## Example of an incorrect proof Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/5fPXK/example-of-an-incorrect-proof)

Here is a summary of the text in 8 sentences, preserving key information and concepts:

The video transcript discusses examples of incorrect proofs using proof by induction. The first example considers the statement "n + 1 is less than n" for all natural numbers, which is clearly false. However, a flawed attempt to prove it was made, missing the basis step. In contrast, the second example attempts to prove that "all pencils are the same color." The attempted proof used induction but failed to address the basis step, assuming every group of two pencils has the same color without justification. Upon closer examination, the flaw in the second attempt becomes apparent when considering the case where k = 1. The transcript highlights the importance of verifying the basis and inductive hypothesis in proof by induction. A correct approach would involve demonstrating that at least one domino falls (i.e., establishing a basis) before proceeding with the inductive step.

---

## Conclusion Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/OWIlT/conclusion)

There is no text provided for me to summarize. The given text appears to be a video transcript with navigation instructions and metadata, but it does not contain any content or information that can be summarized in 8 sentences.

If you provide the actual text or content you would like me to summarize, I will be happy to assist you.

---

## Induction and recursion Reading• . Duration: 45 minutes 45 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/alXTA/induction-and-recursion)

There is not enough information in the provided text for a summary. The text appears to be a course outline or lesson plan for a topic on induction and recursion, but it does not provide any specific content, formulae, links, or technical details. It only includes general instructions on how to approach the material, such as watching videos before studying the essential reading.

---

## Week 4 exercises Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/NjDqO/week-4-exercises)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The exercises for Week 4 aim to test knowledge on mathematical concepts learned so far. One exercise involves proving the statement P(n) = 12 + 22 +···+ n2 = n(n + 1)(2n + 1)/6 for positive integer n. The basis step of this proof requires showing that P(1) is true, which is confirmed by plugging in n = 1 into the formula and verifying its validity. The inductive hypothesis states that if P(k) is true for a positive integer k, then P(k+1) must also be true. To complete the inductive step, one needs to prove that the truth of P(k) implies the truth of P(k+1). This involves using mathematical induction to prove three separate statements: 3n < n! if n is an integer greater than 6, 2n > n2 if n is an integer greater than 4, and 5 divides n5 − n whenever n is a non-negative integer. These exercises are optional but strongly recommended for further practice and to test knowledge.

---

## Week 4 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/NNSPi/week-4-exercises-hints-and-tips)

Lesson 2.3 Inductive proof Lesson 2.4 Conclusion Reading: Reading Week 4 exercises . Duration: 10 minutes 10 min Reading: Reading Week 4 exercises hints and tips . Duration: 10 minutes 10 min Discussion Prompt: What did you learn? What did you like? . Duration: 10 minutes 10 min Video: Video Conclusion . Duration: 2 minutes 2 min Lesson 2.5 Summative assessment

---

