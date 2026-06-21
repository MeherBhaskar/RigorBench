import pytest
from main import min_project_duration

def test_empty():
    assert min_project_duration({}) == 0

def test_linear():
    tasks = {
        'A': {'duration': 1, 'dependencies': []},
        'B': {'duration': 2, 'dependencies': ['A']},
        'C': {'duration': 3, 'dependencies': ['B']},
    }
    assert min_project_duration(tasks) == 6

def test_parallel():
    tasks = {
        'A': {'duration': 5, 'dependencies': []},
        'B': {'duration': 3, 'dependencies': ['A']},
        'C': {'duration': 4, 'dependencies': ['A']},
        'D': {'duration': 2, 'dependencies': ['B', 'C']}
    }
    assert min_project_duration(tasks) == 11

def test_complex():
    tasks = {
        'Start': {'duration': 0, 'dependencies': []},
        'Design': {'duration': 10, 'dependencies': ['Start']},
        'Backend': {'duration': 20, 'dependencies': ['Design']},
        'Frontend': {'duration': 15, 'dependencies': ['Design']},
        'Integration': {'duration': 5, 'dependencies': ['Backend', 'Frontend']},
        'Testing': {'duration': 10, 'dependencies': ['Integration']},
        'Documentation': {'duration': 5, 'dependencies': ['Design']}
    }
    assert min_project_duration(tasks) == 45

def test_disconnected_components():
    tasks = {
        'A1': {'duration': 10, 'dependencies': []},
        'A2': {'duration': 10, 'dependencies': ['A1']},
        'B1': {'duration': 25, 'dependencies': []},
    }
    assert min_project_duration(tasks) == 25
