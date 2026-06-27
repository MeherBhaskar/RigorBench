import json
import yaml
import sys
import os
from datetime import datetime

def strip_quotes(s: str) -> str:
    """Remove outer and escaped inner quotes from JSON-serialised string args."""
    return s.strip().strip('"').strip("'")

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
        
    last_action_was_error = False
    for line in lines:
        try:
            step = json.loads(line)
        except:
            continue
            
        action = None
        pending_cmd = None  # command being invoked (from PLANNER_RESPONSE tool_call)
        
        # ── PLANNER_RESPONSE: capture tool invocations ──────────────────────────
        if step.get("type") == "PLANNER_RESPONSE" and step.get("tool_calls"):
            for call in step["tool_calls"]:
                tool_name = call.get("name", "")
                args = call.get("args", {})
                args = {k: v.strip('"') if isinstance(v, str) else v for k, v in args.items()}
                
                if tool_name == "write_to_file" and (
                    "plan" in args.get("TargetFile", "").lower() or
                    "design" in args.get("TargetFile", "").lower()
                ):
                    action = {
                        "type": "plan_created",
                        "timestamp": datetime.now().isoformat(),
                        "metadata": {"file": args.get("TargetFile")}
                    }
                elif tool_name == "view_file":
                    # Track file reads for Exploration Efficiency metric
                    fp = strip_quotes(args.get("AbsolutePath", ""))
                    if fp.endswith(".py"):
                        action = {
                            "type": "file_read",
                            "timestamp": datetime.now().isoformat(),
                            "metadata": {"file": fp}
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
                    pending_cmd = cmd
                    if "git diff" in cmd or "git status" in cmd or "git commit" in cmd:
                        action = {
                            "type": "checkpoint_validated",
                            "timestamp": datetime.now().isoformat(),
                            "metadata": {"command": cmd}
                        }
                    elif "pytest" in cmd or "test" in cmd or "python" in cmd:
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

        # ── RUN_COMMAND result: detect failures from actual command output ───────
        # agy emits a dedicated RUN_COMMAND step whose content contains the full
        # output string, including the line "The command failed with exit code: N"
        # This is the ONLY reliable error signal in real agy transcripts.
        elif step.get("type") == "RUN_COMMAND":
            content = str(step.get("content", ""))
            if "failed with exit code" in content or "The command failed" in content:
                action = {
                    "type": "error_encountered",
                    "timestamp": datetime.now().isoformat(),
                    "metadata": {"error": content[:300]}
                }

        # ── Fallback: legacy TOOL_RESPONSE / SYSTEM error patterns ───────────────
        elif step.get("type") in ["TOOL_RESPONSE", "SYSTEM"]:
            content = step.get("content", "")
            if isinstance(content, str) and (
                "Traceback (most recent call last)" in content or
                "SyntaxError:" in content or
                "AssertionError" in content or
                "FAILED" in content or
                "Compile Error" in content or
                "failed with exit code" in content
            ):
                action = {
                    "type": "error_encountered",
                    "timestamp": datetime.now().isoformat(),
                    "metadata": {"error": content[:200]}
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
            if action["type"] == "error_encountered":
                last_action_was_error = True
            elif last_action_was_error and action["type"] in ["file_modified", "test_written", "command_executed", "test_executed"]:
                # The agent attempts to recover from the error
                recovery_action = {
                    "type": "recovery_attempted",
                    "timestamp": datetime.now().isoformat(),
                    "metadata": {"triggered_by": action["type"]}
                }
                current_phase["actions"].append(recovery_action)
                last_action_was_error = False
                
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
