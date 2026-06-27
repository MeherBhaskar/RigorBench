def calculate_start_times(tasks):
    """
    Calculates the earliest possible start times for a dictionary of tasks.
    Each task is defined by a dictionary containing a `duration` (integer)
    and `dependencies` (a list of task IDs).
    If there is a circular dependency, raises a ValueError("Cycle detected").
    """
    if not isinstance(tasks, dict):
        raise TypeError("tasks must be a dictionary")

    # Initialize data structures for Kahn's algorithm
    start_times = {}
    in_degree = {}
    graph = {}

    # Initialize all tasks from the input tasks dictionary
    for task in tasks:
        in_degree[task] = 0
        graph[task] = []

    # Build the dependency graph and in-degrees
    for task, info in tasks.items():
        if not isinstance(info, dict):
            continue
        deps = info.get("dependencies", [])
        if not isinstance(deps, list):
            deps = []
        for dep in deps:
            # If the dependency is not in tasks, it is an external dependency.
            # We treat it as starting at 0 and having 0 duration (effectively ignoring it).
            if dep not in tasks:
                continue
            graph[dep].append(task)
            in_degree[task] += 1

    # Queue contains all tasks with no unresolved dependencies
    queue = [task for task in tasks if in_degree[task] == 0]
    
    # Initialize start times of initial tasks to 0
    for task in queue:
        start_times[task] = 0

    processed_count = 0

    while queue:
        curr = queue.pop(0)
        processed_count += 1
        
        # Get the duration of the current task, defaulting to 0 if missing or not an integer
        curr_info = tasks.get(curr, {})
        duration = 0
        if isinstance(curr_info, dict):
            duration = curr_info.get("duration", 0)
            if not isinstance(duration, int):
                try:
                    duration = int(duration)
                except (ValueError, TypeError):
                    duration = 0

        curr_finish = start_times[curr] + duration
        
        for neighbor in graph[curr]:
            # The earliest start time of the neighbor is constrained by the finish time of curr
            start_times[neighbor] = max(start_times.get(neighbor, 0), curr_finish)
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If the number of processed tasks is less than the total tasks, a cycle exists
    if processed_count < len(tasks):
        raise ValueError("Cycle detected")

    return start_times

