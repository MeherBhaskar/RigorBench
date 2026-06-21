import unittest
from config import get_timeout
from utils import calculate_timeout

class TestTimeout(unittest.TestCase):
    def test_get_timeout_returns_int(self):
        timeout = get_timeout()
        self.assertIsInstance(timeout, int)
        self.assertEqual(timeout, 50)

    def test_calculate_timeout(self):
        self.assertEqual(calculate_timeout(10, 5), 50)
        self.assertIsInstance(calculate_timeout(10, 5), int)

if __name__ == '__main__':
    unittest.main()
