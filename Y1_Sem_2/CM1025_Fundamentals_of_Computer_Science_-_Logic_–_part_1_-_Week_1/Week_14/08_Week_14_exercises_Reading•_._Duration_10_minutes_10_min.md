# Week 14 exercises Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/supplement/UO5C3/week-14-exercises)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The exercises for Week 14 aim to test knowledge of Turing machines. The goal is to determine what types of language can be accepted by a Turing machine with a limited tape length from both sides. Using the given grammar, it can be shown that the string 'aab' can be derived: S→aAb, Ab→aAb, Ab→bA, and A→ε. Another challenge involves finding a string that cannot be generated from the same grammar, such as 'bbacac'. To solve this, we use the given formula: {w∣wϵ(a+b+c) + ,N a (w)=N b (w)=N c (w)}. The grammar also includes rules for ABCS and ABBA productions. The language accepted by this Turing machine is defined as: {w |w ϵ (a+b+c)^+, N_a(w)=N_b(w)=N_c(w)}.

