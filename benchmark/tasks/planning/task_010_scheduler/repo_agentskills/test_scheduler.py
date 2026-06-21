import pytest
from scheduler import calculate_project_schedule

def test_simple_sequence():
    tasks = {
        'A': {'duration': 5, 'dependencies': []},
        'B': {'duration': 3, 'dependencies': ['A']},
        'C': {'duration': 2, 'dependencies': ['B']}
    }
    total, start_times = calculate_project_schedule(tasks)
    assert total == 10
    assert start_times == {'A': 0, 'B': 5, 'C': 8}

def test_parallel_tasks():
    tasks = {
        'A': {'duration': 5, 'dependencies': []},
        'B': {'duration': 3, 'dependencies': []},
        'C': {'duration': 4, 'dependencies': ['A', 'B']}
    }
    total, start_times = calculate_project_schedule(tasks)
    assert total == 9
    assert start_times == {'A': 0, 'B': 0, 'C': 5}

def test_complex_graph():
    tasks = {
        'T1': {'duration': 2, 'dependencies': []},
        'T2': {'duration': 4, 'dependencies': ['T1']},
        'T3': {'duration': 3, 'dependencies': ['T1']},
        'T4': {'duration': 1, 'dependencies': ['T2', 'T3']},
        'T5': {'duration': 5, 'dependencies': ['T3']},
        'T6': {'duration': 2, 'dependencies': ['T4', 'T5']}
    }
    total, start_times = calculate_project_schedule(tasks)
    assert total == 12
    assert start_times == {'T1': 0, 'T2': 2, 'T3': 2, 'T4': 6, 'T5': 5, 'T6': 10}

def test_circular_dependency():
    tasks = {
        'A': {'duration': 1, 'dependencies': ['B']},
        'B': {'duration': 1, 'dependencies': ['A']}
    }
    with pytest.raises(ValueError):
        calculate_project_schedule(tasks)

def test_disconnected_components():
    tasks = {
        'A': {'duration': 5, 'dependencies': []},
        'B': {'duration': 2, 'dependencies': ['A']},
        'C': {'duration': 10, 'dependencies': []}
    }
    total, start_times = calculate_project_schedule(tasks)
    assert total == 10
    assert start_times == {'A': 0, 'B': 5, 'C': 0}
