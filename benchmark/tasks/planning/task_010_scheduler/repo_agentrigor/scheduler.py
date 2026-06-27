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
    start_times = {}
    visiting = set()

    def get_start_time(task_id):
        if task_id in visiting:
            raise ValueError("Circular dependency detected")
        if task_id in start_times:
            return start_times[task_id]
        
        visiting.add(task_id)
        
        task = tasks.get(task_id)
        if task is None:
            raise KeyError(f"Task {task_id} not found")
            
        max_dep_time = 0
        for dep in task.get('dependencies', []):
            max_dep_time = max(max_dep_time, get_start_time(dep) + tasks[dep]['duration'])
            
        visiting.remove(task_id)
        start_times[task_id] = max_dep_time
        return max_dep_time

    total_duration = 0
    for task_id in tasks:
        start_time = get_start_time(task_id)
        total_duration = max(total_duration, start_time + tasks[task_id]['duration'])
        
    return total_duration, start_times
