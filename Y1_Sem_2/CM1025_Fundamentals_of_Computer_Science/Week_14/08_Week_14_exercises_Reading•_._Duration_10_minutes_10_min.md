# Week 14 exercises Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/UO5C3/week-14-exercises)

Here is a summary of the text in 8 sentences, preserving all key information:

The exercises provided in Week 14 aim to test knowledge on Turing machines and grammars. The first exercise assumes a bounded tape from both sides and asks about the types of language that can be accepted by such a machine. Using a given grammar, it is possible to derive the string "aab" through the following transitions: S → aAb, Ab → aAb, Ab → bA, and A → ε. The second exercise asks for a string that cannot be generated from the same grammar. By analyzing the grammar, we can see that strings such as "bbacac" are not derivable because they do not meet the condition {w∣wϵ(a+b+c) + ,N a (w)=N b (w)=N c (w)}. The third exercise provides a new grammar for generating strings over the alphabet {(a, b, c)}, which is defined as: S → ABCS|ABC, AB → BA, BA → AB, AC → CA, CA → AC, BC → CB, CB → BC, A → a, B → b, C → a. This grammar generates strings of the form (a+b+c)^+ with equal counts of each letter.

