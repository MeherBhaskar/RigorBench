import json
import yaml
import sys
import os
from datetime import datetime

def parse_transcript(transcript_path, output_yaml_path, task_id, agent_name, rigor_enabled):
    phases = []
    current_phase = {
        "name": "execution",
        "started_at": datetime.now().isoformat(),
        "actions": []
    }
    
    total_tokens = 0
    duration_seconds = 0
    
    if not os.path.exists(transcript_path):
        print(f"Transcript not found: {transcript_path}")
        return

    with open(transcript_path, 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        try:
            step = json.loads(line)
        except:
            continue
            
        action = None
        
        # Check tool calls
        if "tool_calls" in step and step["tool_calls"]:
            for call in step["tool_calls"]:
                tool_name = call.get("name", "")
                args = call.get("args", {})
                
                # Strip extra quotes
                args = {k: v.strip('"') if isinstance(v, str) else v for k, v in args.items()}
                
                # Heuristics for planning
                if tool_name == "write_to_file" and ("plan" in args.get("TargetFile", "").lower() or "design" in args.get("TargetFile", "").lower()):
                    action = {
                        "type": "plan_created",
                        "timestamp": datetime.now().isoformat(),
                        "metadata": {"file": args.get("TargetFile")}
                    }
                elif tool_name in ["write_to_file", "multi_replace_file_content", "replace_file_content"]:
                    if "test" in args.get("TargetFile", "").lower():
                        action = {
                            "type": "test_written",
                            "timestamp": datetime.now().isoformat(),
                            "metadata": {"file": args.get("TargetFile")}
                        }
                    else:
                        action = {
                            "type": "file_modified",
                            "timestamp": datetime.now().isoformat(),
                            "metadata": {"file": args.get("TargetFile")}
                        }
                elif tool_name == "run_command":
                    cmd = args.get("CommandLine", "")
                    if "pytest" in cmd or "test" in cmd:
                        action = {
                            "type": "test_executed",
                            "timestamp": datetime.now().isoformat(),
                            "metadata": {"command": cmd}
                        }
                    else:
                        action = {
                            "type": "command_executed",
                            "timestamp": datetime.now().isoformat(),
                            "metadata": {"command": cmd}
                        }
        
        # Check errors in step status
        if step.get("status") == "ERROR" or (step.get("type") == "MODEL_ERROR"):
            action = {
                "type": "error_encountered",
                "timestamp": datetime.now().isoformat(),
                "metadata": {"error": step.get("content", "Unknown error")}
            }
            
        # Check abstention in text output
        if step.get("type") == "PLANNER_RESPONSE" and "content" in step:
            content_lower = step["content"].lower()
            if "cannot complete" in content_lower or "impossible" in content_lower or "ambiguous" in content_lower:
                action = {
                    "type": "abstention_declared",
                    "timestamp": datetime.now().isoformat(),
                    "metadata": {"reason": step["content"][:100]}
                }

        if action:
            current_phase["actions"].append(action)
            
    phases.append(current_phase)
    
    trajectory = {
        "task_id": task_id,
        "agent_name": agent_name,
        "rigor_enabled": rigor_enabled,
        "total_tokens": total_tokens,
        "duration_seconds": duration_seconds,
        "phases": phases
    }
    
    with open(output_yaml_path, 'w') as f:
        yaml.dump(trajectory, f, sort_keys=False)
    
    print(f"Parsed {len(current_phase['actions'])} actions into {output_yaml_path}")

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: python parse_antigravity_transcript.py <transcript.jsonl> <output.yaml> <task_id> <agent_name> <rigor_enabled>")
        sys.exit(1)
    parse_transcript(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5] == "true")
