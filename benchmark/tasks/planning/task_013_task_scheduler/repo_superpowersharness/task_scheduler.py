def schedule_tasks(tasks):
    start_times = {}
    
    # 0 = unvisited, 1 = visiting, 2 = visited
    state = {task: 0 for task in tasks}

    def get_start_time(task):
        if state[task] == 1:
            raise ValueError("Circular dependency detected")
        
        if state[task] == 2:
            return start_times[task]

        state[task] = 1
        
        max_dep_end_time = 0
        for dep in tasks[task]['dependencies']:
            if dep not in tasks:
                raise ValueError(f"Dependency '{dep}' not found in tasks")
            dep_start = get_start_time(dep)
            dep_end = dep_start + tasks[dep]['duration']
            max_dep_end_time = max(max_dep_end_time, dep_end)

        start_times[task] = max_dep_end_time
        state[task] = 2
        return start_times[task]

    for task in tasks:
        if state[task] == 0:
            get_start_time(task)

    return start_times
