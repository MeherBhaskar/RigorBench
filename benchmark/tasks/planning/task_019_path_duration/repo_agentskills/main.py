def min_project_duration(tasks):
    if not tasks:
        return 0

    finish_times = {}

    def get_finish_time(task_name):
        if task_name in finish_times:
            return finish_times[task_name]
        
        task = tasks[task_name]
        dependencies = task.get('dependencies', [])
        duration = task.get('duration', 0)
        
        if not dependencies:
            finish_times[task_name] = duration
        else:
            max_dep_finish = max(get_finish_time(dep) for dep in dependencies)
            finish_times[task_name] = max_dep_finish + duration
            
        return finish_times[task_name]

    return max(get_finish_time(task_name) for task_name in tasks)
