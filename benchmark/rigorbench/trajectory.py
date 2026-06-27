from __future__ import annotations
import os
import yaml
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Any
from datetime import datetime

_TASKS_DIR = os.path.join(os.path.dirname(__file__), '..', 'tasks')

_HARNESS_REPO = {
    'agent-rigor':    'repo_agentrigor',
    'agentrigor':     'repo_agentrigor',
    'superpowers':    'repo_superpowers',
    'superpowersharness': 'repo_superpowers',
    'agent-skills':   'repo_agentskills',
    'agentskills':    'repo_agentskills',
    'baseline':       'repo_baseline',
    'baseline react': 'repo_baseline',
}

def _find_repo(task_id: str, agent_name: str) -> Optional[str]:
    key = agent_name.lower()
    repo_dir = next((v for k, v in _HARNESS_REPO.items() if k in key), None)
    if not repo_dir:
        return None
    tasks_root = os.path.abspath(_TASKS_DIR)
    for cat in os.listdir(tasks_root):
        candidate = os.path.join(tasks_root, cat, task_id, repo_dir)
        if os.path.isdir(candidate):
            return candidate
    return None

@dataclass
class Action:
    """A single observable action taken by the agent."""
    type: str  # e.g., 'plan_created', 'file_modified', 'error_encountered'
    timestamp: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    
@dataclass
class Phase:
    """A phase of the agent's workflow."""
    name: str
    started_at: str
    actions: List[Action] = field(default_factory=list)

@dataclass
class Trajectory:
    """The complete execution path of an agent on a task."""
    task_id: str
    agent_name: str
    rigor_enabled: bool
    total_tokens: int
    duration_seconds: int
    phases: List[Phase] = field(default_factory=list)
    repo_path: Optional[str] = field(default=None, repr=False)  # resolved at load time

class TrajectoryLogger:
    """Logs agent actions into a Trajectory and serializes to YAML."""
    def __init__(self, task_id: str, agent_name: str, rigor_enabled: bool):
        self.trajectory = Trajectory(
            task_id=task_id,
            agent_name=agent_name,
            rigor_enabled=rigor_enabled,
            total_tokens=0,
            duration_seconds=0
        )
        self.start_time = datetime.now()
        self.current_phase: Optional[Phase] = None

    def start_phase(self, name: str):
        self.current_phase = Phase(name=name, started_at=datetime.now().isoformat())
        self.trajectory.phases.append(self.current_phase)

    def log_action(self, action_type: str, metadata: Dict[str, Any] = None):
        if not self.current_phase:
            self.start_phase("execution")
        
        action = Action(
            type=action_type,
            timestamp=datetime.now().isoformat(),
            metadata=metadata or {}
        )
        self.current_phase.actions.append(action)

    def finish(self, tokens: int):
        self.trajectory.total_tokens = tokens
        self.trajectory.duration_seconds = int((datetime.now() - self.start_time).total_seconds())

    def save(self, filepath: str):
        with open(filepath, 'w') as f:
            yaml.dump(asdict(self.trajectory), f, sort_keys=False)

class TrajectoryLoader:
    """Loads a Trajectory from a YAML file."""
    @staticmethod
    def load(filepath: str) -> Trajectory:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
        
        phases = []
        for p_data in data.get('phases', []):
            actions = [Action(**a) for a in p_data.get('actions', [])]
            phases.append(Phase(name=p_data['name'], started_at=p_data['started_at'], actions=actions))
            
        task_id   = data['task_id']
        agent_name = data['agent_name']
        return Trajectory(
            task_id=task_id,
            agent_name=agent_name,
            rigor_enabled=data['rigor_enabled'],
            total_tokens=data.get('total_tokens', 0),
            duration_seconds=data.get('duration_seconds', 0),
            phases=phases,
            repo_path=_find_repo(task_id, agent_name),
        )
