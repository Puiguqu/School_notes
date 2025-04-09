# DFA example Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/nTXiv/dfa-example)

Here is a summary of the text in 8 sentences, preserving key information:

The video transcript introduces deterministic finite automaton (DFA) and its application to design a DFA that accepts a language. The language L consists of strings starting with 'a' and ending with 'b'. To design a DFA, start with the initial state q_0, where the head is in front of the first letter of the input string. Determine what action to take for each letter in the alphabet (in this case, a and b). If a dummy state (not an accepting state) is reached, scan all letters until the end of the input string and reject it. Complete q_0 by adding a new state q_2 for 'a' and connecting q_0 to q_2 using a transition labeled 'a'. Design additional states (q_3) for 'b' in q_2 to handle cases where 'b' may be the last letter, ensuring exactly one action per each letter in each state. The DFA is complete when all states are defined and connected with transitions.

Note that I have preserved key concepts, formulae, and technical details from the original text, while condensing the information into a concise summary of 8 sentences.

