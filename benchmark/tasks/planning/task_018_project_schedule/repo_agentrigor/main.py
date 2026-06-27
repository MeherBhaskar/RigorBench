from collections import deque

def schedule_tasks(tasks):
    if not tasks:
        return {"total_duration": 0, "start_times": {}}

    task_ids = {task['id'] for task in tasks}
    
    for task in tasks:
        for dep in task['dependencies']:
            if dep not in task_ids:
                raise ValueError(f"Missing dependency: {dep}")

    graph = {tid: [] for tid in task_ids}
    in_degree = {tid: 0 for tid in task_ids}
    durations = {task['id']: task['duration'] for task in tasks}
    start_times = {tid: 0 for tid in task_ids}

    for task in tasks:
        tid = task['id']
        for dep in task['dependencies']:
            graph[dep].append(tid)
            in_degree[tid] += 1

    queue = deque([tid for tid in task_ids if in_degree[tid] == 0])

    processed_count = 0
    max_completion_time = 0

    while queue:
        curr = queue.popleft()
        processed_count += 1
        comp_time = start_times[curr] + durations[curr]
        if comp_time > max_completion_time:
            max_completion_time = comp_time

        for nxt in graph[curr]:
            start_times[nxt] = max(start_times[nxt], comp_time)
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    if processed_count != len(tasks):
        raise ValueError("Cycle detected")

    return {
        "total_duration": max_completion_time,
        "start_times": start_times
    }
