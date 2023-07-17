## the step-by-step algorithm for the Insertion Sort:

* Start with the first element of the array and consider it as sorted.
* Iterate over the remaining elements of the array from left to right.
* For each element, compare it with the elements to its left (which are already sorted) until you find the correct position to insert it.
* Shift all the greater elements to the right by one position to make room for the current element.
* Insert the current element at its correct position in the sorted portion of the array.
* Repeat steps 2-5 until all elements are sorted.
## Visualization:
To visually understand how Insertion Sort works, let's consider an example input array [5, 2, 4, 6, 1, 3]:

* Initial Array: [5, 2, 4, 6, 1, 3]
* Start with the first element (5) and consider it as sorted: [5]
* Consider the second element (2) and insert it in its correct position in the sorted portion of the array: [2, 5]
* Consider the third element (4) and insert it in its correct position: [2, 4, 5]
* Consider the fourth element (6) and insert it in its correct position: [2, 4, 5, 6]
* Consider the fifth element (1) and insert it in its correct position: [1, 2, 4, 5, 6]
* Consider the sixth element (3) and insert it in its correct position: [1, 2, 3, 4, 5, 6]
```
Original Array: [5, 2, 4, 6, 1, 3]
Step 1: [5]                      (5 is already sorted)
Step 2: [2, 5]
Step 3: [2, 4, 5]
Step 4: [2, 4, 5, 6]
Step 5: [1, 2, 4, 5, 6]
Step 6: [1, 2, 3, 4, 5, 6]
```
## The  complexity
The time complexity of the Insertion Sort algorithm is O(n^2) in the worst and average case, and O(n) in the best case when the input array is already sorted. The space complexity is O(1) 