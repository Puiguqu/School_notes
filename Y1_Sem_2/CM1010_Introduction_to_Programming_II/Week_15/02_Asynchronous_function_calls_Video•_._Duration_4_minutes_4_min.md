# Asynchronous function calls Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/MJ687/asynchronous-function-calls)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

Asynchronous function calls in JavaScript allow for non-blocking execution, where the program continues running while waiting for an operation to complete. In synchronous functions, each line of code runs sequentially, pausing until the internal code is executed. Asynchronous functions, on the other hand, allow concurrent execution, enabling other tasks to be performed during the wait period. The `billowed sound` function is an example of an asynchronous function call in P5.js. When loading a sound in the `preload` function, the program continues executing while waiting for the load operation to complete. This can lead to issues, such as undefined values for properties accessed before the load operation is finished, as seen in the provided code example. To resolve this issue, developers can use callbacks or other synchronization mechanisms, as demonstrated by setting a variable equal to `sample.duration` when pressing a key to play the sound. Asynchronous programming allows for more efficient use of processing power, reducing delays and improving overall performance.

