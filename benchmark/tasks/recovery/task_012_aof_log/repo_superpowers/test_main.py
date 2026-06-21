import unittest
from main import recover_data

class TestRecovery(unittest.TestCase):
    def test_clean_log(self):
        log = [
            "SET user_1 Alice",
            "SET user_2 Bob",
            "DEL user_1"
        ]
        expected = {"user_2": "Bob"}
        self.assertEqual(recover_data(log), expected)

    def test_corrupt_log(self):
        log = [
            "SET a 1",
            "CORRUPT LINE",
            "SET b 2",
            "SET c",
            "DEL a",
            "DEL d",
            "UNKNOWN a 1",
            "SET e 3 extra"
        ]
        expected = {"b": "2"}
        self.assertEqual(recover_data(log), expected)

    def test_empty_log(self):
        self.assertEqual(recover_data([]), {})

if __name__ == '__main__':
    unittest.main()
