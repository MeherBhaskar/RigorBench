from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
import yaml
import os

@dataclass
class Task:
    id: str
    name: str
    category: str
    description: str
    difficulty: str
    repo_path: str
    requirements: List[str] = field(default_factory=list)
    rubric: Dict[str, Any] = field(default_factory=dict)
    golden_solution_path: Optional[str] = None

class TaskSuite:
    def __init__(self, directory: str):
        self.directory = directory
        self.tasks: List[Task] = []
        self._load_tasks()

    def _load_tasks(self):
        if not os.path.exists(self.directory):
            return
        for root, _, files in os.walk(self.directory):
            if 'task.yaml' in files:
                with open(os.path.join(root, 'task.yaml'), 'r') as f:
                    data = yaml.safe_load(f)
                    
                rubric_path = os.path.join(root, 'rubric.yaml')
                rubric = {}
                if os.path.exists(rubric_path):
                    with open(rubric_path, 'r') as f:
                        rubric = yaml.safe_load(f)
                        
                task = Task(
                    id=data['id'],
                    name=data['name'],
                    category=data['category'],
                    description=data['description'],
                    difficulty=data.get('difficulty', 'medium'),
                    repo_path=os.path.join(root, 'repo'),
                    requirements=data.get('requirements', []),
                    rubric=rubric
                )
                self.tasks.append(task)

    def get_task(self, task_id: str) -> Optional[Task]:
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None
