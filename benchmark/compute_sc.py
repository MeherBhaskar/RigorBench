"""
compute_sc.py — Specification Coverage (SC) metric

Uses agy --print as LLM-as-judge to measure what fraction of task README
requirements each agent's final code satisfies.

Skips abstention-category tasks (correct answer is "refuse", not "implement").
Run from: /home/meher/dev/rigorbench-paper/benchmark/
Usage:    python3 compute_sc.py [--sample N] [--task TASK_ID]
"""

import os, re, sys, json, yaml, time, subprocess, argparse
from collections import defaultdict

TASKS_DIR   = "tasks"
RESULTS_DIR = "results"
SKIP_CATS   = {"abstention"}   # impossible tasks — SC doesn't apply

HARNESS_REPO_MAP = {
    "agentrigor":         "repo_agentrigor",
    "superpowersharness": "repo_superpowers",
    "agentskills":        "repo_agentskills",
    "baseline":           "repo_baseline",
}
HARNESS_LABELS = {
    "agentrigor":"Agent-Rigor","superpowersharness":"Superpowers",
    "agentskills":"Agent-Skills","baseline":"Baseline",
}


def call_agy(prompt: str) -> str:
    try:
        r = subprocess.run(
            ["agy","--print", prompt,"--dangerously-skip-permissions"],
            capture_output=True, text=True, timeout=90
        )
        return r.stdout.strip()
    except Exception as e:
        print(f"    [ERR] {e}")
        return ""


def parse_json_array(text: str):
    """Extract the first JSON array from text, tolerating markdown fences."""
    # Strip markdown code fences
    text = re.sub(r"```(?:json)?", "", text).strip()
    match = re.search(r"\[.*?\]", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except Exception:
            pass
    return None


def read_task_desc(task_dir: str) -> tuple[str, str]:
    """Returns (description_text, category)."""
    for fname in ["task.yaml","task.yml"]:
        fp = os.path.join(task_dir, fname)
        if os.path.exists(fp):
            with open(fp) as f:
                data = yaml.safe_load(f)
            cat = data.get("category","")
            desc = data.get("description","") or ""
            name = data.get("name","") or ""
            reqs = data.get("requirements","") or ""
            full = f"Task: {name}\n\n{desc}"
            if reqs:
                if isinstance(reqs, list):
                    full += "\n\nRequirements:\n" + "\n".join(f"- {r}" for r in reqs)
                else:
                    full += f"\n\nRequirements:\n{reqs}"
            return full[:2000], cat
    for fname in ["README.md","README.txt"]:
        fp = os.path.join(task_dir, fname)
        if os.path.exists(fp):
            with open(fp) as f:
                return f.read()[:2000], ""
    return "", ""


def read_code(repo_path: str) -> str:
    if not repo_path or not os.path.isdir(repo_path):
        return ""
    parts = []
    for fname in sorted(os.listdir(repo_path)):
        if not fname.endswith(".py") or fname.startswith("test_"):
            continue
        try:
            with open(os.path.join(repo_path, fname)) as f:
                parts.append(f"# === {fname} ===\n{f.read()}")
        except Exception:
            pass
    return "\n\n".join(parts)[:4000]


def extract_requirements(task_desc: str) -> list[str]:
    prompt = (
        "Extract a list of concrete, verifiable software requirements from this task description. "
        "Each requirement must be checkable by reading code (not by running it). "
        "Be specific and strict. Maximum 6 requirements. "
        "Output ONLY a JSON array of strings.\n\n"
        f"Task:\n{task_desc}\n\n"
        "Output: [\"requirement 1\", ...]"
    )
    resp = call_agy(prompt)
    result = parse_json_array(resp)
    if isinstance(result, list) and all(isinstance(r, str) for r in result):
        return result[:6]
    return []


def evaluate_requirements(requirements: list[str], code: str, task_desc: str) -> list[bool]:
    if not requirements or not code:
        return []
    req_list = "\n".join(f"{i+1}. {r}" for i, r in enumerate(requirements))
    prompt = (
        "You are a STRICT code reviewer. For each requirement, answer true ONLY if the "
        "requirement is clearly and explicitly satisfied in the code. "
        "If in doubt, answer false. Do NOT infer or assume — only mark true if you can "
        "point to specific code that satisfies it.\n\n"
        f"Task context:\n{task_desc[:400]}\n\n"
        f"Requirements:\n{req_list}\n\n"
        f"Code:\n{code}\n\n"
        "Output ONLY a JSON array of booleans, same length as requirements. "
        "Example: [true, false, true]"
    )
    resp = call_agy(prompt)
    result = parse_json_array(resp)
    if isinstance(result, list) and len(result) == len(requirements):
        return [bool(r) for r in result]
    return [False] * len(requirements)


def compute_task(task_id: str, task_dir: str, cat: str, task_desc: str) -> dict:
    print(f"    Extracting requirements...")
    requirements = extract_requirements(task_desc)
    if not requirements:
        print(f"    [SKIP] No requirements extracted")
        return {}
    print(f"    {len(requirements)} requirements found")
    time.sleep(1)

    results = {}
    for harness, repo_dir in HARNESS_REPO_MAP.items():
        repo_path = os.path.join(task_dir, repo_dir)
        code = read_code(repo_path)
        if not code:
            continue
        satisfied = evaluate_requirements(requirements, code, task_desc)
        sc = sum(satisfied) / len(requirements)
        results[harness] = {
            "sc": sc, "satisfied": sum(satisfied),
            "total": len(requirements),
            "requirements": requirements,
            "results": satisfied,
        }
        label = HARNESS_LABELS.get(harness, harness)
        print(f"    {label}: SC={sc:.2f} ({sum(satisfied)}/{len(requirements)})")
        time.sleep(1)
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sample", type=int, default=None)
    parser.add_argument("--task",   type=str, default=None)
    parser.add_argument("--out",    type=str, default="results/sc_scores.yaml")
    args = parser.parse_args()

    all_tasks = []
    for cat in sorted(os.listdir(TASKS_DIR)):
        if cat in SKIP_CATS:
            continue
        cat_path = os.path.join(TASKS_DIR, cat)
        if not os.path.isdir(cat_path): continue
        for task in sorted(os.listdir(cat_path)):
            task_dir = os.path.join(cat_path, task)
            if not os.path.isdir(task_dir): continue
            if args.task and task != args.task: continue
            all_tasks.append((task, task_dir, cat))

    if args.sample:
        all_tasks = all_tasks[:args.sample]

    print(f"Computing SC for {len(all_tasks)} tasks (skipping abstention)...\n")

    all_results = {}
    agg = defaultdict(list)

    for task_id, task_dir, cat in all_tasks:
        print(f"  [{cat}] {task_id}")
        task_desc, _ = read_task_desc(task_dir)
        if not task_desc:
            print(f"    [SKIP] No task description")
            continue
        task_results = compute_task(task_id, task_dir, cat, task_desc)
        all_results[task_id] = task_results
        for harness, res in task_results.items():
            agg[HARNESS_LABELS[harness]].append(res["sc"])
        print()

    os.makedirs(os.path.dirname(args.out) if os.path.dirname(args.out) else ".", exist_ok=True)
    with open(args.out, "w") as f:
        yaml.dump(all_results, f)
    print(f"Saved to {args.out}\n")

    ORDER = ["Baseline","Superpowers","Agent-Skills","Agent-Rigor"]
    print(f"\n{'Harness':<20} {'SC Mean':>10} {'N':>6}")
    print("─"*38)
    for h in ORDER:
        vals = agg[h]
        if vals: print(f"{h:<20} {sum(vals)/len(vals):>10.3f} {len(vals):>6}")
        else:    print(f"{h:<20} {'N/A':>10} {'0':>6}")

if __name__ == "__main__":
    main()
