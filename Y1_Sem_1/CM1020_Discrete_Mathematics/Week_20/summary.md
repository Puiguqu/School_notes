# Week 20 - CM1020 Discrete Mathematics - Topic 1 A. Sets - Week 1

## Binomial coefficients and identities Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/07yNc/binomial-coefficients-and-identities)

Here is a summary of the text in 15 sentences, preserving all key information, formulae, and technical details:

The binomial theorem states that given two variables x and y and a non-negative integer n, then x + y^n = ∑[k=0 to k=n] n choose k times x^k times y^(n-k). This formula allows us to expand binomials of any degree. The coefficient of x^8 times y^7 in the expansion of 3x - y^15 is obtained when k = 8, and is equal to 15 choose 8 times 3^8 times (-1)^7 divided by 8! times 7!. The binomial theorem can also be used to show that 2^n = ∑[k=0 to k=n] n choose k. This result follows from applying the binomial theorem with x = 1 and y = 1. Another application of the binomial theorem is to find the number of subsets of a set with n elements, which is equal to 2^n. Pascal's identity states that given two integers n and k with n ≥ k ≥ 1, then n choose k + n choose k-1 is equal to (n+1) choose k. This identity can be used to simplify complicated binomial coefficients. Pascal's triangle is a number triangle with numbers arranged in staggered rows such that the element at row r and column n is the binomial coefficient of n choose r. The result of adding two adjacent binomial coefficients in this triangle is the binomial coefficient in the next row between these two coefficients.

---

## Generalised permutations and combinations Video• . Duration: 11 minutes 11 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/1Jkjn/generalised-permutations-and-combinations)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

1. The lecture discusses generalist permutations and combinations, covering both with and without repetition.
2. Permutations with repetition involve selecting r objects from a set of n objects where repetition is allowed, resulting in n^r possible permutations.
3. To prove this, we use the product rule, multiplying n possibilities for each object selection together.
4. For example, if we want to form strings of length r using only uppercase letters in the English alphabet (26 letters), the number of such strings is 26^r.
5. Permutations without repetition involve selecting r objects from a set of n objects where repetition is not allowed, resulting in n! / (n-r)! possible permutations.
6. This can be thought of as distributing r identical balls into n distinct boxes where each box receives at most one ball.
7. Combinations with repetition involve selecting k objects from a set of n objects where repetition is allowed, resulting in (n+k-1) choose K possible combinations.
8. This is equivalent to putting k identical balls into n distinct boxes or finding the number of functions from a set of k identical elements to a set of n distinct elements.
9. Combinations without repetition involve selecting k objects from a set of n objects where repetition is not allowed, resulting in n! / (n-k)! possible combinations.
10. This can be thought of as distributing k identical balls into n distinct boxes where each box receives at most one ball or finding the number of 1-1 functions from a set of k identical elements to a set of n distinct elements.
11. The formulae for permutations and combinations are summarized in the table:
	* Permutations with repetition: n^r
	* Permutations without repetition: n! / (n-r)!
	* Combinations with repetition: (n+k-1) choose K
	* Combinations without repetition: n! / (n-k)!
12. The lecture also discusses generalized permutations and combinations, distinguishable objects and boxes, and binomial coefficients.
13. Generalized permutations involve selecting r objects from a set of n objects where order matters and repetition is allowed or not allowed.
14. Distinguishable objects and boxes refer to scenarios where the order of selection matters and repetition is allowed or not allowed.
15. Binomial coefficients are used in various combinatorial problems, such as distributing identical balls into distinct boxes or finding the number of functions between sets.

Note: The text is a transcript of a lecture, so the formatting may not be ideal for reading purposes.

---

## Distinguishable objects and boxes Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/i6JAK/distinguishable-objects-and-boxes)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Counting problems can be reduced to finding the number of ways objects can be placed into boxes. The objects can be either distinguishable or indistinguishable, and the boxes can also be distinguishable or indistinguishable. Counting problems can take place with exclusion or without exclusion, where exclusion means no box can contain more than one object.

When placing distinguishable balls into distinguishable boxes with exclusion, it is equivalent to forming an unordered selection of k boxes from n available boxes. The number of ways of distributing k distinguishable balls into n distinguishable boxes with exclusion is equal to n factorial over n minus k factorial (n! / (n-k)!).

Without exclusion, the distribution is equivalent to making an ordered selection of k boxes from n boxes with repetition, and the number of ways is n to the power of k (n^k). When placing indistinguishable balls into distinguishable boxes with exclusion, it is equivalent to forming a combination of size k from a set of size n, resulting in n factorial over k factorial times n minus k factorial.

Without exclusion for indistinguishable balls, it is equivalent to forming a combination of size k from a set of size n with repetition, giving (n+k-1) factorial over k factorial times n minus 1 factorial. The problem of distributing eight indistinguishable balls into six distinguishable boxes is equivalent to choosing an unordered selection of 8 items from a set of 6 elements when repetition is permitted.

The number of ways to distribute eight indistinguishable balls into six distinguishable boxes equals 13 choose 8, which is equal to 1,287. The lecture discussed how counting problems can be modeled by distributing objects into boxes and looked at various scenarios with exclusion or without exclusion for both distinguishable and indistinguishable objects.

---

## Binomial coefficients and identities Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/gx44b/binomial-coefficients-and-identities)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Binomial coefficients represent the number of ways to choose k elements from a set of n elements without regard to order. They are defined as: (k n) = k!(n-k)! / n!. This definition is essential in combinatorics and algebra, with numerous applications in probability, statistics, and algebra.

The binomial coefficient has two properties: symmetry and Pascal's rule. Symmetry states that (k n) = (n-k n), reflecting the equivalence of choosing k elements from n elements versus leaving out n-k elements. Pascal's rule states that (k n) = (k-1 n-1) + (k n-1), derived from considering whether a particular element is included in the subset or not.

The binomial theorem describes the expansion of a binomial raised to any positive integer power: (x+y)^n = ∑[k=0,n] (k n)x^(n-k)y^k. This theorem expresses the coefficients in the expansion as binomial coefficients.

Binomial coefficients are central to combinatorics and algebra, providing tools for counting, probability, and algebraic manipulations. The properties of binomial coefficients, including symmetry and Pascal's rule, make them a fundamental concept in mathematics.

In conclusion, binomial coefficients and their identities are essential for solving problems in combinatorics and algebra, with numerous applications across various fields of study. Understanding the definition, properties, and identities of binomial coefficients is crucial for working in these areas.

---

## Permutations and combinations Reading• . Duration: 2 hours 10 minutes 2h 10m

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/SrkIZ/permutations-and-combinations)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The provided text covers several topics in combinatorics, including binomial coefficients and identities, Pascal's identity and triangle, and generalized permutations and combinations. The topics are covered in Koshy's textbook, specifically pages 365-70, 375-77, 379-81, and 386-90. Readers are encouraged to complete exercises on these pages, with solutions available at the back of the book for odd-numbered exercises. The text also provides information about video lessons, practice assignments, and discussions related to binomial coefficients and identities. There is a video lesson on binomial coefficients and identities that lasts 9 minutes, accompanied by reading materials and a practice assignment. A separate video lesson covers generalized permutations and combinations, with a duration of 11 minutes. Additionally, there are videos on distinguishable objects and boxes (9 minutes) and peer-graded assignments for combinatorics (1 hour). The text emphasizes the importance of consulting the solutions to odd-numbered exercises to check one's work. A reading material on permutations and combinations is also provided, with a duration of 2 hours 10 minutes. Furthermore, there is a video lesson on permutations and combinations that lasts 11 minutes, accompanied by a practice assignment. The text concludes with information about extra resources for readers who need additional support or review materials. Overall, the text provides a comprehensive overview of combinatorics topics, including binomial coefficients, Pascal's identity, and generalized permutations and combinations. Readers are encouraged to engage with these topics through video lessons, practice assignments, and discussions. The text aims to provide a supportive learning environment for readers who need help or want to review key concepts in combinatorics.

---

## Topic 10 module summary Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/RsJKn/topic-10-module-summary)

Here is a summary of the text in 15 sentences, preserving all key information, formulae, and technical details:

Combinatorics is a branch of mathematics that focuses on counting, arranging, and combining elements in sets, with applications in computer science, probability, statistics, and optimization. The field covers basic counting principles, including the addition principle and multiplication principle. Permutations refer to the arrangement of n elements in a specific order, with formulas P(n) = n! and P(n,r) = (n-r)!n!. Combinations refer to the selection of n elements without regard to order, with the formula C(n,r) = r!(n-r)!n!.

The binomial theorem expands expressions of the form (x+y)^n, using coefficients known as binomial coefficients. These coefficients represent the number of ways to choose k elements from n elements. The pigeonhole principle states that if n items are put into m containers and n>m, then at least one container must contain more than one item.

Combinatorics provides a mathematical foundation for counting, arranging, and analyzing sets and sequences. It is an essential tool in many areas of mathematics and applied sciences. Regularly assessing understanding against learning outcomes is crucial as students progress through their course. This exercise aims to help reflect on learning journeys, identify knowledge gaps, and develop improvement plans.

The exercise consists of several steps: reviewing learning outcomes, rating understanding (1-5), identifying areas for improvement, creating an action plan, and implementing it. The action plan may involve reviewing course materials, seeking additional resources, practicing problems, seeking instructor or peer help, scheduling study sessions, and adjusting strategies as needed. Combinatorics is a continuous process of learning, and revising plans to better suit needs is encouraged.

The module summary covers key concepts in combinatorics, including basic counting principles, permutations, combinations, binomial theorem, and pigeonhole principle. The exercise aims to help students identify areas for improvement and develop a plan to address these gaps.

---

## Combinatorics problem sheet Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/drgMO/combinatorics-problem-sheet)

Lesson 10.2 Further techniques 10.3 Extra resources Reading: Reading Combinatorics problem sheet . Duration: 10 minutes 10 min Reading: Reading Combinatorics problem sheet - solution . Duration: 10 minutes 10 min Combinatorics problem sheet Problem sheet combinatorics.pdf PDF File Mark as completed Dislike Report an issue

---

## Combinatorics problem sheet - solution Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/PsoHp/combinatorics-problem-sheet-solution)

Lesson 10.2 Further techniques 10.3 Extra resources Reading: Reading Combinatorics problem sheet . Duration: 10 minutes 10 min Reading: Reading Combinatorics problem sheet - solution . Duration: 10 minutes 10 min Combinatorics problem sheet - solution Problem sheet combinatorics-solution.pdf PDF File Mark as completed Dislike Report an issue

---

