from typing import List

class Task:
    def __init__(self, task_id: str, duration: int, dependencies: List[str]):
        self.task_id = task_id
        self.duration = duration
        self.dependencies = dependencies

def minimum_completion_time(tasks: List[Task]) -> int:
    # Your code here
    pass
