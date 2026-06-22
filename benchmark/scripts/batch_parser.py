import json
import os
import subprocess

import re

BRAIN_DIR = "/home/meher/.gemini/antigravity-cli/brain"
os.makedirs("results", exist_ok=True)

with open("subagents_payload.json") as f:
    subs = json.load(f)

pattern = r"/home/meher/dev/rigorbench-paper/benchmark/tasks/[^/]+/([^/]+)/(repo_[a-zA-Z0-9_-]+)"

parsed_count = 0
for folder in os.listdir(BRAIN_DIR):
    transcript_path = os.path.join(BRAIN_DIR, folder, ".system_generated/logs/transcript.jsonl")
    if not os.path.exists(transcript_path):
        continue
        
    prompt = ""
    with open(transcript_path) as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get("type") == "USER_INPUT":
                    prompt = data.get("content", "")
                    break
            except: pass
            
    if not prompt: continue
    
    # Try regex-based path extraction first
    match = re.search(pattern, prompt)
    if match:
        task_id = match.group(1)
        repo_suffix = match.group(2)
        
        if repo_suffix == "repo_baseline":
            agent_name = "Baseline"
            rigor_enabled = "false"
            safe_agent = "baseline"
        elif repo_suffix in ["repo_rigor", "repo_agentrigor"]:
            agent_name = "Agent-Rigor"
            rigor_enabled = "true"
            safe_agent = "agentrigor"
        elif repo_suffix == "repo_agentskills":
            agent_name = "Agent-Skills"
            rigor_enabled = "true"
            safe_agent = "agentskills"
        elif repo_suffix in ["repo_superpowers", "repo_superpowersharness"]:
            agent_name = "Superpowers-Harness"
            rigor_enabled = "true"
            safe_agent = "superpowersharness"
        else:
            print(f"Unknown repo suffix {repo_suffix} in {folder}")
            continue
            
        out_yaml = f"results/{safe_agent}_{task_id}.yaml"
        print(f"Parsing {folder} ({task_id}, {agent_name}) -> {out_yaml}")
        subprocess.run(["python", "scripts/parse_antigravity_transcript.py", transcript_path, out_yaml, task_id, agent_name, rigor_enabled])
        parsed_count += 1
        continue

    # Fallback to fuzzy match
    matched_s = None
    for s in subs:
        if s["Prompt"] in prompt or prompt in s["Prompt"]:
            matched_s = s
            break
            
    if matched_s:
        role = matched_s["Role"]
        parts = role.split(" ")
        task_id = parts[0]
        agent_name = parts[1]
        if "Rigor" in role or "Skills" in role or "Superpowers" in role:
            agent_name = parts[1] + (("-" + parts[2]) if "-" not in parts[1] else "")
            
        rigor_enabled = "true" if ("Rigor" in role or "Skills" in role or "Superpowers" in role) else "false"
        
        safe_agent = agent_name.replace("-", "").lower()
        out_yaml = f"results/{safe_agent}_{task_id}.yaml"
        
        print(f"Fuzzy-matched Parsing {folder} -> {out_yaml}")
        subprocess.run(["python", "scripts/parse_antigravity_transcript.py", transcript_path, out_yaml, task_id, agent_name, rigor_enabled])
        parsed_count += 1

print(f"Parsed {parsed_count} real transcripts!")
