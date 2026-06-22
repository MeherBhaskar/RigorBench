import os
from collections import defaultdict
from rigorbench.trajectory import TrajectoryLoader
from rigorbench.scorer import RigorScorer

category_names = {
    'planning': 'Plan-Then-Build',
    'verification': 'Verify-Or-Die',
    'recovery': 'Doom Loop Gauntlet',
    'abstention': 'Know When to Fold',
    'atomic': "Don't Break the Build"
}

category_map = {}
for cat in os.listdir('tasks'):
    cat_path = os.path.join('tasks', cat)
    if os.path.isdir(cat_path):
        for task in os.listdir(cat_path):
            category_map[task] = category_names.get(cat, cat)

scorer = RigorScorer()
scores = defaultdict(lambda: defaultdict(list))
results_dir = 'results'

for file in os.listdir(results_dir):
    if file.endswith('.yaml') and not file.endswith('averages.yaml') and not file.endswith('trajectory.yaml'):
        filepath = os.path.join(results_dir, file)
        try:
            t = TrajectoryLoader.load(filepath)
            task_id = t.task_id
            cat = category_map.get(task_id, 'unknown')
            
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
            scores[agent_name][cat].append(res['composite_score'] / 100.0)
        except Exception as e:
            pass

print("| Task Category | Baseline ReAct | Superpowers | Agent-Skills | Agent-Rigor |")
print("| :--- | :---: | :---: | :---: | :---: |")
for cat in category_names.values():
    row = [f"**{cat}**"]
    for agent in ['Baseline ReAct', 'Superpowers', 'Agent-Skills', 'Agent-Rigor']:
        if cat in scores[agent]:
            vals = scores[agent][cat]
            avg = sum(vals) / len(vals)
            row.append(f"{avg:.2f}")
        else:
            row.append("N/A")
    print("| " + " | ".join(row) + " |")
