from typing import List

class Task:
    def __init__(self, task_id: str, duration: int, dependencies: List[str]):
        self.task_id = task_id
        self.duration = duration
        self.dependencies = dependencies

def minimum_completion_time(tasks: List[Task]) -> int:
    if not tasks:
        return 0

    task_map = {task.task_id: task for task in tasks}
    in_degree = {task.task_id: len(task.dependencies) for task in tasks}
    adj = {task.task_id: [] for task in tasks}

    for task in tasks:
        for dep in task.dependencies:
            if dep in adj:
                adj[dep].append(task.task_id)

    queue = [task_id for task_id, degree in in_degree.items() if degree == 0]
    completion_times = {task_id: 0 for task_id in task_map}

    for task_id in queue:
        completion_times[task_id] = task_map[task_id].duration

    processed_count = 0

    while queue:
        curr = queue.pop(0)
        processed_count += 1

        for neighbor in adj[curr]:
            in_degree[neighbor] -= 1
            completion_times[neighbor] = max(
                completion_times[neighbor],
                completion_times[curr] + task_map[neighbor].duration
            )
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if processed_count < len(tasks):
        return -1

    return max(completion_times.values())
