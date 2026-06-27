# Plan for `minimum_completion_time`

1.  **Parse Tasks**: Create a dictionary mapping `task_id` to the corresponding `Task` object for O(1) lookups.
2.  **Memoization and Cycle Detection**:
    *   Use a dictionary `memo` to store the minimum completion time for each task.
    *   Use a set `visiting` to keep track of tasks currently in the recursion stack to detect circular dependencies (cycles).
3.  **DFS Function (`get_time`)**:
    *   For a given `task_id`, if it's not in `task_dict`, it means a dependency is missing. Return `-1` as the project cannot be completed.
    *   If it's in `visiting`, a cycle is detected; return `-1`.
    *   If it's already in `memo`, return `memo[task_id]`.
    *   Add `task_id` to `visiting`.
    *   Recursively calculate the completion time for all dependencies. The maximum of these dependency times is the minimum wait time before the current task can start.
    *   If any dependency returns `-1`, propagate `-1` up.
    *   Remove `task_id` from `visiting`.
    *   The completion time for the current task is its duration plus the maximum dependency time. Store this in `memo` and return it.
4.  **Overall Result**:
    *   Iterate through all tasks and call `get_time`.
    *   If any call returns `-1`, return `-1`.
    *   The project completion time is the maximum of all individual task completion times. If the task list is empty, return 0.

5.  **Testing Strategy**:
    *   Rewrite `test_main.py` using Python's standard `unittest` library to make the tests runnable without external dependencies like `pytest`.
    *   Add additional tests for edge cases: missing dependencies, self-cycles, large task lists, negative/zero durations, and disconnected components.
    *   Run tests using `python3 test_main.py` and verify all tests pass.
