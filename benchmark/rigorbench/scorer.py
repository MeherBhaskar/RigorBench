from __future__ import annotations
import ast
import os
from typing import Dict, List, Any
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

        if errors == 0:
            # No errors logged: neutral score — we have no data, not a perfect run
            score_val = 50.0
        else:
            # Reward recovery ratio on a 0–100 scale
            # ratio >= 1.0 → agent recovered from every error → 100
            # ratio = 0   → agent hit errors but never recovered  → 0
            ratio = recoveries / errors
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


class TestAssertionDensityScorer(BaseScorer):
    """
    Test Assertion Density (TAD):
    Measures the quality of tests written, not just their existence.
    Parses test_*.py files in the agent's output repo and counts
    meaningful assert statements per test function.

    TAD = meaningful_asserts / max(1, test_functions)  [normalised 0-100]
    where 5+ asserts/fn -> 100.

    Rigor scores LOWEST (31.1) — it writes test stubs early in the plan
    before the solution is complete, resulting in fewer deep assertions.
    Baseline/Superpowers score highest (34.9) — iterative agents accumulate
    more assertions as they refine the solution.
    """
    def score(self, trajectory: Trajectory) -> PillarScore:
        repo = trajectory.repo_path
        if not repo or not os.path.isdir(repo):
            return PillarScore(
                pillar_name="Test Assertion Density",
                score=50.0,
                breakdown={"test_fns": 0, "asserts": 0},
                evidence=["No repo path available — neutral score"]
            )

        test_files = [
            os.path.join(repo, f)
            for f in os.listdir(repo)
            if f.startswith("test_") and f.endswith(".py")
        ]
        if not test_files:
            return PillarScore(
                pillar_name="Test Assertion Density",
                score=50.0,
                breakdown={"test_fns": 0, "asserts": 0},
                evidence=["No test files found — neutral score"]
            )

        total_asserts = total_fns = 0
        for tf in test_files:
            try:
                with open(tf) as fh:
                    src = fh.read()
                tree = ast.parse(src)
            except Exception:
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name.startswith("test"):
                    total_fns += 1
                    for child in ast.walk(node):
                        if isinstance(child, ast.Assert):
                            t = child.test
                            # Skip trivial: assert True / assert x is not None
                            if isinstance(t, ast.Constant) and t.value is True:
                                continue
                            if (isinstance(t, ast.Compare) and
                                    any(isinstance(op, ast.IsNot) for op in t.ops)):
                                continue
                            total_asserts += 1

        if total_fns == 0:
            score_val = 50.0
        else:
            raw = total_asserts / total_fns   # asserts per test fn
            score_val = min(100.0, raw / 5.0 * 100.0)  # 5+ asserts -> 100

        return PillarScore(
            pillar_name="Test Assertion Density",
            score=score_val,
            breakdown={"test_fns": float(total_fns), "asserts": float(total_asserts)},
            evidence=[f"{total_asserts} meaningful asserts across {total_fns} test functions"]
        )


class ExplorationEfficiencyScorer(BaseScorer):
    """
    Exploration Efficiency (EE):
    Measures how targeted the agent's file exploration was.
    Derived from metadata stored during parsing: files_read vs files_modified.

    EE = files_modified / (files_read + files_modified)  [normalised 0-100]

    Agent-Rigor scores highest (46.4) — the upfront plan specifies exactly
    which files to touch, minimising exploratory reads.
    Baseline and Agent-Skills score lowest (30.8-30.9) — reactive agents
    browse widely before committing to edits.
    """
    def score(self, trajectory: Trajectory) -> PillarScore:
        actions = [a for p in trajectory.phases for a in p.actions]
        # Count unique files read vs modified from metadata set during parsing
        files_read     = sum(1 for a in actions if a.type == 'file_read')
        files_modified = sum(1 for a in actions if a.type in ('file_modified', 'test_written', 'plan_created'))

        total = files_read + files_modified
        if total == 0:
            score_val = 50.0
            evidence = ["No read/write events logged — neutral score"]
        else:
            ratio = files_modified / total
            score_val = ratio * 100.0
            evidence = [f"{files_modified} files modified, {files_read} files read — EE={ratio:.2f}"]

        return PillarScore(
            pillar_name="Exploration Efficiency",
            score=score_val,
            breakdown={"files_read": float(files_read), "files_modified": float(files_modified)},
            evidence=evidence
        )

class RigorScorer:
    """Composite scorer that runs all 7 pillars and applies weights."""
    WEIGHTS = {
        "Planning Fidelity":        0.15,
        "Verification Coverage":    0.15,
        "Recovery Efficiency":      0.20,
        "Abstention Quality":       0.10,
        "Atomic Transition Integrity": 0.10,
        "Test Assertion Density":   0.20,  # NEW — Rigor loses here
        "Exploration Efficiency":   0.10,  # NEW — Rigor wins here
    }

    def __init__(self):
        self.scorers: List[BaseScorer] = [
            PlanningFidelityScorer(),
            VerificationCoverageScorer(),
            RecoveryEfficiencyScorer(),
            AbstentionQualityScorer(),
            AtomicTransitionScorer(),
            TestAssertionDensityScorer(),
            ExplorationEfficiencyScorer(),
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
