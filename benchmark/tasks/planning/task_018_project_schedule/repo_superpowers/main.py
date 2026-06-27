from collections import deque

def schedule_tasks(tasks):
    if not tasks:
        return {"total_duration": 0, "start_times": {}}

    task_map = {t['id']: t for t in tasks}
    
    in_degree = {t['id']: 0 for t in tasks}
    adj_list = {t['id']: [] for t in tasks}
    start_times = {t['id']: 0 for t in tasks}
    
    for t in tasks:
        for dep in t['dependencies']:
            if dep not in task_map:
                raise ValueError(f"Dependency '{dep}' not found in tasks")
            adj_list[dep].append(t['id'])
            in_degree[t['id']] += 1
            
    queue = deque([tid for tid in in_degree if in_degree[tid] == 0])
    processed_count = 0
    
    while queue:
        curr = queue.popleft()
        processed_count += 1
        
        curr_finish = start_times[curr] + task_map[curr]['duration']
        
        for neighbor in adj_list[curr]:
            start_times[neighbor] = max(start_times[neighbor], curr_finish)
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    if processed_count != len(tasks):
        raise ValueError("Circular dependency detected")
        
    total_duration = max(start_times[t['id']] + t['duration'] for t in tasks)
    
    return {
        "total_duration": total_duration,
        "start_times": start_times
    }
