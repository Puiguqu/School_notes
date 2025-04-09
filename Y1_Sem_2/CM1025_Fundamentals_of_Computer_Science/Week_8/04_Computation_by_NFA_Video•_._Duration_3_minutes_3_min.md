# Computation by NFA Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/QUdck/computation-by-nfa)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The problem being explored is when there are too few transitions in a finite automaton (FA), leading to rejection of certain inputs. The example FA takes an input of 001101 and initially reads the first zero, resulting in no transition from state B, which leads to rejection. This scenario highlights the importance of considering multiple possibilities at each state in non-deterministic finite automata (NFA). To analyze inputs starting with one, a new transition labeled "one" is taken from state A to C, ensuring that any subsequent input will result in acceptance. For inputs starting with zero, a transition labeled "zero" is taken from A to B, requiring the next letter to be one for further processing. If the next letter is zero again, it becomes clear that only strings starting with 01 or 1 will be accepted. In contrast, when analyzing inputs starting with zero, the initial transition forces a sequence of zeros before any subsequent input can be processed. The language recognized by this automaton is binary strings consisting of either "one" or "01".

