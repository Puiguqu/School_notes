# Asynchronous function calls Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/MJ687/asynchronous-function-calls)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

In JavaScript, function calls can be divided into two categories: synchronous and asynchronous. Synchronous functions execute one after another, causing the code to pause while waiting for the previous function to complete. In contrast, asynchronous functions allow other activities to continue running concurrently with the execution of the function. The `billowed sound` function is an example of an asynchronous function call. When calling an asynchronous function in a preload or callback context, the main function continues executing without waiting for the asynchronous operation to complete. This can lead to issues when trying to access the result of the asynchronous function, such as setting a global variable equal to `sample.duration`. To resolve this issue, developers can use callbacks or other techniques to ensure that the asynchronous operation has completed before accessing its result. Asynchronous programming is useful for efficiently utilizing a computer's processing power and reducing "spinning wheels" in software.

