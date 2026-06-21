import unittest
from config import get_timeout
from utils import calculate_timeout

class TestTimeout(unittest.TestCase):
    def test_calculate_timeout(self):
        self.assertEqual(calculate_timeout(10, 5), 50)
        
    def test_get_timeout(self):
        self.assertEqual(get_timeout(), 50)

if __name__ == "__main__":
    unittest.main()
