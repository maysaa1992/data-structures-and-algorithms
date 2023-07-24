import unittest
from hashmap_repeated_word.hashmap_repeated_word import repeated_word


class TestRepeatedWord(unittest.TestCase):

    def test_repeated_word_exists(self):
        input_string = "This is a sample string with repeated words like is and a and sample."
        result = repeated_word(input_string)
        self.assertEqual(result, "is", "Test failed: The first repeated word should be 'is'")

    def test_repeated_word_no_repeats(self):
        input_string = "This is a sample string without any repeated words."
        result = repeated_word(input_string)
        self.assertIsNone(result, "Test failed: No repeated word should be found.")


if __name__ == "__main__":
    unittest.main()