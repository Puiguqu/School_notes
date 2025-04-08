# Unrestricted grammars Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/1AZN4/unrestricted-grammars)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

A language is recursively enumerable if it can be described by an unrestricted grammar, which has no limitations on defining rules. In this type of grammar, both sides of a rule can have any combination of terminals and non-terminals, with the right-hand side allowing epsilon as well. Recursively enumerable languages are a subset of context-sensitive languages, which in turn are a subset of recursively enumerable languages. The example language L consists of strings of the form "a^n b^n c^n" where n can be 0, making epsilon also part of the string. This grammar generates the language by applying rules to replace non-terminal symbols with terminal symbols, ultimately producing the desired string. For instance, the rule "S -> a A B C" is used to generate strings like "aA bB cC". The process involves repeated application of these rules until all non-terminals have been replaced with terminals. This approach can be complex and requires experience to write grammars for both context-sensitive and recursively enumerable languages.

