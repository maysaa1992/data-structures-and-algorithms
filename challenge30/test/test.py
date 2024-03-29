import unittest
from HashTable.hashtable  import HashTable


# Paste the code for Node, LinkedList, and HashTable classes here


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.hash_table = HashTable()

    def test_set_get(self):
        self.hash_table.set('name', 'John')
        self.assertEqual(self.hash_table.get('name'), 'John')

    def test_set_get_collision(self):
        # Add two keys with the same hash to test collision handling
        self.hash_table.set('abc', 'value1')
        self.hash_table.set('bca', 'value2')
        self.assertEqual(self.hash_table.get('abc'), 'value1')
        self.assertEqual(self.hash_table.get('bca'), 'value2')

    def test_set_nonexistent_key(self):
        # Retrieve a value for a key that doesn't exist
        self.assertIsNone(self.hash_table.get('nonexistent_key'))

    def test_unique_keys(self):
        self.hash_table.set('color', 'blue')
        self.hash_table.set('fruit', 'apple')
        self.hash_table.set('shape', 'circle')
        self.hash_table.set('size', 'large')

        keys = self.hash_table.keys()
        self.assertEqual(len(keys), 4)
        self.assertIn('color', keys)
        self.assertIn('fruit', keys)
        self.assertIn('shape', keys)
        self.assertIn('size', keys)

    def test_collision_handling(self):
        # A simple hash function where all keys have the same hash value (0)
        self.hash_table.set('abc', 'value1')
        self.hash_table.set('xyz', 'value2')
        self.assertEqual(self.hash_table.get('abc'), 'value1')
        self.assertEqual(self.hash_table.get('xyz'), 'value2')

    def test_retrieve_from_bucket_with_collision(self):
        self.hash_table.set('abc', 'value1')
        self.hash_table.set('bca', 'value2')
        self.assertEqual(self.hash_table.get('abc'), 'value1')
        self.assertEqual(self.hash_table.get('bca'), 'value2')

    def test_hash_in_range(self):
        # Test whether the hash function generates in-range values
        keys = ['hello', 'world', 'python', 'data', 'structure']
        for key in keys:
            hash_value = self.hash_table._HashTable__hash(key)
            self.assertLess(hash_value, self.hash_table._HashTable__size)
            self.assertGreaterEqual(hash_value, 0)

if __name__ == '__main__':
    unittest.main()