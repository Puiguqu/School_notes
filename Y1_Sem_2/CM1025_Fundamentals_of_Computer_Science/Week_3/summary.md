# Week 3 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## What is a proof? Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/FQYqj/what-is-a-proof)

Unfortunately, there is no text to summarize. The provided text appears to be a video transcript and some additional page content, but it does not contain any specific information or concepts that can be summarized.

However, I can provide a general overview of what a proof is and its importance in mathematics:

A proof is a sequence of connected logical statements that explains why a statement is true. In essence, it's a way to demonstrate the validity of a mathematical concept or theorem. Proofs are essential in mathematics because they allow us to verify the truth value of mathematical statements, which is crucial for building trust in mathematical theories.

The importance of proofs cannot be overstated, as they provide a solid foundation for testing hypotheses and theories. In practical applications, such as software development, proof techniques like formal proofs and proof by contradiction can help ensure that algorithms and systems work correctly and efficiently.

If you'd like to discuss specific concepts or topics related to proofs, I'd be happy to help!

---

## Direct proof Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/cbPmW/direct-proof)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

A direct proof is a type of mathematical proof that uses logical steps to arrive at a desired statement, exploiting definitions and other mathematical theorems. To prove a statement using direct proof, one must know the definitions involved and take the correct first step. The sum of two even numbers is always even because an even number can be written as 2 times another integer (n = 2k and m = 2l for k and l natural numbers), and adding integers results in an integer. This demonstrates that the statement "the sum of two even numbers is always even" follows from basic definitions and rules of arithmetic.

Another example illustrates that n^2 + n is even when n is a natural number, as shown by considering cases where n is even or odd: if n is even, n^2 + n = (2k)^2 + 2k, which is even; if n is odd, n^2 + n = (2k+1)^2 + 2k+1, which is also even due to the addition of two even numbers.

A third example demonstrates that if a < b < 0, then a^2 > b^2 by exploiting inequalities and rules of arithmetic, specifically flipping the inequality sign when multiplying both sides by a negative number.

---

## Proof by contradiction Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/3bbVz/proof-by-contradiction)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The video transcript introduces proof by contradiction (indirect proof), a technique used to prove statements true. The desired statement A is assumed to be false, then definitions and logical steps are applied. This leads to a statement that contradicts the original assumption, making it incorrect. As a result, statement A is proven to be true.

A specific example proves the square root of two is irrational using proof by contradiction: assuming it's rational, leads to contradictions about evenness and divisibility. Another example proves there are infinitely many prime numbers by assuming a finite list and creating a new prime number that contradicts this assumption. This technique is demonstrated in video lectures on proof by contradiction, contrapositive, and examples.

To practice, watch the video "Video Proof by Contradiction" (4 minutes) and complete the practice assignment "Contradiction and Contrapositive" (25 minutes). Additionally, read the lesson materials, including "Reading Week 3 exercises", which includes hints and tips for completion.

---

## Proof by contrapositive Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/J0xQh/proof-by-contrapositive)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The technique of proof by contrapositive exploits equivalent classes of logical statements. To prove a conditional statement "if A then B", it's often easier to show that its contrapositive "if not B, then not A" is true. The contrapositive can be used when the premise is difficult to work with directly. For example, proving "for all integers n, if n^3 + 1 is odd, then n is even", one can start by assuming "n is odd" and show that "n^3 + 1 is even". The contrapositive can be used as a shortcut in proof by contradiction, where one assumes the negation of the statement to be proved and shows it leads to a contradiction. This technique can simplify proofs and make them more efficient. In general, if A then B can be proven either directly or by assuming not-B and proving not-A. The method of contrapositive proof is an alternative approach to traditional proof methods in logic and mathematics.

I left out the detailed explanations of the steps for these two examples because they were too long for this summary format.

---

## Proof by contradiction and contrapositive – examples Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/OUaSj/proof-by-contradiction-and-contrapositive-examples)

Here is a summary of the text in 8 sentences, preserving key information:

The video transcript explores examples of proof by contradiction and contrapositive. The first example claims that if 5n + 2 is even, then n is even. To prove this statement false, the premise (5n + 2 is even) is assumed true and the conclusion (n is even) is assumed false. If n is odd, then 5n + 2 can be shown to be odd using direct calculation, leading to a contradiction and thus proving n must be even. The contrapositive statement is "if n is odd, then 5n + 2 is odd". This statement is proved using direct proof, showing that if n is odd (i.e., n = 2k + 1), then 5n + 2 = 10k + 7, which is odd. The contrapositive and contradiction are logically equivalent statements. The video transcript provides additional resources for learning about formal proof, proof by contradiction, and contrapositive.

---

## Proof Reading• . Duration: 1 hour 25 minutes 1h 25m

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/ZA6E5/proof)

There seems to be a repetition in the text you provided, with multiple instances of almost identical information. To provide a meaningful summary, I will condense the key points into 8 sentences:

The reading covers topics from Week 3, including direct proof, proof by contradiction, and proof by contrapositive. These concepts are essential in discrete mathematics and its applications. The recommended approach is to watch the provided videos before studying the reading. This material can be found in the Online Library and ProQuest Collection, with access instructions available. A detailed explanation of proof by contradiction and contrapositive is presented, along with examples. To further understand these concepts, it's essential to examine Rosen's "Discrete mathematics and its applications" (2011, Chapter 1.7, pp.80-90). The reading includes videos (Proof by contradiction, Proof by contrapositive, and examples) and a practice assignment for students. Additional resources, such as Week 3 exercises and hints/tips, are also available to support learning.

---

## Week 3 exercises Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/sKqOF/week-3-exercises)

Here is a summary of the text in 8 sentences:

To practice concepts learned in Week 3, attempt the exercises provided. The first exercise asks to prove that if m + n and n + p are even integers, then m + p is even using a direct proof solution. Another exercise requires proving that every odd integer can be expressed as the difference of two squares using a direct proof. A third exercise involves showing that if n^3 + 5 is an odd integer, then n must be an even integer, demonstrated through both a proof by contraposition and a proof by contradiction. Additionally, prove that if 3n + 2 is an even integer, then n is also an even integer, using both proofs by contraposition and contradiction. These exercises are optional but strongly recommended for testing knowledge and identifying areas for further study. The solutions to these problems require direct proof, proof by contrapositive, and proof by contradiction techniques.

---

## Week 3 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/o7mHl/week-3-exercises-hints-and-tips)

There is no text provided for me to summarize. The text appears to be a lesson plan or course outline, with various video lessons, reading assignments, and practice activities related to formal proof, proof by contradiction, and contrapositive. If you could provide the actual text, I would be happy to assist you in summarizing it in 7 sentences, preserving key information, formulae, links, and technical details.

---

