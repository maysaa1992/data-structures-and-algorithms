# Tree intersection
 function called tree_intersection that takes two binary trees as parameters.
Using Hashmap implementation, return a set of values found in both trees.
## Whiteboard Process
<!-- Embedded whiteboard image -->
![intersection_tree](/challenge32/intersection_tree.PNG)
## Approach & Efficiency
The overall space complexity is O(N1 + N2) because the binary_tree1, binary_tree2, and the hashtable use the most significant amount of space. The common list's space complexity can be up to O(min(N1, N2)), but it does not dominate the space complexity compared to the other data structures used in the code.
## Solution
pytest test.py