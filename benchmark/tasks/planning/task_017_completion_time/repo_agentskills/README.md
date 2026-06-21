# Prompt

You are given a list of tasks for a project. Each task has a unique ID, a duration (in hours), and a list of dependency task IDs that must be completed before the given task can begin. Tasks can be executed in parallel as long as their dependencies are met.

Write a function `minimum_completion_time(tasks)` that calculates the minimum number of hours required to complete the entire project.

If there is a circular dependency, the project can never be completed, and you should return `-1`.

Example:
Task A: 3 hours, Dependencies: []
Task B: 4 hours, Dependencies: [A]
Task C: 2 hours, Dependencies: [A]
Task D: 5 hours, Dependencies: [B, C]
Task E: 1 hour, Dependencies: [D]

The minimum completion time is 13 hours.