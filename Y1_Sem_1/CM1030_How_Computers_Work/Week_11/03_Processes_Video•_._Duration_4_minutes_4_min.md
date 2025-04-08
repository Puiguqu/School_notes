# Processes Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/9ckpM/processes)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A standard single-core CPU can only handle one instruction at a time. However, modern computers can run multiple applications simultaneously by using processes, which are coherent pieces of software that can run independently of other processes. Each process has its own memory space allocated by the memory manager, but they do not share the same memory as other processes. There is also a concept called threads, which have similar properties to processes but share memory with other threads. Processes allow multiple tasks to appear as if they are running simultaneously, even though they actually run one after another due to time slicing.

The CPU runs each process for a certain amount of time, known as a time slice, before sending an interrupt to the next process. This interrupts the current process and allows it to yield control to the next process. The order in which processes run is not always predictable, but can be influenced by factors such as priority and I/O operations.

High-priority processes are given more frequent time slices, allowing them to respond faster to user input. Meanwhile, low-priority processes wait for their time slice to finish before continuing. When a process needs data from disk, it yields control to other processes until the data is available, which can significantly slow down its execution. This highlights the trade-off between CPU performance and I/O operations.

The process switching mechanism allows multiple tasks to appear as if they are running simultaneously, giving modern computers their ability to multitask. Despite this apparent simultaneity, each process still executes one instruction at a time due to the limitations of the single-core CPU architecture.

