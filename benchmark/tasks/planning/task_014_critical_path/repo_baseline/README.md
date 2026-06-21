# Prompt

You are given a dictionary of tasks where each task has a duration and a list of dependencies. Your goal is to write a function `calculate_minimum_duration(tasks)` that returns the minimum time required to complete all tasks. Tasks can be performed in parallel if their dependencies are met.

Example input:
```python
tasks = {
    'A': {'duration': 5, 'dependencies': []},
    'B': {'duration': 3, 'dependencies': ['A']},
    'C': {'duration': 4, 'dependencies': ['A']},
    'D': {'duration': 2, 'dependencies': ['B', 'C']}
}
```
In this example, the minimum duration is 11 (A takes 5, then C takes 4, then D takes 2).