def calculate_project_schedule(tasks: dict) -> int:
    if not tasks:
        return 0

    completion_times = {}

    def get_completion_time(task_name):
        if task_name in completion_times:
            return completion_times[task_name]
        
        task = tasks[task_name]
        max_dep_time = 0
        for dep in task.get("dependencies", []):
            dep_time = get_completion_time(dep)
            if dep_time > max_dep_time:
                max_dep_time = dep_time
                
        time = max_dep_time + task.get("duration", 0)
        completion_times[task_name] = time
        return time

    max_time = 0
    for task_name in tasks:
        time = get_completion_time(task_name)
        if time > max_time:
            max_time = time
            
    return max_time
