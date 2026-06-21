from main import calculate_minimum_duration

def test_simple_critical_path():
    tasks = {
        'A': {'duration': 5, 'dependencies': []},
        'B': {'duration': 3, 'dependencies': ['A']},
        'C': {'duration': 4, 'dependencies': ['A']},
        'D': {'duration': 2, 'dependencies': ['B', 'C']}
    }
    assert calculate_minimum_duration(tasks) == 11

def test_independent_tasks():
    tasks = {
        'A': {'duration': 5, 'dependencies': []},
        'B': {'duration': 10, 'dependencies': []},
        'C': {'duration': 2, 'dependencies': []}
    }
    assert calculate_minimum_duration(tasks) == 10

def test_complex_dependencies():
    tasks = {
        'T1': {'duration': 2, 'dependencies': []},
        'T2': {'duration': 4, 'dependencies': ['T1']},
        'T3': {'duration': 10, 'dependencies': ['T1']},
        'T4': {'duration': 3, 'dependencies': ['T2']},
        'T5': {'duration': 1, 'dependencies': ['T3', 'T4']}
    }
    assert calculate_minimum_duration(tasks) == 13
