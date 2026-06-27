def schedule_tasks(tasks):
    task_ids = set()
    durations = {}
    graph = {}
    in_degree = {}
    
    for task in tasks:
        t_id = task['id']
        task_ids.add(t_id)
        durations[t_id] = task['duration']
        graph[t_id] = []
        in_degree[t_id] = 0

    for task in tasks:
        t_id = task['id']
        for dep in task.get('dependencies', []):
            if dep not in task_ids:
                raise ValueError(f"Task {t_id} depends on non-existent task {dep}")
            graph[dep].append(t_id)
            in_degree[t_id] += 1
            
    from collections import deque
    q = deque([t for t in task_ids if in_degree[t] == 0])
    
    start_times = {t: 0 for t in task_ids}
    completed_count = 0
    
    while q:
        curr = q.popleft()
        completed_count += 1
        
        for neighbor in graph[curr]:
            start_times[neighbor] = max(start_times[neighbor], start_times[curr] + durations[curr])
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)
                
    if completed_count != len(task_ids):
        raise ValueError("Circular dependency detected")
        
    total_duration = max((start_times[t] + durations[t] for t in task_ids), default=0)
    
    return {
        "total_duration": total_duration,
        "start_times": start_times
    }
