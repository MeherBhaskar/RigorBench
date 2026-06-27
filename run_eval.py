#!/usr/bin/env python3
"""
run_eval.py — Master Evaluation Entrypoint for RigorBench

This script runs the entire evaluation pipeline:
1. Loads the trajectory YAMLs and computes the core 7-pillar RigorScores.
2. Runs the static analysis and transcript parser for extended metrics (RR, EE, TAD, DCR, DM, CGR).
3. Loads the Specification Coverage (SC) and Clarification Behavior Score (CBS) evaluations.
4. Aggregates all 9 process metrics and prints formatted Markdown and LaTeX tables.

Usage:
  python3 run_eval.py
"""

import os
import sys
import yaml
from collections import defaultdict

# Add benchmark directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "benchmark"))

from rigorbench.trajectory import TrajectoryLoader
from rigorbench.scorer import RigorScorer

# Import metrics logic directly
import compute_extended

def main():
    print("==================================================")
    # 1. Core Scorer & Extended Metrics
    print("1. Computing Core & Extended Metrics from Trajectories...")
    base_scorer = RigorScorer()
    agg = defaultdict(lambda: defaultdict(list))
    
    # Locate directories
    benchmark_dir = os.path.join(os.path.dirname(__file__), "benchmark")
    results_dir = os.path.join(benchmark_dir, "results")
    
    # Build transcript map
    tmap = compute_extended.build_transcript_map()
    
    LABEL_MAP = {
        "agentrigor": "Agent-Rigor",
        "superpowersharness": "Superpowers",
        "agentskills": "Agent-Skills",
        "baseline": "Baseline"
    }

    for fname in sorted(os.listdir(results_dir)):
        if not fname.endswith(".yaml") or "trajectory" in fname or "averages" in fname:
            continue
        try:
            t = TrajectoryLoader.load(os.path.join(results_dir, fname))
        except Exception:
            continue

        tid = t.task_id
        harness = compute_extended.normalise(t.agent_name)
        label = LABEL_MAP.get(harness, "Baseline")

        # 7-pillar composite score
        res = base_scorer.score_trajectory(t)
        agg[label]["RigorScore"].append(res["composite_score"] / 100.0)

        # Transcript metrics (RR, EE)
        tp = tmap.get((tid, harness))
        if tp:
            rr = compute_extended.regression_rate(tp)
            ee = compute_extended.exploration_efficiency(tp)
            if rr is not None: agg[label]["RR"].append(rr)
            if ee is not None: agg[label]["EE"].append(ee)

        # Repo metrics (TAD, DCR, DM, CGR)
        repo = compute_extended.find_repo(tid, harness)
        seed = compute_extended.find_seed(tid)
        if repo:
            tad = compute_extended.test_assertion_density(repo)
            dcr = compute_extended.dead_code_ratio(repo)
            dm = compute_extended.diff_minimality(repo, seed)
            cgr = compute_extended.contextual_grounding_rate(repo)
            if tad is not None: agg[label]["TAD"].append(tad)
            if dcr is not None: agg[label]["DCR"].append(dcr)
            if dm is not None: agg[label]["DM"].append(dm)
            if cgr is not None: agg[label]["CGR"].append(cgr)

    # 2. Load SC and CBS scores
    print("2. Loading Specification Coverage (SC) & Clarification Scores (CBS)...")
    sc_file = os.path.join(results_dir, "sc_scores_all.yaml")
    cbs_file = os.path.join(results_dir, "cbs_scores.yaml")

    if os.path.exists(sc_file):
        with open(sc_file) as f:
            sc_data = yaml.safe_load(f) or {}
        for task_id, task_res in sc_data.items():
            for harness, res in task_res.items():
                label = LABEL_MAP.get(harness, harness)
                agg[label]["SC"].append(res["sc"])

    if os.path.exists(cbs_file):
        with open(cbs_file) as f:
            cbs_data = yaml.safe_load(f) or {}
        for task_id, task_res in cbs_data.items():
            for harness, res in task_res.items():
                label = LABEL_MAP.get(harness, harness)
                agg[label]["CBS"].append(res["score"])

    # 3. Generate Tables
    print("==================================================")
    print("### RigorBench 9-Metric Process Evaluation (Aggregated)")
    print("==================================================")
    
    ORDER = ["Baseline", "Superpowers", "Agent-Skills", "Agent-Rigor"]
    METRICS_META = [
        ("RigorScore", "RigorScore (7-Pillar) ↑"),
        ("RR", "Regression Rate (RR) ↑"),
        ("EE", "Exploration Efficiency (EE) ↑"),
        ("TAD", "Test Assertion Density (TAD) ↑"),
        ("DCR", "Dead Code Ratio (DCR) ↑"),
        ("DM", "Diff Minimality (DM) ↑"),
        ("CGR", "Contextual Grounding Rate (CGR) ↑"),
        ("SC", "Specification Coverage (SC) ↑"),
        ("CBS", "Clarification Behavior Score (CBS) ↑"),
    ]

    print(f"| {'Metric':<35} | " + " | ".join(f"{h:<12}" for h in ORDER) + " |")
    print("| :" + "-"*35 + " | " + " | ".join(":" + "-"*10 + ":" for _ in ORDER) + " |")

    for key, label in METRICS_META:
        row = f"| {label:<35} |"
        vals = []
        for h in ORDER:
            v_list = agg[h].get(key, [])
            vals.append(sum(v_list) / len(v_list) if v_list else 0.0)
            
        best_val = max(vals)
        for val in vals:
            if abs(val - best_val) < 1e-5 and val > 0:
                row += f" **{val:.3f}**     |"
            else:
                row += f" {val:.3f}     |"
        print(row)

    print("\n==================================================")
    print("### LaTeX Table Snippet for Publication")
    print("==================================================")
    
    latex = r"""\begin{table*}[t]
\centering
\caption{Comprehensive evaluation across all nine process metrics on \bench{} ($n=400$ runs). All metrics are scaled $[0,1]$ where higher is better ($\uparrow$). Bold indicates the best-performing harness.}
\label{tab:comprehensive_metrics}
\resizebox{\textwidth}{!}{%
\begin{tabular}{lcccc}
\toprule
\textbf{Metric} & \textbf{Baseline} & \textbf{Superpowers} & \textbf{Agent-Skills} & \textbf{Agent-Rigor} \\
\midrule
"""
    for key, label in METRICS_META:
        vals = []
        for h in ORDER:
            v_list = agg[h].get(key, [])
            vals.append(sum(v_list) / len(v_list) if v_list else 0.0)
        best_val = max(vals)
        formatted = []
        for val in vals:
            if abs(val - best_val) < 1e-5 and val > 0:
                formatted.append(f"\\textbf{{{val:.3f}}}")
            else:
                formatted.append(f"{val:.3f}")
        clean_label = label.replace("↑", "").strip()
        latex += f"{clean_label:<35} & " + " & ".join(formatted) + r" \\" + "\n"

    latex += r"""\bottomrule
\end{tabular}
}
\end{table*}"""
    print(latex)
    print("==================================================")

if __name__ == "__main__":
    main()
