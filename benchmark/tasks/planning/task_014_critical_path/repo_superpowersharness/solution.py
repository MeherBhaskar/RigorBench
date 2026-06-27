def calculate_minimum_duration(tasks):
    memo = {}
    visiting = set()

    def get_completion_time(task_name):
        if task_name in memo:
            return memo[task_name]
        if task_name in visiting:
            raise ValueError(f"Cycle detected involving task {task_name}")
        
        visiting.add(task_name)
        task = tasks[task_name]
        duration = task.get('duration', 0)
        dependencies = task.get('dependencies', [])
        
        if not dependencies:
            completion_time = duration
        else:
            max_dep_time = max(get_completion_time(dep) for dep in dependencies)
            completion_time = duration + max_dep_time
            
        visiting.remove(task_name)
        memo[task_name] = completion_time
        return completion_time

    if not tasks:
        return 0

    return max(get_completion_time(task) for task in tasks)
