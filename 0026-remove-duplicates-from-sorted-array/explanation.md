# Remove Duplicates from Sorted Array

**Problem:** #26
**Difficulty:** Easy
**Language:** Python

## Algorithm

**Two-Pointer Technique**

The student implemented the two-pointer technique to remove duplicates from a sorted array in-place. One pointer (j) scans through the array to find unique elements, while the other pointer (i) keeps track of the position where the next unique element should be placed.

## Step-by-step

1. Check if the input list nums is empty. If it is, return 0 immediately.
2. Initialize a pointer i to 0, which points to the last known unique element.
3. Loop through the array starting from the second element using a pointer j from index 1 to the end of the array.
4. Compare the element at nums[j] with the element at nums[i].
5. If they are not equal, it means a new unique element has been found. Increment i by 1.
6. Update nums[i] with the value of nums[j] to shift unique elements to the front of the array.
7. After the loop finishes, return i + 1, which represents the total count of unique elements.

## Time Complexity

**O(n)**

## Space Complexity

**O(1)**

## Key Concept

Two Pointers
