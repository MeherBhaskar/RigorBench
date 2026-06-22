import os
import subprocess
import json
import yaml
import sys
from parse_antigravity_transcript import parse_transcript

BRAIN_DIR = os.path.expanduser("~/.gemini/antigravity-cli/brain/")

def get_latest_conversation_dir():
    try:
        dirs = [os.path.join(BRAIN_DIR, d) for d in os.listdir(BRAIN_DIR)]
        dirs = [d for d in dirs if os.path.isdir(d)]
        if not dirs:
            return None
        return max(dirs, key=os.path.getmtime)
    except Exception as e:
        print(f"Error reading brain dir: {e}")
        return None

def main():
    task_id = "task_001_date_parser"
    cat_path = "/home/meher/dev/rigorbench-paper/benchmark/tasks/verification"
    task_path = os.path.join(cat_path, task_id)
    repo_path = os.path.join(task_path, "repo_baseline")
    readme_path = os.path.join(repo_path, "README.md")
    
    prompt_core = f"Solve the task described in {repo_path}."
    if os.path.exists(readme_path):
        with open(readme_path, "r") as f:
            prompt_core = f.read().strip()
            
    # We will append some instructions to trigger error and recovery:
    prompt = (
        f"Your task is in {repo_path}. {prompt_core}\n"
        "To help verify telemetry: You MUST run standard pytest command to view test failures, modify the code to address it, and run `git status` or `git diff` to verify the state of your codebase."
    )
    
    print(f"Running live agent on {task_id}...")
    try:
        subprocess.run(
            ["agy", "--dangerously-skip-permissions", "--print", prompt],
            timeout=300 # 5 minutes timeout
        )
    except subprocess.TimeoutExpired:
        print("Timeout expired.")
        
    latest_dir = get_latest_conversation_dir()
    if not latest_dir:
        print("Could not find latest conversation directory.")
        return
        
    transcript_path = os.path.join(latest_dir, ".system_generated", "logs", "transcript.jsonl")
    if not os.path.exists(transcript_path):
        print(f"Transcript not found at {transcript_path}")
        return
        
    output_yaml = "test_run_parsed.yaml"
    print(f"Parsing transcript at {transcript_path}...")
    parse_transcript(transcript_path, output_yaml, task_id, "test-agent", False)
    
    if os.path.exists(output_yaml):
        with open(output_yaml, "r") as f:
            data = yaml.safe_load(f)
            actions = data.get("phases", [{}])[0].get("actions", [])
            print("\nExtracted Actions from Trajectory:")
            for a in actions:
                print(f"- Type: {a['type']}, Metadata: {a.get('metadata')}")
    else:
        print("Output YAML was not generated.")

if __name__ == "__main__":
    main()
