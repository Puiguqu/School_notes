# Design regular expressions example Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/JsmIX/design-regular-expressions-example)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The Sigma star regular expression generates all strings over an alphabet, represented as a union of b* or a+b*. To generate all strings containing at least one 'a', use Σ* +. Similarly, to generate strings starting with 'a' or ending with 'a', use Σ*a and Σ*a respectively. Concatenating the regular expression a+b with itself generates all strings with even lengths, so adding a star to this concatenation yields even-length strings: (ab+)*. To generate odd numbers, use Σ*(1+3) since an odd number ends in either '1' or '3'. For numbers greater than 200, use the union of Σ*2+3 and Σ*2Σ*3Σ*, where Σ* denotes repetition of any character. This ensures that all four-digit numbers are greater than 200. In general, regular expressions can be designed to generate languages with specific properties, such as even-length strings or odd numbers.

