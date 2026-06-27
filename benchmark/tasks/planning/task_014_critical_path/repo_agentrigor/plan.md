# Plan for `calculate_minimum_duration`

## Problem Understanding
We are given a dictionary of tasks. Each task has:
- `duration`: integer
- `dependencies`: list of task names (strings)

We want to find the minimum time required to complete all tasks, assuming tasks can be done in parallel if their dependencies are met.
This is equivalent to finding the maximum completion time among all tasks.
The completion time of a task = its `duration` + max(completion time of all its dependencies).
Since there are dependencies, this forms a Directed Acyclic Graph (DAG). We can compute the completion time of each task using memoization (Depth First Search) or by computing topological sort first.

## Approach
1. **Memoization / DFS**:
    - We will define a recursive function `get_completion_time(task)` that returns the minimum time at which `task` will be completed.
    - If the task has no dependencies, its completion time is just its duration.
    - If it has dependencies, its completion time is `duration + max(get_completion_time(dep) for dep in dependencies)`.
    - We will use a dictionary `memo` to store the computed completion times of tasks to avoid redundant calculations.
    - We can also handle cyclic dependencies by keeping track of a `visiting` set. If we encounter a task currently being visited, there is a cycle (though the problem implies a valid DAG).
    - Finally, the overall minimum duration to complete *all* tasks is the maximum completion time across all tasks.

2. **Algorithm Steps**:
    - Initialize `memo = {}`.
    - Initialize `visiting = set()`.
    - Define `dfs(task)`:
        - If `task` in `visiting`: raise ValueError("Cycle detected").
        - If `task` in `memo`: return `memo[task]`.
        - `visiting.add(task)`
        - `max_dep_time = 0`
        - For `dep` in `tasks[task]['dependencies']`:
            - `max_dep_time = max(max_dep_time, dfs(dep))`
        - `completion_time = tasks[task]['duration'] + max_dep_time`
        - `memo[task] = completion_time`
        - `visiting.remove(task)`
        - return `completion_time`
    - Iterate over all `task` in `tasks`:
        - `dfs(task)`
    - Return `max(memo.values())` if `memo` is not empty, else 0.

3. **Implementation**:
    - Create a Python file containing this function.
    - Create a test file with sample inputs, edge cases (no tasks, no dependencies, linear dependencies, complex DAG).

4. **Testing**:
    - Run the tests to ensure correctness.
