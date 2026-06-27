"""
reparse_all_results.py
======================
Re-parse all benchmark brain conversations using the improved parser
(which correctly detects 'The command failed with exit code: N' errors).

Scans brain/ for conversations whose USER_INPUT references a benchmark task path,
extracts task_id + harness from the path, and re-emits the result YAML.
"""
import os
import sys
import json
import re
import subprocess
import datetime

BRAIN_DIR = os.path.expanduser("~/.gemini/antigravity-cli/brain")
RESULTS_DIR = "/home/meher/dev/rigorbench-paper/benchmark/results"
PARSER_SCRIPT = "/home/meher/dev/rigorbench-paper/benchmark/scripts/parse_antigravity_transcript.py"

# Pattern: /home/.../tasks/<cat>/<task_id>/repo_<harness>
TASK_PATTERN = re.compile(
    r"tasks/\w+/(task_\d+_\w+)/repo_(\w+)"
)

HARNESS_FILENAME_MAP = {
    "agentrigor":         lambda tid: f"agentrigor_{tid}.yaml",
    "agentskills":        lambda tid: f"agentskills_{tid}.yaml",
    "superpowersharness": lambda tid: f"superpowersharness_{tid}.yaml",
    "baseline":           lambda tid: f"baseline_{tid}.yaml",
}

def get_task_harness_from_transcript(transcript_path):
    """Return (task_id, harness_prefix) by reading the USER_INPUT step."""
    try:
        with open(transcript_path) as f:
            for line in f:
                s = json.loads(line)
                if s.get("type") == "USER_INPUT":
                    content = str(s.get("content", ""))
                    m = TASK_PATTERN.search(content)
                    if m:
                        task_id = m.group(1)
                        harness = m.group(2)
                        return task_id, harness
    except Exception:
        pass
    return None, None


def main():
    all_dirs = [
        os.path.join(BRAIN_DIR, d)
        for d in os.listdir(BRAIN_DIR)
        if os.path.isdir(os.path.join(BRAIN_DIR, d))
    ]

    matched = 0
    updated = 0
    skipped = 0

    for d in sorted(all_dirs, key=os.path.getmtime):
        tp = os.path.join(d, ".system_generated", "logs", "transcript.jsonl")
        if not os.path.exists(tp):
            continue

        # Quick size check — skip tiny/trivial conversations
        with open(tp) as f:
            lines = f.readlines()
        if len(lines) < 8:
            continue

        task_id, harness = get_task_harness_from_transcript(tp)
        if not task_id or harness not in HARNESS_FILENAME_MAP:
            continue

        filename = HARNESS_FILENAME_MAP[harness](task_id)
        output_path = os.path.join(RESULTS_DIR, filename)

        if not os.path.exists(output_path):
            skipped += 1
            continue  # result file doesn't exist yet – skip

        matched += 1
        rigor_flag = "true" if harness == "agentrigor" else "false"

        result = subprocess.run(
            [
                sys.executable, PARSER_SCRIPT,
                tp, output_path, task_id, harness, rigor_flag
            ],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            updated += 1
            print(f"  ✓ {filename}  ({result.stdout.strip()})")
        else:
            print(f"  ✗ {filename}: {result.stderr.strip()[:100]}")

    print(f"\nDone. Matched: {matched}, Updated: {updated}, Skipped (no result file): {skipped}")


if __name__ == "__main__":
    main()
