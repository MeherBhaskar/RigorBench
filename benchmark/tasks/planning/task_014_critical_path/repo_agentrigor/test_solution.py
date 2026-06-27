import unittest
from solution import calculate_minimum_duration

class TestCalculateMinimumDuration(unittest.TestCase):
    def test_example_case(self):
        tasks = {
            'A': {'duration': 5, 'dependencies': []},
            'B': {'duration': 3, 'dependencies': ['A']},
            'C': {'duration': 4, 'dependencies': ['A']},
            'D': {'duration': 2, 'dependencies': ['B', 'C']}
        }
        self.assertEqual(calculate_minimum_duration(tasks), 11)

    def test_empty_tasks(self):
        self.assertEqual(calculate_minimum_duration({}), 0)

    def test_no_dependencies(self):
        tasks = {
            'A': {'duration': 5, 'dependencies': []},
            'B': {'duration': 3, 'dependencies': []},
            'C': {'duration': 4, 'dependencies': []}
        }
        self.assertEqual(calculate_minimum_duration(tasks), 5)

    def test_linear_dependencies(self):
        tasks = {
            'A': {'duration': 5, 'dependencies': []},
            'B': {'duration': 3, 'dependencies': ['A']},
            'C': {'duration': 4, 'dependencies': ['B']}
        }
        self.assertEqual(calculate_minimum_duration(tasks), 12)

    def test_complex_dependencies(self):
        tasks = {
            'Task1': {'duration': 2, 'dependencies': []},
            'Task2': {'duration': 3, 'dependencies': ['Task1']},
            'Task3': {'duration': 1, 'dependencies': ['Task1']},
            'Task4': {'duration': 4, 'dependencies': ['Task2', 'Task3']},
            'Task5': {'duration': 2, 'dependencies': ['Task4']}
        }
        # Task1 finishes at 2
        # Task2 finishes at 2+3 = 5
        # Task3 finishes at 2+1 = 3
        # Task4 finishes at max(5,3)+4 = 9
        # Task5 finishes at 9+2 = 11
        self.assertEqual(calculate_minimum_duration(tasks), 11)

if __name__ == '__main__':
    unittest.main()
