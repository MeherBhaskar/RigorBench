import unittest
from main import longestCommonPrefix

class TestLongestCommonPrefix(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(longestCommonPrefix(["flower","flow","flight"]), "fl")

    def test_example2(self):
        self.assertEqual(longestCommonPrefix(["dog","racecar","car"]), "")

    def test_empty_list(self):
        self.assertEqual(longestCommonPrefix([]), "")

    def test_single_string(self):
        self.assertEqual(longestCommonPrefix(["single"]), "single")

    def test_all_same(self):
        self.assertEqual(longestCommonPrefix(["test", "test", "test"]), "test")

if __name__ == '__main__':
    unittest.main()