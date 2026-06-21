# Prompt
Write a function `calculate_start_times(tasks)` that takes a dictionary of tasks and returns a dictionary of their earliest possible start times. Each task is defined by a dictionary containing a `duration` (integer) and `dependencies` (a list of task IDs that must be completed before this task can start). If there is a circular dependency, the function should raise a `ValueError("Cycle detected")`.

Example input:
```python
tasks = {
    "A": {"duration": 5, "dependencies": []},
    "B": {"duration": 3, "dependencies": ["A"]},
    "C": {"duration": 4, "dependencies": ["A"]},
    "D": {"duration": 2, "dependencies": ["B", "C"]}
}
```
Expected output:
```python
{
    "A": 0,
    "B": 5,
    "C": 5,
    "D": 9
}
```