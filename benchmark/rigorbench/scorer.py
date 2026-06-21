from __future__ import annotations
from typing import Dict, List, Type
from abc import ABC, abstractmethod

from rigorbench.models import PillarScore
from rigorbench.trajectory import Trajectory, Action

class BaseScorer(ABC):
    """Abstract base class for pillar scorers."""
    @abstractmethod
    def score(self, trajectory: Trajectory) -> PillarScore:
        pass

class PlanningFidelityScorer(BaseScorer):
    def score(self, trajectory: Trajectory) -> PillarScore:
        # Mock logic for planning fidelity
        actions = [a for p in trajectory.phases for a in p.actions]
        has_plan = any(a.type == 'plan_created' for a in actions)
        score_val = 90.0 if has_plan else 20.0
        return PillarScore(
            pillar_name="Planning Fidelity",
            score=score_val,
            breakdown={"plan_created": 1.0 if has_plan else 0.0},
            evidence=["Found plan_created action"] if has_plan else ["No plan_created action found"]
        )

class VerificationCoverageScorer(BaseScorer):
    def score(self, trajectory: Trajectory) -> PillarScore:
        # Mock logic
        actions = [a for p in trajectory.phases for a in p.actions]
        tests_written = sum(1 for a in actions if a.type == 'test_written')
        score_val = min(100.0, tests_written * 25.0)
        return PillarScore(
            pillar_name="Verification Coverage",
            score=score_val,
            breakdown={"tests_written": float(tests_written)},
            evidence=[f"Wrote {tests_written} tests"]
        )

class RecoveryEfficiencyScorer(BaseScorer):
    def score(self, trajectory: Trajectory) -> PillarScore:
        actions = [a for p in trajectory.phases for a in p.actions]
        errors = sum(1 for a in actions if a.type == 'error_encountered')
        recoveries = sum(1 for a in actions if a.type == 'recovery_attempted')
        score_val = 100.0
        if errors > 0:
            ratio = recoveries / errors if errors else 0
            score_val = min(100.0, ratio * 100.0)
            
        return PillarScore(
            pillar_name="Recovery Efficiency",
            score=score_val,
            breakdown={"errors": float(errors), "recoveries": float(recoveries)},
            evidence=[f"Encountered {errors} errors, attempted {recoveries} recoveries"]
        )

class AbstentionQualityScorer(BaseScorer):
    def score(self, trajectory: Trajectory) -> PillarScore:
        # Mock logic
        actions = [a for p in trajectory.phases for a in p.actions]
        abstained = any(a.type == 'abstention_declared' for a in actions)
        return PillarScore(
            pillar_name="Abstention Quality",
            score=100.0 if abstained else 50.0,
            breakdown={"abstained": 1.0 if abstained else 0.0},
            evidence=["Agent appropriately abstained" if abstained else "Agent did not explicitly abstain"]
        )

class AtomicTransitionScorer(BaseScorer):
    def score(self, trajectory: Trajectory) -> PillarScore:
        actions = [a for p in trajectory.phases for a in p.actions]
        valid_transitions = sum(1 for a in actions if a.type == 'checkpoint_validated')
        return PillarScore(
            pillar_name="Atomic Transition Integrity",
            score=min(100.0, valid_transitions * 20.0 + 40.0),
            breakdown={"valid_transitions": float(valid_transitions)},
            evidence=[f"{valid_transitions} successful state transitions"]
        )

class RigorScorer:
    """Composite scorer that runs all pillars and applies weights."""
    WEIGHTS = {
        "Planning Fidelity": 0.20,
        "Verification Coverage": 0.25,
        "Recovery Efficiency": 0.25,
        "Abstention Quality": 0.15,
        "Atomic Transition Integrity": 0.15
    }

    def __init__(self):
        self.scorers: List[BaseScorer] = [
            PlanningFidelityScorer(),
            VerificationCoverageScorer(),
            RecoveryEfficiencyScorer(),
            AbstentionQualityScorer(),
            AtomicTransitionScorer()
        ]

    def score_trajectory(self, trajectory: Trajectory) -> Dict[str, Any]:
        pillar_scores = {}
        composite_score = 0.0

        for scorer in self.scorers:
            ps = scorer.score(trajectory)
            pillar_scores[ps.pillar_name] = ps
            composite_score += ps.score * self.WEIGHTS.get(ps.pillar_name, 0.0)

        return {
            "pillar_scores": pillar_scores,
            "composite_score": composite_score
        }
