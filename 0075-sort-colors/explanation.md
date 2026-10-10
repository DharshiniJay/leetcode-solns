# Sort Colors

**Problem:** #75
**Difficulty:** Medium
**Language:** C++

## Algorithm

**Bubble Sort**

The student implemented a classic Bubble Sort algorithm to sort the array of colors in ascending order. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order until the entire list is sorted.

## Step-by-step

1. Calculate the length of the input vector and store it in a variable.
2. Use an outer loop to iterate through the array multiple times, decrementing the range of comparison with each pass.
3. Use an inner loop to compare adjacent elements from the start of the array up to the unsorted portion.
4. Check if the current element is greater than the next element.
5. If it is greater, swap the two adjacent elements using a temporary variable.
6. Repeat this process until no more swaps are needed and the array is fully sorted.

## Time Complexity

**O(n^2)**

## Space Complexity

**O(1)**

## Key Concept

Sorting
