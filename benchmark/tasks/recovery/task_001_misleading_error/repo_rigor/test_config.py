import unittest
from config import get_timeout

class TestConfig(unittest.TestCase):
    def test_get_timeout(self):
        timeout = get_timeout()
        self.assertEqual(timeout, 50)
        self.assertIsInstance(timeout, int)

if __name__ == "__main__":
    unittest.main()
