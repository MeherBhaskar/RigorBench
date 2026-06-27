# Plan for schedule_tasks

## Overview
We need to implement a function `schedule_tasks(tasks)` that calculates the earliest start time for a set of tasks. Each task has a `duration` and a list of `dependencies`.

## Approach
1.  **Topological Sorting & Dynamic Programming:**
    *   We can use Kahn's algorithm or Depth First Search (DFS) with memoization.
    *   Let's use DFS with memoization, as it naturally handles calculating the start time of a task based on its dependencies.
    *   For a task, its earliest start time is the maximum of `(earliest start time of dependency + duration of dependency)` over all its dependencies.
    *   If a task has no dependencies, its earliest start time is `0`.

2.  **Cycle Detection:**
    *   While performing DFS, we keep track of the current path (or recursion stack) in a set, `visiting`.
    *   If we encounter a task that is already in the `visiting` set, it means we have found a circular dependency. We should immediately raise a `ValueError`.
    *   We also keep a dictionary `memo` to store the calculated earliest start time for each task to avoid redundant calculations and infinite loops (though the `visiting` set already catches infinite loops/cycles).

3.  **Implementation Steps:**
    *   Initialize `memo` as an empty dictionary.
    *   Define a helper recursive function `get_start_time(task, visiting)`.
    *   Inside `get_start_time`:
        *   If `task` is in `visiting`, raise `ValueError`.
        *   If `task` is in `memo`, return `memo[task]`.
        *   Add `task` to `visiting`.
        *   Initialize `max_dep_end_time = 0`.
        *   Iterate through `tasks[task]['dependencies']`.
            *   For each dependency `dep`, recursively call `get_start_time(dep, visiting)`.
            *   Calculate the end time of the dependency: `dep_end_time = memo[dep] + tasks[dep]['duration']`.
            *   Update `max_dep_end_time = max(max_dep_end_time, dep_end_time)`.
        *   Remove `task` from `visiting`.
        *   Set `memo[task] = max_dep_end_time` and return it.
    *   Iterate through all tasks in `tasks` and call `get_start_time(task, set())`.
    *   Return the `memo` dictionary.

## Testing Strategy
1.  **Basic test case:** Tasks with no dependencies.
2.  **Linear dependency:** A -> B -> C.
3.  **Multiple dependencies:** C depends on A and B.
4.  **Complex dependency graph:** A mix of dependencies with different durations.
5.  **Cycle detection:** A -> B -> C -> A. Should raise `ValueError`.
6.  **Cycle detection (self-dependency):** A -> A. Should raise `ValueError`.
