# Week 4 - CM1020 Discrete Mathematics - Topic 1 A. Sets - Week 1

## Function composition Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/GAd9B/function-composition)

Here is a summary of the text in 15 sentences, preserving key information and technical details:

The lecture discusses function composition, which involves combining two functions F and G to create a new function F ∘ G. The output of F ∘ G can be calculated in two stages: first, input X into G to get G(X), then use G(X) as an input into F to get F(G(X)). An example illustrates this concept, where F doubles the input and G squares it; applying them together results in a function that doubles the square of the input. Function composition can be visualized using three sets A, B, and C, with functions G and F mapping between them. This visualization demonstrates how F ∘ G applies first to an element in A and then maps the result through F, resulting in an output in set C. The lecture provides an example of two functions F and G defined over the same domain and codomain (R), where F(x) = 2x + 3 and G(x) = 3x + 2. To illustrate function composition, we apply these functions to an element of R, say "1". First, applying G(1) gives us 5, then applying F(5) gives us 13. This example demonstrates that F ∘ G is not the same as G ∘ F, meaning that the order of composition matters.

In general, when composing two functions F and G, the output of G becomes the input to F, resulting in a new function F ∘ G. The function composition relation is not commutative, meaning that reversing the order of composition changes the result.

This lecture introduces function composition as an essential concept for understanding many mathematical and real-world applications.

---

## Bijective functions Video• . Duration: 11 minutes 11 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/mQfoi/bijective-functions)

This is not a typical math lesson in which a specific topic and problems are presented. The text appears to be a transcript of a video lecture or a learning platform's content, where various topics related to functions and mathematical concepts are briefly discussed.

There isn't a specific problem or question that requires a step-by-step solution. However, I can provide an overview of the topics covered in the lesson:

1. **Functions**: The text discusses what functions are, examples of functions (e.g., F of X = 2X), and how to prove that a function is bijection.
2. **Bijective Functions**: The lesson explains what bijective functions are, how to prove a function is bijective, and provides practice assignments.
3. **Inverse Functions**: The text discusses finding the inverse function of a given function (e.g., F-1 of X = X/2) and its properties (e.g., composition).
4. **Symmetry with Respect to the Line Y = X**: The lesson explains how to visualize functions and their inverses on a graph, highlighting the symmetry between the two.

If you'd like, I can help with solving problems related to these topics or provide additional explanations on any of the concepts covered in this text.

---

## Logarithmic functions Video• . Duration: 12 minutes 12 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/JfFgL/logarithmic-functions)

Here is a summary of the text in 5 paragraphs:

The lecture discusses two fundamental concepts in mathematics: exponential functions and logarithmic functions. Exponential functions are introduced as functions that grow or decrease continuously, whereas logarithmic functions are defined as inverse operations to exponential functions.

The lecture introduces logarithmic functions with any base, but focuses on common bases such as the natural logarithm (ln x) with a base of e = 2.71828. The properties of logarithmic functions, including their graphs and domains, are discussed. It is explained that logarithmic functions have an increasing trend when the base is greater than 1, while decreasing when the base is less than 1.

The relationship between exponential and logarithmic functions is emphasized as they are inverse operations. This means that if we take a function f(x) = e^x (exponential), its inverse is log(x) (logarithm). The graphs of exponential and logarithmic functions are also shown to be symmetric with respect to the line y = x.

Logarithmic functions have several important properties, including intercepting the x-axis at 1,0. The domains and ranges of logarithmic functions are discussed in detail. It is explained that logarithmic functions are increasing when the base is greater than 1, while decreasing when the base is less than 1.

The lecture concludes by discussing natural logarithms (ln x) with a base of e = 2.71828, which have several unique properties. The graph of the natural logarithm function is shown to be an increasing curve that passes through the point (e, 1).

---

## The floor and ceiling functions Video• . Duration: 12 minutes 12 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/NQl51/the-floor-and-ceiling-functions)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The floor function is defined as a function from R to Z that takes a real number x as input and gives output the largest integer less than or equal to x. The ceiling function is also defined as a function from R to Z that takes a real number x as input and gives output the smallest integer greater than or equal to x.

The floor function rounds down a real number, while the ceiling function rounds up a real number.

For example, given an integer n, if n is less than or equal to x, and x is strictly less than n plus 1, then the floor of x is equal to n. Similarly, for negative numbers, if x is between two integers, the floor of x will be the lower integer.

The ceiling function rounds up a real number to the nearest integer. For example, given an integer n, if n is greater than or equal to x, and x is strictly less than n minus 1, then the ceiling of x is equal to n.

To prove that the floor function satisfies certain properties, let m be an integer and assume that the floor of x is equal to m. Adding n to both sides of this inequality yields the result that the floor of x plus n equals the floor of x on its own plus n.

The ceiling function also has similar properties.

---

## Answer to question 1 on the problem sheet Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/zEG84/answer-to-question-1-on-the-problem-sheet)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The video transcript discusses functions A, B, and C, as well as two functions f and g that map between these sets. The domain of a function is the set of all inputs, while the co-domain is the set of all possible outputs. The range of a function is the set of all actual outputs. Function f maps set A to set B, with a table defining the mapping: x = 1 => f(x) = a, x = 2 => f(x) = b, etc. Similarly, function g maps set B to set C: x = a => g(x) = w, x = b => g(x) = x, etc. The domain of f is {1, 2, 3, 4, 5, 6}, the co-domain is {a, b, c, d}, and the range is also {a, b, c, d}. For function g, the domain is {a, b, c, d} and the range is {w, x, y, z}. To find f(1), we look at the table and see that f(1) = a. The pre-image of d under function f is {5, 6}, as both are mapped to d. Finally, g(f(3)) = g(a) = w. Function f is not one-to-one because multiple inputs map to the same output (d = 5 and d = 6). However, function f is onto because every element in the co-domain has a pre-image. To show that g is both one-to-one and onto, we can see from the arrow diagram that each element in the range has a unique pre-image, making g one-to-one. Additionally, since the range equals the co-domain, g is also onto.

---

## Answer to question 7 on the problem sheet Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/eteEc/answer-to-question-7-on-the-problem-sheet)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The floor function F(X) is defined as the largest integer less than or equal to X, where f maps real numbers to integers. The graph of F(X) for X in the interval from -3 to 3 is plotted. To find the floor of π, which is between 3 and 4, we get 3; for -2.5, we get -3; and for -1, we get -1. The function F is not injective because each element of its range has more than one pre-image, such as the case where the floor of 2.5 equals both 2 and 2.1. However, it is bijective (onto) since every element of its codomain has a pre-image on the floor function.

Furthermore, the graph shows that F(X) = -3 for multiple values of X. For example, floor(2.5), floor(-0.5), and floor(4) all yield 2. Since there is no real number such that the floor function equals only one value in the codomain (negative integers), the set {n ∈ ℤ: n ≥ -3} has an infinite number of elements and cannot be exactly equal to any integer; therefore, F(X) = n ≠ for all n > -3. The solution is also proven using logical reasoning.

In conclusion, while the floor function maps real numbers into integers (but doesn't always map one-to-one), it does provide every integer in its codomain with pre images: there are values that take the same output on both sides; therefore it can be said to be a bijective function.

---

## Webinar on functions Video• . Duration: 1 hour 48 minutes 1h 48m

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/UR9TP/webinar-on-functions)

This appears to be a transcript of an online learning session or lecture on functions and sets. The transcript covers various topics, including:

1. A discussion on the concept of a function, its domain, and range.
2. An explanation of why minus 1 is not included in the domain of a certain function.
3. A proof that a given function is one-to-one (injective).
4. A problem on sets, where the learner needs to show that a power set of A union B is a subset of another power set.

The transcript does not provide any direct answers or solutions to the problems. Instead, it presents the topics and problems in a detailed manner, allowing learners to understand the concepts and work through the problems on their own.

If you're looking for help with these topics or need assistance with the problems presented in the transcript, I can try to provide guidance and explanations. However, please note that I'll need more context and specific questions to address your needs effectively.

---

## Topic 2 webinar Video• . Duration: 1 hour 5 minutes 1h 5m

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/lecture/36hey/topic-2-webinar)

There is no specific problem to solve in the provided transcript, as it appears to be a lecture on functions, including what constitutes an invertible function, how to find the inverse of a function, and the relationship between a graph of a function and its inverse.

However, if you'd like to practice solving problems related to functions based on this lecture, I can provide some examples. Here are a few:

1. Determine whether the following functions are invertible:
a) f(x) = x^2
b) g(x) = 3x - 2
c) h(x) = x + 1

If you're unsure how to determine if a function is invertible, let me know and I can explain the criteria.

2. Find the inverse of each of the following functions:
a) f(x) = 2x + 1
b) g(x) = x^3 - 2
c) h(x) = (x-2)^2

If you'd like help with these problems or need further clarification on any concept, feel free to ask!

3. Graph the inverse of each of the following functions:
a) f(x) = x^2 + 1
b) g(x) = 3x - 2
c) h(x) = x - 2

Remember that the graph of a function and its inverse are symmetric with respect to the line y = x.

Let me know if you'd like help with these problems or have any specific questions about functions!

---

## Functions reading and practice exercises Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/EFDUr/functions-reading-and-practice-exercises)

Here is a summary of the text in 15 sentences:

The provided extract aims to consolidate knowledge on function composition, bijections, and the floor and ceiling functions. The recommended reading is from Koshy, pp.125-128 and 150-153. After reading, exercises are suggested for completion (pp.134 exercises 1-3, 5, 6, 10, 11, pp.155 exercises 1-8, 13, 15, 16). The reader is advised to consult the "Solutions to Odd-Numbered Exercises" section at the back of the book for answers. Function composition is a crucial concept in this topic. Bijections are a type of bijection that establishes a one-to-one correspondence between two sets. The floor and ceiling functions are also discussed in relation to functions. The goal of these exercises is to reinforce understanding of these concepts. Function composition involves combining multiple functions to create a new function. Bijections establish a unique mapping between sets, ensuring that each element in the domain maps to exactly one element in the codomain. The floor and ceiling functions are used to round down or up values within a given range. These functions are essential in mathematics and real-world applications. Understanding these concepts is crucial for problem-solving and critical thinking skills. The exercises provided will help students apply their knowledge and develop their analytical skills.

Note: I did not include any specific formulae or technical details as they were not mentioned in the provided text.

---

## Functions problem sheet Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/UmlOw/functions-problem-sheet)

Here is a summary of the text in 12 sentences, focusing on key concepts and findings:

The lesson plan for Topic 2 includes a variety of videos, practice assignments, and discussions to reinforce understanding of functions. The first video topic is function composition, lasting 4 minutes, followed by a 30-minute practice assignment. A subsequent video covers bijective functions, taking 11 minutes to watch, accompanied by a 30-minute practice assignment. Logarithmic functions are also explored in a 12-minute video, with a 30-minute practice assignment. The lesson plan includes a discussion prompt on functions, lasting 20 minutes. Additionally, there are two reading materials: "Functions" reading and practice exercises (1 hour) and a problem sheet with solutions (10 minutes). Video answers to questions 1 and 7 from the problem sheet are also provided (7 and 3 minutes, respectively). The lesson plan concludes with a reading summary of Topic 2 (15 minutes).

---

## Functions problem sheet - solutions Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/94NiN/functions-problem-sheet-solutions)

Lesson 2.2 More about functions Video: Video Function composition . Duration: 4 minutes 4 min Practice Assignment: Function composition . Duration: 30 minutes 30 min Video: Video Bijective functions . Duration: 11 minutes 11 min Practice Assignment: Bijective functions . Duration: 30 minutes 30 min Video: Video Logarithmic functions . Duration: 12 minutes 12 min Practice Assignment: Logarithmic functions . Duration: 30 minutes 30 min Video: Video The floor and ceiling functions ....

---

## Topic 2 summary Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/Hv0v8/topic-2-summary)

Here are the 15 key points about functions that preserve all essential information:

1. Functions in programming are modular units of code designed to perform specific tasks, allowing for code reuse and organization.
2. A function f maps one element from a set A to a unique element in a set B, denoted as f:A→B.
3. Understanding the domain, co-domain, and range of a function is crucial.
4. Injective (one-to-one) functions map each element in the domain to a distinct element in the co-domain.
5. Surjective (onto) functions map every element in the co-domain to at least one element in the domain.
6. Bijective functions are both injective and surjective, meaning they establish a one-to-one correspondence between the domain and co-domain.
7. The inverse function of a bijective function can be found by swapping the domain and co-domain.
8. To plot a graph of a function f, one needs to understand if the function is injective, surjective, or bijective.
9. If a function f is a bijection, its graph will be symmetric with respect to the straight line y=x.
10. Function composition is denoted as (f∘g)=f(g()), where f and g are functions in the same domain and range.

Some specific functions that need understanding include:

11. Linear functions: f(x) = mx + b, where m and b are constants.
12. Quadratic functions: f(x) = ax^2 + bx + c, where a, b, and c are constants.
13. Ceiling function: ⌈x⌉ = the smallest integer greater than or equal to x.
14. Floor function: ⌊x⌋ = the largest integer less than or equal to x.
15. Exponential function: f(x) = e^x, where e is a base constant.

The learning exercise aims to help students reflect on their understanding of functions and identify areas for improvement by rating their knowledge against the learning outcomes and creating an action plan to address any gaps in their understanding.

---

