import os
import shutil

TASKS_DIR = "tasks/"

for category in os.listdir(TASKS_DIR):
    cat_dir = os.path.join(TASKS_DIR, category)
    if not os.path.isdir(cat_dir): continue
    for task in os.listdir(cat_dir):
        task_dir = os.path.join(cat_dir, task)
        repo_dir = os.path.join(task_dir, "repo")
        if os.path.exists(repo_dir):
            for suffix in ["_baseline", "_rigor", "_agentskills", "_superpowers"]:
                dest = os.path.join(task_dir, f"repo{suffix}")
                if os.path.exists(dest):
                    shutil.rmtree(dest)
                shutil.copytree(repo_dir, dest)

print("Duplicated repos!")
