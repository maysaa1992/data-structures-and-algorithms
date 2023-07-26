from trees.trees import BinaryTree,TNode

class Hashtable:
    def __init__(self):
        self.map = {}

    def insert(self, key):
        self.map[key] = True

    def contains(self, key):
        return key in self.map
    
    

def tree_intersection(tree_1,tree_2):
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