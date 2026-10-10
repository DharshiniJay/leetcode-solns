# Palindrome Number

**Problem:** #9
**Difficulty:** Easy
**Language:** Python

## Algorithm

**String Reversal Comparison**

The student converts the given integer into a string, creates a reversed copy of that string using Python's slicing feature, and then compares the original string to the reversed one. If they are equal, the number is a palindrome and the function returns True; otherwise, it returns False.

## Step-by-step

1. Convert the integer x to its string representation and store it in variable s.
2. Reverse the string s using Python slicing [::-1] and store the result in variable a.
3. Compare the original string s with the reversed string a.
4. If s equals a, return True.
5. Otherwise, return False.

## Time Complexity

**O(N) where N is the number of digits in the integer, because converting the integer to a string and reversing it both take time proportional to the length of the string.**

## Space Complexity

**O(N) where N is the number of digits in the integer, because storing both the original string and the reversed string requires memory proportional to the number of digits.**

## Key Concept

Strings
