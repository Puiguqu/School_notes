# Grammar examples Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/dkAwR/grammar-examples)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The video transcript discusses designing regular grammars using finite state machines. The first example is to design a regular grammar for the regular expression `a+ b+`, which generates all strings with at least one `a` and an even number of `b`s. To solve this, the authors create a DFA that accepts this language and then construct a regular grammar from it, adding rules for each transition and an epsilon rule for the accepting state. The second example is to design a regular grammar for a language over `a` and `b`, which contains all strings with an odd number of `a`s and an even number of `b`s. This DFA also leads to a constructed regular grammar, following similar steps as in the first example. The authors emphasize that labeling states with variables can simplify the construction process. For each transition, they add rules based on the destination state, resulting in a finite set of rules for the generated grammar. By constructing these grammars using DFAs, it is possible to formally define and verify regular languages, enabling more efficient processing and analysis of strings from these languages.

Note: The text does not provide explicit links or formulae, so I had to remove these elements while still trying to preserve key information.

