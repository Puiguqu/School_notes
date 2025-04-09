# Linear search algorithm Video• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-algorithms-and-data-structures-1/lecture/ihhPi/linear-search-algorithm)

I can help you with the problem. Here's a step-by-step solution:

## Step 1: Define the Problem
The problem is to search for a specific birthday within a given decimal expansion of pi, which is stored in a vector.

## Step 2: Understand the Algorithm
We need to implement a linear search algorithm to find the birthday within the pi decimal expansion. This involves iterating through each digit of the pi decimal expansion and comparing it with the corresponding digit of the birthday.

## Step 3: Initialize Variables
We need to initialize two vectors, one for the pi decimal expansion and another for the birthday. We also need to set a flag to indicate whether the birthday has been found.

## Step 4: Iterate Through Pi Decimal Expansion
We iterate through each digit of the pi decimal expansion using a loop, starting from the first digit (index 0).

## Step 5: Compare with Birthday
For each digit in the pi decimal expansion, we compare it with the corresponding digit of the birthday. If they match, we set the flag to true and break out of the loop.

## Step 6: Return Flag Value
After iterating through all digits, if the flag is still false, it means the birthday was not found, so we return a message indicating that the birthday is not in the pi decimal expansion.

## Step 7: Implement the Algorithm

Here's some sample code to implement the algorithm:
```
function searchBirthday(piDecimalExpansion, birthday) {
  let found = false;
  for (let i = 0; i < len(piDecimalExpansion); i++) {
    if (piDecimalExpansion[i] == birthday[i]) {
      found = true;
      break;
    }
  }
  return found ? "Found in pi decimal expansion" : "Not found in pi decimal expansion";
}
```
Note: This code assumes that the pi decimal expansion is stored in a vector of digits and the birthday is also stored in a vector of digits.

The final answer is: There is no specific numerical answer to this problem, as it involves implementing an algorithm. However, I can provide you with a sample solution in a programming language of your choice.

