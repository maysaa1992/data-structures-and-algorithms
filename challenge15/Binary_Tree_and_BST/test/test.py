import pytest

from Binary_Tree_and_BST.Binary_Tree_and_BST import BinarySearchTree
from Binary_Tree_and_BST.Binary_Tree_and_BST import Tnode
from Binary_Tree_and_BST.Binary_Tree_and_BST import Search_Tree



def test_instantiate_empty_tree():
        tree = BinarySearchTree()
        actual=tree.root
        expected=None
        assert actual == expected

def test_instantiate_tree_with_single_root_node():
        tree = BinarySearchTree()
        tree.root= Tnode(10)
        actual_root=tree.root.value
        expected_root=10
        actual_left=None
        expected_left=None
        actual_right=None
        expected_right=None
        assert actual_root == expected_root
        assert actual_left==expected_left
        assert actual_right==expected_right      

# def test_add_left_child_and_right_child_to_node():
#         tree = Search_Tree()
#         actual= tree.Add(70)
#         expected="add to left"
#         assert actual==expected
            

def test_return_collection_from_pre_order_traversal():
        tree = BinarySearchTree()
        tree.root= Tnode(10)
        tree.root.left=Tnode(20)
        tree.root.right = Tnode(50)
        tree.root.left.left = Tnode(30)
        tree.root.left.right = Tnode(40)
        tree.root.right.left = Tnode(60)
        Tnode(20).left=Tnode(30)
        actual=tree.pre_order()
        expected=[10,20,30,40,50,60]
        assert actual==expected
        

    
def test_return_collection_from_in_order_traversal():
        tree = BinarySearchTree()
        tree.root= Tnode(10)
        tree.root.left=Tnode(20)
        tree.root.right = Tnode(50)
        tree.root.left.left = Tnode(30)
        tree.root.left.right = Tnode(40)
        tree.root.right.left = Tnode(60)
        Tnode(20).left=Tnode(30)
        actual=tree.in_order()
        expected=[30, 20, 40, 10, 60, 50]
        assert actual==expected

def test_return_collection_from_post_order_traversal():
        tree = BinarySearchTree()
        tree.root= Tnode(10)
        tree.root.left=Tnode(20)
        tree.root.right = Tnode(50)
        tree.root.left.left = Tnode(30)
        tree.root.left.right = Tnode(40)
        tree.root.right.left = Tnode(60)
        Tnode(20).left=Tnode(30)
        actual=tree.post_order()
        expected=[30, 40, 20, 60, 50, 10]
        assert actual==expected
