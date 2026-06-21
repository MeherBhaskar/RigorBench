import pytest
from main import schedule_tasks

def test_linear_schedule():
    tasks = [
        {"id": "A", "duration": 2, "dependencies": []},
        {"id": "B", "duration": 3, "dependencies": ["A"]},
        {"id": "C", "duration": 1, "dependencies": ["B"]}
    ]
    res = schedule_tasks(tasks)
    assert res["total_duration"] == 6
    assert res["start_times"] == {"A": 0, "B": 2, "C": 5}

def test_parallel_schedule():
    tasks = [
        {"id": "A", "duration": 5, "dependencies": []},
        {"id": "B", "duration": 3, "dependencies": []},
        {"id": "C", "duration": 2, "dependencies": ["A", "B"]}
    ]
    res = schedule_tasks(tasks)
    assert res["total_duration"] == 7
    assert res["start_times"] == {"A": 0, "B": 0, "C": 5}

def test_complex_dependencies():
    tasks = [
        {"id": "start", "duration": 1, "dependencies": []},
        {"id": "task1", "duration": 4, "dependencies": ["start"]},
        {"id": "task2", "duration": 2, "dependencies": ["start"]},
        {"id": "task3", "duration": 3, "dependencies": ["task2"]},
        {"id": "end", "duration": 1, "dependencies": ["task1", "task3"]}
    ]
    res = schedule_tasks(tasks)
    assert res["total_duration"] == 7
    assert res["start_times"] == {"start": 0, "task1": 1, "task2": 1, "task3": 3, "end": 6}

def test_cycle_raises_value_error():
    tasks = [
        {"id": "A", "duration": 1, "dependencies": ["B"]},
        {"id": "B", "duration": 1, "dependencies": ["A"]}
    ]
    with pytest.raises(ValueError):
        schedule_tasks(tasks)

def test_missing_dependency_raises_value_error():
    tasks = [
        {"id": "A", "duration": 1, "dependencies": ["C"]}
    ]
    with pytest.raises(ValueError):
        schedule_tasks(tasks)

def test_empty_tasks():
    tasks = []
    res = schedule_tasks(tasks)
    assert res["total_duration"] == 0
    assert res["start_times"] == {}
