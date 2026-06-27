def schedule_tasks(tasks):
    start_times = {}
    visiting = set()

    def get_start_time(task):
        if task in start_times:
            return start_times[task]
        if task in visiting:
            raise ValueError("Circular dependency")
        
        visiting.add(task)
        
        earliest = 0
        for dep in tasks[task].get("dependencies", []):
            if dep not in tasks:
                raise ValueError(f"Missing dependency: {dep}")
            dep_start = get_start_time(dep)
            earliest = max(earliest, dep_start + tasks[dep]["duration"])
            
        visiting.remove(task)
        start_times[task] = earliest
        return earliest

    for task in tasks:
        get_start_time(task)
        
    return start_times
