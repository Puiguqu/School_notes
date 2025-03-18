# Week 2 - CM1030 How Computers Work - How a computer works - Week 1

## The deep secret of computer science Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/TJFVG/the-deep-secret-of-computer-science)

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

## State Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/xG0f0/state)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A computer program can be in multiple different states, which affect how it responds to interaction. A state is a temporary configuration of a computer system that affects its behavior. A computer has two primary states: on and off. When a computer is on, it performs various tasks, while when it's off, it doesn't perform any actions. The video player has multiple states, including stopped, playing, pause, buffering, and loading. The state of the video player changes due to user input (play/pause) or internal decisions (buffering/loading). Other software components, such as a word processor, also have states that affect their behavior. A cursor in a word processor can be in three states: absent, typing, and selection. Each state triggers different actions and behaviors. Understanding the states of software is crucial to troubleshooting issues and getting over confusing problems. Software can get stuck in certain states due to internet connection failures or other external factors. This can lead to unpredictable behavior, such as freezing or displaying incomplete data. Recognizing the states of software can help developers anticipate and address potential issues. The concept of states is fundamental to computer science and applies to various aspects of software design and functionality.

---

## An e-commerce site Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/IjLKa/an-e-commerce-site)

Here is a summary of the text in 15 sentences, focusing on key concepts and findings:

An e-commerce website operates using states, which represent different stages of the user's interaction with the site. The first state is typically the default homepage, where users search for products. This transition to the second state, the search page, involves a change in data stored by the website about the user. Clicking on a product leads to a third state, examining the product details. Adding a product to the shopping cart represents another state change. The shopping cart is often conditional, requiring users to be logged in to proceed. Logging in itself constitutes a separate state, and completing it allows access to the shopping cart. Progressing through states involves entering payment details and choosing delivery options. Each of these steps represents a distinct state, with transitions triggered by user input or server-side transactions. The checkout process is characterized by multiple states, including entering an address, credit card information, and delivery method. Once the payment has been processed, the website confirms the purchase in its final state. In computer science, states are often used to model the behavior of software systems, with each state representing a specific condition or action. The concept of states is fundamental to understanding how computer programs work, particularly those that involve user input and data processing. By analyzing states in software systems, developers can identify inefficiencies and improve system performance. The use of states allows for more modular and maintainable code, as each stage of the program can be treated independently.

Note: I did not include the additional content from Lesson 2.1-3 as it was not part of the original text provided.

---

## Why does turning it off and on again work? Video• . Duration: 3 minutes 3 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/8j55j/why-does-turning-it-off-and-on-again-work)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Computers and software can be in different states at various levels of abstraction. The state of a cursor in a word processor affects only one detail of a single application. In contrast, the formatting of a document is an example of a state that encompasses multiple features. When typing, the text will match the formatting of the text around the cursor. However, pressing a key can change massively depending on where you are in the text. For instance, pressing the E key creates bold characters in one location and heading font in another. The real state of a word processor is complex, containing many minor features such as selection status, text color, and font size. This complexity arises from how computer memory is set up, which can store billions of numbers. At the most detailed level, a state depends on these numbers, making it astronomical. Most states won't do anything useful or will cause errors, but programs are written to avoid nonsense states. Modern computer programs are complex and impossible to test every possible state. This means that if a program enters an unusable state, recovery is difficult. Networked or Web-based applications can become stuck in strange states due to internet connectivity issues. When this happens, restarting the computer often resolves the issue. The best fix for a strange state is to turn it off and on again. This method works because most programs return to their default state when restarted, forgetting about previous states.

---

## A notional machine: files Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/qCl7Z/a-notional-machine-files)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A file is an abstraction of data on a hard disk that can be thought of as a single thing, even if it's just a collection of bits. The operating system presents files as a set of files sitting in a folder, making it easier to understand the data. Files can contain various types of data, such as words, pixels, or audio samples, and have associated metadata that is stored by the operating system. Metadata includes information about the file, such as its creation date and ownership.

The operating system uses metadata to determine which files are open and editable for a user. If two applications try to edit the same file simultaneously, the operating system locks the file to prevent data corruption. When an application opens a file, it sets locked metadata to indicate that the file is being edited. The application then copies the file into memory, resulting in two identical copies of the data: one on the hard disk and one in memory.

As the application edits the file, the copy in memory becomes different from the original on the hard disk. To prevent data loss, the application must save changes to the disk by opening the file again and locking it. The changes are then copied back to the hard disk, resulting in two identical copies of the data: one that has been modified in memory and another that remains unchanged.

If an application crashes while editing the file, the data will be lost unless a backup is saved to the disk. To prevent data loss, applications often check the time of the last modification of the file before making changes. This allows them to detect potential conflicts with other applications working on the same file.

Understanding how files work and their associated metadata can help users troubleshoot common problems and interact effectively with operating systems and applications.

---

## Modularity Video• . Duration: 2 minutes 2 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/sftXs/modularity)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Modularity is a fundamental concept in computer science based on abstraction, which allows complex systems to be understood and built by breaking them down into smaller, independent modules. Computer systems are composed of multiple components, such as CPU, memory, hard disks, and displays, which can be split into modules to improve manageability. Software development also employs modularity, where existing elements from operating systems, open-source software, or other developers are utilized to create complex software. A key example of a module is a hardware driver, which interacts with specific hardware components, such as printers or sound cards.

To simplify the development process, drivers are independent of applications and can interact with different hardware components in a consistent manner. This allows application developers to write code that interacts with drivers, while hardware developers only need to write one driver for each hardware component. The benefits of modularity include reduced work for software development and improved compatibility with new hardware releases.

Modularity is essential for understanding software, as it helps identify the individual modules that make up a piece of software. By analyzing these components, developers can improve their notional machine skills and better comprehend complex software systems. Understanding modularity also enables developers to debug and troubleshoot issues more effectively.

In addition to its benefits for software development, modularity is also important in understanding how applications interact with hardware components. The use of drivers and modules allows applications to access various hardware features without requiring customized code for each component. This enables applications to function consistently across different hardware platforms.

---

## Applications Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/dtzlA/applications)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The concept of an application is closely related to software that interacts with computers, smartphones, and tablets. Applications can be thought of as instructions or code that tell the CPU what actions to perform on data. The first computers had their programs wired into their hardware, but modern applications are much more complex. They consist of multiple files, including executable files that contain code, drivers that interact with hardware, libraries that provide standard software modules, and resource files that store data and preferences. Applications often use these libraries to access services like Dropbox or Twitter without having to write custom code. These libraries can be integrated into the application code as a single file or as separate dynamic libraries that interact with the main executable file. The user interface library is an example of a standard software module used by many applications to provide a consistent interface across different platforms. Applications also include resource files that contain data and text, such as language-dependent text in menus and icons. These resources are often stored in separate files that can be easily updated or customized without changing the application code. The executable code file is the core of an application, interacting with drivers, libraries, and resource files to perform its functions. Understanding these components is essential to understanding how applications work and how they interact with hardware and software services. Applications are complex systems that can be analyzed by looking at their individual files and components. By doing so, users can gain insights into the inner workings of an application and potentially debug or modify it. This knowledge is crucial for developing robust and efficient software that meets user needs.

Note: The original text is a transcript from a video lecture on computer science, specifically about applications and how they work. I've condensed the information into 15 sentences while preserving key concepts and technical details.

---

## Debugging Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/IUWJM/debugging)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

Debugging is a crucial skill for computer scientists to identify and fix errors in computer programs, known as "bugs." The term "bug" originated in the 1940s when Admiral Grace Hopper found a moth inside a computer. Debugging involves finding the cause of an error and fixing it, which can be challenging. To debug effectively, one must understand the system, look for clues without assumptions, and systematically change variables to isolate the problem.

The first step is to understand the system, including software and hardware components involved in printing a document. Next, look for error messages or signs of trouble from the word processor or printer. Check the print manager software for any error messages or explanations. If there are no error messages, try searching online for help.

To properly debug, change one variable at a time to see if it makes a difference. This can involve printing a different document, closing and reopening the word processor, or trying from another application. If the problem persists after these steps, try restarting the computer, printer, or even turning it off and on again. In some cases, reinstalling drivers may resolve the issue.

Remember to only change one variable at a time to avoid confusion and ensure accurate diagnosis. Another important step is to check the plug, as many errors can be caused by simple oversights like this. Debugging requires patience, persistence, and attention to detail. With practice and experience, anyone can develop this skill, even if not intending to become a computer scientist.

---

## Summary Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/8Jn9x/summary)

There is no text to summarize. The provided "VIDEO TRANSCRIPT" appears to be a table of contents or lesson plan, listing various components and durations for a computer science course. It does not contain any specific information or technical details.

If you could provide the actual text you'd like me to summarize, I would be happy to assist you in condensing it into 14 sentences while preserving key concepts, formulae, and technical details.

---

## Looking inside applications Reading• . Duration: 20 minutes 20 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/supplement/DTR7y/looking-inside-applications)

Here is a summary of the text in 15 sentences:

On a Mac, applications appear to be single files due to the operating system's design, but they are actually folders containing multiple files. To view the contents of an application, navigate to the Applications folder and right-click (or hold down Ctrl and click) on the application icon. Selecting 'Show Package Contents' will reveal all the files that make up the application. Windows is less secretive and allows users to view application folders without special action.

Applications are typically stored in the 'C:\Program Files' directory. This directory contains a folder for each installed application, which includes its executable file, resource files, and libraries (represented by .dll files). To examine the components of an application, look at the files within each application's folder. The files should include the executable (.exe) file, resources files, and libraries.

The Mac requires users to take steps to view the contents of an application, while Windows makes this information more accessible. Understanding how applications are structured can be helpful for debugging and troubleshooting issues. The concept of modularity is relevant here, as applications are composed of multiple components that work together.

---

## Modularity and applications – lecture summaries Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/supplement/ieHEN/modularity-and-applications-lecture-summaries)

This appears to be a large amount of unformatted text, likely from a educational or training platform. I'll do my best to summarize the main topics and provide some general guidance.

The text covers three main topics:

1. **Understanding Applications**: This section explains what applications are, their basic components (executable code, operating system services, libraries, and resource files), and how they interact with hardware and other software.
2. **Modularity in Software Development**: This section introduces the concept of modularity in software development, including breaking down complex systems into smaller, manageable modules, drivers as software that manage hardware interactions, and the importance of understanding these components to grasp how applications work.
3. **Notional Machine and Understanding Software**: This section emphasizes the importance of developing a good notional machine (i.e., understanding the fundamental concepts of software) to comprehend software better.

The text also provides checklists for mastery, which can be used to track progress and ensure understanding of each topic.

Some general guidance for those who may have encountered this text:

* **Take your time**: This text is dense and assumes a certain level of background knowledge in computer science. Take your time to review each section carefully.
* **Focus on the key concepts**: Identify the most important ideas and concepts presented in each section, and try to understand how they relate to one another.
* **Use analogies or examples**: Try to think of real-world examples or analogies that can help illustrate complex software concepts.
* **Practice coding or problem-solving**: Apply your newfound understanding by working on small projects or exercises that involve building applications or understanding software components.

If you have any specific questions about these topics, feel free to ask!

---

## Peer review rubric Reading• . Duration: 20 minutes 20 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/supplement/8WiRP/peer-review-rubric)

It appears that you have provided a rubric for assessing the quality of student responses in a computer science course. The rubric has four criteria:

1. **The work describes computer science concepts for this week**
	* No: The response does not describe the relevant concepts.
	* Yes, but: The response contains some mistakes or unclear points.
	* Yes: The response accurately describes the relevant concepts.
	* Yes, and: The response also includes new ideas or perspectives not taught in class.
	* Wow!: The response exceeds expectations by providing a deep understanding of the concepts beyond what was taught in class.
2. **The work illustrates these ideas with an example**
	* No: The response does not provide an example to illustrate the concepts.
	* Yes, but: The response contains some mistakes or unclear points in the example.
	* Yes: The response provides a clear and accurate example that illustrates the concepts.
	* Yes, and: The response also includes new ideas or perspectives not taught in class through the example.
	* Wow!: The response exceeds expectations by providing an innovative and insightful example that goes beyond what was taught in class.
3. **The work explains how the computer system works**
	* No: The response does not explain how the computer system works.
	* Yes, but: The response contains some mistakes or unclear points in the explanation.
	* Yes: The response provides a clear and accurate explanation of how the computer system works.
	* Yes, and: The response also includes new ideas or perspectives not taught in class through the explanation.
	* Wow!: The response exceeds expectations by providing a detailed and insightful explanation that goes beyond what was taught in class.
4. **The work predicts how different technical choices or situations would affect a system**
	* No: The response does not make predictions about how different technical choices or situations would affect a system.
	* Yes, but: The response contains some mistakes or unclear points in the prediction.
	* Yes: The response provides a clear and accurate prediction of how different technical choices or situations would affect a system.
	* Yes, and: The response also includes new ideas or perspectives not taught in class through the prediction.
	* Wow!: The response exceeds expectations by providing a detailed and insightful prediction that goes beyond what was taught in class.

Overall, this rubric provides a clear and structured framework for assessing student responses, with four levels of evaluation (No, Yes, Yes, and Wow!) to help instructors gauge the quality of student work.

---

