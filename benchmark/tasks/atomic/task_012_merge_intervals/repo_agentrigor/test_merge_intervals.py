import unittest
from merge_intervals import merge_intervals

class TestMergeIntervals(unittest.TestCase):
    def test_example_1(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_example_2(self):
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_empty(self):
        intervals = []
        expected = []
        self.assertEqual(merge_intervals(intervals), expected)

    def test_single_interval(self):
        intervals = [[1, 5]]
        expected = [[1, 5]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_non_overlapping(self):
        intervals = [[1, 2], [3, 4], [5, 6]]
        expected = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_completely_overlapping(self):
        intervals = [[1, 10], [2, 6], [3, 4]]
        expected = [[1, 10]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_multiple_overlapping(self):
        intervals = [[1, 4], [2, 5], [7, 9], [8, 10], [11, 15], [12, 13]]
        expected = [[1, 5], [7, 10], [11, 15]]
        self.assertEqual(merge_intervals(intervals), expected)

if __name__ == '__main__':
    unittest.main()
