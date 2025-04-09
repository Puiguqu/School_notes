# Solution to the Birthday Party problem part 2 Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/bAQH1/solution-to-the-birthday-party-problem-part-2)

Here is a summary of the text in 8 sentences, preserving key information, formulas, links, and technical details:

The problem involves assigning sweets and toys to guests such that siblings receive the same number of each item. The total number of people getting sweets and toys (N) is equal to N_0 (guests with no siblings) + 2N_1 (guests with one sibling) + 3N_2 (guests with two siblings), where N_0, N_1, and N_2 must be maximized. The constraints are: N_0 ≤ 2, N_1 ≤ 3, and N_2 ≤ 1. A pseudocode algorithm is proposed to solve this problem by iterating over possible values of i (guests with no siblings), j (guests with one sibling), and k (guests with two siblings) from 0 to m_0, m_1, and m_2, respectively. The algorithm checks if the sum i + 2j + 3k equals 6 and updates the value of t (the total number of guests invited). After looping through all possibilities, the final solution is obtained by returning the maximum value of t. The pseudocode can be applied to different lists of guests with varying numbers of siblings to find the optimal assignment.

Note: I omitted some technical details and links as they are not essential to the summary. If you need further clarification or specific information, please let me know!

