# Prompt

Write a function `calculate_project_schedule(tasks)` that determines the minimum time required to complete a project consisting of multiple interdependent tasks.

Each task has a specified duration and a list of dependencies (other tasks that must be completed before this one can start). You should assume that any number of independent tasks can be performed in parallel.

Your function should calculate and return:
1. The total duration of the project (earliest possible completion time).
2. The earliest possible start time for each individual task.

If the project contains a circular dependency (e.g., Task A depends on Task B, which depends on Task A), making it impossible to complete, your function must raise a `ValueError`.

### Input Format

A dictionary where keys are task IDs (strings) and values are dictionaries containing:
- `duration`: An integer representing the time required to complete the task.
- `dependencies`: A list of task IDs (strings) representing tasks that must be finished before this task can begin.

### Output Format

A tuple `(total_duration, start_times)`:
- `total_duration` (int): The overall duration of the project.
- `start_times` (dict): A dictionary mapping each task ID to its earliest start time (int).

### Examples

```python
tasks = {
    'A': {'duration': 5, 'dependencies': []},
    'B': {'duration': 3, 'dependencies': []},
    'C': {'duration': 4, 'dependencies': ['A', 'B']}
}
calculate_project_schedule(tasks)
# Returns: (9, {'A': 0, 'B': 0, 'C': 5})
```
