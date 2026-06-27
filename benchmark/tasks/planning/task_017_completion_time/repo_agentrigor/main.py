from typing import List

class Task:
    def __init__(self, task_id: str, duration: int, dependencies: List[str]):
        self.task_id = task_id
        self.duration = duration
        self.dependencies = dependencies

def minimum_completion_time(tasks: List[Task]) -> int:
    task_dict = {task.task_id: task for task in tasks}
    memo = {}
    visiting = set()
    
    def get_time(task_id: str) -> int:
        if task_id not in task_dict:
            return -1 # Dependency not found
        if task_id in visiting:
            return -1 # Cycle detected
        if task_id in memo:
            return memo[task_id]
        
        visiting.add(task_id)
        task = task_dict[task_id]
        
        max_dep_time = 0
        for dep in task.dependencies:
            dep_time = get_time(dep)
            if dep_time == -1:
                return -1
            max_dep_time = max(max_dep_time, dep_time)
            
        visiting.remove(task_id)
        memo[task_id] = task.duration + max_dep_time
        return memo[task_id]

    max_time = 0
    for task in tasks:
        time = get_time(task.task_id)
        if time == -1:
            return -1
        max_time = max(max_time, time)
        
    return max_time
