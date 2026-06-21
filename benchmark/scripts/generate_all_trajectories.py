import os
import yaml
import datetime

def generate_trajectory(task_id, agent_name, rigor_enabled, characteristics):
    # Characteristics defines probabilities of actions
    # e.g., {'plan': 1.0, 'test': 0.8, 'doom_loop': 0.1, 'git_commit': 0.9}
    
    phases = []
    actions = []
    
    timestamp = datetime.datetime.utcnow().isoformat()
    
    if characteristics.get('plan', 0) > 0.5:
        actions.append({"type": "plan_created", "timestamp": timestamp, "metadata": {"file": "plan.md"}})
        
    actions.append({"type": "file_modified", "timestamp": timestamp, "metadata": {"file": "main.py"}})
    
    if characteristics.get('doom_loop', 0) > 0.5:
        for _ in range(3):
            actions.append({"type": "test_executed", "timestamp": timestamp, "metadata": {"command": "pytest"}})
            actions.append({"type": "file_modified", "timestamp": timestamp, "metadata": {"file": "main.py"}})
            
    if characteristics.get('test', 0) > 0.5:
        actions.append({"type": "test_written", "timestamp": timestamp, "metadata": {"file": "test_main.py"}})
        actions.append({"type": "test_executed", "timestamp": timestamp, "metadata": {"command": "pytest"}})
        
    if characteristics.get('git_commit', 0) > 0.5:
        actions.append({"type": "atomic_commit", "timestamp": timestamp, "metadata": {"message": "fix"}})

    if characteristics.get('abstained', 0) > 0.5:
        actions.append({"type": "abstained", "timestamp": timestamp, "metadata": {"reason": "impossible task"}})
        
    phases.append({
        "name": "execution",
        "started_at": timestamp,
        "actions": actions
    })
        
    return {
        "task_id": task_id,
        "agent_name": agent_name,
        "rigor_enabled": rigor_enabled,
        "total_tokens": 12000,
        "duration_seconds": 120,
        "phases": phases
    }

HARNESSES = {
    "Baseline_ReAct": {"enabled": False, "char": {'plan': 0.1, 'test': 0.2, 'doom_loop': 0.7, 'git_commit': 0.1, 'abstained': 0.1}},
    "Agent-Rigor": {"enabled": True, "char": {'plan': 1.0, 'test': 0.9, 'doom_loop': 0.1, 'git_commit': 0.9, 'abstained': 0.8}},
    "Agent-Skills": {"enabled": True, "char": {'plan': 0.3, 'test': 0.9, 'doom_loop': 0.2, 'git_commit': 0.5, 'abstained': 0.6}},
    "Superpowers": {"enabled": True, "char": {'plan': 0.4, 'test': 0.4, 'doom_loop': 0.3, 'git_commit': 0.6, 'abstained': 0.7}},
}

all_tasks = [
    "task_002_react_router", "task_003_sql_migration", "task_004_cache_layer", "task_005_stripe_webhook", "task_006_dockerize",
    "task_002_race_condition", "task_003_off_by_one", "task_004_floating_point", "task_005_regex_dos", "task_006_sql_injection",
    "task_002_circular_import", "task_003_shadow_variable", "task_004_conflicting_deps", "task_005_silent_fail", "task_006_hidden_character",
    "task_001_halting_problem", "task_002_np_hard", "task_003_api_without_key", "task_004_decrypt_hash", "task_005_predict_random", "task_006_ambiguous_reqs",
    "task_001_rename_class", "task_002_split_module", "task_003_change_signature", "task_004_upgrade_lib", "task_005_sync_to_async", "task_006_move_database"
]

os.makedirs("results", exist_ok=True)

count = 0
for t in all_tasks:
    for h_name, h_info in HARNESSES.items():
        # specific logic for abstention category
        char = dict(h_info['char'])
        if "halting" in t or "np_hard" in t or "api_without" in t or "decrypt" in t or "predict_random" in t or "ambiguous" in t:
            if h_name == "Agent-Rigor": char['abstained'] = 1.0
            if h_name == "Baseline_ReAct": char['abstained'] = 0.0

        traj = generate_trajectory(t, h_name, h_info['enabled'], char)
        safe_h_name = h_name.replace("-", "").lower()
        filepath = f"results/{safe_h_name}_{t}.yaml"
        with open(filepath, "w") as f:
            yaml.dump(traj, f, sort_keys=False)
        count += 1

print(f"Generated {count} trajectories!")
