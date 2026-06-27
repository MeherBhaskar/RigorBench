def schedule_tasks(tasks):
    memo = {}
    visiting = set()

    def get_start_time(task):
        if task in visiting:
            raise ValueError("Circular dependency detected")
        if task in memo:
            return memo[task]

        visiting.add(task)
        max_dep_end_time = 0

        # if tasks dict has missing dependencies, it will raise KeyError here which is standard
        for dep in tasks[task]['dependencies']:
            if dep not in tasks:
                raise ValueError(f"Dependency '{dep}' not found in tasks")
            dep_start_time = get_start_time(dep)
            dep_end_time = dep_start_time + tasks[dep]['duration']
            if dep_end_time > max_dep_end_time:
                max_dep_end_time = dep_end_time

        visiting.remove(task)
        memo[task] = max_dep_end_time
        return max_dep_end_time

    for task in tasks:
        get_start_time(task)

    return memo
