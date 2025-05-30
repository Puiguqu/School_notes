# Week 7 - CM1030 How Computers Work - How a computer works - Week 1

## Introduction: What does code really do? Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/vZoRm/introduction-what-does-code-really-do)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The course introduces programming as a crucial skill for computer scientists to learn. Programming involves writing code that makes software work. The example provided uses JavaScript with p5.js to animate a moving dot on the screen. This code is executed every frame, allowing the circle to move from frame to frame.

A core part of this program changes a variable called "i" by adding 1 to it, and then draws a dot based on that value. This process is repeated until the variable reaches a certain threshold. The program uses an if statement to make choices about what actions to take, depending on the value of "i".

The use of if statements allows the program to control its behavior in different situations. The program's behavior can be understood by analyzing the code line by line. However, it is also useful to consider how the software interacts with the CPU.

This lesson introduces the concept of computer architecture and machine language, which are essential for understanding how software works at a lower level. Machine language is the lowest-level programming language that directly translates to CPU instructions.

The program used in this example is written in C, which is a simpler language than JavaScript but still has similar syntax. The goal of this lesson is to explore what happens behind the scenes on the CPU when running a program, using a simplified language like C as an example.

In future lessons, students will examine how programs are executed on the CPU and understand the intricacies of machine language and execution.

---

## CPU and memory Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/9MiBV/cpu-and-memory)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

1. The CPU (Central Processing Unit) is the active part of a computer that performs calculations and instructions.
2. Data is moved between memory and the CPU using a bus, a set of wiring that connects the two.
3. The arithmetic logical unit (ALU) performs numerical mathematical calculations within the CPU.
4. The control unit controls the running of a program by executing instructions and making choices.
5. Registers are small amounts of memory on the CPU that can store data, allowing for quick access to it.
6. Data is loaded from memory into registers before being manipulated using the ALU.
7. The cache is a smaller, faster set of memory that stores frequently used values, reducing the need to access main memory.
8. The CPU has multiple layers of memory, including registers, cache, and main memory, which affect its performance.
9. Instructions are stored in memory like data, using the stored program concept.
10. The program counter (PC) tells the CPU where to find the current instruction in memory.
11. The instruction register stores the current instruction being executed by the CPU.
12. The fetch-execute cycle involves fetching an instruction from memory based on the PC and then executing it.
13. While CPU speed is important, bus speed and memory speed have a greater impact on computer performance.
14. A large and fast cache can significantly improve computer performance by reducing the need to access main memory.
15. When considering buying a computer, factors like cache size, bus speed, and memory speed are just as important as CPU speed.

---

## Machine language Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/arzaF/machine-language)

The provided text appears to be a transcript of an educational lecture or video on computer science, specifically on the topic of machine language and computer architecture. The content covers various aspects of machine language, including:

1. **Machine instructions**: The basic building blocks of a computer's programming language.
2. **Data transfer operations**: Instructions that move data between memory and registers, such as load and store.
3. **Control instructions**: Instructions that control the flow of a program, such as jump and conditional jumps.
4. **Program counter**: A register that holds the memory location of the next instruction to be executed.

The lecture also touches on the concept of high-level programming languages, such as C and JavaScript, and how they are converted into machine instructions using compilers and interpreters.

**Key concepts:**

* Machine language is a low-level, binary representation of code that a computer's processor can execute directly.
* Machine instructions are used to perform specific tasks, such as data transfer operations and control instructions.
* The program counter plays a crucial role in determining the next instruction to be executed.

**Learning objectives:**

* Understand the basics of machine language and its role in computer programming.
* Learn about different types of machine instructions, including data transfer operations and control instructions.
* Appreciate the importance of the program counter in controlling the flow of a program.

This content is suitable for students pursuing a degree in computer science or related fields, as well as anyone interested in learning about the fundamentals of computer architecture and programming.

---

## CPU and memory – Lecture summary Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/supplement/UFcrz/cpu-and-memory-lecture-summary)

Here is a summary of the text in 15 sentences, preserving all key information, formulae, and technical details:

The Central Processing Unit (CPU) plays a crucial role in a computer system, responsible for executing instructions and processing data. The CPU consists of primary components such as the bus, arithmetic logical unit (ALU), control unit, registers, and cache memory. The bus connects the CPU to other components like memory, allowing fast data interchange. Data is moved between memory and the CPU via the bus, enabling quick access and processing.

The ALU performs numerical and logical calculations, forming the core of the CPU's computational abilities. Examples of tasks handled by the ALU include adding values to variables or performing mathematical operations. The control unit manages the execution of instructions within a program, including conditional operations like 'if' statements. It decides which bit of code to execute based on a condition.

Registers are small, fast memory locations within the CPU used to store data temporarily during calculations. Data is loaded from main memory into registers for quick access during arithmetic operations. Cache memory is a smaller, faster type of memory located close to the CPU, used to store frequently accessed data to speed up processing. A large and fast cache can significantly enhance computer performance by reducing the need to access slower main memory.

The stored program concept allows programs and instructions to be stored in memory like data, providing flexibility in using different software on the same hardware. The fetch-execute cycle is a process where the CPU fetches instructions from memory and executes them, guided by special registers like the program counter and instruction register. CPU speed, measured in gigahertz, is important but not the only factor affecting performance. Bus speed, memory speed, and cache size also significantly impact performance.

To successfully master this content, one should understand CPU and memory interaction, grasp the role of the control unit, identify the purpose of registers, appreciate the importance of cache memory, and comprehend the fetch-execute cycle. Recognizing factors influencing computer performance is essential to optimize system performance.

---

## Computer architecture Reading• . Duration: 45 minutes 45 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/supplement/eCKMV/computer-architecture)

Brookshear, J.G. and D. Brylow Computer science: an overview . (Harlow: Pearson Education, 2019) 13th edition (Global Edition). Chapter 2 Data Manipulation. Read Section 2.1. This reading is available in the Online Library via the VLeBooks collection. Lesson 7.0 Introduction Lesson 7.1 Computer architecture Video: Video CPU and memory . Duration: 7 minutes 7 min Reading: Reading CPU and memory – Lecture summary . Duration: 10 minutes 10 min Practice Assignment: Practice quiz - CPU and memory ....

---

## Machine language Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/supplement/71bCG/machine-language)

Brookshear, J.G. and D. Brylow Computer science: an overview . (Harlow: Pearson Education, 2019) 13th edition (Global Edition). Chapter 2 Data Manipulation. Read Sections 2.2 and 2.3. This reading is available in the Online Library via the VLeBooks collection. Lesson 7.0 Introduction Lesson 7.1 Computer architecture Lesson 7.2 Machine language and execution Video: Video Machine language . Duration: 10 minutes 10 min Reading: Reading Machine language ....

---

## CPU simulation Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/supplement/wGKjs/cpu-simulation)

Here is a summary of the text in 15 sentences:

The interactive simulation will teach how a CPU executes machine instructions by playing the part of the CPU. The simulation consists of a help text at the bottom, guides the user through each stage, and has registers on the right side. Registers are used to store values, and entering a value into a register requires pressing "return". Most instructions involve putting numbers into registers or using existing register values. Register numbers range from 0 to 7, but users should not use the actual values in the operands. Each turn, the user needs to press "Fetch Instruction" to get a new instruction. The instruction is fetched at the memory address in the programme counter. In most cases, the programme counter updates automatically, so no changes are needed. However, when using a JUMP instruction, the programmer must set the programme counter address manually. The MEMLOAD instruction loads data from memory by entering the memory address into the address field and pressing "Fetch". The value appears next to the Fetch button, which can be copied into a register. The MEMSTORE instruction writes values back to memory by putting the memory address in one field and the store value in another, then pressing "return" or "Store" if correct.

Here are some important details:

* Registers 0-7 are used for operands.
* Programme counter updates automatically, unless using JUMP instructions.
* MEMLOAD instruction loads data from memory by fetching at a specific address.
* MEMSTORE instruction writes values back to memory by storing in one field and pressing "Store" if correct.

Overall, the simulation focuses on understanding how a CPU executes machine instructions, including loading and storing data from memory.

---

