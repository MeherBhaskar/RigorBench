# Plan for `calculate_project_schedule`

## Problem Understanding
The goal is to calculate the minimum time required to complete a project and find the earliest start times for each task, given a dictionary of tasks where each task has a duration and a list of dependencies. We also need to detect circular dependencies and raise a `ValueError`.

## Approach
This can be modeled as finding the longest path in a Directed Acyclic Graph (DAG) where tasks are nodes, and dependencies are directed edges. 
We can use a memoized Depth-First Search (DFS) approach.

### Algorithm
1. Initialize a dictionary `start_times` to store the earliest start time for each task. This also acts as our memoization table.
2. Define a recursive function `get_start_time(task_id, visiting)`:
    - If `task_id` is in `visiting`, we have a circular dependency. Raise a `ValueError`.
    - If `task_id` is already in `start_times`, return `start_times[task_id]`.
    - Add `task_id` to `visiting`.
    - If the task has no dependencies, its start time is 0.
    - If it has dependencies, its start time is the maximum of `get_start_time(dep) + tasks[dep]['duration']` over all dependencies `dep`. If a dependency doesn't exist in the `tasks` dictionary, we should probably raise a `KeyError` or handle it gracefully (the problem assumes dependencies are within the keys).
    - Remove `task_id` from `visiting`.
    - Store the calculated start time in `start_times[task_id]` and return it.
3. Iterate over all keys in the `tasks` dictionary and call `get_start_time` for each.
4. The total project duration is the maximum of `start_times[task_id] + tasks[task_id]['duration']` for all tasks. If there are no tasks, total duration is 0.
5. Return the tuple `(total_duration, start_times)`.

## Steps
1. Write the `calculate_project_schedule` function in a Python file (e.g., `scheduler.py`).
2. Write unit tests in `test_scheduler.py` covering:
   - Basic cases with sequential dependencies.
   - Parallel dependencies (e.g., the example provided).
   - Complex DAGs.
   - Circular dependencies.
   - Empty project.
3. Run the tests to verify the implementation.
