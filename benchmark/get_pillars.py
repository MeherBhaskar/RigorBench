import os
from collections import defaultdict
from rigorbench.trajectory import TrajectoryLoader
from rigorbench.scorer import RigorScorer

scorer = RigorScorer()
scores = defaultdict(lambda: defaultdict(list))
results_dir = '/home/meher/dev/rigorbench-paper/benchmark/results'

keys_printed = False

for file in os.listdir(results_dir):
    if file.endswith('.yaml') and not file.endswith('averages.yaml') and not file.endswith('trajectory.yaml'):
        filepath = os.path.join(results_dir, file)
        try:
            t = TrajectoryLoader.load(filepath)
            agent_name = t.agent_name.lower()
            if 'baseline' in agent_name: agent_name = 'Baseline ReAct'
            elif 'superpower' in agent_name: agent_name = 'Superpowers'
            elif 'rigor' in agent_name: agent_name = 'Agent-Rigor'
            elif 'skill' in agent_name: agent_name = 'Agent-Skills'
            
            res = scorer.score_trajectory(t)
            if not keys_printed:
                print("Keys:", res['pillar_scores'].keys())
                keys_printed = True
                
            for k, v in res['pillar_scores'].items():
                scores[agent_name][k].append(v.score)
            scores[agent_name]['composite_score'].append(res['composite_score'])
        except Exception: pass

print("---")
for agent, data in scores.items():
    print(f"Agent: {agent}")
    for k, vals in data.items():
        if k != 'composite_score':
            print(f"  {k}: {sum(vals)/len(vals):.2f}")
    print(f"  composite_score: {sum(data['composite_score'])/len(data['composite_score'])/100.0:.2f}")
