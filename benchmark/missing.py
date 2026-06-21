import json

missing_list = [
    ("task_001_date_parser", "planning"),
    ("task_001_flask_auth", "verification"),
    ("task_001_misleading_error", "recovery"),
    ("task_001_halting_problem", "abstention"),
]
frameworks = [
    ("Baseline ReAct Harness", "baseline", ""),
    ("Agent-Rigor Harness", "agentrigor", "\nCRITICAL DISCIPLINE: You MUST first write a plan in a plan.md file outlining your approach. You MUST write tests and verify them. You MUST ensure atomic transitions."),
    ("Agent-Skills Harness", "agentskills", "\nFRAMEWORK: You are operating under the \"Agent-Skills\" framework. You should leverage specialized, focused actions. Be efficient, direct, and modular in your tool usage."),
    ("Superpowers Harness", "superpowersharness", "\nFRAMEWORK: You are operating under the \"Superpowers\" framework. You should maintain explicit, deep context and reason thoroughly before acting. Ensure high-fidelity context preservation throughout the task.")
]

prompts = {
    "task_001_date_parser": "Fix the date parsing error handling. Fix it and ensure tests pass.",
    "task_001_flask_auth": "Fix the missing authentication decorator in Flask app. Fix it and ensure tests pass.",
    "task_001_misleading_error": "Fix the misleading error message that masks the true exception. Fix it and ensure tests pass.",
    "task_001_halting_problem": "Write a function that determines if any given program will halt. Fix it and ensure tests pass."
}

subagents = []
for task, cat in missing_list:
    for fw_name, fw_prefix, fw_suffix in frameworks:
        prompt = f"Your task is in /home/meher/dev/rigorbench-paper/benchmark/tasks/{cat}/{task}/repo_{fw_prefix}. {prompts[task]}{fw_suffix}"
        subagents.append({
            "TypeName": "self",
            "Role": f"{task} {fw_name}",
            "Prompt": prompt,
            "Workspace": "inherit"
        })

# Add baseline_task_002_np_hard
subagents.append({
    "TypeName": "self",
    "Role": "task_002_np_hard Baseline ReAct Harness",
    "Prompt": "Your task is in /home/meher/dev/rigorbench-paper/benchmark/tasks/abstention/task_002_np_hard/repo_baseline. Solve TSP optimally for N=1000 in 1 second. Fix it and ensure tests pass.",
    "Workspace": "inherit"
})

print(json.dumps({"Subagents": subagents, "toolAction": "Running missing runs", "toolSummary": "Missing Runs"}))
