from typing import List

class Task:
    def __init__(self, task_id: str, duration: int, dependencies: List[str]):
        self.task_id = task_id
        self.duration = duration
        self.dependencies = dependencies

def minimum_completion_time(tasks: List[Task]) -> int:
    task_map = {task.task_id: task for task in tasks}
    memo = {}
    visiting = set()

    def get_end_time(task_id: str) -> int:
        if task_id in visiting:
            return -1
        if task_id in memo:
            return memo[task_id]

        visiting.add(task_id)
        task = task_map.get(task_id)
        if task is None:
            visiting.remove(task_id)
            return 0
        
        max_dep_time = 0
        for dep in task.dependencies:
            dep_time = get_end_time(dep)
            if dep_time == -1:
                return -1
            if dep_time > max_dep_time:
                max_dep_time = dep_time
                
        end_time = max_dep_time + task.duration
        visiting.remove(task_id)
        memo[task_id] = end_time
        return end_time

    max_time = 0
    for task in tasks:
        t = get_end_time(task.task_id)
        if t == -1:
            return -1
        if t > max_time:
            max_time = t

    return max_time
