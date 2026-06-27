# Plan for Project Schedule Calculation

1. Initialize a memoization dictionary to store the completion time of each task.
2. Define a recursive function `get_completion_time(task_name)`:
   - If `task_name` is in memoization dict, return its value.
   - For each dependency of `task_name`, recursively calculate its completion time.
   - The start time of `task_name` is the maximum completion time of all its dependencies (or 0 if no dependencies).
   - The completion time of `task_name` is its start time plus its duration.
   - Store the completion time in the memoization dict and return it.
3. Iterate through all tasks in the given `tasks` dictionary.
4. Calculate the completion time for each task using `get_completion_time(task_name)`.
5. The overall minimum project completion time is the maximum of all individual task completion times. (If the `tasks` dictionary is empty, return 0).
6. Return the result.
