import unittest
from run_length_encoding import run_length_encode

class TestRunLengthEncode(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(run_length_encode(""), "")

    def test_single_character(self):
        self.assertEqual(run_length_encode("A"), "1A")

    def test_all_same_characters(self):
        self.assertEqual(run_length_encode("AAAAA"), "5A")

    def test_all_different_characters(self):
        self.assertEqual(run_length_encode("ABCDE"), "1A1B1C1D1E")

    def test_mixed_characters(self):
        self.assertEqual(run_length_encode("AABBCCCA"), "2A2B3C1A")

if __name__ == '__main__':
    unittest.main()
