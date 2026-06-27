# Plan: Minimum Project Duration

## Problem Statement
We need to calculate the minimum project duration given a set of tasks, their durations, and their dependencies. All tasks can run in parallel, provided their dependencies are completed. We are guaranteed no circular dependencies (it's a DAG).

## Approach
This is the classic longest path problem in a Directed Acyclic Graph (DAG), or critical path method.
1. The completion time of any given task is its `duration` plus the maximum completion time among all of its `dependencies`.
2. The overall project duration is the maximum completion time over all tasks in the project.
3. We can efficiently compute this using depth-first search (DFS) with memoization.
4. If there are no tasks, return 0.

## Implementation details
- Create a `memo` dictionary mapping `task_name` to its `completion_time`.
- Define a recursive `get_completion_time(task_name)` function:
  - If `task_name` is in `memo`, return its value.
  - Calculate `max_dep_time` as the maximum of `get_completion_time(dep)` for all `dep` in `tasks[task_name]['dependencies']`.
  - The task's completion time is `tasks[task_name]['duration'] + max_dep_time`.
  - Store it in `memo[task_name]` and return it.
- Iterate over all tasks, find the completion time for each, and keep track of the overall maximum.
- Return the maximum duration.
