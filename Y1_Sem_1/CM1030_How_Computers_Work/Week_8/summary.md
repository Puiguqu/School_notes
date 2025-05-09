# Week 8 - CM1030 How Computers Work - How a computer works - Week 1

## Peripherals Video• . Duration: 7 minutes 7 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/kkWAg/peripherals)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

1. A computer consists of a CPU (central processing unit) and memory, but also includes various peripheral devices such as screens, keyboards, hard disks, sound cards, and more.
2. These devices are connected to the CPU and memory via the bus, which is like a central highway for data transfer.
3. The bus allows for communication between the CPU, memory, and peripheral devices, including displays, keyboards, and graphics cards.
4. Each peripheral device has its own controller, which decodes data received from the bus and sends it to the device.
5. Graphics processing units (GPUs) are highly specialized controllers that handle parallel programming and produce high-speed graphics.
6. Universal Serial Bus (USB) is a type of controller used for connecting devices such as hard disks, external sound cards, and keyboards to computers.
7. USB supports multiple devices and allows for independent data transfer between the CPU and devices.
8. Bluetooth is another protocol used for wireless communication between peripheral devices and computers.
9. Devices communicate with the CPU using load instructions, which send signals along the bus to the controller and then to the device.
10. Some machine languages have specialized commands for accessing peripheral devices, while others use memory-mapped IO (input/output) to simplify communication.
11. Memory-mapped IO allows peripherals to be treated as part of the main memory, reducing the number of instructions needed to interact with them.
12. The speed of memory and devices is critical in determining the overall performance of a computer, as accessing peripheral devices can be many times slower than memory or registers.
13. Software can often execute other instructions while waiting for data from memory, but may be blocked if that data is not available.
14. Direct memory access (DMA) enables faster communication between devices and memory by allowing them to communicate directly without CPU intervention.
15. Understanding the interaction between peripheral devices and the CPU is crucial in optimizing computer performance and software functionality.

---

## Case study: virtual reality Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/rHf6L/case-study-virtual-reality)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Virtual reality (VR) is an interactive technology that surrounds users with a virtual world. The headset, which connects to the computer via HDMI cable, provides a display similar to a screen. However, it also has a USB 3.0 connector, allowing for power and data transfer. The headset sends information back to the computer via USB, tracking head movement and sending data about it.

Touch controllers are used to interact with virtual objects in VR space, allowing users to grab and manipulate virtual objects as if they were real. These controllers use Bluetooth protocol to connect to the headset wirelessly, rather than being wired to the computer. The connection is proprietary, ensuring fast communication between the controllers and the headset.

VR places strong demands on speed, requiring immediate updates when turning the head or moving in space. This can cause nausea, known as simulator sickness, if the delay is too long. Computers have made significant progress in processing power, allowing for instantaneous updates to be displayed within 20 milliseconds. 

The graphics processing unit (GPU) handles high-quality computer graphics required for VR, working in a parallel manner to ensure fast rendering. A powerful GPU or graphics card is necessary to unlock virtual reality applications that require rapid communication between devices.

VR relies on new peripheral devices that enable users to interact with computers in novel ways, creating challenges for computer scientists to balance usability, fun, and performance.

---

## Case study debrief Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/ruHoI/case-study-debrief)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The code being analyzed is written in C and consists of simple instructions that demonstrate how code works on a CPU. The first line adds two numbers together using an add instruction, which operates on registers (e.g., register three stores value one). The arithmetic logical unit performs the addition, saves the result back into register five, and then stores variable i back into memory. The next line is an if statement implemented by conditional jump, comparing the value of variable i with 100 in register zero. If equal, it jumps to code implementing "i equals zero." Otherwise, it moves to the "here" instruction. Variable i is set using a move operation and stored back in memory.

The final line calls a function called "point," which executes complex code behind the scenes. Functions allow simple code to utilize lots of functionality by jumping away from the current code. Point is a drawing function that sends data to the graphics card, which is likely implemented as a store instruction to peripheral devices. The add instruction is fast due to register access, while load and store instructions are slower.

The performance of the program can be affected by interacting with peripherals, using too many memory accesses, or calling functions, especially if they take small amounts of time. Modern graphics work by storing data in registers before sending it all together to minimize slow stores. The amount of memory accessed can also impact performance, as excessive memory access can lead to cache misses.

Functions can be optimized through inlining, which copies function code into standard code to avoid jump instructions and potential slowdowns. In summary, understanding how code works involves grasping the basics of register operations, conditional jumps, functions, and peripheral interactions. This knowledge is crucial for writing efficient code that takes advantage of CPU capabilities while minimizing slow operations.

---

## Summary Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/qlqLR/summary)

There is no text provided for me to summarize. The given text appears to be a video transcript and additional page content related to an online course or tutorial on computer science, specifically covering the basics of computer hardware, CPU, memory, machine language, and peripherals.

However, I can provide a summary based on general knowledge about these topics:

In computer science, the Central Processing Unit (CPU) is the primary component that executes instructions and performs calculations. Memory plays a crucial role in storing data and program instructions. Machine language is the lowest-level programming language that CPUs can execute directly, consisting of binary code.

The interaction between CPUs, memory, and peripherals enables computers to perform various tasks, such as processing visual and auditory information, interacting with users, and communicating over networks like the Internet.

Computers use a variety of input/output devices, including keyboards, displays, and speakers, which interact with the CPU and memory through standardized interfaces. Understanding how code works involves grasping the fundamental principles of programming languages, data types, control structures, and algorithms.

In this course, students will delve deeper into topics such as hardware-software interaction, networking, and software development, building on their foundational knowledge of computer science concepts.

---

## Communicating with other devices Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/supplement/UNXz2/communicating-with-other-devices)

Brookshear, J.G. and D. Brylow Computer science: an overview . (Harlow: Pearson Education, 2019) 13th edition (Global Edition). Chapter 2 Data Manipulation. Read Section 2.5. This reading is available in the Online Library via the VLeBooks collection. Lesson 8.1 Communicating with devices Video: Video Peripherals . Duration: 7 minutes 7 min Reading: Reading Communicating with other devices . Duration: 1 hour 1h Practice Assignment: Practice quiz – Devices ....

---

