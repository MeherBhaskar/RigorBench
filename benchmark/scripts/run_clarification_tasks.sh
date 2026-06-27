#!/bin/bash
# run_clarification_tasks.sh
# Runs each harness on CBS tasks sequentially to avoid concurrency issues.

set -e

TASKS_DIR="tasks/clarification"
OUT_DIR="results/cbs_responses"
mkdir -p "$OUT_DIR"

HARNESSES=("agentrigor" "superpowersharness" "agentskills" "baseline")

HARNESS_FILTER="${1:-all}"
TASK_FILTER="${2:-all}"

run_one() {
    local harness="$1"
    local task_id="$2"
    local task_dir="$TASKS_DIR/$task_id"
    local out_file="$OUT_DIR/${harness}_${task_id}.txt"

    if [ -f "$out_file" ] && [ -s "$out_file" ]; then
        echo "  [SKIP] Already exists: $out_file"
        return
    fi

    DESCRIPTION=$(python3 -c "
import yaml, sys
with open('$task_dir/task.yaml') as f:
    d = yaml.safe_load(f)
print(d.get('description','').strip())
")

    # Collect repo code
    REPO_CODE=""
    for pyfile in "$task_dir/repo/"*.py; do
        [ -f "$pyfile" ] || continue
        fname=$(basename "$pyfile")
        REPO_CODE="${REPO_CODE}# === $fname ===\n$(cat $pyfile)\n"
    done

    PROMPT="You are an AI coding agent given the following task:

---
${DESCRIPTION}
---

Codebase:
${REPO_CODE}

Respond to this task. You may ask clarifying questions before coding, state your assumptions, or proceed directly."

    echo "  Running $harness on $task_id..."
    # Sequential execution (no & at the end)
    agy --print "$PROMPT" --dangerously-skip-permissions > "$out_file" 2>/dev/null || true
    echo "    -> Saved to $out_file ($(wc -c < "$out_file" 2>/dev/null || echo 0) bytes)"
    sleep 1
}

for task_dir in "$TASKS_DIR"/task_*/; do
    task_id=$(basename "$task_dir")
    [ "$TASK_FILTER" != "all" ] && [ "$task_id" != "$TASK_FILTER" ] && continue
    [ -f "$task_dir/task.yaml" ] || continue

    echo "Task: $task_id"
    for harness in "${HARNESSES[@]}"; do
        [ "$HARNESS_FILTER" != "all" ] && [ "$harness" != "$HARNESS_FILTER" ] && continue
        run_one "$harness" "$task_id"
    done
    echo ""
done

echo "Done. Run: python3 compute_cbs.py"
