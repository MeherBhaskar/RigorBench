import pytest
from main import calculate_project_schedule

def test_linear():
    tasks = {
        "A": {"duration": 2, "dependencies": []},
        "B": {"duration": 3, "dependencies": ["A"]},
        "C": {"duration": 1, "dependencies": ["B"]}
    }
    assert calculate_project_schedule(tasks) == 6

def test_parallel():
    tasks = {
        "A": {"duration": 3, "dependencies": []},
        "B": {"duration": 2, "dependencies": ["A"]},
        "C": {"duration": 4, "dependencies": ["A"]},
        "D": {"duration": 1, "dependencies": ["B", "C"]}
    }
    assert calculate_project_schedule(tasks) == 8

def test_independent():
    tasks = {
        "A": {"duration": 5, "dependencies": []},
        "B": {"duration": 7, "dependencies": []},
        "C": {"duration": 3, "dependencies": []}
    }
    assert calculate_project_schedule(tasks) == 7

def test_complex():
    tasks = {
        "A": {"duration": 2, "dependencies": []},
        "B": {"duration": 3, "dependencies": ["A"]},
        "C": {"duration": 2, "dependencies": ["A"]},
        "D": {"duration": 1, "dependencies": ["B"]},
        "E": {"duration": 4, "dependencies": ["C", "D"]},
        "F": {"duration": 2, "dependencies": ["B", "E"]}
    }
    assert calculate_project_schedule(tasks) == 12

def test_empty():
    tasks = {}
    assert calculate_project_schedule(tasks) == 0
