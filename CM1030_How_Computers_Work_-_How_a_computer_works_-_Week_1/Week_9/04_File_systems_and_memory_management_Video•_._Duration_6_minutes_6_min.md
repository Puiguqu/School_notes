# File systems and memory management Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/7MdG2/file-systems-and-memory-management)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

The operating system kernel provides fundamental services to applications, including managing device drivers. Device drivers allow applications to interact with hardware, such as printers, while providing a standard interface for all applications. The kernel manages drivers and interacts with them to communicate with the underlying hardware. One important function of the kernel is to provide an interface for mass storage devices, such as hard disks, and manage files and folders.

The file manager is responsible for storing and managing metadata associated with files, including dates and owners. Folders, also known as directories, contain files and can be nested to create a hierarchical structure. The kernel provides a standard interface for applications to access the file system, allowing them to organize and retrieve files efficiently. Another important function of the kernel is to manage memory allocation and deallocation for applications.

The kernel allocates memory addresses to applications when they start up, ensuring that each application has its own area of memory. The kernel also prevents one application from accessing the memory of another, preventing conflicts and potential security vulnerabilities. When memory becomes full, the kernel can move data from main memory to hard disk storage using a process called paging.

Paging involves copying chunks of memory, known as pages, to disk storage when they are not in use. This frees up space for other applications and allows the kernel to provide virtual memory, which is essentially disc space that acts like memory. The kernel's memory management function provides basic services that applications need over time, such as loading files and accessing memory.

