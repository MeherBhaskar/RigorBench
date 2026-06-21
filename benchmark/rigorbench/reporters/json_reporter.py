"""JSON reporter for machine-readable benchmark output."""
from __future__ import annotations

import json
from pathlib import Path

from rigorbench.models import BenchmarkSummary, RigorResult


class JsonReporter:
    """Serialize RigorBench results to JSON."""

    def report_result(self, result: RigorResult) -> str:
        """Serialize a single rigor result to a JSON string.

        Args:
            result: A ``RigorResult`` instance.

        Returns:
            A pretty-printed JSON string representing the result.
        """
        payload = {
            "task_id": result.task_id,
            "overall_score": result.overall_score,
            "pillar_scores": [
                {
                    "name": p.name,
                    "score": p.score,
                    "weight": p.weight,
                    "weighted_score": p.score * p.weight,
                }
                for p in result.pillar_scores
            ],
        }
        return json.dumps(payload, indent=2)

    def report_summary(self, summary: BenchmarkSummary) -> str:
        """Serialize a benchmark summary to a JSON string.

        Args:
            summary: A ``BenchmarkSummary`` aggregating results for one agent.

        Returns:
            A pretty-printed JSON string representing the summary.
        """
        payload = {
            "agent_name": summary.agent_name,
            "mean_score": summary.mean_score,
            "results": [
                {
                    "task_id": r.task_id,
                    "overall_score": r.overall_score,
                    "pillar_scores": [
                        {
                            "name": p.name,
                            "score": p.score,
                            "weight": p.weight,
                            "weighted_score": p.score * p.weight,
                        }
                        for p in r.pillar_scores
                    ],
                }
                for r in summary.results
            ],
        }
        return json.dumps(payload, indent=2)

    def save(self, data: str, path: str) -> None:
        """Write a JSON string to a file.

        Creates parent directories if they do not exist.

        Args:
            data: The JSON string to write.
            path: Destination file path.
        """
        dest = Path(path)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(data, encoding="utf-8")
