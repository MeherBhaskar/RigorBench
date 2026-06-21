# Prompt

Write a function `schedule_tasks(tasks)` that calculates the earliest possible start time for a set of tasks.

The input `tasks` is a dictionary where each key is a task name (string) and the value is a dictionary containing:
- `duration`: An integer representing how long the task takes.
- `dependencies`: A list of task names that must be completed before this task can start.

The function should return a dictionary mapping each task name to its earliest possible start time (integer).
If there is a circular dependency among the tasks, the function must raise a `ValueError`.
Tasks with no dependencies can start at time 0.