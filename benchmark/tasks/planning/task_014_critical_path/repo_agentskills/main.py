def calculate_minimum_duration(tasks):
    if not tasks:
        return 0

    memo = {}

    def get_duration(task_name):
        if task_name in memo:
            return memo[task_name]
        
        task = tasks[task_name]
        dependencies = task.get('dependencies', [])
        
        max_dep_duration = 0
        if dependencies:
            max_dep_duration = max(get_duration(dep) for dep in dependencies)
            
        result = task['duration'] + max_dep_duration
        memo[task_name] = result
        return result

    return max(get_duration(task_name) for task_name in tasks)
