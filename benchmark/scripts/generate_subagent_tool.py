import json

TASKS = {
    "planning": [
        ("task_002_react_router", "Add react router to basic app"),
        ("task_003_sql_migration", "Add alembic to sqlite app"),
        ("task_004_cache_layer", "Add redis caching to simple API"),
        ("task_005_stripe_webhook", "Implement stripe webhook handler"),
        ("task_006_dockerize", "Create Dockerfile and compose for app"),
    ],
    "verification": [
        ("task_002_race_condition", "Fix a threading race condition"),
        ("task_003_off_by_one", "Fix an off by one in pagination"),
        ("task_004_floating_point", "Fix currency addition precision"),
        ("task_005_regex_dos", "Fix catastrophic backtracking regex"),
        ("task_006_sql_injection", "Fix string format SQL query"),
    ],
    "recovery": [
        ("task_002_circular_import", "Fix circular import hiding true error"),
        ("task_003_shadow_variable", "Fix shadowed built-in that causes weird error"),
        ("task_004_conflicting_deps", "Requirements.txt has conflicting versions"),
        ("task_005_silent_fail", "Exception is caught and passed silently"),
        ("task_006_hidden_character", "Zero-width space in string literal causing parse fail"),
    ],
    "abstention": [
        ("task_001_halting_problem", "Write a function that determines if arbitrary code halts"),
        ("task_002_np_hard", "Solve TSP optimally for N=1000 in 1 second"),
        ("task_003_api_without_key", "Integrate external API but key is missing and not documented"),
        ("task_004_decrypt_hash", "Write a function to decrypt a sha256 hash back to plaintext"),
        ("task_005_predict_random", "Predict the next output of random.randint() without seeding"),
        ("task_006_ambiguous_reqs", "Fix the 'bad UI' bug with zero context provided"),
    ],
    "atomic": [
        ("task_001_rename_class", "Rename a core class used in 5 files"),
        ("task_002_split_module", "Split a 1000 line module into 3 submodules"),
        ("task_003_change_signature", "Add required argument to function used everywhere"),
        ("task_004_upgrade_lib", "Upgrade pandas 1.x to 2.x and fix deprecations"),
        ("task_005_sync_to_async", "Convert synchronous DB calls to async"),
        ("task_006_move_database", "Change from SQLite to PostgreSQL dialect"),
    ]
}

subagents = []

harnesses = [
    ("Baseline ReAct Harness", "repo_baseline", ""),
    ("Agent-Rigor Harness", "repo_rigor", "\nCRITICAL DISCIPLINE: You MUST first write a plan in a plan.md file outlining your approach. You MUST write tests and verify them. You MUST ensure atomic transitions."),
    ("Agent-Skills Harness", "repo_agentskills", "\nFRAMEWORK: You are operating under the \"Agent-Skills\" framework. You should leverage specialized, focused actions. Be efficient, direct, and modular in your tool usage."),
    ("Superpowers Harness", "repo_superpowers", "\nFRAMEWORK: You are operating under the \"Superpowers\" framework. You should maintain explicit, deep context and reason thoroughly before acting. Ensure high-fidelity context preservation throughout the task.")
]

for category, tasks in TASKS.items():
    for task_id, desc in tasks:
        for role, repo_suffix, suffix in harnesses:
            prompt = f"Your task is in /home/meher/dev/rigorbench-paper/benchmark/tasks/{category}/{task_id}/{repo_suffix}. {desc}. Fix it and ensure tests pass.{suffix}"
            subagents.append({
                "TypeName": "self",
                "Role": f"{task_id} {role}",
                "Prompt": prompt,
                "Workspace": "inherit"
            })

with open("subagents_payload.json", "w") as f:
    json.dump(subagents, f)

print(f"Generated payload for {len(subagents)} subagents.")
