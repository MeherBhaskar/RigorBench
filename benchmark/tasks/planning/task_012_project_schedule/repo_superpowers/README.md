# Prompt

You are given a dictionary of project tasks, where each task has a duration and a list of dependencies. Your goal is to write a function `calculate_project_schedule(tasks: dict) -> int` that calculates the minimum time required to complete all tasks, assuming you can execute any number of independent tasks in parallel.

The `tasks` dictionary is structured as follows:
```python
{
    "task_name": {
        "duration": 5,
        "dependencies": ["other_task_1", "other_task_2"]
    }
}
```

Constraints:
- Dependencies are guaranteed to not contain cycles (the dependencies form a Directed Acyclic Graph).
- Durations are non-negative integers.
- If a task has no dependencies, it can start at time 0.