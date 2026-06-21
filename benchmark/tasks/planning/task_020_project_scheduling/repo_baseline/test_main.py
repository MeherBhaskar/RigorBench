import pytest
from main import min_completion_time

def test_simple_scheduling():
    tasks = [
        {"id": "A", "duration": 3, "prerequisites": []},
        {"id": "B", "duration": 2, "prerequisites": ["A"]},
        {"id": "C", "duration": 4, "prerequisites": ["A"]},
        {"id": "D", "duration": 1, "prerequisites": ["B", "C"]}
    ]
    assert min_completion_time(tasks, 2) == 8
    assert min_completion_time(tasks, 1) == 10

def test_cycle_detection():
    tasks = [
        {"id": "A", "duration": 1, "prerequisites": ["B"]},
        {"id": "B", "duration": 1, "prerequisites": ["A"]}
    ]
    assert min_completion_time(tasks, 2) == -1

def test_independent_tasks():
    tasks = [
        {"id": "A", "duration": 5, "prerequisites": []},
        {"id": "B", "duration": 5, "prerequisites": []},
        {"id": "C", "duration": 5, "prerequisites": []}
    ]
    assert min_completion_time(tasks, 3) == 5
    assert min_completion_time(tasks, 2) == 10
    assert min_completion_time(tasks, 1) == 15

def test_bottleneck_prerequisite():
    tasks = [
        {"id": "A", "duration": 10, "prerequisites": []},
        {"id": "B", "duration": 1, "prerequisites": ["A"]},
        {"id": "C", "duration": 1, "prerequisites": ["A"]},
        {"id": "D", "duration": 1, "prerequisites": ["A"]}
    ]
    assert min_completion_time(tasks, 3) == 11
    assert min_completion_time(tasks, 2) == 12

def test_complex_dependencies():
    tasks = [
        {"id": "T1", "duration": 2, "prerequisites": []},
        {"id": "T2", "duration": 3, "prerequisites": []},
        {"id": "T3", "duration": 1, "prerequisites": ["T1"]},
        {"id": "T4", "duration": 4, "prerequisites": ["T2"]},
        {"id": "T5", "duration": 2, "prerequisites": ["T3", "T4"]},
        {"id": "T6", "duration": 3, "prerequisites": ["T1", "T2"]}
    ]
    assert min_completion_time(tasks, 2) == 9
