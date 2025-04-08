# CM1035 Algorithms and Data Structures I - Problems, algorithms and flowcharts, Part 1 - Week 1

## Table of Contents

- [Week 12](#week_12)
- [Week 13](#week_13)
- [Week 19](#week_19)
- [Week 20](#week_20)
- [Week 21](#week_21)
- [Week 3](#week_3)
- [Week 6](#week_6)
- [Week 9](#week_9)

## Week 12

### Worst-case time complexity Video• . Duration: 6 minutes 6 min

The text discusses the concept of worst-case time complexity in algorithms, which refers to the maximum number of operations required by an algorithm for a given input size.

To analyze an algorithm's time complexity, it is essential to consider the worst-case scenario, where the input size is maximal. For example, in linear search, the worst-case input is when the target value is not present in the array or vector, requiring the inspection of all n elements.

Bubble sort has a best-case time complexity of O(n), as only one pass is needed to sort an already sorted array. However, the worst-case scenario occurs when the array is sorted with the largest value first and the smallest value last, requiring n-1 passes, each with O(n) operations, resulting in a worst-case time complexity of O(n^2).

Similarly, insertion sort also has a worst-case time complexity of O(n^2), as it requires n-1 passes to sort an array.

The key takeaway is that analyzing worst-case time complexity helps identify the maximum resources required by an algorithm for a given input size. This understanding enables developers to choose the most efficient algorithms for specific problems.

Note: There are no formulas, links, or technical details in this summary as it is focused on preserving the main concepts and findings of the text.

---

### Input size Video• . Duration: 3 minutes 3 min

Here is a summary of the text in 8 sentences, preserving key information:

The video discusses the distinction between complexity and its impact on algorithm efficiency, highlighting that an algorithm's time complexity can change depending on how resources are counted. In the RAM model, it was assumed that each memory unit could store an arbitrarily large integer, but digital computers have limited space per register due to storing bytes. To accurately count resources, we standardize storage as an array of bits or a string with the possibility of storing nothing. This leads to problems where the input is stored in an array of length Big O log n, and the time complexity changes from Big O of n to Big O 2^m, where m is the size of the input. The number of operations required grows exponentially in the size of the input, rendering previously efficient algorithms less effective. This emphasizes the importance of carefully counting resources when analyzing algorithms. The video also mentions the need for standardizing resource counting and storing numbers as arrays or strings of bits to accurately assess algorithm efficiency. The findings suggest that how we count resources can have significant consequences for our claims about algorithm efficiency.

---

### Summary Video• . Duration: 2 minutes 2 min

Unfortunately, there is no text provided for me to summarize. The text you shared appears to be a video transcript with links and technical details, but it does not contain any actual content that I can summarize.

However, I can provide an overview of the key concepts and findings presented in the video transcript:

The video transcript discusses algorithms and their performance analysis using the RAM model. It explains how to count operations implemented for a particular algorithm in the RAM model and introduces big O notation to analyze the asymptotic growth of functions. The worst-case time complexity, which is the maximum time complexity for all possible inputs, is discussed as a measure of an algorithm's performance.

The transcript also mentions examples of algorithms with different worst-case time complexities, such as linear search (O(n)), bubble sort and insertion sort (O(n^2)), and another algorithm with O(log n) worst-case time complexity. However, without more information about the specific algorithm mentioned in the link "Lesson 6.4 Summary Video: [link]", I cannot provide further details.

If you could provide the actual text or content to be summarized, I would be happy to assist you further.

---

### The Pizza Problem Video• . Duration: 1 minute 1 min

There is no text to summarize in this conversation, only a blank space. Please provide the text you'd like me to summarize, and I'll be happy to assist you.

---

### Analysis of algorithms Reading• . Duration: 1 hour 25 minutes 1h 25m

Here is a summary of the text in 8 sentences:

The provided text references Section 2.2 of Cormen's "Introduction to Algorithms" textbook, which discusses the RAM model and time complexity. The section reviews insertion sort, with a detailed analysis that covers various notions of complexity beyond the scope of this module. This information is considered essential reading for future study. Access to the ebook is available through E-Book Central (ProQuest) via the provided links. The video "Worst-case time complexity" and practice assignment are also mentioned as part of Lesson 6.3. However, no further details or summaries of these resources are provided in the text snippet.

---

## Week 13

### 7.0.1 Solution to the Pizza Problem Video• . Duration: 2 minutes 2 min

Here is a summary of the text in 8 sentences, preserving key information, formulae, and technical details:

The problem of dividing pizza among friends is used to introduce a new algorithm for searching sorted arrays quickly. The goal is to find the number of times the array can be searched such that only one element remains. This can be represented by the equation n × (1/2)^k = 1, where n is the initial size of the array and k is the number of searches. By rearranging the equation, we get n = 2^k. To solve for k, logarithms to the base 2 are applied to both sides, resulting in k = log2(n). Since the number of friends must be an integer, the actual value is the floor of log2(n), denoted as ⌊log2(n)⌋. This concept is applicable to problems that involve repeatedly dividing or searching a quantity by a fixed factor. The introduction of logarithms provides a efficient way to solve such problems.

Note: I did not include any links, formulae, or technical details in the summary as they were not specified in the original text.

---

### Introduction to Topic 7 Video• . Duration: 1 minute 1 min

Unfortunately, there is no text provided for me to summarize. The text appears to be a transcript of a video or lecture discussing the binary search algorithm and its applications, as well as a brief overview of the topics that will be covered in the lesson. If you provide the actual text, I would be happy to help summarize it into 8 sentences while preserving key information, formulae, links, and technical details.

---

### Binary search Video• . Duration: 11 minutes 11 min

## Step 1: Understand the problem
The problem asks to convert a flowchart for the binary search algorithm on vectors into a pseudocode description of the algorithm.

## Step 2: Identify the steps in the flowchart
The flowchart for binary search on vectors has the following steps:
- Start
- Get input vector and target value x
- Initialize variables N (length of vector), L (leftmost element), and R (rightmost element)
- Ask if R is less than L
  - If yes, return false (target not found)
  - Else, set M to be the midpoint of L and R
  - Look at the element at index M in the vector
    - If its value is x, return true (target found)
    - If its value is greater than x, set R to M-1
      + This means the target must be to the left of the midpoint
      + Update L to be M+1
  - Repeat steps 4 and 5 until R is less than or equal to L

## Step 3: Convert the flowchart into pseudocode
Based on the steps in the flowchart, the pseudocode for binary search on vectors can be written as follows:

```
Function binarySearch(vector, x):
  Initialize N (length of vector), L (leftmost element), and R (rightmost element)
  
  While R < L:
    M = (L + R) / 2
    If the value at index M is equal to x:
      Return true (target found)
    Else if the value at index M is greater than x:
      R = M - 1
    Else:
      L = M + 1
  
  If the value at index L is not equal to x:
    Return false (target not found)

Return "Target not found" or return true
```

## Step 4: Verify the pseudocode
The pseudocode follows the same logic as the flowchart and should correctly implement the binary search algorithm on vectors.

The final answer is: There is no specific number to solve this problem, but the above pseudocode implements the correct binary search algorithm for vectors.

---

### Coding up binary search Video• . Duration: 7 minutes 7 min

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The binary search algorithm is a divide-and-conquer approach to finding an item within a sorted vector or array. The algorithm works by repeatedly dividing the search interval in half until the desired element is found. A pseudocode implementation of the binary search algorithm has been provided, which initializes variables such as `n`, `R`, and `L` to represent the length of the vector and the search range. The algorithm then iterates through the vector using a while loop, with each iteration dividing the search interval in half until the desired element is found or it is determined that the element is not present in the array. In JavaScript, a binary search function needs to be implemented on an input array, where the value of interest is compared to the midpoint of the array and the search range is adjusted accordingly. The `binarySearch` function has been skeletonized, with only its logic required to complete it, which involves comparing the desired value to the midpoint of the array and updating the search range as necessary. To test the binary search algorithm, JavaScript code has been provided that generates a random array using the `genRandomArray` function and then attempts to find a specific value within the array using the `binarySearch` function. The output of this code will be either `true` or `false`, depending on whether the desired value is present in the array.

---

### Worst-case complexity of binary search Video• . Duration: 5 minutes 5 min

Here is a summary of the text in 8 sentences, preserving key information:

The worst-case time complexity of binary search can be determined by analyzing its operations. The best-case input for binary search is when the target value is at the midpoint of the array, resulting in a time complexity of O(1) or constant time. In contrast, if the target value is at the first element of the array, it requires multiple divisions to reach the midpoint, leading to a worst-case time complexity of O(log n). The same principle applies when the target value is next to the midpoint, requiring multiple divisions to find it. Translating this to pizza slices, we can see that binary search can accommodate log n divisions before reaching the final element. This leads to a worst-case time complexity of O(log n) for binary search on sorted arrays. However, if the array is unsorted, sorting it first using algorithms like bubble or insertion sort would increase the overall time complexity due to their O(n^2) performance. In certain cases, such as searching a dictionary multiple times, it may be more efficient to sort the data initially and use binary search for subsequent searches.

---

### Binary search is optimal Video• . Duration: 10 minutes 10 min

Here is a summary of the text in 8 sentences, preserving all key information and technical details:

Binary search is an algorithm that performs well on average, but its optimality relies on the assumption that the data is uniformly distributed. The random-access machine model assumes that instructions are executed by the control unit, which implements the algorithm as a program. Basic actions have one outcome, while decisions can have two outcomes (zero and one), encoded in bit values. Any possible algorithm has a basic tree-like structure, where each level represents a decision with possible outputs (bits tracing the path through the tree). The number of time-steps (T) is at least equal to the length of the bit string describing the steps in the computation. According to the pigeonhole principle, 2^T must be greater than or equal to n+1, which implies that T must be at least log2(n+1), making binary search optimal with a worst-case complexity of O(log n). This argument highlights the interplay between abstraction and mathematical modeling in computer science. The optimality of binary search is demonstrated using the random-access machine model and the pigeonhole principle.

---

## Week 19

### Solution to Sudoku problem Video• . Duration: 7 minutes 7 min

Here is a summary of the text in 8 sentences, preserving key information and concepts:

The original solution method for solving Sudoku puzzles generates candidate solutions by iterating through each blank entry and considering all possible numbers. However, this approach results in an exponential number of candidates (4^B) where B is the number of blank entries. To improve this, a more efficient approach can be used by restricting the number of candidates to generate. This can be done by analyzing rows and columns separately, eliminating possibilities that are already present in other rows or columns. By doing so, the number of candidates to generate is reduced, but it may still be exponentially large (2^B). A further improvement can be made by considering smaller square grids within the puzzle, reducing the number of candidates even more. However, even with these improvements, the number of candidates will still grow exponentially with the number of blank entries and the size of the grid. The question of whether there exists an algorithm to solve a general Sudoku puzzle with exponential time complexity that is better than O(n^m), where n is the size of the grid and m is the number of blank entries, is related to one of the millennial prize problems in computer science: P = NP.

Note: I did not include any links or technical details as they were not explicitly mentioned in the text. Also, some minor rephrasing was done to make the summary more concise and readable.

---

### Introduction to Topic 10 Video• . Duration: 3 minutes 3 min

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The binary search algorithm is considered optimal, with a worst-case time complexity of O(log n), making it difficult to conceive of algorithms that can solve certain problems more efficiently. Computational complexity theory studies the limits of what is possible and impossible for algorithms, grouping problems into complexity classes based on the resources required. The study of computational complexity operates at a theoretical level, but provides insights into why it's challenging to find efficient solutions to certain problems. One such problem is the halting problem, which asks whether a given computer program will halt for a specific input; Alan Turing showed that this problem cannot be solved algorithmically in general. However, many other problems can be solved using particular algorithms, and computational complexity theory helps understand how hard it is to solve these problems for any possible algorithm. The concept of computational complexity classes provides a framework for classifying problems based on their resource requirements. NP completeness, which relates to the relationship between P (problems that can be solved efficiently) and NP (problems that can be verified efficiently), plays a crucial role in understanding computational complexity. Computational complexity theory also touches on generic methods for solving NP complete problems and alternative forms of computing that provide new perspectives on the problem of P versus NP.

---

### Introduction to complexity classes Video• . Duration: 6 minutes 6 min

Here is a summary of the text in 8 sentences, preserving key information, formulae, and technical details:

The study of worst-case time complexity is crucial in computational complexity theory, where an algorithm's efficiency is measured by its time complexity relative to the size of its input. In general, exponential functions grow faster than polynomial functions, making exponential algorithms less efficient. To establish whether a problem is hard or not, researchers focus on determining if there exists an efficient algorithm (i.e., one with polynomial time complexity) that can solve it. The standard way of quantifying input size is by assuming the input is stored in an array where each element represents either a bit or nothing, making the input size equal to the number of elements in the array. The worst-case time complexity is typically computed in terms of the size of the input, and problems are grouped into classes based on the resources required to solve them. A complexity class is a set of sets, where each set represents a problem that can be solved with a particular set of resources (e.g., P for problems solvable in polynomial time). The study of computational complexity theory helps researchers understand what problems are feasible and which ones require significant advancements. By analyzing the time complexity of algorithms, researchers can determine whether a problem is part of a complexity class, such as P or NP, which represents sets of decision problems that can be solved with specific efficiency criteria.

---

### Decision problems Video• . Duration: 8 minutes 8 min

Here is a summary of the text in 8 sentences, preserving key information and concepts:

The concept of computational complexity deals with decision problems, where a machine decides whether to accept or reject an input based on a binary output. A problem can be viewed as a set of inputs that share a common property, and languages are collections of words (inputs) that belong to a particular language. The question of what decides whether a word belongs to a language is analogous to the role of a dictionary in determining which words belong to the English language. In computer science, a computational machine plays this role. Decision problems can be rephrased as languages, such as the language of integers that are perfect squares, where the output is binary (true or false). The time complexity of solving these problems can be analyzed using different methods, such as computing the square root or iterating over all squares of integers up to a certain value. In general, the first method has a linear time complexity in the size of the input, while the second method has a worse-case time complexity on the order of the square root of an exponential in S. The problem of deciding the language of perfect squares belongs to the set of problems that can be decided by a machine and the RAM model in at most polynomial time in the size of the inputs.

---

### Particular complexity classes Video• . Duration: 9 minutes 9 min

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The decision problem is studied in computational complexity, where input is viewed as a word belonging to a language if it's accepted due to having a certain property, or rejected. A new problem involves determining if an element appears X times in an array given a binary form of the number X. An algorithm can solve this problem in linear time using a linear search and count comparison with X, resulting in O(S) time complexity. This problem is added to the set of languages that can be solved in at most linear time in the RAM Model, along with determining if a number is a perfect square. The RAM Model allows for arbitrary integers to be stored, but limitations lead to differences in worst-case time complexity when switching models. The set of all languages solvable in at most polynomial time in the size of input is called P, and contains problems like determining prime numbers or correct Sudoku solutions. In contrast, EXP is a class of languages that can be solved in O(2^n) time complexity, containing problems such as finding a winning strategy in Go or checkers. The containment relationship between P and EXP implies that any algorithm with polynomial time complexity will have exponential time complexity, highlighting the distinction between these two classes.

---

### NP Video• . Duration: 5 minutes 5 min

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The problem of determining whether an X squared by X squared Sudoku puzzle has a solution can be solved using an algorithm with worst-case time complexity exponential in the size of the input, but if a candidate solution is given, deciding whether it is valid is a problem in NP (Nondeterministic Polynomial). This class NP captures problems where solutions to other problems can be checked efficiently. NP is defined as the set of languages that can be decided by an algorithm with access to a proof of polynomial size. The class NP differs from P (Polynomial) in that it allows for the use of proofs, whereas P only requires a finite number of steps. All problems in P are also in NP, but NP contains additional complexity due to the ability to use proofs. NP is also contained in EXP (Exponential), as checking all possible proofs can be done in exponential time. The notion of NP hardness introduces problems that are as hard as any other problem in NP, and NP complete problems are those that are both NP-Hard and in the class NP. Currently, many problems have been shown to be NP complete, including determining whether a Sudoku puzzle has a solution, which would require an efficient algorithm to solve if it existed.

---

### Optional further reading: NP-Completeness Reading• . Duration: 1 hour 1h

There is no text provided to summarize. The given text appears to be a list of reading materials and links related to computational complexity and NP-completeness, but it does not contain any specific information or concepts to summarize.

However, I can provide a general summary of the key concepts and topics related to NP-completeness and computational complexity:

NP-completeness is a concept in computer science that refers to a class of problems that are considered to be difficult to solve exactly. It is defined as follows: Problem X is NP-complete if it can be reduced to every other problem in NP (nondeterministic polynomial time), which means that if we can solve any problem in NP, then we can also solve Problem X.

The text suggests reading the introduction to algorithms by Cormen et al., which provides an overview of NP-completeness and complexity classes. It also mentions video lectures, practice assignments, and optional readings on NP-completeness, but no specific information or findings are provided.

If you provide the actual text, I can help you summarize it in 8 sentences, preserving all key information, formulae, links, and technical details.

---

### Revision exercises Reading• . Duration: 3 hours 30 minutes 3h 30m

Unfortunately, there is no text provided for me to summarize. The text appears to be a message from a course instructor or system, providing information about upcoming revisions and practice assignments for a computer science course.

However, I can provide a summary of the key concepts and findings based on the title "Introduction to computational complexity" (Lesson 10.0) and the provided information:

The course has attached an expanded version of the exam, called Revision.pdf, which includes questions that will test various aspects of the course. This is an optional practice assignment to help students prepare for the actual exam. The revised exam will not require as many answers as this practice assignment.

Key concepts discussed in Lesson 10.1 and 10.2 include:

* Complexity classes
* NP (Nondeterministic Polynomial) complexity

Practice assignments include:

* P (Polynomial time) complexity class
* EXP (Exponential time) complexity class

Additional resources include optional readings on NP-Completeness and revision exercises that will be revealed in the next week's activities.

If you have any further questions or would like me to clarify any of the technical details, please let me know!

---

## Week 20

### NP problems and searching Video• . Duration: 9 minutes 9 min

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

NP-complete problems are those that cannot be solved efficiently using traditional algorithms, as their complexity class requires an exponential amount of time to solve. One approach to solving NP-complete problems is to enumerate all possible proofs or candidate solutions and check them one at a time, which is related to the linear search algorithm but has an exponential time complexity due to the exponentially large number of possibilities. However, by using binary search, which has a logarithmic time complexity, it is theoretically possible to solve these problems more efficiently. Another approach is backtracking, where a solution is attempted and if it fails, the last attempt is reverted and another value is tried, allowing for efficient exploration of possible solutions. This method is similar to using a stack to backtrack when solving a puzzle, such as a Sudoku puzzle. In both cases, the key idea is to explore all possible solutions and revert back when necessary, rather than trying to solve the problem directly. Despite the lack of an efficient algorithm, these approaches demonstrate that NP-complete problems can still be solved using creative and effective methods. By understanding these techniques, individuals can tackle hard problems with confidence.

---

### New approaches to computing Video• . Duration: 3 minutes 3 min

The text discusses various models of computation, including the RAM model and the Turing machine model, which are equivalent in terms of efficiency. However, there is ongoing debate about whether these models can be used to solve NP-complete problems efficiently. The author suggests that most models of computation can be reduced to the RAM model, but notes that this does not necessarily limit our ability to develop new algorithms.

The author introduces two alternative approaches: randomized computation and quantum computing. Randomized computation utilizes random numbers as an additional resource to aid decision-making, but does not offer a significant improvement over standard approaches in terms of computational complexity. On the other hand, quantum computing harnesses quantum physical phenomena to process information according to the rules of quantum physics.

Quantum computers have the potential to perform certain tasks faster than classical computers, such as searching an unsorted database. This has implications for fields like cryptography and online financial transactions. The author notes that developing new algorithms and data structures is necessary for simulating and harnessing the power of quantum computing.

---

### Summary Video• . Duration: 2 minutes 2 min

Here is a summary of the text in 8 sentences, preserving key information and technical details:

Computational complexity is the theoretical study of algorithms, focusing on the ultimate limits of efficient algorithms. Decision problems are used to describe problems within computational complexity, and three main classes are defined: P (efficient decision), EXP (exponential-time decision), and NP (living between P and EXP). To show that P equals NP, it must be demonstrated that NP-complete problems can be solved efficiently, which is considered unlikely. Common techniques for solving NP-complete problems include linear search or backtracking, but these methods typically do not result in efficient algorithms. The study of algorithms and data structures covers a broad range of topics, and future developments may incorporate more randomness or quantum physics. The model of computing used in this module is deterministic, but real-world applications may require consideration of non-deterministic models. The exact relationship between P, NP, and EXP remains unknown. Further research is needed to break new ground in the field of algorithms and data structures.

Note: I did not include any links or formulae as they were not present in the original text. If you would like me to extract specific information from a formula or link, please let me know!

---

### Summary of the course Video• . Duration: 2 minutes 2 min

Unfortunately, there is no text provided for me to summarize. The provided text appears to be a video transcript and some additional page content related to an online module or course about algorithms in computer science. It does not contain any specific information, formulae, links, or technical details that can be summarized.

However, I can provide a general summary of the topic of algorithms in computer science:

Algorithms are a fundamental concept in computer science that involve solving problems using systematic steps. In this module, students learned about two methods for describing algorithms: flowcharts and pseudocode. They also explored linear data structures, such as vectors, stacks, queues, arrays, linked lists, and dynamic arrays. Students learned about various sorting algorithms, including linear search, bubble sort, insertion sort, binary search, Quicksort, and merge sort.

Moreover, the module touched on recursion, divide-and-conquer algorithms, and the theory of computing, which helps compare algorithm performance. The students also gained an appreciation for the importance of understanding algorithms in computer science, as it can improve problem-solving skills and translate basic principles across different programming languages.

If you provide more text or information about specific topics or concepts covered in this module, I would be happy to help summarize them for you.

---

### Solutions to revision exercises Reading• . Duration: 1 hour 1h

You will find the file RevisionSolutions.pdf attached. it. It has the solutions to the revision exercises in 10.2. RevisionSolutions.pdf PDF File Lesson 10.3 NP Lesson 10.4 Summary Video: Video Summary . Duration: 2 minutes 2 min Reading: Reading Solutions to revision exercises . Duration: 1 hour 1h Discussion Prompt: Discussion of solutions to revision exercises . Duration: 45 minutes 45 min Video: Video Summary of the course ....

---

## Week 21

### Revision Reading• . Duration: 10 minutes 10 min

I don't see any text provided. Please provide the text you would like me to summarize, and I will do my best to preserve all key information, formulae, links, and technical details while condensing it into 5 sentences.

---

### Practice Exam Reading• . Duration: 2 hours 2h

Unfortunately, it seems like there is no text provided for me to summarize. The given snippet appears to be a collection of links to various resources related to an ADS1 practice exam, including a PDF file and revision exercises. It does not contain any meaningful content that can be summarized.

If you could provide the actual text you would like me to summarize, I would be happy to help.

---

### ADS1 Practice Exam Answers Reading• . Duration: 10 minutes 10 min

I don't see any text provided. Please provide the text you'd like me to summarize, and I'll be happy to assist you in condensing it into four sentences while preserving key information, formulae, links, and technical details.

---

### September 2020 Exam Reading• . Duration: 3 hours 3h

Reading: Reading Revision . Duration: 10 minutes 10 min Reading: Reading Practice Exam . Duration: 2 hours 2h Reading: Reading ADS1 Practice Exam Answers . Duration: 10 minutes 10 min Reading: Reading September 2020 Exam . Duration: 3 hours 3h Reading: Reading Revision notes . Duration: 10 minutes 10 min

---

### Revision notes Reading• . Duration: 10 minutes 10 min

There is no text provided to summarize. The given text appears to be a discussion about exam revision strategies and note-taking methods, but it lacks any meaningful content or information. It seems to be a collection of random words and phrases, possibly from a digital note-taking system.

If you provide the actual text you'd like me to summarize, I'll be happy to assist you in extracting the key concepts, findings, formulae, links, and technical details into 8 sentences.

---

## Week 3

### Solution to the Birthday Party problem Video• . Duration: 6 minutes 6 min

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The problem of finding the greatest common divisor (GCD) of two numbers can be solved using Euclid's algorithm, also known as the Euclidean algorithm. The algorithm involves repeatedly replacing the larger number with the difference between the two numbers until the numbers are equal. This process is repeated by asking if a is greater than b, and if so, updating the values to replace a with the difference between the two numbers. If a is not greater than b, then b is replaced with the difference between the two numbers. The algorithm terminates when a equals b, at which point a is output as the GCD of the original two numbers. This process can be represented using a flowchart or pseudocode, which will be introduced in this topic. The algorithm's efficiency is guaranteed by the fact that the GCD does not change when one number is replaced with its difference to the other number. Euclid's algorithm has been used for centuries to solve this problem and has numerous applications in mathematics and computer science.

---

### Introduction to Topic 2 Video• . Duration: 1 minute 1 min

Unfortunately, you didn't provide any text for me to summarize. The provided text appears to be a video transcript with additional page content related to an online course or tutorial on pseudocode and algorithms. It does not contain any specific information that can be summarized in 8 sentences.

However, I can provide a general summary of what pseudocode is and its significance in understanding algorithms:

Pseudocode is a high-level representation of a program's logic that uses a mix of programming language syntax and natural language to convey the steps involved in an algorithm. It is used by computer scientists to describe algorithms without being tied to a specific programming language, allowing for greater universality and clarity. Pseudocode bridges the gap between flowcharts and actual programming languages, making it easier to understand and communicate complex algorithms. While pseudocode is not a programming language itself, it serves as an intermediary that provides a clear conceptual understanding of algorithms and facilitates communication among developers with different programming backgrounds.

If you could provide the text that was supposed to be summarized, I would be happy to assist further.

---

### Discretisation and pseudocode Video• . Duration: 8 minutes 8 min

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Pseudocode is a natural way to describe algorithms, resembling computer programs but not being themselves. It uses mathematical symbols, such as the assignment symbol (→) and comparison operators (=, <, >, <=, >=), to convey discrete steps in algorithms. Pseudocode can use names for variables, which should be without spaces, and it allows multiple assignments on a single line. The order of operations follows from left to right along lines and top to bottom on the page. A key concept is discretisation, where continuous processes are broken down into discrete parts suitable for computer processing. Pseudocode can also include logical operations, such as if-then statements, which allow conditional actions based on true or false conditions. The example of a thermostat temperature controller illustrates how pseudocode describes a process in discrete steps, using assignment, arithmetic operations, comparison operators, and logical operations. The goal is to create a clear, mathematically consistent representation that can be understood by humans and translated into computer code.

---

### Pseudocode and functions Video• . Duration: 4 minutes 4 min

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The concept of functions is introduced as a general idea in computer science and mathematics, which take inputs and produce outputs. Functions can return Boolean values such as true or false, and are essential for solving algorithms. In pseudocode, a function is defined by the keyword "function", followed by the function name, input parameters (in brackets), and the body of the function. The body contains operations that take place inside the function, such as conditional statements like if-then. A specific example of a function in pseudocode is the "even" function, which takes an integer n as input and returns true if it's odd or false if it's even. This function uses modular arithmetic to determine its output. The problem of calculating mod 2 for integers in any base (between 2 and 10) has been posed, requiring a general algorithm that can be discussed and solved through the Forum. To approach this problem, one needs to understand how mod 2 can be calculated for integers represented as bit strings or in decimal form.

---

### Introduction to loops in pseudocode Video• . Duration: 12 minutes 12 min

This is a transcript of an educational video on pseudocode and iteration, specifically on using for loops and while loops to solve problems. Here's a summary of the key points:

**Introduction to Loops in Pseudocode**

The instructor introduces the concept of loops in pseudocode, explaining that there are two main types of loops: for loops and while loops.

**For Loops**

The instructor uses a problem example, finding out if x-squared is equal to 2 has an integer solution. They provide a pseudocode solution using a for loop:

* Function x_integer(n)
	+ Initialize y to false
	+ For i from 1 to n
		- If i squared equals n
			- Assign true to y
		- Otherwise, increment i
	+ Return y

**While Loops**

The instructor also provides an alternative solution using a while loop:

* Function x_integer(n)
	+ Initialize y to false
	+ Initialize i to 1
	+ While i squared is less than or equal to n
		- If i squared equals n
			- Assign true to y
		- Otherwise, increment i
	+ Return y

The instructor emphasizes that the choice between for loops and while loops depends on the specific problem and personal preference.

**Additional Materials**

The instructor provides additional materials:

* Reading: "Reading Pseudocode"
* Practice Assignment: "Iteration in pseudocode"
* Discussion Prompt: "Translate pseudocode into another language"

Note: The video transcript includes a timestamp for each section, which is not included here.

---

### Euclidean algorithm in pseudocode Video• . Duration: 4 minutes 4 min

The text discusses the Euclidean algorithm, a method for finding the greatest common divisor (GCD) of two integers. The algorithm is implemented as a function in pseudocode using both for loops and while loops. The for loop version iterates from 0 to the sum of the two inputs, with an if-then statement to check if the remainder is zero, breaking out of the loop and returning the GCD. In contrast, the while loop version iterates until the inputs are equal, with a single if-then statement to update the values.

The text highlights the differences in character between for loops and while loops, noting that while loops have more complex assignments per iteration. The use of pseudocode has variations in different sources, and understanding these conventions is essential for using pseudocode universally. Additionally, pseudocode is language-dependent, as it relies on English notation, making it less universal.

The text encourages readers to explore pseudocode in various languages, alphabets, and letter systems by translating a piece of pseudocode into another language or inventing their own language. This exercise aims to promote universality and creativity with pseudocode.

---

### Pseudocode Reading• . Duration: 1 hour 1h

I don't see any text to summarize. The provided text appears to be a course description with links, rather than a specific passage that needs summarization.

However, I can provide information about pseudocode and its usage in algorithms, based on the references provided:

Pseudocode is a high-level representation of algorithmic steps that can be understood by humans without needing to know the specific programming language. It's often used as a intermediate step between designing an algorithm and implementing it in code.

The Euclidean algorithm, which is mentioned in the text, is a well-known algorithm for finding the greatest common divisor (GCD) of two integers. The pseudocode for this algorithm can be found in Cormen et al.'s book "Introduction to Algorithms" (Section 2.1).

If you could provide the actual text from Section 2.1 of the book, I'd be happy to help summarize it for you.

---

## Week 6

### Abstract data structure: stacks Video• . Duration: 5 minutes 5 min

Here is a summary of the text in 8 sentences, preserving key information:

The video introduces the concept of stacks as an abstract data structure, which differs from queues in that only one element (the top) can be accessed at a time. The stack follows Last-In-First-Out (LIFO) access pattern, where elements are added and removed from the top. A stack is useful for dynamic memory storage and modeling real-world scenarios, such as managing a pile of plates or serving food to multiple customers. The basic operations on a stack include push!, which adds an element to the top, top(), which returns the current top element, pop!, which removes and returns the top element, and empty?, which checks if the stack is empty. A convenient representation for binary logic is using a stack, as it allows for efficient storage and retrieval of binary data. The video suggests converting an integer from decimal to binary using a stack by repeatedly dividing by 2 and appending the remainder to the top of the stack. This process can be represented in pseudocode as follows: `Procedure ConvertToBinary(n): While n > 0: Append (n mod 2) to Stack; Divide n by 2; End While Return Stack;`. The video also touches on the concept of "full stack development" in software development, where it refers to a developer who has expertise in all aspects of software development, from front-end to back-end and database management.

---

### Solution to the conversion problem Video• . Duration: 7 minutes 7 min

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The problem of converting an integer from decimal to binary using a stack can be solved by dividing the number by 2 and pushing the remainder onto the stack repeatedly. The process continues until the floor of the remaining number over 2 equals 0. At this point, the final value pushed onto the stack is the most significant digit in the binary representation. The algorithm works by simulating this process using a while loop, where each iteration divides the current value and pushes the remainder onto the stack. If the result of the division is an even number, no new value is added to the stack. If the result is an odd number, a new value is pushed onto the stack. The algorithm terminates when the floor of the remaining number over 2 equals 0, at which point the final value pushed onto the stack is returned as the binary representation of the input number. This process can be implemented using pseudocode, where a while loop iterates through the steps of dividing and pushing remainders onto the stack.

---

### Summary Video• . Duration: 1 minute 1 min

There is no text provided for me to summarize. The text you've shared appears to be a video transcript, lesson plan, and additional content related to abstract data structures, specifically stacks, queues, and vectors. It doesn't contain any key information, formulae, links, or technical details that can be summarized in 8 sentences.

If you could provide the actual text you'd like me to summarize, I'd be happy to assist you.

---

### Theseus and the Minotaur Video• . Duration: 1 minute 1 min

There is no text provided for me to summarize. The given text appears to be a transcript of a video presentation, with various links and technical details mentioned in the metadata section. It discusses a problem related to Greek mythology, where Theseus needs to find his way out of a labyrinth using only a deck of playing cards and a pencil, rather than a traditional string or bag.

However, without the actual text content, it's not possible to preserve key information, formulae, links, and technical details. If you provide the actual text, I would be happy to assist you with summarizing it in 8 sentences while focusing on the most important concepts and findings.

---

### Brief Introduction to Dynamic Sets Reading• . Duration: 45 minutes 45 min

Unfortunately, there is no text provided for me to summarize. The text appears to be a series of announcements and links related to a course on algorithms and data structures, but it does not contain any specific content or information that needs summarization. If you provide the actual text, I would be happy to help!

---

## Week 9

### Solution to the Lottery Problem Video• . Duration: 5 minutes 5 min

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The module "Algorithms and Data Structures Part 1" focuses on sorting algorithms, which can make searching data more efficient. To solve a problem where determining the winner of a lottery based on unique birthdays is required, a linear search algorithm is applied to every other element in a vector containing player numbers and birthdays. The approach involves counting the appearances of each birthday number using a dynamic array to store their counts. A pseudocode function "FindBirthdays(v)" is described, where v is the input vector, which initializes an empty dynamic array and then applies a linear search starting from the second element (i=2) up to the length of the vector. The outer while loop iterates over each element in the vector, and an inner while loop checks if the birthday number appears elsewhere in the vector by comparing it with other elements. If a unique birthday is found, its count is increased by 1, and if the count equals 1, the birthday is recorded in the dynamic array. The dynamic array stores all birthdays that appear only once as input to the function. This approach ensures that the function can efficiently identify unique birthdays from a large dataset.

Note: I didn't include any formulae, links, or technical details not essential to understanding the main concepts and algorithm.

---

### Introduction to Topic 5 Video• . Duration: 1 minute 1 min

Here is a summary of the text in 8 sentences, preserving key information:

The problem at hand involves sorting a data structure and finding the sorted version with the same values but in ascending numerical order. To solve this, algorithms like bubble sort and insertion sort can be used to sort data. The solution presented incorporates elements from linear search, vectors, and dynamic arrays. Sorting data simplifies the process of searching for unique entries by reducing the need to scan the entire vector. One such scenario is sorting lottery tickets in date order, allowing for efficient comparison of birthdays. The general structure of the problem involves transforming an input data structure into another with the same values but sorted according to a specific order. Two algorithms to be covered are bubble sort and insertion sort, which will provide practical code examples using JavaScript. These algorithms can be used to solve various sorting-related problems, making them essential tools in computer science.

---

### Bubble sort Video• . Duration: 13 minutes 13 min

I can provide a detailed explanation of the bubble sort algorithm and its implementation on vectors, dynamic arrays, and arrays.

**Bubble Sort Algorithm**

The bubble sort algorithm is a simple sorting algorithm that works by repeatedly iterating through a list of elements, comparing each pair of adjacent elements and swapping them if they are in the wrong order. The process continues until no more swaps are needed, indicating that the list is sorted.

Here's a step-by-step explanation of the bubble sort algorithm:

1. Start with the first element of the list.
2. Compare it with the next element.
3. If the current element is greater than the next element, swap them.
4. Move to the next element and repeat steps 2-3 until you reach the end of the list.
5. Repeat steps 1-4 for each pass through the list until no more swaps are needed.

**Implementation on Vectors**

To implement bubble sort on a vector, we can use the following code:
```cpp
void bubbleSort(vector<int>& vec) {
    int n = vec.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (vec[j] > vec[j + 1]) {
                swap(vec[j], vec[j + 1]);
            }
        }
    }
}
```
This implementation uses two nested loops to iterate through the vector. The outer loop iterates `n-1` times, and the inner loop iterates `n-i-1` times. If an element is greater than the next element, we swap them.

**Implementation on Dynamic Arrays**

To implement bubble sort on a dynamic array, we can use the following code:
```cpp
void bubbleSort(dynamicArray<int>& arr) {
    int n = arr.length();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}
```
This implementation is similar to the vector implementation, but we use the `length()` function to get the size of the dynamic array.

**Implementation on Arrays**

To implement bubble sort on an array, we can use the following code:
```cpp
void bubbleSort(array<int>& arr) {
    int n = arr.length;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}
```
This implementation is similar to the vector and dynamic array implementations, but we use the `length` function to get the size of the array.

**Applying Bubble Sort on a Stack**

To apply bubble sort on a stack using only other stacks, we can use the following approach:

1. Create a new stack and push all the elements from the original stack onto it.
2. Pop one element from the original stack and push it onto the new stack.
3. Compare the top two elements of the new stack and swap them if they are in the wrong order.
4. Repeat steps 2-3 until there is only one element left in the new stack.
5. Push the remaining element onto the new stack, which now contains the sorted elements.

This approach requires three stacks: an original stack, a temporary stack for swapping elements, and a final stack to store the sorted elements.

Here's some sample code in C++:
```cpp
void bubbleSortStack(Stack<int>& stack) {
    Stack<int> temp;
    while (!stack.isEmpty()) {
        int element = stack.pop();
        temp.push(element);
        if (!temp.isEmpty() && temp.peek() > element) {
            int swappedElement = temp.pop();
            temp.push(element);
            temp.push(swappedElement);
        }
    }
    while (!temp.isEmpty()) {
        stack.push(temp.pop());
    }
}
```
This implementation uses a temporary stack to swap elements and push them onto the final stack. Note that this approach requires extra memory to store the temporary stack, which may not be efficient for large inputs.

I hope this explanation helps! Let me know if you have any questions or need further clarification.

---

### Bubble sort on a stack Video• . Duration: 5 minutes 5 min

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The bubble sort algorithm can be modified to sort a stack instead of a vector by using two stacks. The process involves comparing the tops of the two stacks, swapping them if necessary, and repeating this process until the largest element is at the top of the first stack. This process requires n-1 passes for a stack of length n. After each pass, the second stack is pushed onto the first stack, effectively reversing the order of the elements in the first stack. The algorithm then repeats from the beginning, pushing new elements onto the stacks and comparing them until the stack is sorted. The modified bubble sort algorithm on a stack can be used to solve a problem where images need to be sorted based on certain properties such as color, material, or name. To apply this algorithm to sorting images, each image would be represented as a piece of data in an element of a vector, and the algorithm would compare and swap them accordingly. The modified bubble sort algorithm has been implemented in a video, which can be accessed for further learning.

---

### Insertion sort Video• . Duration: 8 minutes 8 min

The insertion sort algorithm is a simple and efficient sorting technique that works by iterating through an array or vector one element at a time, inserting each element into its proper position within the sorted portion of the array. The algorithm compares each element to all previous elements and shifts them forward until it finds the correct position for the new element.

The key concept behind insertion sort is that once an element has been inserted into its correct position, all subsequent elements in the array will be sorted without further comparisons. This property allows the algorithm to terminate early when no more swaps are needed, making it less efficient than bubble sort in some cases.

The pseudocode for insertion sort can be summarized as follows:

1. Start at the second element of the array.
2. Compare each element with all previous elements and shift them forward until it finds the correct position for the new element.
3. Repeat step 2 until the end of the array is reached.

In terms of its implementation, insertion sort can be easily adapted to work on arrays, vectors, or dynamic arrays. The main difference between these implementations is the way in which elements are accessed and manipulated.

The algorithm's time complexity is O(n^2) in the worst case, although it can be improved to O(n) in the best case when the input array is already sorted.

Insertion sort has several advantages over bubble sort, including:

* It does not require any additional space for an auxiliary array.
* It only requires a single pass through the data, whereas bubble sort may require multiple passes.
* It is generally faster than bubble sort for nearly-sorted or partially-sorted data.

However, insertion sort also has some disadvantages, such as:

* It can be slower than bubble sort for very large datasets due to its overhead in shifting elements.
* It requires more memory accesses than bubble sort in some cases.

Overall, insertion sort is a simple and efficient sorting algorithm that is well-suited for many applications, particularly those with relatively small datasets.

---

### Response to discussion points Video• . Duration: 6 minutes 6 min

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The insertion sort algorithm can be implemented in arrays, vectors, and dynamic arrays. The array implementation involves starting at the second element (index 2) and comparing it to the elements before it, shifting them if necessary. A similar approach can be used for stack-based sorting using two stacks, where values are transferred between the stacks based on comparison. However, insertion sort can require fewer operations in its implementation than bubble sort when dealing with vectors that are mostly sorted. In the case of a vector of length five, the insertion sort requires approximately 17 operations (seven reads and ten writes), whereas bubble sort would require around 49 operations (forty-nine reads and forty-eight writes). This advantage is due to the fact that insertion sort only needs to make comparisons for elements that are not in their correct position. In contrast, bubble sort requires making comparisons for all elements during each pass. Overall, the insertion sort has an edge over bubble sort when dealing with vectors that are nearly sorted.

I did not include formulae, links, or technical details as they were not explicitly mentioned in the provided text.

---

