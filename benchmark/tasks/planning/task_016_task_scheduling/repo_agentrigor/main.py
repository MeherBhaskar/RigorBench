def calculate_start_times(tasks):
    """
    Calculates the earliest possible start times for a set of tasks.
    
    Args:
        tasks (dict): A dictionary where keys are task IDs and values are dicts
                      containing 'duration' (int) and 'dependencies' (list of task IDs).
                      
    Returns:
        dict: A dictionary mapping each task ID to its earliest possible start time.
        
    Raises:
        ValueError: If a circular dependency (cycle) is detected.
    """
    from collections import deque

    # Initialize in-degrees and start times for all tasks in the input
    indegrees = {task: 0 for task in tasks}
    start_times = {task: 0 for task in tasks}
    graph = {task: [] for task in tasks}

    # Build the adjacency list and compute in-degrees
    for task, data in tasks.items():
        dependencies = data.get("dependencies", [])
        indegrees[task] = len(dependencies)
        for dep in dependencies:
            if dep in graph:
                graph[dep].append(task)
            else:
                # Handle cases where a dependency might not be in the tasks dict.
                # We still record the dependency relationship, but the missing dependency
                # itself won't have an in-degree or be processed, which will correctly
                # trigger the cycle/unresolvable check.
                graph[dep] = [task]

    # Initialize the queue with tasks that have no dependencies
    queue = deque([task for task, ind in indegrees.items() if ind == 0])
    processed_nodes = 0

    while queue:
        current = queue.popleft()
        processed_nodes += 1
        
        # Get the duration of the current task (default to 0 if not specified)
        duration = tasks[current].get("duration", 0)
        
        # Update the start times of all tasks that depend on the current task
        for neighbor in graph[current]:
            # The neighbor might not be in tasks if the input is malformed,
            # so we check if neighbor is in start_times to avoid KeyError.
            if neighbor in start_times:
                current_finish_time = start_times[current] + duration
                if start_times[neighbor] < current_finish_time:
                    start_times[neighbor] = current_finish_time
                
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

    # If the number of processed tasks is less than the total tasks,
    # it means there is a cycle (or an unresolvable dependency).
    if processed_nodes < len(tasks):
        raise ValueError("Cycle detected")

    return start_times
