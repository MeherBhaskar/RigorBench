import pytest
from main import calculate_start_times

def test_simple_schedule():
    tasks = {
        "A": {"duration": 5, "dependencies": []},
        "B": {"duration": 3, "dependencies": ["A"]},
        "C": {"duration": 4, "dependencies": ["A"]},
        "D": {"duration": 2, "dependencies": ["B", "C"]}
    }
    expected = {"A": 0, "B": 5, "C": 5, "D": 9}
    assert calculate_start_times(tasks) == expected

def test_independent_tasks():
    tasks = {
        "A": {"duration": 5, "dependencies": []},
        "B": {"duration": 3, "dependencies": []}
    }
    expected = {"A": 0, "B": 0}
    assert calculate_start_times(tasks) == expected

def test_cycle_detection():
    tasks = {
        "A": {"duration": 1, "dependencies": ["C"]},
        "B": {"duration": 1, "dependencies": ["A"]},
        "C": {"duration": 1, "dependencies": ["B"]}
    }
    with pytest.raises(ValueError, match="Cycle detected"):
        calculate_start_times(tasks)

def test_complex_schedule():
    tasks = {
        "Start": {"duration": 0, "dependencies": []},
        "Task1": {"duration": 10, "dependencies": ["Start"]},
        "Task2": {"duration": 15, "dependencies": ["Start"]},
        "Task3": {"duration": 5, "dependencies": ["Task1"]},
        "Task4": {"duration": 5, "dependencies": ["Task2"]},
        "End": {"duration": 0, "dependencies": ["Task3", "Task4"]}
    }
    expected = {
        "Start": 0,
        "Task1": 0,
        "Task2": 0,
        "Task3": 10,
        "Task4": 15,
        "End": 20
    }
    assert calculate_start_times(tasks) == expected
