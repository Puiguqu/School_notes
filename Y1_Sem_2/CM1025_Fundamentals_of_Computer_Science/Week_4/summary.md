# Week 4 - CM1025 Fundamentals of Computer Science - Logic – part 1 - Week 1

## Proof by induction Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/NJOxu/proof-by-induction)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Mathematical induction is a form of proof that can be used to prove statements are true for all natural numbers. The principle of mathematical induction states that if P(0) is true, then for all k in N, if p(k) is true, P(k + 1) is also true. This means that if it is true for a step k, it is also true for the next step k + 1. To prove this formally, there are three steps: (1) proving that P(0) is true (the basis), (2) proving that if P(k) is true then P(k + 1) is true (the inductive step), and (3) writing 'therefore, for all n in N, P(n) is true'. The inductive hypothesis assumes that P(k) is true to show that P(k + 1) is also true. Mathematical induction can be thought of as a chain of dominoes, where each domino represents a statement being proved true for the next number. This technique is useful when proving statements about natural numbers or chains.

---

## Example of a correct proof Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/ANgoA/example-of-a-correct-proof)

Here is a summary of the text in 8 sentences, preserving key information and concepts:

The video transcript presents examples of proof by induction for two statements: (1) the sum of the first n powers of two equals 2^n - 1, and (2) n is less than 3^n. The first statement is proven using the basis step, where P1 is shown to be true, and the inductive step, where if Pk is true, then Pk+1 is also true. In the second example, the basis step proves that P1 is true (1 < 3^1), and the inductive step shows that if Pk is true (k < 3^k), then P(k+1) is also true (k+1 < 3^(k+1)). The proof by induction for both statements involves assuming a hypothesis (Pk or Pk+1 is true) and proving that it implies the next statement in the sequence. This process is repeated to show that the statement holds for all natural numbers n. Proof by induction is a method used to prove mathematical statements, where the basis step establishes the truth of the statement for the smallest possible value of n, and the inductive step shows that if the statement holds for one value of n, it also holds for the next consecutive value. The video transcript provides examples and explanations of proof by induction, as well as a discussion prompt and reading materials to help viewers understand the concept better.

[Note: Since there are no links or technical details mentioned in the text, they have been excluded from this summary.]

---

## Example of an incorrect proof Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/5fPXK/example-of-an-incorrect-proof)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The video discusses incorrect proofs using proof by induction. The first example shows that if we assume Pk is true for all natural numbers n, we can prove Pn+1 is also true, but we failed to show that at least one domino falls (i.e., the basis step), making the proof incomplete. In the second example, a person claims that all pencils are the same color using proof by induction, but they fail to show that every group of two pencils has the same color (basis) and assumes it's true for k+1 without justification. To prove Pn is true for all n, we need to establish both the basis step and the inductive step correctly. In this case, the person mistakenly assumed that if all k pencils are the same color, then adding one more pencil will also be the same color. However, they missed showing that every group of two pencils has the same color, which is a necessary condition for proving Pn+1 is true. The video highlights the importance of following the steps correctly in proof by induction and provides examples of both correct and incorrect proofs to illustrate the concept.

---

## Conclusion Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/OWIlT/conclusion)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The video transcript discusses powerful proof techniques, including induction and contrapositive. Induction can help prove statements by building on the fact that natural numbers are like a chain. A puzzle is presented where 27 marbles, all but one weighing the same, need to be found using a scale no more than three times. The solution involves dividing the marbles into groups of three and then further grouping them until only one marble remains. For 9 marbles, two weighings are needed to find the faulty marble. By extrapolating this to 27 marbles, divided into three groups of nine, it is proved that only three weighings are needed. The solution relies on the process of elimination and the fact that each weighing can help narrow down the possible locations of the faulty marble. This demonstrates a clever application of induction and logical reasoning to solve a seemingly complex problem.

---

## Induction and recursion Reading• . Duration: 45 minutes 45 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/alXTA/induction-and-recursion)

There is not enough information in the provided text to create a summary with key information, formulae, links, and technical details. The text appears to be a course description or instruction on what to study in relation to Topic 2 (Weeks 3 and 4), covering subjects such as proof by induction.

However, here is a possible paraphrased version of the main points:

The essential reading for Topic 2 covers key concepts such as correct proof and proof by induction. To understand these topics, it is recommended to first watch the provided videos and then study the accompanying readings. The reading material includes a chapter by Rosen (pp.311–330) and addresses specific lesson plans, including video examples of both correct and incorrect proofs, as well as discussions and summative assessments related to inductive proof and recursion.

No formulae, links, or technical details are mentioned in the text, as it appears to be more of a general course outline rather than a technical explanation.

---

## Week 4 exercises Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/NjDqO/week-4-exercises)

Here is a summary of the text in 8 sentences, preserving key information:

To practice concepts learned in Week 4, attempt exercises with hints and tips provided on the next page. The statement P(n) is to be proved: 12 + 22 +···+ n2 = n(n + 1)(2n + 1)/6 for positive integer n. To start, evaluate P(1), which is true, completing the basis step of the proof. The inductive hypothesis states that if P(k) is true for some k, then P(k+1) is also true. In the inductive step, prove that 3k < k! if k > 6, using the inductive hypothesis. Next, prove that 2k > k^2 if k > 4, again using the inductive hypothesis. Finally, use induction to show that 5 divides n^5 - n for all non-negative integers n.

---

## Week 4 exercises hints and tips Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/NNSPi/week-4-exercises-hints-and-tips)

There is no text provided for me to summarize. The given text appears to be a schedule or outline for a lesson, with durations and activities listed, but it does not contain any information that can be summarized. If you could provide the actual text you'd like me to summarize, I would be happy to help!

---

