# Plan for Min Completion Time

## Approach
We will use an A* search or memoized Depth First Search (DFS) to explore the state space of possible schedules.
Since the maximum number of tasks is very small (<= 15), the state space is manageable.

### 1. Preprocessing
- Map each task to an integer index `0` to `N-1`.
- Store the duration of each task.
- Convert the `prerequisites` list of each task into a bitmask of required task indices.
- Check for cyclic dependencies using a standard topological sort or DFS. If a cycle is detected, return `-1`.

### 2. State Representation
The state in our memoized DFS will be defined by:
- `completed_mask`: A bitmask representing the tasks that have fully completed.
- `running`: A tuple of currently running tasks, each represented as a pair `(task_index, time_remaining)`. To ensure states are canonically represented, this tuple will be sorted by `task_index`.

### 3. Transitions
At each decision point (state), we have a number of `free_workers = num_workers - len(running)`.
We find all `available` tasks, which are those that are not completed, not currently running, and have all their prerequisites satisfied (i.e., `prerequisites_mask & completed_mask == prerequisites_mask`).

For the available tasks, we can choose to start any subset of them of size at most `free_workers`.
For each valid subset `to_start` chosen:
1. We add the tasks in `to_start` to our `running` set with their initial durations.
2. If the new `running` set is empty, it means we have no running tasks and no tasks we want to start. If all tasks are completed, we are done (return 0). Otherwise, we are in a deadlock (return infinity).
3. We advance time by `min_rem`, which is the minimum `time_remaining` among all tasks in the new `running` set.
4. We update the `running` tasks by subtracting `min_rem` from their remaining times. Tasks whose remaining time becomes 0 are removed from `running` and added to `completed_mask`.
5. We recursively compute the minimum time to complete the remaining tasks from this new state, and add `min_rem` to it.

We return the minimum time across all valid choices of `to_start`.

### 4. Pruning and Optimizations
- **Memoization**: Cache the results of the `solve(completed_mask, running)` function to avoid recomputing identical states.
- **Topological Check**: The initial cycle check guarantees that if a schedule is possible, our search will find it. If no schedule is possible, the cycle check will catch it immediately.

### 5. Implementation Details
We will write a `min_completion_time` function embodying the above logic. We will also include tests using `unittest` or simple `assert` statements to verify correctness before finishing.
