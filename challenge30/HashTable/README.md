# challenge30 : Hash Table

data structure that store key-value pairs of data using buckets to increace data accessing efficiency

### Author : LeeNa Alzaben & Maysa'a Al-bataineh


## Approach & Efficiency
* time complexity 


the time complexity of the set, get, and has methods is O(1) on average (amortized), but it can be up to O(n) in the worst case due to collisions. The time complexity of the keys method is O(1) because it returns the self.key_list, which is a simple list operation with constant time complexity. 


* space complexity
the space complexity of the HashTable class is O(n + size), where n is the number of unique keys stored, and size is the number of buckets used. The other classes, Node and LinkedList, have constant space complexity and do not significantly contribute to the overall space complexity of the entire implementation.

## Solution
pytest test.py