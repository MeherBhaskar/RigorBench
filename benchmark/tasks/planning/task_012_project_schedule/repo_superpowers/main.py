def calculate_project_schedule(tasks: dict) -> int:
    if not tasks:
        return 0
        
    memo = {}
    
    def get_time(task_name):
        if task_name in memo:
            return memo[task_name]
        
        task = tasks[task_name]
        deps = task.get("dependencies", [])
        
        if not deps:
            memo[task_name] = task["duration"]
        else:
            max_dep_time = max(get_time(dep) for dep in deps)
            memo[task_name] = max_dep_time + task["duration"]
            
        return memo[task_name]
        
    max_time = 0
    for task in tasks:
        max_time = max(max_time, get_time(task))
        
    return max_time
