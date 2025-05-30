# Mobile payments Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/lecture/rRGZg/mobile-payments)

Here is a summary of the text in 15 sentences, preserving key information and technical details:

A computer system needs to handle money processes, which has become increasingly important with digital services and mobile payments. Kenya's M-Pesa system was a pioneering example of mobile payments, allowing users to add and transfer funds using their mobile phones. The system works by sending requests to the M-Pesa servers, where databases record user accounts and balances. A program looks up the balance, adds the transferred amount, and updates the database with a new number.

The servers need to handle many transactions simultaneously, which is achieved through processes. However, if multiple requests are made to the same account, the previous transaction's result may be overwritten, leading to errors. This is where semaphores come in - they ensure that only one process can write to an account at a time, preventing overwrites.

The use of semaphores is crucial in financial systems, such as bank accounts and databases, to prevent simultaneous access without the risk of data loss. The scenario described illustrates the problem of lost transactions due to concurrent access. In practice, concurrency problems like this are common in computer systems that handle multiple requests simultaneously. Mobile payments, such as those made through M-Pesa, rely on the coordination of processes and semaphores to ensure accurate transactions.

The system's architecture is designed to handle millions of users and thousands of transactions daily, with servers creating new processes for each request. The use of semaphores allows the system to manage concurrent access to user accounts and prevent data corruption. The importance of semaphores in financial systems cannot be overstated, as they enable the creation of secure and reliable payment processing systems.

Overall, the use of semaphores and concurrency control mechanisms is essential for ensuring the accuracy and reliability of financial transactions, particularly in systems that handle multiple requests simultaneously.

