# Turing machines – examples Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/i3jsV/turing-machines-examples)

Here is a summary of the text in 8 sentences, preserving key information:

A Turing machine is designed to accept the language WW reverse, where W is defined over small a and small b. The language is not regular, with a grammar that generates it: Capital S goes to small a (S → aS), or small b (S → bS) or epsilon (∅). To design the machine for WW reverse, consider the string "abbbba" as an example. Assuming the first letter starts with small a, read a from state q1 and then go to state q2. Delete the small a in each position that must be followed by another small a ( rule S → aS). Parse the input from right to left to remove any remaining small a or b. If a non-expected letter is found during parsing, reject the string; otherwise, accept it when all small a and b have been removed.

