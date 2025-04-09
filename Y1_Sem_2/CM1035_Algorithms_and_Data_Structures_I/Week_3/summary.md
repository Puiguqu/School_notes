# Week 3 - CM1035 Algorithms and Data Structures I - Problems, algorithms and flowcharts, Part 1 - Week 1

## Solution to the Birthday Party problem Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/Tlqn5/solution-to-the-birthday-party-problem)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The topic introduces pseudocode, a new way of describing algorithms that resembles a programming language. The problem of finding the greatest common divisor (GCD) of two numbers is used to illustrate this concept. Euclid's algorithm, also known as the Euclidean algorithm, is an existing algorithm for computing GCD. A flowchart illustrating the steps of Euclid's algorithm is provided, but it is recommended that viewers study it further to understand its logic. The algorithm works by repeatedly replacing one number with the difference between the two numbers until they are equal. In the case of finding the GCD of 48 and 42, the algorithm is applied step-by-step, reducing the numbers until the final result (GCD) is obtained. This process involves decisions to determine which number is larger or smaller, and adjusting the values accordingly. Ultimately, the algorithm outputs the greatest common divisor, which in this case is six.

Note that I omitted some technical details and formulas to keep the summary concise, but preserved the essential concepts and logical flow of the original text.

---

## Introduction to Topic 2 Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/dklfH/introduction-to-topic-2)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

Pseudocode is widely used by computer scientists when discussing algorithms as it bridges the gap between programming languages and descriptive English. Flowcharts are effective at conveying algorithmic flow but can be cumbersome to translate into programs. Pseudocode provides a clear conceptual understanding of algorithms and is universal, allowing individuals with different programming backgrounds to understand implementations. It is not a programming language itself, but rather a tool for describing algorithms in a way that is easily readable and understood by anyone. Pseudocode is particularly useful when discussing iteration, as it allows for the specification of how code should be translated from flowcharts into specific programming languages. In this topic, you will learn the basics of pseudocode, including iteration, and how to convert between flowcharts and pseudocode. Understanding pseudocode is essential for studying algorithms, as textbooks and research papers often use it to bypass issues with programming languages. The goal of this topic is to provide a clear conceptual understanding of algorithms using pseudocode, making it easier for individuals to understand and implement them in their own programming languages.

---

## Discretisation and pseudocode Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/4Sm0D/discretisation-and-pseudocode)

Here is a summary of the text in 8 sentences, preserving key information, formulas, links, and technical details:

Discretisation is the process of turning continuous processes into discrete steps, which are essential for algorithms written in computer programs. Pseudocode is a natural way to describe algorithms as it closely resembles computer programs but is not itself a program. Pseudocode uses mathematical symbols such as the assignment symbol (an arrow) and common mathematical operations like addition, subtraction, multiplication, division, comparison operators, and logical operations. Variables can be given simple notation (single letter) or names, with the constraint of no spaces in variable names. Pseudocode allows for multiple assignments to be made, and updates can be made using old values. The order of operations follows from left to right along a line and from top to bottom on the page. An if-then statement is used to make decisions based on conditions, where the action is taken if the condition is true and something else is done if it's false. In the context of increasing the temperature on a thermostat, pseudocode can be used to describe the process of getting the current temperature reading from the thermostat and adjusting it if necessary, with the goal of reaching a desired temperature.

---

## Pseudocode and functions Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/7Nj0L/pseudocode-and-functions)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

Functions are a fundamental concept in computer science and mathematics that take inputs and produce outputs. In pseudocode, functions are represented by the keyword "function", followed by the function name and input (e.g., `function even(n)`). The body of a function contains the operations to be performed on the input, which can include conditional statements like if-then. Functions can return Boolean variables such as true or false. In pseudocode, functions are defined using an if-then statement with a return keyword to terminate the function and produce an output (e.g., `return n mod 2 == 0` for even). The concept of mod 2 can be applied to integers in any base between 2 and 10 using modular arithmetic. To calculate an integer mod 2 in any base, a general algorithm is needed that considers the representation of the input number in different bases (bit strings or decimal form). This problem will be discussed further in the next topic, with practice assignments provided to help students understand how to implement such an algorithm.

Note: I've kept the original formatting and technical details, including pseudocode examples, as they are crucial to understanding the concepts being described.

---

## Introduction to loops in pseudocode Video• . Duration: 12 minutes 12 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/IBVE3/introduction-to-loops-in-pseudocode)

This text is a transcript of a video lecture on the topic of iteration in pseudocode. The lecturer discusses the importance of understanding loops in programming and provides examples of how to use for loops and while loops to solve problems.

The lecture begins by explaining that there are different types of iterations, including for loops and while loops. It then proceeds to discuss the benefits of using each type of loop, such as the simplicity of while loops versus the readability of for loops.

The lecturer also provides examples of how to use iteration in pseudocode, including calculating the square root of a number and determining whether a number is an integer. The lecture uses pseudocode examples to illustrate how to use iteration to solve problems, rather than providing actual code.

One of the key takeaways from this lesson is that knowing which type of loop to use can make a big difference in terms of writing simple and elegant pseudocode. The lecturer emphasizes that completely on their own, students should practice using iteration in pseudocode, including revisiting the Euclidean algorithm for finding the greatest common divisor.

Overall, this lecture provides an introduction to loops in pseudocode, highlighting the importance of understanding iteration in programming and providing examples of how to use different types of loops to solve problems.

---

## Euclidean algorithm in pseudocode Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/dBeok/euclidean-algorithm-in-pseudocode)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The Euclidean algorithm can be represented as a function in pseudocode using both for loops and while loops. The function, "Greatest Common Divisor (a, b)", takes two integer inputs and returns their greatest common divisor. In the for loop version, the function iterates from 0 to `a + b`, assigning new values to `a` or `b` based on whether `a > b` or not. If `a == b`, the loop ends and the function returns `a`. The while loop version is simpler, iterating until `a == b` and returning `a` at the end. Using a while loop allows for more interesting assignments to occur in each iteration. Pseudocode can be written in different conventions and notations, which may limit its universality. To further explore pseudocode, students are encouraged to translate examples into other languages or create their own language and translate it back.

Note that the original text is a transcript of a video lecture, and I've tried to preserve the tone and style of the original while summarizing the key points in 8 sentences.

---

## Pseudocode Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/supplement/9BKNS/pseudocode)

I don't see any text to summarize in your message. You seem to have provided a prompt that appears to be related to online learning, but there is no actual text to extract information from.

If you could provide the text from Section 2.1 of Cormen's "Introduction to Algorithms" book or another relevant source, I would be happy to help summarize it in 8 sentences, preserving key information, formulae, links, and technical details.

---

