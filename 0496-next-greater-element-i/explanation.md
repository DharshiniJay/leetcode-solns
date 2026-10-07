# Next Greater Element I

**Problem:** #496
**Difficulty:** Easy
**Language:** C++

## Algorithm

**Brute Force Search**

The student implemented a straightforward brute force approach by iterating through each element in nums1 and searching for its matching position in nums2. Once the element is found in nums2, the code scans all subsequent elements to the right to find the first element that is strictly greater. If a greater element is found, it is added to the result vector; otherwise, -1 is added.

## Step-by-step

1. Initialize an empty result vector b to store the answers.
2. Loop through each element of nums1 using an outer loop with index k.
3. Set a boolean flag found to false for the current element in nums1.
4. Loop through each element of nums2 using a middle loop with index i to find where nums1[k] matches nums2[i].
5. Once the match is found, start an inner loop with index j from i + 1 to the end of nums2.
6. Check if nums2[j] is greater than nums2[i]. If it is, push nums2[j] into vector b, set found to true, and break out of the inner loop.
7. After checking all elements to the right, if found remains false, push -1 into vector b.
8. Return the completed vector b after processing all elements in nums1.

## Time Complexity

**O(M * N) where M is the size of nums1 and N is the size of nums2, due to the nested loops searching through nums2 for each element in nums1.**

## Space Complexity

**O(1) auxiliary space, excluding the space required for the output vector b.**

## Key Concept

Array traversal and nested iteration
