from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any

@dataclass
class PillarScore:
    """Score for a single measurement pillar."""
    pillar_name: str
    score: float  # 0 to 100
    breakdown: Dict[str, float] = field(default_factory=dict)
    evidence: List[str] = field(default_factory=list)

@dataclass
class RigorResult:
    """Full benchmark result for a single task run."""
    task_id: str
    agent: str
    rigor_enabled: bool
    pillar_scores: Dict[str, PillarScore]
    composite_score: float
    trajectory_path: str

@dataclass
class BenchmarkSummary:
    """Summary of benchmark runs across multiple tasks."""
    agent: str
    task_suite: str
    results: List[RigorResult]
    
    @property
    def aggregate_score(self) -> float:
        if not self.results:
            return 0.0
        return sum(r.composite_score for r in self.results) / len(self.results)
