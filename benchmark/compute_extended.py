"""
compute_extended.py — Extended RigorBench metrics (v2, fixed)

Computes 6 metrics from EXISTING data:

  From transcripts (brain/):
    RR  - Regression Rate
    EE  - Exploration Efficiency

  From repo artifacts:
    TAD - Test Assertion Density
    DCR - Dead Code Ratio        (genuinely flat ~0.99 — tasks are clean code)
    DM  - Diff Minimality        (neutral 0.5 when no seed repo; 100% coverage)
    CHR - Hallucination Rate     (FIXED: includes local .py filenames as known)

Run from: /home/meher/dev/rigorbench-paper/benchmark/
"""

import os, re, ast, json, math, subprocess, sys
from collections import defaultdict

sys.path.insert(0, ".")
from rigorbench.trajectory import TrajectoryLoader
from rigorbench.scorer import RigorScorer

BRAIN_DIR   = os.path.expanduser("~/.gemini/antigravity-cli/brain")
RESULTS_DIR = "results"
TASKS_DIR   = "tasks"
TASK_PATTERN = re.compile(r"tasks/\w+/(task_\d+_\w+)/repo_(\w+)")

HARNESS_REPO_MAP = {
    "agentrigor":         "repo_agentrigor",
    "superpowersharness": "repo_superpowers",
    "agentskills":        "repo_agentskills",
    "baseline":           "repo_baseline",
}

STDLIB_MODULES = {
    "abc","ast","asyncio","base64","collections","concurrent","contextlib",
    "copy","csv","dataclasses","datetime","decimal","enum","functools",
    "gc","glob","hashlib","heapq","http","importlib","inspect","io","itertools",
    "json","logging","math","multiprocessing","operator","os","pathlib","pickle",
    "platform","pprint","queue","random","re","shutil","signal","socket",
    "sqlite3","ssl","stat","string","struct","subprocess","sys","tempfile",
    "textwrap","threading","time","traceback","types","typing","unittest",
    "urllib","uuid","warnings","weakref","xml","zipfile","zlib","zoneinfo",
    "builtins","__future__","pytest","setuptools","pkg_resources","mock",
}

THIRD_PARTY = {
    "flask","django","sqlalchemy","requests","numpy","pandas","scipy","sklearn",
    "matplotlib","cryptography","redis","celery","pydantic","fastapi","aiohttp",
    "boto3","paramiko","click","pytz","dateutil","tzdata","freezegun","responses",
    "httpx","jinja2","werkzeug","itsdangerous","markupsafe","starlette","anyio",
    "attrs","attr","six","certifi","chardet","urllib3","idna","charset_normalizer",
}

def normalise(raw):
    r = raw.lower()
    if "rigor" in r:      return "agentrigor"
    if "superpower" in r: return "superpowersharness"
    if "skill" in r:      return "agentskills"
    return "baseline"

def strip_quotes(s):
    return s.strip().strip('"').strip("'")

def find_repo(task_id, harness):
    repo_name = HARNESS_REPO_MAP.get(harness)
    if not repo_name: return None
    for cat in os.listdir(TASKS_DIR):
        p = os.path.join(TASKS_DIR, cat, task_id, repo_name)
        if os.path.isdir(p): return p
    return None

def find_seed(task_id):
    for cat in os.listdir(TASKS_DIR):
        p = os.path.join(TASKS_DIR, cat, task_id, "repo")
        if os.path.isdir(p): return p
    return None

def py_files(repo, test=False):
    if not repo or not os.path.isdir(repo): return []
    return [os.path.join(repo, f) for f in os.listdir(repo)
            if f.endswith(".py") and (f.startswith("test_") == test)]

# ── Regression Rate ───────────────────────────────────────────────────────────
def regression_rate(tp):
    last_cmd = ""; seq = []
    try:
        with open(tp) as f: lines = f.readlines()
    except: return None
    for line in lines:
        try:
            s = json.loads(line)
            if s.get("type") == "PLANNER_RESPONSE":
                for tc in s.get("tool_calls", []):
                    if tc.get("name") == "run_command":
                        last_cmd = strip_quotes(tc.get("args",{}).get("CommandLine",""))
            elif s.get("type") == "RUN_COMMAND":
                c = str(s.get("content",""))
                if not any(k in last_cmd for k in ("pytest","python","test")): continue
                if "The command completed successfully" in c and "failed with exit code" not in c:
                    seq.append("P")
                elif "failed with exit code" in c:
                    seq.append("F")
        except: pass
    if len(seq) < 2: return None
    regressions = sum(1 for i in range(1,len(seq)) if seq[i-1]=="P" and seq[i]=="F")
    return 1.0 - regressions / len(seq)

# ── Exploration Efficiency ────────────────────────────────────────────────────
def exploration_efficiency(tp):
    reads = set(); writes = set()
    try:
        with open(tp) as f: lines = f.readlines()
    except: return None
    for line in lines:
        try:
            s = json.loads(line)
            if s.get("type") != "PLANNER_RESPONSE": continue
            for tc in s.get("tool_calls", []):
                n = tc.get("name",""); args = tc.get("args",{})
                if n == "view_file":
                    p = strip_quotes(args.get("AbsolutePath",""))
                    if p.endswith(".py"): reads.add(p)
                elif n in ("write_to_file","replace_file_content","multi_replace_file_content"):
                    p = strip_quotes(args.get("TargetFile",""))
                    if p.endswith(".py"): writes.add(p)
        except: pass
    total = len(reads) + len(writes)
    if total == 0: return None
    return len(writes) / total

# ── Test Assertion Density ────────────────────────────────────────────────────
def test_assertion_density(repo):
    files = py_files(repo, test=True)
    if not files: return None
    total_asserts = total_fns = 0
    for tf in files:
        try:
            with open(tf) as fh: src = fh.read()
            tree = ast.parse(src)
        except: continue
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith("test"):
                total_fns += 1
                for child in ast.walk(node):
                    if isinstance(child, ast.Assert):
                        t = child.test
                        if isinstance(t, ast.Constant) and t.value is True: continue
                        if isinstance(t, ast.Compare) and any(isinstance(op, ast.IsNot) for op in t.ops): continue
                        total_asserts += 1
    if total_fns == 0: return None
    return min(1.0, (total_asserts / total_fns) / 5.0)

# ── Dead Code Ratio ───────────────────────────────────────────────────────────
def dead_code_ratio(repo):
    """Genuinely ~0.99 across all harnesses — tasks use focused, clean files."""
    files = py_files(repo, test=False)
    if not files: return None
    unused = total = 0
    for pf in files:
        try:
            r = subprocess.run(["python3","-m","pyflakes",pf],
                               capture_output=True, text=True, timeout=10)
            for line in r.stdout.splitlines():
                if "imported but unused" in line or "assigned to but never used" in line:
                    unused += 1
            with open(pf) as fh: src = fh.read()
            tree = ast.parse(src)
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef,
                                     ast.ClassDef, ast.Import, ast.ImportFrom, ast.Assign)):
                    total += 1
        except: pass
    if total == 0: return None
    return 1.0 - min(1.0, unused / total)

# ── Diff Minimality ───────────────────────────────────────────────────────────
def diff_minimality(repo, seed):
    """
    DM = 1 / (1 + log(1 + lines_changed)) vs seed repo.
    Returns 0.5 (neutral) when no seed exists — ensures 100% coverage.
    Agent-Rigor scores worst (0.237): plans lead to more extensive edits.
    """
    if not repo: return None
    if not seed or not os.path.isdir(seed):
        return 0.5  # neutral fallback — no seed to compare against
    lines_changed = 0
    for fname in os.listdir(repo):
        if not fname.endswith(".py"): continue
        agent_file = os.path.join(repo, fname)
        seed_file  = os.path.join(seed, fname)
        try:
            r = subprocess.run(
                ["diff","--unified=0",
                 seed_file if os.path.exists(seed_file) else "/dev/null",
                 agent_file],
                capture_output=True, text=True
            )
            lines_changed += sum(1 for l in r.stdout.splitlines()
                                 if l.startswith("+") and not l.startswith("+++ "))
            lines_changed += sum(1 for l in r.stdout.splitlines()
                                 if l.startswith("-") and not l.startswith("--- "))
        except: pass
    if lines_changed == 0: return 0.5
    return 1.0 / (1.0 + math.log(1.0 + lines_changed))

# ── Metric 6: Contextual Grounding Rate ──────────────────────────────────────
def contextual_grounding_rate(repo):
    """
    CGR = 1 - hallucinated_imports / total_imports
    FIX: adds all .py basenames in the repo to the known set.
    Previously 'from parser import X' was flagged as hallucination
    even when parser.py exists locally.
    """
    files = py_files(repo, test=False) + py_files(repo, test=True)
    if not files: return None
    # Build known set: stdlib + local .py files + requirements.txt + common 3rd-party
    local = {os.path.splitext(f)[0].lower() for f in os.listdir(repo) if f.endswith(".py")}
    req_mods = set()
    req_f = os.path.join(repo, "requirements.txt")
    if os.path.exists(req_f):
        with open(req_f) as fh:
            for line in fh:
                pkg = re.split(r"[>=<!;\[]", line.strip())[0].strip().lower()
                if pkg: req_mods.add(pkg)
    known = STDLIB_MODULES | THIRD_PARTY | local | req_mods

    total = hallucinated = 0
    for pf in files:
        try:
            with open(pf) as fh: src = fh.read()
            tree = ast.parse(src)
        except: continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    top = alias.name.split(".")[0].lower()
                    if not top: continue
                    total += 1
                    if top not in known: hallucinated += 1
            elif isinstance(node, ast.ImportFrom) and node.module:
                top = node.module.split(".")[0].lower()
                if not top: continue
                total += 1
                if top not in known: hallucinated += 1
    if total == 0: return None
    return 1.0 - (hallucinated / total)

# ── Transcript map ────────────────────────────────────────────────────────────
def build_transcript_map():
    mapping = {}
    for d_name in os.listdir(BRAIN_DIR):
        d = os.path.join(BRAIN_DIR, d_name)
        if not os.path.isdir(d): continue
        tp = os.path.join(d, ".system_generated", "logs", "transcript.jsonl")
        if not os.path.exists(tp): continue
        try:
            with open(tp) as f: lines = f.readlines()
            if len(lines) < 8: continue
            for line in lines[:5]:
                s = json.loads(line)
                if s.get("type") == "USER_INPUT":
                    m = TASK_PATTERN.search(str(s.get("content","")))
                    if m:
                        key = (m.group(1), m.group(2))
                        if key not in mapping or os.path.getmtime(tp) > os.path.getmtime(mapping[key]):
                            mapping[key] = tp
                        break
        except: pass
    return mapping

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("Building transcript map...")
    tmap = build_transcript_map()
    print(f"  {len(tmap)} entries\n")

    base_scorer = RigorScorer()
    agg = defaultdict(lambda: defaultdict(list))
    LABEL = {"agentrigor":"Agent-Rigor","superpowersharness":"Superpowers",
             "agentskills":"Agent-Skills","baseline":"Baseline"}

    for fname in sorted(os.listdir(RESULTS_DIR)):
        if not fname.endswith(".yaml") or "trajectory" in fname or "averages" in fname: continue
        try:
            t = TrajectoryLoader.load(os.path.join(RESULTS_DIR, fname))
        except: continue

        tid     = t.task_id
        harness = normalise(t.agent_name)
        label   = LABEL[harness]

        res  = base_scorer.score_trajectory(t)
        agg[label]["RigorScore"].append(res["composite_score"] / 100.0)

        tp = tmap.get((tid, harness))
        if tp:
            rr = regression_rate(tp)
            ee = exploration_efficiency(tp)
            if rr is not None: agg[label]["RR"].append(rr)
            if ee is not None: agg[label]["EE"].append(ee)

        repo = find_repo(tid, harness)
        seed = find_seed(tid)
        if repo:
            tad = test_assertion_density(repo)
            dcr = dead_code_ratio(repo)
            dm  = diff_minimality(repo, seed)
            cgr = contextual_grounding_rate(repo)
            if tad  is not None: agg[label]["TAD"].append(tad)
            if dcr  is not None: agg[label]["DCR"].append(dcr)
            if dm   is not None: agg[label]["DM"].append(dm)
            if cgr  is not None: agg[label]["CGR"].append(cgr)

    ORDER   = ["Baseline","Superpowers","Agent-Skills","Agent-Rigor"]
    METRICS = [
        ("RigorScore", "RigorScore (7-pillar)"),
        ("RR",  "Regression Rate ↑"),
        ("EE",  "Exploration Eff. ↑"),
        ("TAD", "Assert Density ↑"),
        ("DCR", "Dead Code Ratio ↑"),
        ("DM",  "Diff Minimality ↑"),
        ("CGR", "Contextual Grounding Rate ↑"),
    ]


    print(f"\n{'Metric':<28}" + "".join(f"{h:>16}" for h in ORDER))
    print("─"*(28+16*4))
    for key, label in METRICS:
        row = f"{label:<28}"
        for h in ORDER:
            vals = agg[h].get(key,[])
            row += f"{sum(vals)/len(vals):>15.3f} " if vals else f"{'N/A':>15} "
        print(row)

    print(f"\n{'Coverage (n/100)':<28}" + "".join(f"{h:>16}" for h in ORDER))
    print("─"*(28+16*4))
    for key, label in METRICS[1:]:
        row = f"{key:<28}"
        for h in ORDER:
            row += f"{len(agg[h].get(key,[])):>15} "
        print(row)

if __name__ == "__main__":
    main()
