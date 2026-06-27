# Plan for `schedule_tasks`

## Goal
Calculate the optimal schedule for a list of tasks with dependencies, assuming unlimited parallel execution. Determine the total duration and the start times of each task.

## Approach
1. **Input Validation**: Check if all tasks referenced in `dependencies` actually exist in the provided list of tasks. If not, raise a `ValueError`.
2. **Graph Construction**: Create a graph representation using adjacency lists where a node points to its dependents (tasks that wait for it). Also, compute the in-degree (number of dependencies) for each task.
3. **Data Structures**:
   - `durations`: Map of `task_id` to its duration.
   - `start_times`: Map of `task_id` to its calculated start time.
   - `graph`: Map of `task_id` to a list of `dependent_task_ids`.
   - `in_degree`: Map of `task_id` to integer.
4. **Topological Sort (Kahn's Algorithm)**:
   - Initialize a queue with all tasks that have an in-degree of 0 (no dependencies).
   - Set their `start_times` to 0.
   - Keep a `processed_count` to detect cycles.
   - While the queue is not empty:
     - Pop a `current_task` from the queue.
     - Increment `processed_count`.
     - Calculate its completion time: `completion_time = start_times[current_task] + durations[current_task]`.
     - For each `dependent` in `graph[current_task]`:
       - Update the start time of the `dependent`: `start_times[dependent] = max(start_times.get(dependent, 0), completion_time)`.
       - Decrement the in-degree of `dependent`.
       - If the in-degree of `dependent` becomes 0, push it to the queue.
5. **Cycle Detection**: After the loop, if `processed_count` is not equal to the total number of tasks, it means there is a circular dependency. Raise a `ValueError`.
6. **Result**:
   - The `total_duration` will be the maximum completion time across all tasks. If there are no tasks, it is 0.
   - Return `{"total_duration": total_duration, "start_times": start_times}`.

## Next Steps
- Implement the algorithm in `main.py`.
- Run pytest to verify the correctness.
