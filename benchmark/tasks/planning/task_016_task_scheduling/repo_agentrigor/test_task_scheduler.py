import unittest
from task_scheduler import calculate_start_times

class TestTaskScheduler(unittest.TestCase):
    def test_example_case(self):
        tasks = {
            "A": {"duration": 5, "dependencies": []},
            "B": {"duration": 3, "dependencies": ["A"]},
            "C": {"duration": 4, "dependencies": ["A"]},
            "D": {"duration": 2, "dependencies": ["B", "C"]}
        }
        expected = {
            "A": 0,
            "B": 5,
            "C": 5,
            "D": 9
        }
        self.assertEqual(calculate_start_times(tasks), expected)

    def test_cycle_detection(self):
        tasks = {
            "A": {"duration": 5, "dependencies": ["B"]},
            "B": {"duration": 3, "dependencies": ["A"]}
        }
        with self.assertRaises(ValueError) as context:
            calculate_start_times(tasks)
        self.assertEqual(str(context.exception), "Cycle detected")
        
    def test_complex_cycle(self):
        tasks = {
            "A": {"duration": 1, "dependencies": []},
            "B": {"duration": 1, "dependencies": ["A", "C"]},
            "C": {"duration": 1, "dependencies": ["B"]}
        }
        with self.assertRaises(ValueError) as context:
            calculate_start_times(tasks)
        self.assertEqual(str(context.exception), "Cycle detected")

    def test_independent_tasks(self):
        tasks = {
            "A": {"duration": 5, "dependencies": []},
            "B": {"duration": 3, "dependencies": []}
        }
        expected = {
            "A": 0,
            "B": 0
        }
        self.assertEqual(calculate_start_times(tasks), expected)

    def test_empty_tasks(self):
        self.assertEqual(calculate_start_times({}), {})

if __name__ == "__main__":
    unittest.main()
