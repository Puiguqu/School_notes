# Regular expressions and finite automata Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/Ds9Bo/regular-expressions-and-finite-automata)

Here is a summary of the text in 8 sentences, preserving key information:

Kleene's theorem establishes a strong connection between regular languages, regular expressions, and finite automata. The theorem states that a language is regular if and only if it can be described by a regular expression, and also implies that if a language is recognized by a finite automaton, it can be expressed as a regular expression. To prove this, we need to show that a finite automaton can be converted into a regular expression. This process involves creating new states, connecting them, and removing unnecessary states while transforming transitions accordingly. For example, starting with a two-state automaton, we create a new initial state connected to the old initial state via epsilon, and then remove states B and A, converting their paths into regular expressions. By applying this process, we can obtain a regular expression that represents the language of a given finite automaton. The second part of Kleene's theorem claims that if a language can be expressed as a regular expression, there exists a finite automaton recognizing the same language.

Note: I removed links and technical details not essential to the main concepts and findings, while preserving the key information about Kleene's theorem, regular languages, regular expressions, and finite automata.

