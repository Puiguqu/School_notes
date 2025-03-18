# Answer to question 5 on problem sheet Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/zCRV3/answer-to-question-5-on-problem-sheet)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Propositional logic is the study of statements that can be either true or false, and how to reason about them using logical operators. Two propositions, p and q, are considered. A truth table is constructed to show the truth value of each logical statement involving p and q. The truth table has at least 2^n rows, where n is the number of propositions. For two propositions, there are 4 possible combinations: 0, 0; 0, 1; 1, 0; and 1, 1. Notation for negation (not) is used to create new columns in the truth table.

The first column represents p, with values 0 and 1. The second column represents q, also with values 0 and 1. The third column represents not p, which is 1 when p is 0, and 0 when p is 1. Similarly, the fourth column represents not q. 

To evaluate the truth value of "p or q", the columns are examined for rows in which either p or q (or both) is true. The first row has neither p nor q true; all other rows have at least one proposition true, so the statement "p or q" is true for those rows.

Similarly, to evaluate the truth value of "p and q", the columns are examined for rows in which both p and q are true. Only the last row meets this condition, so "p and q" is false for that row and true otherwise.

Noting the statement "not p or not q", its truth table is constructed similarly to the others. This statement holds if either not p (and thus) not q is true; only when both are 0 does it hold that the statements are false.

DeMorgan's second law states that "not p or not q" and "not p and not q" are equivalent, meaning they have the same truth values for all combinations of p and q. This equivalence is demonstrated using the truth table.

This summary provides an overview of constructing truth tables for propositional logic statements involving two propositions (p and q), evaluating their truth values, and demonstrating DeMorgan's second law.

