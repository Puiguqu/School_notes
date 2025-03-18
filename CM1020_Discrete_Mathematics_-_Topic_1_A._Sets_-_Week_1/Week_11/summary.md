# Week 11 - CM1020 Discrete Mathematics - Topic 1 A. Sets - Week 1

## Introduction to proofs Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/eNrRe/introduction-to-proofs)

Here is a summary of the text in 15 sentences, preserving all key information, formulae, and technical details:

1. The lecture introduces three types of proof: direct proof, proof by contraposition, and proof by contradiction.
2. A theorem is a formal statement that can be shown to be true, an axiom is a statement assumed to be true for further arguments, and a lemma is a proven statement used as a step in a larger result.
3. The theorem "there exists a real number between any two not equal real numbers" is formalized as: ∀x, y ∈ ℝ, if x < y, then ∃z ∈ ℝ such that x < z < y.
4. Direct proof involves showing that a conditional statement p implies q is true by assuming p is true and using axioms, definitions, and theorems to show q must be true.
5. Proof by contrapositive involves proving the contrapositive of a conditional statement, not q implies not p, which is equivalent to proving p implies q.
6. The theorem "if n² is even, then n is even" can be proved using direct proof or proof by contraposition.
7. In direct proof, we assume n is even and show that n² is even, but it doesn't seem intuitive to prove this directly.
8. Proof by contradiction involves assuming the statement to be proved is false and showing that this assumption leads to a false proposition.
9. The theorem "there are infinitely many prime numbers" can be proved using proof by contradiction.
10. We assume there are only finitely many prime numbers, list them as p₁, p₂, ..., and show that the product of all primes plus 1 has at least one prime divisor, leading to a contradiction.
11. The three types of proof provide different approaches to proving mathematical statements: direct proof, proof by contraposition, and proof by contradiction.
12. Each type of proof relies on axioms, definitions, theorems, and rules of inference to establish the truth of a statement.
13. Understanding these proofs is essential for building mathematical arguments and developing logical reasoning skills.
14. The lecture emphasizes the importance of formalizing statements and using logical rules to construct valid arguments.
15. By mastering these proof techniques, students can develop a deeper understanding of mathematical concepts and improve their problem-solving skills.

---

## The principle of mathematical induction Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/kJ0Xr/the-principle-of-mathematical-induction)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Mathematical induction is a principle used to assert that a propositional function P(n) is true for all positive integers n. The formal definition of mathematical induction involves two steps: the basic step (proving P(1) is true) and the inductive step (proving that if P(k) is true, then P(k+1) is also true). The intuition behind induction is that if a property holds true for one value (P(1)), it will hold true for all subsequent values due to the iterative application of the property. This can be formalized using the following rule of inference: P(1) is true, and for all k, P(k) implies P(k+1). Therefore, for all n, P(n) is true. Mathematical induction can be used to prove statements about formulas, inequalities, divisibility, properties of subsets, and their cardinality. It can also be applied to assert that a propositional function P(n) is true for all integers greater than a particular integer. The structure of mathematical induction involves verifying the basic step (P(1) = True) and the inductive step (if P(k) is true, then P(k+1) is also true). In strong induction, the assumption that P(k-1) is true is made before the induction hypothesis. Mathematical induction can be used to prove statements about infinite sequences, allowing for the conclusion that a statement holds true for all positive integers. The principle of mathematical induction has various applications in mathematics and other fields, including algebra, geometry, and computer science. It provides a powerful tool for proving statements about properties of numbers and functions. By using mathematical induction, mathematicians can establish the validity of a wide range of statements with high confidence.

---

## Proof by induction Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/uZ1u0/proof-by-induction)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Mathematical induction is a method used to prove formulas, inequalities, and divisibility for all positive integers. To prove a propositional function P(n), two steps must be verified: the basis step (P(1) is true) and the inductive step (if P(k) is true, then P(k+1) is true). The formula "sum from 1 to n is equal n multiplied by n plus 1 divided by 2" can be proved using mathematical induction. The basis step states that for n=1, the sum from 1 to 1 is indeed equal 1*(1+1)/2 = 1. The inductive step involves assuming P(k) is true and showing that P(k+1) is also true. For example, if P(n) states "3^n is less than n!", then if P(7) is true (3^7 < 7!), it can be shown that P(8) is also true (3^8 < 8!). Mathematical induction can be used to prove inequalities and divisibility as well. For instance, it can be used to prove "6^n+4 is divisible by 5" for all positive integers n. However, not all statements can be proved using mathematical induction. An incorrect example of an induction proof is given, where the statement "2^i = sum from i=0 to n-1 2^i" is claimed to be true, but it is actually false (e.g., 2^0 ≠ 3). This highlights the importance of verifying both the basis step and inductive step to avoid false conclusions. In general, mathematical induction requires careful attention to both steps to ensure a valid proof.

---

## Strong induction Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/R07UA/strong-induction)

Here is a summary of the text in 15 sentences, preserving all key information, formulae, and technical details:

Strong induction is another form of mathematical induction that can be formalized using the following rule of inference: P(k) is true for all k in N, if P(1), P(2), ..., P(k-1) are true, then implies P(k) is true. This means that for all n in N, if P(n) is true for all n ≤ k, then P(k+1) is also true. The well-ordering property states that every nonempty subset of the positive integers has a least element. Mathematical induction can be used to prove statements about natural numbers, and it is equivalent to strong induction and the well-ordering property. A statement P(n) for all n in N where n ≥ 2, n is divisible by a prime number, was proved using strong induction. The basis step involves verifying that 2 is divisible by itself, while the inductive step involves assuming P(k) is true and showing that P(k+1) is also true. The well-ordering property can be used to prove statements about natural numbers by contradiction. Let S be a nonempty set of positive integers with no prime divisor, and assume it has a smallest element n. Then n cannot be prime, so it must have a divisor d between 1 and n, which leads to a contradiction. Therefore, S is empty, verifying the statement P(n). The principles of mathematical induction, strong induction, and well-ordering are all equivalent, meaning that each implies the validity of the other two techniques. This means that proofs using one technique can be adapted for use with another technique if necessary. Strong induction was introduced as an alternative to mathematical induction, but it has a similar structure and proof style. The formal expression of strong induction involves assuming P(1), P(2), ..., P(k-1) are true and showing that P(k+1) is also true. This can be used to prove statements about natural numbers in different ways.

---

## Induction Reading• . Duration: 2 hours 2h

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/p92LX/induction)

There is no text provided for me to summarize. The text appears to be a list of resources and assignments related to mathematical induction, but it does not contain any information that needs to be summarized.

If you provide the actual text, I would be happy to assist you in summarizing it into 15 sentences, preserving key information, formulae, and technical details, while focusing on the most important concepts and findings.

---

