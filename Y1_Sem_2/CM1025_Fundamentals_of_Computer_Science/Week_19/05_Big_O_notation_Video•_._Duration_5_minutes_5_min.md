# Big O notation Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-fundamentals-of-computer-science/lecture/aCIDO/big-o-notation)

Here is a summary of the text in 8 sentences, preserving key information and concepts:

Big O notation is used to describe the growth rate of a function. Two functions f(x) and g(x) are related by f(x) being O(g(x)) if there exist constants c and k such that f(x) ≤ c*g(x) for all x > k. This means that f(x) grows slower than some multiple of g(x) as x increases. The constants c and k are called witnesses to the relation between f(x) and g(x). For example, if g(x) = n^2 and f(x) = 2n^2 + 4n + 40, then the witnesses are c = 3 and k = 9. The concept of Big O notation is similar to asymptotic behavior, which describes how a function grows as the input variable increases. To show that one function is O of another, we need to find constants c and k such that the first function is less than or equal to c times the second function for all x > k. This concept is important in computer science because it allows us to analyze the time complexity of algorithms and make predictions about their performance.

