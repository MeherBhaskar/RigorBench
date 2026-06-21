import os
import glob
from collections import defaultdict
from rigorbench.trajectory import TrajectoryLoader
from rigorbench.scorer import RigorScorer

def main():
    results_dir = "results"
    yaml_files = glob.glob(os.path.join(results_dir, "*.yaml"))
    
    scorer = RigorScorer()
    
    # metrics[framework][pillar] = [scores]
    metrics = defaultdict(lambda: defaultdict(list))
    
    for yf in yaml_files:
        try:
            traj = TrajectoryLoader.load(yf)
            scores = scorer.score_trajectory(traj)
            
            fw = traj.agent_name
            # If the parser normalized it to 'superpowersharness', 'agentrigor', etc, let's look at the filename or the loaded agent_name
            # Wait, parse_antigravity_transcript.py: `agent_name = parts[1] + (("-" + parts[2]) if "-" not in parts[1] else "")`
            # For "Baseline ReAct Harness", it parses as "ReAct-Harness". wait, parts[1] is ReAct, parts[2] is Harness -> ReAct-Harness.
            # Let's group by agent_name!
            
            for pillar, ps in scores["pillar_scores"].items():
                metrics[fw][pillar].append(ps.score)
            metrics[fw]["Composite Score"].append(scores["composite_score"])
        except Exception as e:
            print(f"Failed to process {yf}: {e}")

    print("=== RigorBench Evaluation Results ===")
    for fw, fw_metrics in metrics.items():
        print(f"\nFramework: {fw}")
        for metric_name, scores in fw_metrics.items():
            avg = sum(scores) / len(scores) if scores else 0
            print(f"  {metric_name}: {avg:.2f} (from {len(scores)} runs)")

if __name__ == "__main__":
    main()
