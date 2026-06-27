from typing import List

class Task:
    def __init__(self, task_id: str, duration: int, dependencies: List[str]):
        self.task_id = task_id
        self.duration = duration
        self.dependencies = dependencies

def minimum_completion_time(tasks: List[Task]) -> int:
    if not tasks:
        return 0

    task_dict = {task.task_id: task for task in tasks}
    in_degree = {task.task_id: len(task.dependencies) for task in tasks}
    adj = {task.task_id: [] for task in tasks}

    for task in tasks:
        for dep in task.dependencies:
            if dep in adj:
                adj[dep].append(task.task_id)

    from collections import deque
    queue = deque()
    completion_time = {task.task_id: 0 for task in tasks}

    for task_id, degree in in_degree.items():
        if degree == 0:
            queue.append(task_id)
            completion_time[task_id] = task_dict[task_id].duration

    processed_count = 0

    while queue:
        u = queue.popleft()
        processed_count += 1

        for v in adj[u]:
            completion_time[v] = max(completion_time[v], completion_time[u] + task_dict[v].duration)
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if processed_count < len(tasks):
        return -1

    return max(completion_time.values())
