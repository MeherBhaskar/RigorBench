import unittest
from main import Task, minimum_completion_time

class TestMinimumCompletionTime(unittest.TestCase):
    def test_linear_dependencies(self):
        tasks = [
            Task("A", 5, []),
            Task("B", 10, ["A"]),
            Task("C", 15, ["B"])
        ]
        self.assertEqual(minimum_completion_time(tasks), 30)

    def test_parallel_execution(self):
        tasks = [
            Task("A", 5, []),
            Task("B", 10, []),
            Task("C", 15, [])
        ]
        self.assertEqual(minimum_completion_time(tasks), 15)

    def test_complex_dependencies(self):
        tasks = [
            Task("A", 3, []),
            Task("B", 4, ["A"]),
            Task("C", 2, ["A"]),
            Task("D", 5, ["B", "C"]),
            Task("E", 1, ["D"])
        ]
        self.assertEqual(minimum_completion_time(tasks), 13)

    def test_circular_dependency(self):
        tasks = [
            Task("A", 5, ["C"]),
            Task("B", 5, ["A"]),
            Task("C", 5, ["B"])
        ]
        self.assertEqual(minimum_completion_time(tasks), -1)

    def test_empty_project(self):
        self.assertEqual(minimum_completion_time([]), 0)

    def test_missing_dependency(self):
        tasks = [
            Task("A", 5, ["B"])
        ]
        self.assertEqual(minimum_completion_time(tasks), -1)

    def test_self_dependency(self):
        tasks = [
            Task("A", 5, ["A"])
        ]
        self.assertEqual(minimum_completion_time(tasks), -1)

    def test_disconnected_components(self):
        tasks = [
            Task("A", 5, []),
            Task("B", 10, []),
            Task("C", 3, ["A"]),
            Task("D", 4, ["B"])
        ]
        # Max of path A->C (5+3=8) and path B->D (10+4=14) is 14
        self.assertEqual(minimum_completion_time(tasks), 14)

if __name__ == '__main__':
    unittest.main()
