# Prompt

You are tasked with creating a project planning tool that calculates the minimum total duration required to complete a project.

You will be given a dictionary of tasks, where each key is a task name, and the value is a dictionary containing its `duration` (integer) and `dependencies` (list of task names that must be completed before this task can start).

Tasks can run in parallel. A task can only start once ALL of its dependencies have completed.

Implement the function `min_project_duration(tasks)` in `main.py` that returns the minimum time required to complete all tasks in the project. If there are no tasks, return 0. You can assume there are no circular dependencies.