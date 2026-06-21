"""Markdown reporter for generating human-readable benchmark reports."""
from __future__ import annotations

from pathlib import Path

from rigorbench.models import BenchmarkSummary, RigorResult


class MarkdownReporter:
    """Render RigorBench results as Markdown tables."""

    def report_result(self, result: RigorResult) -> str:
        """Generate a Markdown table of pillar scores for a single result.

        Args:
            result: A ``RigorResult`` instance.

        Returns:
            A Markdown-formatted string with a pillar-score table.
        """
        lines: list[str] = [
            f"## Result: {result.task_id}",
            "",
            "| Pillar | Score | Weight | Weighted |",
            "|--------|------:|-------:|---------:|",
        ]
        for pillar in result.pillar_scores:
            weighted = pillar.score * pillar.weight
            lines.append(
                f"| {pillar.name} | {pillar.score:.3f} | {pillar.weight:.2f} | {weighted:.3f} |"
            )

        lines.append("")
        lines.append(f"**Overall score:** {result.overall_score:.3f}")
        lines.append("")
        return "\n".join(lines)

    def report_summary(self, summary: BenchmarkSummary) -> str:
        """Generate a Markdown summary with header and task-score table.

        Args:
            summary: A ``BenchmarkSummary`` aggregating results for one agent.

        Returns:
            A Markdown-formatted string with a summary table.
        """
        lines: list[str] = [
            f"# Benchmark Summary — {summary.agent_name}",
            "",
            "| Task | Overall Score |",
            "|------|-------------:|",
        ]
        for result in summary.results:
            lines.append(f"| {result.task_id} | {result.overall_score:.3f} |")

        lines.append("")
        lines.append(f"**Mean score:** {summary.mean_score:.3f}")
        lines.append("")
        return "\n".join(lines)

    def report_comparison(self, summaries: list[BenchmarkSummary]) -> str:
        """Generate a Markdown comparison table across multiple agents.

        Each row is a task; each column is an agent's overall score.

        Args:
            summaries: A list of ``BenchmarkSummary`` instances, one per agent.

        Returns:
            A Markdown-formatted comparison table.
        """
        agent_names = [s.agent_name for s in summaries]

        # Collect the union of task IDs in order of first appearance.
        all_task_ids: list[str] = []
        seen: set[str] = set()
        for summary in summaries:
            for result in summary.results:
                if result.task_id not in seen:
                    all_task_ids.append(result.task_id)
                    seen.add(result.task_id)

        # Build lookup: agent_name -> task_id -> score
        lookup: dict[str, dict[str, float]] = {}
        for summary in summaries:
            lookup[summary.agent_name] = {
                r.task_id: r.overall_score for r in summary.results
            }

        # Header
        header = "| Task | " + " | ".join(agent_names) + " |"
        separator = "|------" + "".join("| -----:" for _ in agent_names) + "|"

        lines: list[str] = [
            "# Agent Comparison",
            "",
            header,
            separator,
        ]

        for task_id in all_task_ids:
            cells = [task_id]
            for name in agent_names:
                score = lookup[name].get(task_id)
                cells.append(f"{score:.3f}" if score is not None else "—")
            lines.append("| " + " | ".join(cells) + " |")

        # Mean row
        lines.append(
            "| **Mean** | "
            + " | ".join(f"{s.mean_score:.3f}" for s in summaries)
            + " |"
        )
        lines.append("")
        return "\n".join(lines)

    def save(self, content: str, path: str) -> None:
        """Write Markdown content to a file.

        Creates parent directories if they do not exist.

        Args:
            content: The Markdown string to write.
            path: Destination file path.
        """
        dest = Path(path)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")
