from schedule_tasks import schedule_tasks

def test_no_dependencies():
    tasks = {
        'A': {'duration': 5, 'dependencies': []},
        'B': {'duration': 3, 'dependencies': []}
    }
    expected = {'A': 0, 'B': 0}
    assert schedule_tasks(tasks) == expected

def test_linear_dependencies():
    tasks = {
        'A': {'duration': 5, 'dependencies': []},
        'B': {'duration': 3, 'dependencies': ['A']},
        'C': {'duration': 2, 'dependencies': ['B']}
    }
    expected = {'A': 0, 'B': 5, 'C': 8}
    assert schedule_tasks(tasks) == expected

def test_multiple_dependencies():
    tasks = {
        'A': {'duration': 5, 'dependencies': []},
        'B': {'duration': 3, 'dependencies': []},
        'C': {'duration': 2, 'dependencies': ['A', 'B']}
    }
    expected = {'A': 0, 'B': 0, 'C': 5}
    assert schedule_tasks(tasks) == expected

def test_complex_dependencies():
    tasks = {
        'A': {'duration': 5, 'dependencies': []},
        'B': {'duration': 3, 'dependencies': ['A']},
        'C': {'duration': 2, 'dependencies': ['A']},
        'D': {'duration': 4, 'dependencies': ['B', 'C']}
    }
    expected = {'A': 0, 'B': 5, 'C': 5, 'D': 8}
    assert schedule_tasks(tasks) == expected

def test_circular_dependency():
    tasks = {
        'A': {'duration': 5, 'dependencies': ['C']},
        'B': {'duration': 3, 'dependencies': ['A']},
        'C': {'duration': 2, 'dependencies': ['B']}
    }
    try:
        schedule_tasks(tasks)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert str(e) == "Circular dependency detected"

def test_self_dependency():
    tasks = {
        'A': {'duration': 5, 'dependencies': ['A']}
    }
    try:
        schedule_tasks(tasks)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert str(e) == "Circular dependency detected"

def test_missing_dependency():
    tasks = {
        'A': {'duration': 5, 'dependencies': ['B']}
    }
    try:
        schedule_tasks(tasks)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert str(e) == "Dependency 'B' not found in tasks"

if __name__ == '__main__':
    test_no_dependencies()
    test_linear_dependencies()
    test_multiple_dependencies()
    test_complex_dependencies()
    test_circular_dependency()
    test_self_dependency()
    test_missing_dependency()
    print("All tests passed.")
