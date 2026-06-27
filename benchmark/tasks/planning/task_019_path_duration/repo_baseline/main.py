def min_project_duration(tasks):
    if not tasks:
        return 0

    memo = {}

    def get_completion_time(task_name):
        if task_name in memo:
            return memo[task_name]

        task = tasks[task_name]
        max_dep_time = 0
        for dep in task['dependencies']:
            max_dep_time = max(max_dep_time, get_completion_time(dep))

        completion_time = max_dep_time + task['duration']
        memo[task_name] = completion_time
        return completion_time

    return max(get_completion_time(t) for t in tasks)
