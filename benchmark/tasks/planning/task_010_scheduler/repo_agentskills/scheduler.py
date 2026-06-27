def calculate_project_schedule(tasks: dict) -> tuple:
    """
    Calculates the earliest start times and total project duration.
    
    Args:
        tasks: A dictionary where keys are task IDs (str) and values are dicts with:
               'duration': int, the time required to complete the task.
               'dependencies': list of str, IDs of tasks that must be completed first.
               
    Returns:
        A tuple containing:
        - total_duration (int): The minimum time required to complete all tasks.
        - start_times (dict): A dictionary mapping task IDs to their earliest start times.
        
    Raises:
        ValueError: If there is a circular dependency.
    """
    in_degree = {t: 0 for t in tasks}
    adj = {t: [] for t in tasks}
    
    for t, info in tasks.items():
        for dep in info['dependencies']:
            if dep not in adj:
                adj[dep] = []
            adj[dep].append(t)
            in_degree[t] += 1
            
    queue = [t for t in tasks if in_degree[t] == 0]
    
    start_times = {t: 0 for t in tasks}
    completed_count = 0
    
    while queue:
        curr = queue.pop(0)
        completed_count += 1
        
        curr_end_time = start_times[curr] + tasks.get(curr, {}).get('duration', 0)
        
        for neighbor in adj.get(curr, []):
            if neighbor in in_degree:
                in_degree[neighbor] -= 1
                if start_times[neighbor] < curr_end_time:
                    start_times[neighbor] = curr_end_time
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
    if completed_count < len(tasks):
        raise ValueError("Circular dependency detected.")
        
    if not tasks:
        return 0, {}
        
    total_duration = max(start_times[t] + tasks[t]['duration'] for t in tasks)
    
    return total_duration, start_times
