import unittest
from tree_intersection.tree_intersection import tree_intersection, BinaryTree

class TestTreeIntersection(unittest.TestCase):
    def test_tree_intersection_with_common_values(self):
        # Create two binary trees with common values
        tree1 = BinaryTree()
        tree1.insert(5)
        tree1.insert(3)
        tree1.insert(8)
        tree1.insert(2)
        tree1.insert(4)

        tree2 = BinaryTree()
        tree2.insert(8)
        tree2.insert(2)
        tree2.insert(9)
        tree2.insert(7)

        # Check the intersection of values
        result = tree_intersection(tree1, tree2)
        expected_result = {8, 2}
        self.assertEqual(set(result), expected_result)

    def test_tree_intersection_without_common_values(self):
        tree1 = BinaryTree()
        tree1.insert(5)
        tree1.insert(3)
        tree1.insert(8)

        tree2 = BinaryTree()
        tree2.insert(2)
        tree2.insert(9)
        tree2.insert(7)

        result = tree_intersection(tree1, tree2)
        expected_result = []
        self.assertEqual(set(result), set(expected_result))

    def test_tree_intersection_with_empty_trees(self):
        tree1 = BinaryTree()
        tree2 = BinaryTree()

        result = tree_intersection(tree1, tree2)
        expected_result = []
        self.assertEqual(set(result), set(expected_result))

if __name__ == '__main__':
    unittest.main()
