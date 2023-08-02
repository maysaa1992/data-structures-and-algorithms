class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)
class Hashtable:
    def __init__(self):
        self.map = {}

    def insert(self, key):
        self.map[key] = True

    def contains(self, key):
        return key in self.map
    
    

def tree_intersection(tree_1,tree_2):
    
    '''        
    Find the common values in two binary trees using a Hashtable.

        This function takes two binary trees as input and returns a list of values that are common in both trees.

        Parameters:
            tree_1 (BinaryTree): The first binary tree.
            tree_2 (BinaryTree): The second binary tree.

        Returns:
            list: A list containing the values that are present in both `tree_1` and `tree_2`.
    '''
   
    
    common = []
    binary_tree1 = tree_1.pre_order()
    binary_tree2 = tree_2.pre_order()
    hashtable = Hashtable()
    for value in binary_tree1:
        hashtable.set(key=str(value), value=value)
    for value in binary_tree2:
        if hashtable.has(str(value)):
            common.append(value)
    return common