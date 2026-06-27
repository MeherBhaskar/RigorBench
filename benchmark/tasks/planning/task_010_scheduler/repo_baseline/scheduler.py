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
    graph = {task: [] for task in tasks}
    
    for task, data in tasks.items():
        for dep in data.get('dependencies', []):
            if dep in graph:
                graph[dep].append(task)
            in_degree[task] += 1
                
    queue = deque([task for task, degree in in_degree.items() if degree == 0])
    
    start_times = {task: 0 for task in tasks}
    processed_count = 0
    
    while queue:
        current = queue.popleft()
        processed_count += 1
        
        current_end_time = start_times[current] + tasks[current].get('duration', 0)
        
        for neighbor in graph[current]:
            if current_end_time > start_times[neighbor]:
                start_times[neighbor] = current_end_time
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    if processed_count != len(tasks):
        raise ValueError("Circular dependency detected.")
        
    total_duration = max((start_times[t] + tasks[t].get('duration', 0) for t in tasks), default=0)
    
    return total_duration, start_times
