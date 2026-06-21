"""Console reporter using rich tables for terminal output."""
from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from rigorbench.models import BenchmarkSummary, RigorResult


def _score_style(score: float) -> str:
    """Return a rich style string based on the score value.

    Args:
        score: A float between 0.0 and 1.0.

    Returns:
        A rich markup style string — green for ≥ 0.8, yellow for ≥ 0.5,
        red for < 0.5.
    """
    if score >= 0.8:
        return "bold green"
    if score >= 0.5:
        return "bold yellow"
    return "bold red"


class ConsoleReporter:
    """Render RigorBench results as rich tables in the terminal."""

    def __init__(self) -> None:
        self._console = Console()

    # ------------------------------------------------------------------
    # Single result
    # ------------------------------------------------------------------

    def report_result(self, result: RigorResult) -> None:
        """Print a single rigor result with a rich table.

        The table shows each pillar's score, its weight, and the weighted
        contribution to the overall score.

        Args:
            result: A ``RigorResult`` instance to display.
        """
        table = Table(
            title=f"Rigor Result — {result.task_id}",
            show_header=True,
            header_style="bold cyan",
        )
        table.add_column("Pillar", style="dim", min_width=20)
        table.add_column("Score", justify="right", min_width=10)
        table.add_column("Weight", justify="right", min_width=10)
        table.add_column("Weighted", justify="right", min_width=10)

        for pillar in result.pillar_scores:
            score = pillar.score
            weight = pillar.weight
            weighted = score * weight
            style = _score_style(score)
            table.add_row(
                pillar.name,
                f"[{style}]{score:.3f}[/{style}]",
                f"{weight:.2f}",
                f"[{style}]{weighted:.3f}[/{style}]",
            )

        table.add_section()
        overall_style = _score_style(result.overall_score)
        table.add_row(
            "Overall",
            f"[{overall_style}]{result.overall_score:.3f}[/{overall_style}]",
            "",
            "",
        )

        self._console.print(Panel(table, border_style="blue"))

    # ------------------------------------------------------------------
    # Summary across tasks
    # ------------------------------------------------------------------

    def report_summary(self, summary: BenchmarkSummary) -> None:
        """Print a summary table with all tasks and mean scores.

        Args:
            summary: A ``BenchmarkSummary`` aggregating results for one agent.
        """
        table = Table(
            title=f"Benchmark Summary — {summary.agent_name}",
            show_header=True,
            header_style="bold magenta",
        )
        table.add_column("Task", style="dim", min_width=25)
        table.add_column("Overall Score", justify="right", min_width=15)

        for result in summary.results:
            style = _score_style(result.overall_score)
            table.add_row(
                result.task_id,
                f"[{style}]{result.overall_score:.3f}[/{style}]",
            )

        table.add_section()
        mean_style = _score_style(summary.mean_score)
        table.add_row(
            "[bold]Mean[/bold]",
            f"[{mean_style}]{summary.mean_score:.3f}[/{mean_style}]",
        )

        self._console.print(Panel(table, border_style="magenta"))

    # ------------------------------------------------------------------
    # Agent comparison
    # ------------------------------------------------------------------

    def report_comparison(self, summaries: list[BenchmarkSummary]) -> None:
        """Compare multiple agents side by side in a single table.

        Each row is a task; each column is an agent's overall score for that
        task, plus a final row for the mean.

        Args:
            summaries: A list of ``BenchmarkSummary`` instances, one per agent.
        """
        table = Table(
            title="Agent Comparison",
            show_header=True,
            header_style="bold cyan",
        )
        table.add_column("Task", style="dim", min_width=25)
        for summary in summaries:
            table.add_column(summary.agent_name, justify="right", min_width=12)

        # Collect the union of task IDs in order of first appearance.
        all_task_ids: list[str] = []
        seen: set[str] = set()
        for summary in summaries:
            for result in summary.results:
                if result.task_id not in seen:
                    all_task_ids.append(result.task_id)
                    seen.add(result.task_id)

        # Build a lookup: agent_name -> task_id -> overall_score
        lookup: dict[str, dict[str, float]] = {}
        for summary in summaries:
            lookup[summary.agent_name] = {
                r.task_id: r.overall_score for r in summary.results
            }

        for task_id in all_task_ids:
            row: list[str] = [task_id]
            for summary in summaries:
                score = lookup[summary.agent_name].get(task_id)
                if score is not None:
                    style = _score_style(score)
                    row.append(f"[{style}]{score:.3f}[/{style}]")
                else:
                    row.append("[dim]—[/dim]")
            table.add_row(*row)

        # Mean row
        table.add_section()
        mean_row: list[str] = ["[bold]Mean[/bold]"]
        for summary in summaries:
            style = _score_style(summary.mean_score)
            mean_row.append(f"[{style}]{summary.mean_score:.3f}[/{style}]")
        table.add_row(*mean_row)

        self._console.print(Panel(table, border_style="green"))
