import os
from collections import defaultdict
from rigorbench.trajectory import TrajectoryLoader
from rigorbench.scorer import RigorScorer

scorer = RigorScorer()
# scores[task_id][agent] = score
scores = defaultdict(dict)
results_dir = '/home/meher/dev/rigorbench-paper/benchmark/results'

for file in os.listdir(results_dir):
    if file.endswith('.yaml') and not file.endswith('averages.yaml') and not file.endswith('trajectory.yaml'):
        filepath = os.path.join(results_dir, file)
        try:
            t = TrajectoryLoader.load(filepath)
            agent_name = t.agent_name.lower()
            if 'baseline' in agent_name:
                agent_name = 'Baseline'
            elif 'superpower' in agent_name:
                agent_name = 'Superpowers'
            elif 'rigor' in agent_name:
                agent_name = 'Agent-Rigor'
            elif 'skill' in agent_name:
                agent_name = 'Agent-Skills'
            res = scorer.score_trajectory(t)
            scores[t.task_id][agent_name] = res['composite_score'] / 100.0
        except Exception: pass

print("Tasks where Agent-Rigor was beaten:")
for task, task_scores in scores.items():
    if 'Agent-Rigor' in task_scores:
        rigor = task_scores['Agent-Rigor']
        beaten_by = []
        for agent, score in task_scores.items():
            if agent != 'Agent-Rigor' and score > rigor:
                beaten_by.append((agent, score))
        if beaten_by:
            print(f"- {task}: Agent-Rigor scored {rigor:.2f}. Beaten by: ", end="")
            print(", ".join([f"{a} ({s:.2f})" for a, s in beaten_by]))
