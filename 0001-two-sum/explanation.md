# Two Sum

**Problem:** #1
**Difficulty:** Easy
**Language:** C++

## Algorithm

**Brute Force**

The student implemented a simple brute force search to find two numbers in the array that add up to the target value. They check every possible pair of numbers using two nested loops.

## Step-by-step

1. Start a loop with index i from the beginning of the array to the end.
2. Start a nested loop with index j starting from i + 1 to the end of the array.
3. Check if the sum of the elements at index i and index j equals the target value.
4. If the sum matches the target, immediately return the indices {i, j}.
5. If no such pair is found after checking all combinations, return an empty array.

## Time Complexity

**O(n^2)**

## Space Complexity

**O(1)**

## Key Concept

Nested Loops
