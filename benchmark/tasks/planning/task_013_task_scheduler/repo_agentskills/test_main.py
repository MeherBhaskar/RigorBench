import pytest
from main import schedule_tasks

def test_schedule_tasks_simple():
    tasks = {
        "A": {"duration": 5, "dependencies": []},
        "B": {"duration": 3, "dependencies": ["A"]},
        "C": {"duration": 4, "dependencies": ["A"]},
        "D": {"duration": 2, "dependencies": ["B", "C"]}
    }
    expected = {"A": 0, "B": 5, "C": 5, "D": 9}
    assert schedule_tasks(tasks) == expected

def test_schedule_tasks_independent():
    tasks = {
        "T1": {"duration": 10, "dependencies": []},
        "T2": {"duration": 5, "dependencies": []}
    }
    expected = {"T1": 0, "T2": 0}
    assert schedule_tasks(tasks) == expected

def test_schedule_tasks_circular():
    tasks = {
        "A": {"duration": 1, "dependencies": ["B"]},
        "B": {"duration": 1, "dependencies": ["A"]}
    }
    with pytest.raises(ValueError):
        schedule_tasks(tasks)

def test_schedule_tasks_missing():
    tasks = {
        "A": {"duration": 5, "dependencies": ["B"]}
    }
    with pytest.raises(ValueError) as excinfo:
        schedule_tasks(tasks)
    assert "not found in tasks" in str(excinfo.value)

