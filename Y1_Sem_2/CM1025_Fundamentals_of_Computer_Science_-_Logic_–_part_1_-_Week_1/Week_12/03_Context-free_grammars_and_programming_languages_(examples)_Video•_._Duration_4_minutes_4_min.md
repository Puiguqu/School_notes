# Context-free grammars and programming languages (examples) Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/YUHpe/context-free-grammars-and-programming-languages-examples)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

Context-free grammars are used to describe the structure of programming languages. The assignment statement "x = 10" can be generated using a context-free grammar where the starting symbol is AST (Assignment Statement). To derive this expression, we start with the identity rule ID -> x, followed by E -> T, F -> NO, and finally NO -> 10. In contrast, Y loops in languages like C can be described using a grammar that starts with "it" and follows rules to generate statements such as assignment, while statements, or if statements. The grammar for Y loops involves two main branches: one for the loop condition (E -> OP -> E) inside parentheses, and another for the statement (ST -> ST or epsilon). This grammar uses le S as a starting symbol and allows recursive use of rules to generate more complex statements. The grammar is designed to handle different types of statements and allows for recursive application of rules.

