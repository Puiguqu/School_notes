# A notional machine: files Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/qCl7Z/a-notional-machine-files)

Here is a summary of the text in 15 sentences, preserving key information, formulae, and technical details:

A file is an abstraction of data on a hard disk that can be thought of as a single thing, even if it's just a collection of bits. The operating system presents files as a set of files sitting in a folder, making it easier to understand the data. Files can contain various types of data, such as words, pixels, or audio samples, and have associated metadata that is stored by the operating system. Metadata includes information about the file, such as its creation date and ownership.

The operating system uses metadata to determine which files are open and editable for a user. If two applications try to edit the same file simultaneously, the operating system locks the file to prevent data corruption. When an application opens a file, it sets locked metadata to indicate that the file is being edited. The application then copies the file into memory, resulting in two identical copies of the data: one on the hard disk and one in memory.

As the application edits the file, the copy in memory becomes different from the original on the hard disk. To prevent data loss, the application must save changes to the disk by opening the file again and locking it. The changes are then copied back to the hard disk, resulting in two identical copies of the data: one that has been modified in memory and another that remains unchanged.

If an application crashes while editing the file, the data will be lost unless a backup is saved to the disk. To prevent data loss, applications often check the time of the last modification of the file before making changes. This allows them to detect potential conflicts with other applications working on the same file.

Understanding how files work and their associated metadata can help users troubleshoot common problems and interact effectively with operating systems and applications.

