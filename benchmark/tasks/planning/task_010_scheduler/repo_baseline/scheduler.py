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
    pass
