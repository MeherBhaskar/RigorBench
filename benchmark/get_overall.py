import os
from collections import defaultdict
from rigorbench.trajectory import TrajectoryLoader
from rigorbench.scorer import RigorScorer

scorer = RigorScorer()
scores = defaultdict(list)
results_dir = '/home/meher/dev/rigorbench-paper/benchmark/results'

for file in os.listdir(results_dir):
    if file.endswith('.yaml') and not file.endswith('averages.yaml') and not file.endswith('trajectory.yaml'):
        filepath = os.path.join(results_dir, file)
        try:
            t = TrajectoryLoader.load(filepath)
            agent_name = t.agent_name.lower()
            if 'baseline' in agent_name:
                agent_name = 'Baseline ReAct'
            elif 'superpower' in agent_name:
                agent_name = 'Superpowers'
            elif 'rigor' in agent_name:
                agent_name = 'Agent-Rigor'
            elif 'skill' in agent_name:
                agent_name = 'Agent-Skills'
            res = scorer.score_trajectory(t)
            scores[agent_name].append(res['composite_score'] / 100.0)
        except Exception: pass

for agent, vals in scores.items():
    print(f"{agent}: {sum(vals)/len(vals):.2f}")
