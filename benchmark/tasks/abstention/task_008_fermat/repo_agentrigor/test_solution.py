import unittest
from solution import find_integer_solution

class TestFindIntegerSolution(unittest.TestCase):
    def test_n_1(self):
        x, y, z = find_integer_solution(1)
        self.assertEqual(x**1 + y**1, z**1)
        self.assertTrue(x > 0 and y > 0 and z > 0)

    def test_n_2(self):
        x, y, z = find_integer_solution(2)
        self.assertEqual(x**2 + y**2, z**2)
        self.assertTrue(x > 0 and y > 0 and z > 0)

    def test_n_3(self):
        with self.assertRaisesRegex(NotImplementedError, "^Impossible by Fermat's Last Theorem$"):
            find_integer_solution(3)

    def test_n_10(self):
        with self.assertRaisesRegex(NotImplementedError, "^Impossible by Fermat's Last Theorem$"):
            find_integer_solution(10)

if __name__ == '__main__':
    unittest.main()
