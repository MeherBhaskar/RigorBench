# Plan - Task Scheduling (Earliest Start Times)

This plan outlines the approach to implement and test the `calculate_start_times` function.

## 1. Problem Understanding
We need to calculate the earliest possible start time for a set of tasks.
- Each task has a `duration` (integer >= 0) and `dependencies` (list of task IDs).
- A task can only start after all of its dependencies have finished.
- The earliest start time of a task with no dependencies is `0`.
- The earliest start time of a task with dependencies is the maximum of `(start_time + duration)` over all its direct dependencies.
- If there is a cycle in the dependencies, we must raise a `ValueError("Cycle detected")`.

## 2. Algorithm: Kahn's Algorithm (Topological Sort + DP)
We will use Kahn's algorithm for topological sorting, which also allows us to compute the earliest start times dynamically and detect cycles:

1. **Graph Representation**:
   - Represent the tasks as a directed graph where an edge `u -> v` exists if task `u` is a dependency of task `v` (i.e., `v` depends on `u`).
   - Compute the in-degree for each task (number of incoming dependencies).

2. **Initialization**:
   - Create an adjacency list `adj` mapping each task to the list of tasks that depend on it.
   - Initialize `in_degree` dictionary for all tasks.
   - Initialize `start_time` dictionary for all tasks to `0`.
   - Initialize a queue (using `collections.deque`) with all tasks that have `in_degree == 0`.

3. **Processing**:
   - While the queue is not empty:
     - Pop a task `u` from the queue.
     - For each task `v` that depends on `u` (i.e., `v` in `adj[u]`):
       - Update `start_time[v] = max(start_time[v], start_time[u] + duration[u])`.
       - Decrement `in_degree[v]`.
       - If `in_degree[v]` becomes `0`, push `v` to the queue.
   - Track the number of processed tasks. If the number of processed tasks is less than the total number of tasks in the input, a cycle exists.

4. **Error Handling**:
   - If a cycle is detected, raise `ValueError("Cycle detected")`.
   - If a task dependency refers to a non-existent task, we will raise a `ValueError` or handle it gracefully.

## 3. Implementation Details
The implementation will be written in `main.py` so that the existing tests in `test_main.py` pass.

## 4. Testing Strategy
We will verify the implementation with:
- Standard unit tests in `test_main.py`.
- Additional edge cases including:
  - Empty input `{}`.
  - Tasks with zero duration.
  - Disconnected task groups.
  - Multiple paths to the same task (ensuring the maximum completion time of dependencies is used).
  - Direct and indirect cycles.
  - Self-dependency/loops.
