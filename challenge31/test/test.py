import unittest
from hashmap_repeated_word.hashmap_repeated_word import repeated_word

class TestRepeatedWord(unittest.TestCase):
    def test_repeated_word_found(self):
        input_string = "This is a sample string with repeated words like is and a and sample."
        self.assertEqual(repeated_word(input_string), "is")

    def test_repeated_word_not_found(self):
        input_string = "This is a test string with no repeated words."
        self.assertIsNone(repeated_word(input_string))

    def test_repeated_word_case_insensitive(self):
        input_string = "Testing testing ONE two Three three tHrEe."
        self.assertEqual(repeated_word(input_string), "testing")

    def test_repeated_word_empty_string(self):
        input_string = ""
        self.assertIsNone(repeated_word(input_string))

    def test_repeated_word_single_word(self):
        input_string = "Hello"
        self.assertIsNone(repeated_word(input_string))

    def test_repeated_word_large_string(self):
        import random
        import string

        # Generate a large random string
        input_string = ''.join(random.choices(string.ascii_lowercase + ' ', k=10**6))

        # Make sure no word is repeated
        self.assertIsNone(repeated_word(input_string))

if __name__ == "__main__":
    unittest.main()