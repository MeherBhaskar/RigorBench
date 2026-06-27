def schedule_tasks(tasks):
    start_times = {}
    visiting = set()

    def get_start_time(task_name):
        if task_name in start_times:
            return start_times[task_name]
        
        if task_name in visiting:
            raise ValueError("Circular dependency detected")
        
        visiting.add(task_name)
        
        max_dep_end_time = 0
        for dep in tasks[task_name]["dependencies"]:
            if dep not in tasks:
                raise ValueError(f"Dependency '{dep}' not found in tasks")
            dep_start = get_start_time(dep)
            dep_end = dep_start + tasks[dep]["duration"]
            if dep_end > max_dep_end_time:
                max_dep_end_time = dep_end
        
        visiting.remove(task_name)
        start_times[task_name] = max_dep_end_time
        return max_dep_end_time

    for task in tasks:
        get_start_time(task)

    return start_times
