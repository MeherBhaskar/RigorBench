from collections import deque

def schedule_tasks(tasks):
    if not tasks:
        return {"total_duration": 0, "start_times": {}}

    task_by_id = {t["id"]: t for t in tasks}
    adj = {t["id"]: [] for t in tasks}
    indegree = {t["id"]: 0 for t in tasks}
    start_times = {t["id"]: 0 for t in tasks}

    for t in tasks:
        for dep in t["dependencies"]:
            if dep not in task_by_id:
                raise ValueError(f"Task {t['id']} depends on unknown task {dep}")
            adj[dep].append(t["id"])
            indegree[t["id"]] += 1

    queue = deque([t["id"] for t in tasks if indegree[t["id"]] == 0])
    completed_count = 0

    while queue:
        curr = queue.popleft()
        completed_count += 1
        curr_end_time = start_times[curr] + task_by_id[curr]["duration"]

        for neighbor in adj[curr]:
            if curr_end_time > start_times[neighbor]:
                start_times[neighbor] = curr_end_time
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if completed_count < len(tasks):
        raise ValueError("Circular dependency detected")

    total_duration = max(start_times[t["id"]] + t["duration"] for t in tasks)

    return {
        "total_duration": total_duration,
        "start_times": start_times
    }
