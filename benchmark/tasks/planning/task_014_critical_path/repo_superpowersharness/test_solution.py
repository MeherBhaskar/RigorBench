from solution import calculate_minimum_duration

def test_calculate_minimum_duration():
    tasks = {
        'A': {'duration': 5, 'dependencies': []},
        'B': {'duration': 3, 'dependencies': ['A']},
        'C': {'duration': 4, 'dependencies': ['A']},
        'D': {'duration': 2, 'dependencies': ['B', 'C']}
    }
    assert calculate_minimum_duration(tasks) == 11

    tasks2 = {
        'A': {'duration': 1, 'dependencies': []},
        'B': {'duration': 2, 'dependencies': []},
    }
    assert calculate_minimum_duration(tasks2) == 2

    print("All tests passed!")

if __name__ == '__main__':
    test_calculate_minimum_duration()
