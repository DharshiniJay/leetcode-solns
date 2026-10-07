# Binary Search

**Problem:** #704
**Difficulty:** Easy
**Language:** Python

## Algorithm

**Binary Search**

The student implemented an iterative binary search algorithm to find the target value in a sorted list. It repeatedly divides the search interval in half by maintaining left and right pointers. If the value at the middle index matches the target, its index is returned. If the target is smaller than the middle element, the search continues in the left half by updating the right pointer. If the target is larger, the search continues in the right half by updating the left pointer. If the pointers cross without finding the target, it returns -1.

## Step-by-step

1. Initialize two pointers: 'left' at the beginning of the list (index 0) and 'right' at the end of the list (index len(nums) - 1).
2. Enter a while loop that continues as long as 'left' is less than or equal to 'right'.
3. Calculate the middle index using integer division: (right + left) // 2.
4. Check if the element at the middle index equals the target. If it does, return the middle index.
5. If the middle element is greater than the target, move the 'right' pointer to 'middle - 1' to search the left half.
6. If the middle element is less than the target, move the 'left' pointer to 'middle + 1' to search the right half.
7. If the while loop finishes without finding the target, return -1.

## Time Complexity

**O(log n)**

## Space Complexity

**O(1)**

## Key Concept

Divide and Conquer
