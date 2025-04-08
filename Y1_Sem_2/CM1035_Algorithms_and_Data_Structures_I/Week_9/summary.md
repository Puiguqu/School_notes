# Week 9 - CM1035 Algorithms and Data Structures I - Problems, algorithms and flowcharts, Part 1 - Week 1

## Solution to the Lottery Problem Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/SSDZj/solution-to-the-lottery-problem)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The module "Algorithms and Data Structures Part 1" focuses on sorting algorithms, which can make searching data more efficient. To solve a problem where determining the winner of a lottery based on unique birthdays is required, a linear search algorithm is applied to every other element in a vector containing player numbers and birthdays. The approach involves counting the appearances of each birthday number using a dynamic array to store their counts. A pseudocode function "FindBirthdays(v)" is described, where v is the input vector, which initializes an empty dynamic array and then applies a linear search starting from the second element (i=2) up to the length of the vector. The outer while loop iterates over each element in the vector, and an inner while loop checks if the birthday number appears elsewhere in the vector by comparing it with other elements. If a unique birthday is found, its count is increased by 1, and if the count equals 1, the birthday is recorded in the dynamic array. The dynamic array stores all birthdays that appear only once as input to the function. This approach ensures that the function can efficiently identify unique birthdays from a large dataset.

Note: I didn't include any formulae, links, or technical details not essential to understanding the main concepts and algorithm.

---

## Introduction to Topic 5 Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/CAyNt/introduction-to-topic-5)

Here is a summary of the text in 8 sentences, preserving key information:

The problem at hand involves sorting a data structure and finding the sorted version with the same values but in ascending numerical order. To solve this, algorithms like bubble sort and insertion sort can be used to sort data. The solution presented incorporates elements from linear search, vectors, and dynamic arrays. Sorting data simplifies the process of searching for unique entries by reducing the need to scan the entire vector. One such scenario is sorting lottery tickets in date order, allowing for efficient comparison of birthdays. The general structure of the problem involves transforming an input data structure into another with the same values but sorted according to a specific order. Two algorithms to be covered are bubble sort and insertion sort, which will provide practical code examples using JavaScript. These algorithms can be used to solve various sorting-related problems, making them essential tools in computer science.

---

## Bubble sort Video• . Duration: 13 minutes 13 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/0K8II/bubble-sort)

I can provide a detailed explanation of the bubble sort algorithm and its implementation on vectors, dynamic arrays, and arrays.

**Bubble Sort Algorithm**

The bubble sort algorithm is a simple sorting algorithm that works by repeatedly iterating through a list of elements, comparing each pair of adjacent elements and swapping them if they are in the wrong order. The process continues until no more swaps are needed, indicating that the list is sorted.

Here's a step-by-step explanation of the bubble sort algorithm:

1. Start with the first element of the list.
2. Compare it with the next element.
3. If the current element is greater than the next element, swap them.
4. Move to the next element and repeat steps 2-3 until you reach the end of the list.
5. Repeat steps 1-4 for each pass through the list until no more swaps are needed.

**Implementation on Vectors**

To implement bubble sort on a vector, we can use the following code:
```cpp
void bubbleSort(vector<int>& vec) {
    int n = vec.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (vec[j] > vec[j + 1]) {
                swap(vec[j], vec[j + 1]);
            }
        }
    }
}
```
This implementation uses two nested loops to iterate through the vector. The outer loop iterates `n-1` times, and the inner loop iterates `n-i-1` times. If an element is greater than the next element, we swap them.

**Implementation on Dynamic Arrays**

To implement bubble sort on a dynamic array, we can use the following code:
```cpp
void bubbleSort(dynamicArray<int>& arr) {
    int n = arr.length();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}
```
This implementation is similar to the vector implementation, but we use the `length()` function to get the size of the dynamic array.

**Implementation on Arrays**

To implement bubble sort on an array, we can use the following code:
```cpp
void bubbleSort(array<int>& arr) {
    int n = arr.length;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}
```
This implementation is similar to the vector and dynamic array implementations, but we use the `length` function to get the size of the array.

**Applying Bubble Sort on a Stack**

To apply bubble sort on a stack using only other stacks, we can use the following approach:

1. Create a new stack and push all the elements from the original stack onto it.
2. Pop one element from the original stack and push it onto the new stack.
3. Compare the top two elements of the new stack and swap them if they are in the wrong order.
4. Repeat steps 2-3 until there is only one element left in the new stack.
5. Push the remaining element onto the new stack, which now contains the sorted elements.

This approach requires three stacks: an original stack, a temporary stack for swapping elements, and a final stack to store the sorted elements.

Here's some sample code in C++:
```cpp
void bubbleSortStack(Stack<int>& stack) {
    Stack<int> temp;
    while (!stack.isEmpty()) {
        int element = stack.pop();
        temp.push(element);
        if (!temp.isEmpty() && temp.peek() > element) {
            int swappedElement = temp.pop();
            temp.push(element);
            temp.push(swappedElement);
        }
    }
    while (!temp.isEmpty()) {
        stack.push(temp.pop());
    }
}
```
This implementation uses a temporary stack to swap elements and push them onto the final stack. Note that this approach requires extra memory to store the temporary stack, which may not be efficient for large inputs.

I hope this explanation helps! Let me know if you have any questions or need further clarification.

---

## Bubble sort on a stack Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/TLCUo/bubble-sort-on-a-stack)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The bubble sort algorithm can be modified to sort a stack instead of a vector by using two stacks. The process involves comparing the tops of the two stacks, swapping them if necessary, and repeating this process until the largest element is at the top of the first stack. This process requires n-1 passes for a stack of length n. After each pass, the second stack is pushed onto the first stack, effectively reversing the order of the elements in the first stack. The algorithm then repeats from the beginning, pushing new elements onto the stacks and comparing them until the stack is sorted. The modified bubble sort algorithm on a stack can be used to solve a problem where images need to be sorted based on certain properties such as color, material, or name. To apply this algorithm to sorting images, each image would be represented as a piece of data in an element of a vector, and the algorithm would compare and swap them accordingly. The modified bubble sort algorithm has been implemented in a video, which can be accessed for further learning.

---

## Insertion sort Video• . Duration: 8 minutes 8 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/qyL1L/insertion-sort)

The insertion sort algorithm is a simple and efficient sorting technique that works by iterating through an array or vector one element at a time, inserting each element into its proper position within the sorted portion of the array. The algorithm compares each element to all previous elements and shifts them forward until it finds the correct position for the new element.

The key concept behind insertion sort is that once an element has been inserted into its correct position, all subsequent elements in the array will be sorted without further comparisons. This property allows the algorithm to terminate early when no more swaps are needed, making it less efficient than bubble sort in some cases.

The pseudocode for insertion sort can be summarized as follows:

1. Start at the second element of the array.
2. Compare each element with all previous elements and shift them forward until it finds the correct position for the new element.
3. Repeat step 2 until the end of the array is reached.

In terms of its implementation, insertion sort can be easily adapted to work on arrays, vectors, or dynamic arrays. The main difference between these implementations is the way in which elements are accessed and manipulated.

The algorithm's time complexity is O(n^2) in the worst case, although it can be improved to O(n) in the best case when the input array is already sorted.

Insertion sort has several advantages over bubble sort, including:

* It does not require any additional space for an auxiliary array.
* It only requires a single pass through the data, whereas bubble sort may require multiple passes.
* It is generally faster than bubble sort for nearly-sorted or partially-sorted data.

However, insertion sort also has some disadvantages, such as:

* It can be slower than bubble sort for very large datasets due to its overhead in shifting elements.
* It requires more memory accesses than bubble sort in some cases.

Overall, insertion sort is a simple and efficient sorting algorithm that is well-suited for many applications, particularly those with relatively small datasets.

---

## Response to discussion points Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/OrksV/response-to-discussion-points)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The insertion sort algorithm can be implemented in arrays, vectors, and dynamic arrays. The array implementation involves starting at the second element (index 2) and comparing it to the elements before it, shifting them if necessary. A similar approach can be used for stack-based sorting using two stacks, where values are transferred between the stacks based on comparison. However, insertion sort can require fewer operations in its implementation than bubble sort when dealing with vectors that are mostly sorted. In the case of a vector of length five, the insertion sort requires approximately 17 operations (seven reads and ten writes), whereas bubble sort would require around 49 operations (forty-nine reads and forty-eight writes). This advantage is due to the fact that insertion sort only needs to make comparisons for elements that are not in their correct position. In contrast, bubble sort requires making comparisons for all elements during each pass. Overall, the insertion sort has an edge over bubble sort when dealing with vectors that are nearly sorted.

I did not include formulae, links, or technical details as they were not explicitly mentioned in the provided text.

---

