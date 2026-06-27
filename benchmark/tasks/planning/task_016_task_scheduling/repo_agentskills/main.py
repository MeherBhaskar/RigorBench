def calculate_start_times(tasks):
    start_times = {}
    visiting = set()

    def get_start_time(task):
        if task in visiting:
            raise ValueError("Cycle detected")
        if task in start_times:
            return start_times[task]

        visiting.add(task)
        max_end_time = 0
        for dep in tasks[task].get("dependencies", []):
            dep_end_time = get_start_time(dep) + tasks[dep]["duration"]
            if dep_end_time > max_end_time:
                max_end_time = dep_end_time

        visiting.remove(task)
        start_times[task] = max_end_time
        return max_end_time

    for task in tasks:
        get_start_time(task)

    return start_times
