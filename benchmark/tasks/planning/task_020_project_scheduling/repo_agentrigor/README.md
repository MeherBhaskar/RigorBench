# Prompt

You are given a list of tasks for a project, where each task has an ID, a duration (in hours), and a list of prerequisite task IDs. You have a fixed number of workers `num_workers`. Each worker can work on one task at a time. Once a worker starts a task, they must finish it uninterrupted before taking on another. A task can only be started if all its prerequisites have been fully completed.

Write a function `min_completion_time(tasks: list[dict], num_workers: int) -> int` that calculates the minimum time required to complete all tasks.

The `tasks` list contains dictionaries with the following keys:
- `id` (str): Unique identifier for the task.
- `duration` (int): Time required to complete the task.
- `prerequisites` (list[str]): List of task IDs that must be completed before this task can start.

Return the minimum total time. If not all tasks can be completed (e.g., due to cyclic dependencies), return `-1`.

### Constraints:
- 1 <= number of tasks <= 15
- 1 <= duration <= 100
- 1 <= num_workers <= 5

### Example:
```python
tasks = [
    {"id": "A", "duration": 3, "prerequisites": []},
    {"id": "B", "duration": 2, "prerequisites": ["A"]},
    {"id": "C", "duration": 4, "prerequisites": ["A"]},
    {"id": "D", "duration": 1, "prerequisites": ["B", "C"]}
]

min_completion_time(tasks, 2) # returns 8
```
Explanation: 
- Task A takes 3 hours (Worker 1).
- At hour 3, Worker 1 starts Task B and Worker 2 starts Task C.
- Worker 1 finishes B at hour 5, but D cannot start until C finishes.
- Worker 2 finishes C at hour 7.
- Worker 1 or 2 starts D at hour 7 and finishes at hour 8.