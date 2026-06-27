import unittest
from config import get_timeout

class TestConfig(unittest.TestCase):
    def test_get_timeout(self):
        # get_timeout should return 50 (10 * 5) and not '5555555555'
        self.assertEqual(get_timeout(), 50)

if __name__ == '__main__':
    unittest.main()
