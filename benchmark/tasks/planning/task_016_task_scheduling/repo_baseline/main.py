def calculate_start_times(tasks):
    start_times = {}
    in_degree = {task: 0 for task in tasks}
    graph = {task: [] for task in tasks}

    for task, info in tasks.items():
        for dep in info['dependencies']:
            if dep not in tasks:
                continue
            graph[dep].append(task)
            in_degree[task] += 1

    queue = [task for task in tasks if in_degree[task] == 0]
    processed_count = 0
    
    for task in queue:
        start_times[task] = 0

    while queue:
        curr = queue.pop(0)
        processed_count += 1
        
        curr_finish = start_times[curr] + tasks[curr]['duration']
        
        for neighbor in graph[curr]:
            start_times[neighbor] = max(start_times.get(neighbor, 0), curr_finish)
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if processed_count != len(tasks):
        raise ValueError("Cycle detected")

    return start_times
