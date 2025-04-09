# Language of the automata Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/VEs40/language-of-the-automata)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The language accepted by an automaton can be determined by analyzing the input strings that are accepted by the automaton. The red curve shows the path from the start state following the input "110", which results in a loop on state B and acceptance of input "1110". To find all accepted inputs, we choose a final state (E) and examine the arrows entering it, finding that accepting inputs terminate with "10". We also identify all states with incoming arrows labeled 0, which is only state C. The remaining final state is D, and its transitions are labeled 1 and come from states E and C. To ensure no string ends in "10" at non-final states, we circle all transitions coming into E or C, labeling them 0. This results in the language of the automaton being accepted by inputs ending with either "01" or "10". The set of all strings accepted by an automaton is called the language of the automaton.

Note: I did not include any links or technical details that were not relevant to summarizing the main concepts and findings.

