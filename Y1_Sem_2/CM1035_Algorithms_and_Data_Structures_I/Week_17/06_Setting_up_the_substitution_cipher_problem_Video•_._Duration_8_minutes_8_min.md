# Setting up the substitution cipher problem Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/LX0xT/setting-up-the-substitution-cipher-problem)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The programming activity involves implementing merge sort on a simplified version of the permutations problem. The goal is to decode an encoded message by permuting letters in the original message. Six letters (w, r, e, s, h, i) are used, with frequencies of appearance in the original message as follows: r (5), w (3), e and s (2), h and i (1). The `permutations` function generates all possible permutations of these six letters, resulting in 6! = 720 permutations. A new function, `frequency_order`, sorts the elements of the permutations array according to how frequently the first element appears in the English language. This is achieved by assigning a number to each letter based on its frequency in English and using this numerical information to sort the permutations. The merge sort algorithm is implemented, taking an array as input and merging it into one big sorted array. However, the implementation requires additional steps to handle the sorting of elements according to their frequency in English.

