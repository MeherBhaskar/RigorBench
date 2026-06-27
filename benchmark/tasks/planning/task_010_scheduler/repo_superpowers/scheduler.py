from collections import deque

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
    in_degree = {task: 0 for task in tasks}
    adj_list = {task: [] for task in tasks}
    
    for task, info in tasks.items():
        for dep in info.get('dependencies', []):
            if dep not in tasks:
                raise ValueError(f"Dependency {dep} not found in tasks")
            adj_list[dep].append(task)
            in_degree[task] += 1
            
    queue = deque([task for task, deg in in_degree.items() if deg == 0])
    start_times = {task: 0 for task in tasks}
    processed = 0
    
    while queue:
        u = queue.popleft()
        processed += 1
        
        completion_time = start_times[u] + tasks[u].get('duration', 0)
        
        for v in adj_list[u]:
            start_times[v] = max(start_times[v], completion_time)
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    if processed != len(tasks):
        raise ValueError("Circular dependency detected")
        
    total_duration = max((start_times[u] + tasks[u].get('duration', 0) for u in tasks), default=0)
    
    return total_duration, start_times
