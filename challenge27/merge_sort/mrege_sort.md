Challenge Title
Code Challenge no.27: Merge Sort
Whiteboard Process
Merge Sort

Approach & Efficiency
Start with divided the array to left and right side.
Call Recursively merge_sort(left) && merge_sort(right).
Then do merge_sort(L,R)
When the length of the array is greater than 1 go inside
To divide the array to left and right left = [8] and right = [4].
And Call again do mearge to have the last merge sorted array. Time complexity: O(n^2) Space Complixity :O(n1)
Solution
To run the code, you have to pass an array and a value to be inserted:

Test code: pytest tests/test_merge_sort.py
Run code: python3 merge_Sort.merge_sort.py