# Week 11 - CM1030 How Computers Work - How a computer works - Week 1

## Multitasking Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/BDym1/multitasking)

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

## History of operating systems Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/J9pDh/history-of-operating-systems)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The first fully operational computer was built at the University of Cambridge, called EDSAC, designed by Maurice Wilkes. Wilkes taught the author, who also highlighted Alan Turing's contributions to building ACE, another early computer. Turing was a genius in laying mathematical foundations for computing and developing AI ideas. John Von Neumann, J Presper Eckert, and John Mauchly in the US laid technical foundations for computers, influencing Wilkes and Turing's machines. Early computers lacked operating systems, with users signing up for time slots to use them. The introduction of punched cards allowed programmers to input programs into computers. Programmers made holes in the card at positions representing machine instructions, which were then interpreted by the computer. For fast results, massive computers with screens and keyboards (terminals) were needed in the 1970s. These terminals linked users to main computers for multi-processing or timesharing. The concept of sharing primary computers is still relevant today, such as when websites share a server. Timesharing remains necessary due to running multiple applications on shared CPUs. Modern computers have multiple CPUs (multi-core), but still require load balancing to efficiently allocate tasks. Load balancing is crucial in managing computer programs and optimizing computing resources. The development of operating systems focuses on managing computer programs and allocating tasks to CPUs efficiently.

---

## Processes Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/9ckpM/processes)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A standard single-core CPU can only handle one instruction at a time. However, modern computers can run multiple applications simultaneously by using processes, which are coherent pieces of software that can run independently of other processes. Each process has its own memory space allocated by the memory manager, but they do not share the same memory as other processes. There is also a concept called threads, which have similar properties to processes but share memory with other threads. Processes allow multiple tasks to appear as if they are running simultaneously, even though they actually run one after another due to time slicing.

The CPU runs each process for a certain amount of time, known as a time slice, before sending an interrupt to the next process. This interrupts the current process and allows it to yield control to the next process. The order in which processes run is not always predictable, but can be influenced by factors such as priority and I/O operations.

High-priority processes are given more frequent time slices, allowing them to respond faster to user input. Meanwhile, low-priority processes wait for their time slice to finish before continuing. When a process needs data from disk, it yields control to other processes until the data is available, which can significantly slow down its execution. This highlights the trade-off between CPU performance and I/O operations.

The process switching mechanism allows multiple tasks to appear as if they are running simultaneously, giving modern computers their ability to multitask. Despite this apparent simultaneity, each process still executes one instruction at a time due to the limitations of the single-core CPU architecture.

---

## History of operating systems Reading• . Duration: 50 minutes 50 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/supplement/1nuzR/history-of-operating-systems)

There is no text provided to summarize. The text appears to be a course outline or a syllabus from a computer science class, specifically Chapter 3 of "Computer Science: An Overview" by J.G. Brookshear and D. Brylow. It lists the chapter's content, including:

- Section 3.1 on the history of operating systems
- A video lecture on the history of operating systems (6 minutes)
- A reading assignment on the history of operating systems (50 minutes)
- A practice quiz on the history of operating systems (30 minutes)
- A discussion prompt to share one's computer history (1 hour)

However, there is no text to summarize, and therefore, no information can be preserved or summarized.

---

## Coordinating the machine's activities Reading• . Duration: 45 minutes 45 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/supplement/0rmTR/coordinating-the-machines-activities)

Brookshear, J.G. and D. Brylow Computer science: an overview . (Harlow: Pearson Education, 2019) 13th edition (Global Edition). Chapter 3 Operating systems. Read Section 3.3. This reading is available in the Online Library via the VLeBooks collection. Lesson 11.0 Introduction Lesson 11.1 History of operating systems Lesson 11.2 Processes Video: Video Processes . Duration: 4 minutes 4 min Reading: Reading Coordinating the machine's activities ....

---

## Process simulation Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/supplement/1qw09/process-simulation)

Here is a summary of the text in 15 sentences:

The next activity is a simulation game where you play the role of an operating system process manager, tasked with selecting which processes to run on a computer. The game shows various processes that might run on a typical computer, including a word processor, video player, email client, web browser, and cloud sync process. Your job is to choose which process to run by clicking on it, turning the selected process green.

When a process is waiting for a resource, it will have "WAITING" written before its status. You should not select these processes to run as there is no benefit. On the other hand, if a non-waiting process is left idle for too long, the application may become slow and unresponsive to the user.

The goal of the game is to prevent this from happening by selecting the correct processes to run at any given time. If a yellow process remains idle for an extended period, it will seem unresponsive to the user and turn red, resulting in a loss of the game.

To succeed, you must balance the needs of each process and ensure that no single process is left idle for too long. This requires careful consideration of each process's status and requirements. The simulation game provides a realistic scenario for understanding the importance of resource allocation in operating systems.

Overall, the goal of the simulation game is to practice coordinating the machine's activities and making decisions about which processes to run on a computer. By completing this activity, you will gain a better understanding of how operating systems manage resources and prioritize tasks.

---

