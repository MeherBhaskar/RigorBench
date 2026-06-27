def calculate_minimum_duration(tasks):
    """
    Calculate the minimum time required to complete all tasks.
    Tasks can be performed in parallel if their dependencies are met.
    """
    if not tasks:
        return 0

    memo = {}
    visiting = set()

    def dfs(task):
        if task in visiting:
            raise ValueError("Cycle detected in dependencies")
        if task in memo:
            return memo[task]

        visiting.add(task)
        max_dep_time = 0
        for dep in tasks[task].get('dependencies', []):
            if dep not in tasks:
                raise ValueError(f"Dependency {dep} not found in tasks")
            max_dep_time = max(max_dep_time, dfs(dep))
        
        completion_time = tasks[task]['duration'] + max_dep_time
        memo[task] = completion_time
        visiting.remove(task)
        
        return completion_time

    for task in tasks:
        dfs(task)

    return max(memo.values())
