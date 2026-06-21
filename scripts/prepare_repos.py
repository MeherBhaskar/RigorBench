import os
import shutil

categories = ['planning', 'verification', 'recovery', 'abstention', 'atomic']
base_dir = '/home/meher/dev/rigorbench-paper/benchmark/tasks'

for cat in categories:
    cat_path = os.path.join(base_dir, cat)
    if not os.path.exists(cat_path):
        continue
    for task in os.listdir(cat_path):
        task_path = os.path.join(cat_path, task)
        if not os.path.isdir(task_path):
            continue
        
        rigor_repo = os.path.join(task_path, 'repo_agentrigor')
        if not os.path.exists(rigor_repo):
            continue
            
        for new_repo in ['repo_baseline', 'repo_agentskills', 'repo_superpowers']:
            new_path = os.path.join(task_path, new_repo)
            if not os.path.exists(new_path):
                print(f"Copying {rigor_repo} to {new_path}")
                shutil.copytree(rigor_repo, new_path)
