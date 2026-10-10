# Reverse Integer

**Problem:** #7
**Difficulty:** Medium
**Language:** Python

## Algorithm

**Mathematical Digit Extraction and Reversal**

The student implemented a mathematical approach to reverse the digits of an integer. First, it checks if the number is negative, setting a flag and converting it to positive. Then, it uses a while loop with modulo and integer division to extract the last digit of the number, add it to the reversed number (shifted by multiplying by 10), and reduce the original number until it becomes zero. Finally, it checks for 32-bit integer overflow limits, applies the negative sign if necessary, and returns the result.

## Step-by-step

1. Initialize two variables rev to 0 and flag to 0.
2. Check if the input x is less than 0. If it is, set flag to 1 and make x positive.
3. Enter a while loop that continues as long as x is not equal to 0.
4. Inside the loop, multiply rev by 10 and add the last digit of x using the modulo operator (x % 10).
5. Update x by performing integer division by 10 (x // 10).
6. After the loop finishes, check if the flag is 1. If so, negate the rev value and check if it fits within the 32-bit signed integer range.
7. Check if rev exceeds the 32-bit signed integer limits (2^31 - 1 or -2^31). If it overflows, return 0.
8. Return the final reversed integer.

## Time Complexity

**O(log10(x))**

## Space Complexity

**O(1)**

## Key Concept

Math and Arithmetic Operations
