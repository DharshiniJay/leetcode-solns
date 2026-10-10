# Number of 1 Bits

**Problem:** #191
**Difficulty:** Easy
**Language:** Python

## Algorithm

**String Conversion and Iteration**

The student converts the given integer into its binary string representation using Python's format function. Then, they iterate through each character of the binary string, count how many characters are equal to '1', and return the final count.

## Step-by-step

1. Convert the integer n to its binary string representation using format(n, 'b').
2. Initialize a counter variable l to 0.
3. Loop through each character i in the binary string.
4. Check if the character i is equal to '1'.
5. If it is, increment the counter l by 1.
6. After the loop finishes, return the total count stored in l.

## Time Complexity

**O(log n)**

## Space Complexity

**O(log n)**

## Key Concept

Bit manipulation via string conversion
