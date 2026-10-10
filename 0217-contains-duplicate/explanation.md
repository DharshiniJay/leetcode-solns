# Contains Duplicate

**Problem:** #217
**Difficulty:** Easy
**Language:** Python

## Algorithm

**Set Length Comparison**

The student checks if there are any duplicate numbers in the list by comparing the total count of elements in the original list with the count of elements after converting the list into a set. Since a set only keeps unique values, a smaller set size means duplicates were removed.

## Step-by-step

1. Calculate the total number of elements in the input list nums and store it in variable a.
2. Convert the input list nums into a set to remove all duplicate values, then calculate its size and store it in variable b.
3. Compare the two sizes: if a is not equal to b, it means duplicates existed, so return True.
4. If a is equal to b, all elements were already unique, so return False.

## Time Complexity

**O(n)**

## Space Complexity

**O(n)**

## Key Concept

Hash Set
