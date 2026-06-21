# Prompt
You are given a list of tasks for a project. Each task is represented as a dictionary with the following keys:
- `id` (str): A unique identifier for the task.
- `duration` (int): The number of days required to complete the task.
- `dependencies` (list of str): A list of task IDs that must be fully completed before this task can start.

Your goal is to write a function `schedule_tasks(tasks)` that calculates the optimal schedule, assuming you have unlimited resources and can run any number of independent tasks in parallel.

The function should return a dictionary with:
- `total_duration`: The minimum total number of days required to complete all tasks.
- `start_times`: A dictionary mapping each task ID to its earliest possible start time (an integer, starting at day 0).

If there is a circular dependency (a cycle), or if a task depends on an ID that is not present in the list of tasks, the function must raise a `ValueError`.