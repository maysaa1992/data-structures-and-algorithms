import unittest

# Import the left_join function from your module
from hashmap_left_join.hashmap_left_join import HashTable,left_join

class TestLeftJoin(unittest.TestCase):
    def test_left_join_basic(self):
        hashtable1 = HashTable()
        hashtable1.set('happy', 'joyful')
        hashtable1.set('sad', 'unhappy')
        hashtable1.set('big', 'large')
        hashtable1.set('small', 'tiny')

        hashtable2 = HashTable()
        hashtable2.set('happy', 'unhappy')
        hashtable2.set('small', 'big')
        hashtable2.set('big', 'small')

        result = left_join(hashtable1, hashtable2)

        # Assert the result
        expected_result = [
            ['happy', 'joyful', 'unhappy'],
            ['sad', 'unhappy', None],
            ['big', 'large', 'small'],
            ['small', 'tiny', 'big']
        ]
        self.assertEqual(result, expected_result)

    def test_left_join_empty_hashtable2(self):
        hashtable1 = HashTable()
        hashtable1.set('happy', 'joyful')
        hashtable1.set('sad', 'unhappy')
        hashtable1.set('big', 'large')
        hashtable1.set('small', 'tiny')

        hashtable2 = HashTable()

        result = left_join(hashtable1, hashtable2)

        # Assert the result when hashtable2 is empty
        expected_result = [
            ['happy', 'joyful', None],
            ['sad', 'unhappy', None],
            ['big', 'large', None],
            ['small', 'tiny', None]
        ]
        self.assertEqual(result, expected_result)

    def test_left_join_empty_hashtable1(self):
        hashtable1 = HashTable()

        hashtable2 = HashTable()
        hashtable2.set('happy', 'unhappy')
        hashtable2.set('small', 'big')
        hashtable2.set('big', 'small')

        result = left_join(hashtable1, hashtable2)

        # Assert the result when hashtable1 is empty
        expected_result = []
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
