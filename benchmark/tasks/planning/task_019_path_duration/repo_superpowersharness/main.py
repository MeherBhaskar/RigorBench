def min_project_duration(tasks):
    if not tasks:
        return 0

    memo = {}

    def get_completion_time(task_name):
        if task_name in memo:
            return memo[task_name]
        
        task_info = tasks[task_name]
        duration = task_info.get("duration", 0)
        dependencies = task_info.get("dependencies", [])
        
        max_dep_time = 0
        for dep in dependencies:
            max_dep_time = max(max_dep_time, get_completion_time(dep))
            
        completion_time = max_dep_time + duration
        memo[task_name] = completion_time
        return completion_time

    max_duration = 0
    for task_name in tasks:
        max_duration = max(max_duration, get_completion_time(task_name))

    return max_duration
