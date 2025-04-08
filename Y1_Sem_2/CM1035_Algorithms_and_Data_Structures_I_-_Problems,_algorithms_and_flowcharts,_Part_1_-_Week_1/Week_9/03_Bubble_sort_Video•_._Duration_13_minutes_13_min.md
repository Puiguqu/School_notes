# Bubble sort Video• . Duration: 13 minutes 13 min

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

