def calculate_start_times(tasks):
    from collections import deque

    indegrees = {task: 0 for task in tasks}
    start_times = {task: 0 for task in tasks}
    graph = {task: [] for task in tasks}

    for task, data in tasks.items():
        dependencies = data.get("dependencies", [])
        indegrees[task] = len(dependencies)
        for dep in dependencies:
            if dep in graph:
                graph[dep].append(task)
            else:
                # If a dependency is not in the tasks dictionary, we might want to handle it.
                # Assuming all dependencies exist in the tasks dict based on standard inputs.
                graph[dep] = [task]

    queue = deque([task for task, ind in indegrees.items() if ind == 0])
    processed_nodes = 0

    while queue:
        current = queue.popleft()
        processed_nodes += 1
        
        duration = tasks[current].get("duration", 0)
        
        for neighbor in graph[current]:
            # Update the start time of the neighbor
            if start_times[neighbor] < start_times[current] + duration:
                start_times[neighbor] = start_times[current] + duration
            
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    if processed_nodes < len(tasks):
        raise ValueError("Cycle detected")

    return start_times
