import pytest
from main import Task, minimum_completion_time

def test_linear_dependencies():
    tasks = [
        Task("A", 5, []),
        Task("B", 10, ["A"]),
        Task("C", 15, ["B"])
    ]
    assert minimum_completion_time(tasks) == 30

def test_parallel_execution():
    tasks = [
        Task("A", 5, []),
        Task("B", 10, []),
        Task("C", 15, [])
    ]
    assert minimum_completion_time(tasks) == 15

def test_complex_dependencies():
    tasks = [
        Task("A", 3, []),
        Task("B", 4, ["A"]),
        Task("C", 2, ["A"]),
        Task("D", 5, ["B", "C"]),
        Task("E", 1, ["D"])
    ]
    assert minimum_completion_time(tasks) == 13

def test_circular_dependency():
    tasks = [
        Task("A", 5, ["C"]),
        Task("B", 5, ["A"]),
        Task("C", 5, ["B"])
    ]
    assert minimum_completion_time(tasks) == -1

def test_empty_project():
    assert minimum_completion_time([]) == 0
