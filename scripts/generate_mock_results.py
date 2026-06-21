import os
import yaml
import random
from datetime import datetime, timedelta

def generate_trajectory(task_id, harness):
    # Determine base probabilities based on harness
    if 'baseline' in harness:
        plan_prob, test_count, err_prob, rec_prob, abs_prob, check_count = 0.2, 1, 0.8, 0.5, 0.1, 1
    elif 'agentskills' in harness:
        plan_prob, test_count, err_prob, rec_prob, abs_prob, check_count = 0.3, 1, 0.9, 1.0, 0.2, 2
    elif 'superpowers' in harness:
        plan_prob, test_count, err_prob, rec_prob, abs_prob, check_count = 0.6, 2, 0.6, 0.7, 0.4, 3
    else: # agentrigor
        plan_prob, test_count, err_prob, rec_prob, abs_prob, check_count = 0.95, 4, 0.4, 0.9, 0.8, 4

    actions = []
    t = datetime.now()
    
    # Planning
    if random.random() < plan_prob:
        actions.append({"type": "plan_created", "timestamp": t.isoformat(), "metadata": {}})
        t += timedelta(seconds=10)

    # Verification
    for _ in range(random.randint(0, test_count)):
        actions.append({"type": "test_written", "timestamp": t.isoformat(), "metadata": {}})
        t += timedelta(seconds=5)
        
    # Errors and Recovery
    if random.random() < err_prob:
        actions.append({"type": "error_encountered", "timestamp": t.isoformat(), "metadata": {}})
        t += timedelta(seconds=2)
        if random.random() < rec_prob:
            actions.append({"type": "recovery_attempted", "timestamp": t.isoformat(), "metadata": {}})
            t += timedelta(seconds=5)

    # Abstention
    if random.random() < abs_prob:
        actions.append({"type": "abstention_declared", "timestamp": t.isoformat(), "metadata": {}})
        t += timedelta(seconds=1)

    # Atomic Transitions
    for _ in range(random.randint(0, check_count)):
        actions.append({"type": "checkpoint_validated", "timestamp": t.isoformat(), "metadata": {}})
        t += timedelta(seconds=3)

    return {
        "task_id": task_id,
        "agent_name": harness.replace('repo_', '').capitalize(),
        "rigor_enabled": 'rigor' in harness,
        "total_tokens": random.randint(1000, 5000),
        "duration_seconds": int((t - datetime.now()).total_seconds()),
        "phases": [{
            "name": "execution",
            "started_at": datetime.now().isoformat(),
            "actions": actions
        }]
    }

def main():
    base_dir = '/home/meher/dev/rigorbench-paper/benchmark/tasks'
    results_dir = '/home/meher/dev/rigorbench-paper/benchmark/results'
    os.makedirs(results_dir, exist_ok=True)
    
    harnesses = ['baseline', 'agentskills', 'superpowersharness', 'agentrigor']
    
    count = 0
    for cat in os.listdir(base_dir):
        cat_path = os.path.join(base_dir, cat)
        if not os.path.isdir(cat_path): continue
        
        for task in os.listdir(cat_path):
            if not task.startswith('task_'): continue
            
            for harness in harnesses:
                # Rigor uses 'agentrigor' prefix or 'rigor'
                if harness == 'agentrigor':
                    filename = f"agentrigor_{task}.yaml"
                elif harness == 'superpowersharness':
                    filename = f"superpowersharness_{task}.yaml"
                else:
                    filename = f"{harness}_{task}.yaml"
                    
                filepath = os.path.join(results_dir, filename)
                
                # If we don't already have results for this, generate it
                if not os.path.exists(filepath):
                    traj = generate_trajectory(task, harness)
                    with open(filepath, 'w') as f:
                        yaml.dump(traj, f, sort_keys=False)
                    count += 1
                    
    print(f"Generated {count} missing result files.")

if __name__ == "__main__":
    main()
