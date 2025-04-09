# Chomsky normal form Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/XWY4n/chomsky-normal-form)

Here is a summary of the text in 8 sentences, preserving key information:

Context-free grammar is a type of formal grammar that is not in Chomsky normal form (CNF) if it contains rules with lengths greater than two or non-terminal symbols on the right-hand side. To convert to CNF, three steps are taken: adding a new start variable, eliminating silent rules, and removing unit and improper rules. The first step involves adding a new start variable, which ensures that the start symbol never appears on the right-hand side of any rule. Silent rules are eliminated by creating new rules for each occurrence of the silent non-terminal, effectively copying its production rules to a new non-terminal. Unit rules are removed by adding an auxiliary non-terminal to replace the unit non-terminal, and improper rules are converted to proper forms by adding additional rules to break up long sequences of terminals and variables. The final step involves making sure that all remaining rules have lengths less than or equal to two and that there is a start symbol. The process can be repeated multiple times to achieve CNF. By following these steps, context-free grammars can be converted to Chomsky normal form, which allows for more efficient parsing and analysis of the grammar.

