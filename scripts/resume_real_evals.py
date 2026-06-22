import os
import subprocess
import time
import sys
import yaml

BRAIN_DIR = os.path.expanduser("~/.gemini/antigravity-cli/brain/")

def get_latest_conversation_dir():
    try:
        dirs = [os.path.join(BRAIN_DIR, d) for d in os.listdir(BRAIN_DIR)]
        dirs = [d for d in dirs if os.path.isdir(d)]
        if not dirs:
            return None
        return max(dirs, key=os.path.getmtime)
    except FileNotFoundError:
        return None

def main():
    base_dir = '/home/meher/dev/rigorbench-paper/benchmark/tasks'
    results_dir = '/home/meher/dev/rigorbench-paper/benchmark/results'
    parser_script = '/home/meher/dev/rigorbench-paper/benchmark/scripts/parse_antigravity_transcript.py'
    
    os.makedirs(results_dir, exist_ok=True)
    
    # First, cleanup empty mock results
    deleted_count = 0
    for filename in os.listdir(results_dir):
        if not filename.endswith('.yaml'): continue
        filepath = os.path.join(results_dir, filename)
        with open(filepath, 'r') as f:
            try:
                data = yaml.safe_load(f)
                if data and len(data.get('phases', [])[0].get('actions', [])) == 0:
                    os.remove(filepath)
                    deleted_count += 1
            except:
                pass
    print(f"Deleted {deleted_count} failed/empty results.")

    frameworks = [
        ("baseline", ""),
        ("agentrigor", "\nCRITICAL DISCIPLINE: You MUST first write a plan in a plan.md file outlining your approach. You MUST write tests and verify them. You MUST ensure atomic transitions."),
        ("agentskills", "\nFRAMEWORK: You are operating under the \"Agent-Skills\" framework. You should leverage specialized, focused actions. Be efficient, direct, and modular in your tool usage."),
        ("superpowersharness", "\nFRAMEWORK: You are operating under the \"Superpowers\" framework. You should maintain explicit, deep context and reason thoroughly before acting. Ensure high-fidelity context preservation throughout the task.")
    ]
    
    total = 0
    
    for cat in os.listdir(base_dir):
        cat_path = os.path.join(base_dir, cat)
        if not os.path.isdir(cat_path): continue
        for task in os.listdir(cat_path):
            if not task.startswith('task_'): continue
            for fw_prefix, _ in frameworks:
                if fw_prefix == 'agentrigor': filename = f"agentrigor_{task}.yaml"
                elif fw_prefix == 'superpowersharness': filename = f"superpowersharness_{task}.yaml"
                else: filename = f"{fw_prefix}_{task}.yaml"
                if not os.path.exists(os.path.join(results_dir, filename)):
                    total += 1

    print(f"Found {total} missing real test runs.")
    count = 0
    
    for cat in os.listdir(base_dir):
        cat_path = os.path.join(base_dir, cat)
        if not os.path.isdir(cat_path): continue
        
        for task in os.listdir(cat_path):
            if not task.startswith('task_'): continue
            
            repo_path = os.path.join(cat_path, task, 'repo_baseline')
            readme_path = os.path.join(repo_path, 'README.md')
            prompt_core = f"Solve the task described in {repo_path}."
            if os.path.exists(readme_path):
                with open(readme_path, 'r') as f: prompt_core = f.read().strip()
            
            for fw_prefix, fw_suffix in frameworks:
                if fw_prefix == 'agentrigor': filename = f"agentrigor_{task}.yaml"
                elif fw_prefix == 'superpowersharness': filename = f"superpowersharness_{task}.yaml"
                else: filename = f"{fw_prefix}_{task}.yaml"
                filepath = os.path.join(results_dir, filename)
                
                if os.path.exists(filepath): continue
                    
                prompt = f"Your task is in {os.path.join(cat_path, task, 'repo_' + fw_prefix)}. {prompt_core}{fw_suffix}"
                print(f"[{count+1}/{total}] Running live agent for {task} ({fw_prefix})...")
                
                previous_latest = get_latest_conversation_dir()
                
                try:
                    res = subprocess.run(
                        ['agy', '--dangerously-skip-permissions', '--print-timeout', '10m', '--print', prompt],
                        timeout=1800,
                        capture_output=True, text=True
                    )
                    if res.returncode != 0:
                        print(f"  [Error] agy failed with code {res.returncode}. Stopping.")
                        print(f"  Stderr: {res.stderr}")
                        sys.exit(1)
                except subprocess.TimeoutExpired:
                    print(f"  Timeout expired for {task} ({fw_prefix})")
                
                # Check for new dir
                time.sleep(2)
                latest_dir = get_latest_conversation_dir()
                if latest_dir and latest_dir != previous_latest:
                    transcript_path = os.path.join(latest_dir, '.system_generated', 'logs', 'transcript.jsonl')
                    if os.path.exists(transcript_path):
                        print(f"  Parsing transcript from {transcript_path}...")
                        subprocess.run([sys.executable, parser_script, transcript_path, filepath, task, fw_prefix, str(fw_prefix == 'agentrigor').lower()])
                    else: print("  Failed to locate transcript.jsonl")
                else:
                    print("  [Error] No new conversation directory was created! agy might have failed silently.")
                    print(f"  Stdout: {res.stdout}")
                    sys.exit(1)
                
                count += 1

if __name__ == "__main__":
    main()
