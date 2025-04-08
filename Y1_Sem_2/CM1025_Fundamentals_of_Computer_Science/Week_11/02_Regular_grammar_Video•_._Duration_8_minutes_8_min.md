# Regular grammar Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/3EpkS/regular-grammar)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

Regular grammar is a compact way to describe languages using rules for connecting strings together. A regular grammar consists of four components: variables (non-terminals denoted by capital letters), terminals (finite set of lowercase letters), production rules (mapping one variable to a string consisting of at most one variable and one terminal), and start variable (usually positioned on the left-hand side of the top rule). The structure of each rule must be in the form A → ε or A → aB, where A and B are variables and a is a terminal. The type of regular grammar used in this module is right-linear. To generate strings from a grammar, we start with the start variable and read its rule, then find the variable in the rule and replace it with the rule of that variable until there are no variables left. A derivation is a sequence of substitutions for generating a string from a variable. The process can be repeated to derive different strings from the same grammar. Regular grammars can be used to describe regular languages, which include strings such as "ba" and "bbba", and are useful for parsing and analyzing these types of languages.

