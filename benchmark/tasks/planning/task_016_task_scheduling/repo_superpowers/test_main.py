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

def test_empty_tasks():
    assert calculate_start_times({}) == {}

def test_self_dependency():
    tasks = {
        "A": {"duration": 5, "dependencies": ["A"]}
    }
    with pytest.raises(ValueError, match="Cycle detected"):
        calculate_start_times(tasks)

def test_disconnected_components():
    tasks = {
        "A": {"duration": 2, "dependencies": []},
        "B": {"duration": 3, "dependencies": ["A"]},
        "X": {"duration": 4, "dependencies": []},
        "Y": {"duration": 5, "dependencies": ["X"]}
    }
    expected = {"A": 0, "B": 2, "X": 0, "Y": 4}
    assert calculate_start_times(tasks) == expected

def test_missing_dependency():
    tasks = {
        "A": {"duration": 5, "dependencies": ["MissingTask"]},
        "B": {"duration": 3, "dependencies": ["A"]}
    }
    # "MissingTask" is treated as starting at 0 and finishing at 0, so A should start at 0.
    expected = {"A": 0, "B": 5}
    assert calculate_start_times(tasks) == expected

def test_missing_keys():
    tasks = {
        "A": {"dependencies": []},  # duration missing, defaults to 0
        "B": {"duration": 3},        # dependencies missing, defaults to []
        "C": {"duration": 4, "dependencies": ["A", "B"]}
    }
    expected = {"A": 0, "B": 0, "C": 3}
    assert calculate_start_times(tasks) == expected

def test_non_integer_duration():
    tasks = {
        "A": {"duration": "5", "dependencies": []},  # string duration castable to int
        "B": {"duration": "invalid", "dependencies": ["A"]}, # non-castable duration defaults to 0
        "C": {"duration": 4, "dependencies": ["B"]}
    }
    expected = {"A": 0, "B": 5, "C": 5}
    assert calculate_start_times(tasks) == expected

def test_large_chain():
    # Chain of 100 tasks to ensure no recursion depth limit issues
    tasks = {}
    expected = {}
    for i in range(100):
        task_id = f"Task{i}"
        deps = [f"Task{i-1}"] if i > 0 else []
        tasks[task_id] = {"duration": 2, "dependencies": deps}
        expected[task_id] = i * 2
    assert calculate_start_times(tasks) == expected

