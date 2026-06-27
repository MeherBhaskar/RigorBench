def calculate_minimum_duration(tasks):
    memo = {}

    def get_time(task):
        if task in memo:
            return memo[task]
        
        max_dep = 0
        for dep in tasks[task]['dependencies']:
            max_dep = max(max_dep, get_time(dep))
            
        memo[task] = tasks[task]['duration'] + max_dep
        return memo[task]

    if not tasks:
        return 0

    return max(get_time(task) for task in tasks)
