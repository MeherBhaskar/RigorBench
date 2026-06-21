import argparse
from rich.console import Console
from rich.table import Table

from rigorbench.trajectory import TrajectoryLoader
from rigorbench.scorer import RigorScorer

console = Console()

def cmd_score(args):
    """Scores a single trajectory file."""
    try:
        traj = TrajectoryLoader.load(args.trajectory)
    except Exception as e:
        console.print(f"[red]Error loading trajectory: {e}[/red]")
        return

    scorer = RigorScorer()
    results = scorer.score_trajectory(traj)
    
    console.print(f"\n[bold blue]RigorBench Score Report[/bold blue]")
    console.print(f"Task ID: {traj.task_id}")
    console.print(f"Agent: {traj.agent_name}")
    console.print(f"Rigor Enabled: {traj.rigor_enabled}\n")

    table = Table(title="Pillar Scores")
    table.add_column("Pillar", style="cyan")
    table.add_column("Score", justify="right", style="green")
    
    for name, ps in results["pillar_scores"].items():
        table.add_row(name, f"{ps.score:.1f}/100")
        
    console.print(table)
    console.print(f"\n[bold white]Composite RigorScore: {results['composite_score']:.1f}/100[/bold white]\n")

def main():
    parser = argparse.ArgumentParser(description="RigorBench: AI Agent Engineering Process Discipline Benchmark")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Run command
    parser_run = subparsers.add_parser("run", help="Run benchmark on an agent")
    parser_run.add_argument("--agent", required=True, help="Agent name (e.g., claude-code)")
    parser_run.add_argument("--task-suite", required=True, help="Task category to run")
    parser_run.add_argument("--rigor-enabled", action="store_true", help="Run with agent-rigor enabled")
    
    # Score command
    parser_score = subparsers.add_parser("score", help="Score a trajectory file")
    parser_score.add_argument("--trajectory", required=True, help="Path to trajectory YAML file")
    
    # List tasks command
    parser_list = subparsers.add_parser("list-tasks", help="List available tasks")
    parser_list.add_argument("--category", help="Filter by category")

    args = parser.parse_args()
    
    if args.command == "score":
        cmd_score(args)
    elif args.command == "run":
        console.print(f"[yellow]Running agent '{args.agent}' on suite '{args.task_suite}'... (Not implemented in mock harness)[/yellow]")
    elif args.command == "list-tasks":
        console.print("[yellow]Listing tasks... (Not implemented in mock harness)[/yellow]")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
