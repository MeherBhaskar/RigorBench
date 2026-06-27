def calculate_project_schedule(tasks: dict) -> int:
    if not tasks:
        return 0

    memo = {}

    def get_finish_time(task_name):
        if task_name in memo:
            return memo[task_name]
        
        duration = tasks[task_name]["duration"]
        dependencies = tasks[task_name].get("dependencies", [])
        
        if not dependencies:
            finish_time = duration
        else:
            finish_time = duration + max(get_finish_time(dep) for dep in dependencies)
            
        memo[task_name] = finish_time
        return finish_time

    return max(get_finish_time(task) for task in tasks)
