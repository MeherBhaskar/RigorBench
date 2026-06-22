import json
import os
import yaml
from parse_antigravity_transcript import parse_transcript

def main():
    mock_transcript_path = "mock_transcript.jsonl"
    output_yaml_path = "mock_run_parsed.yaml"
    
    # Construct a mock JSONL transcript showing:
    # 1. A tool call running pytest (test_executed)
    # 2. A tool response indicating a failure (error_encountered)
    # 3. A file modification to fix the code (file_modified & recovery_attempted)
    # 4. A git status call (checkpoint_validated)
    mock_steps = [
        # Step 1: Tool call running pytest
        {
            "step_index": 1,
            "type": "PLANNER_RESPONSE",
            "tool_calls": [
                {
                    "name": "run_command",
                    "args": {"CommandLine": "pytest test_parser.py"}
                }
            ]
        },
        # Step 2: Pytest output indicating a Traceback/failure
        {
            "step_index": 2,
            "type": "TOOL_RESPONSE",
            "content": "Traceback (most recent call last):\n  File \"parser.py\", line 10, in convert_to_utc\n    raise ValueError(\"DST error\")\nValueError: DST error\nFAILED test_parser.py::test_timezone"
        },
        # Step 3: File modification to apply the fix
        {
            "step_index": 3,
            "type": "PLANNER_RESPONSE",
            "tool_calls": [
                {
                    "name": "replace_file_content",
                    "args": {"TargetFile": "parser.py", "ReplacementContent": "pass"}
                }
            ]
        },
        # Step 4: Verification checkpoint check via git status
        {
            "step_index": 4,
            "type": "PLANNER_RESPONSE",
            "tool_calls": [
                {
                    "name": "run_command",
                    "args": {"CommandLine": "git status"}
                }
            ]
        }
    ]
    
    with open(mock_transcript_path, "w") as f:
        for step in mock_steps:
            f.write(json.dumps(step) + "\n")
            
    print("Running parser on mock transcript...")
    parse_transcript(mock_transcript_path, output_yaml_path, "mock_task", "test-agent", True)
    
    # Load and assert parsed actions
    assert os.path.exists(output_yaml_path), "Output YAML not created"
    with open(output_yaml_path, "r") as f:
        data = yaml.safe_load(f)
        actions = data.get("phases", [{}])[0].get("actions", [])
        
        types = [a["type"] for a in actions]
        print("Parsed Action Types:", types)
        
        # We expect:
        # - test_executed (from Step 1)
        # - error_encountered (from Step 2 traceback)
        # - recovery_attempted (triggered by step 3 action after error)
        # - file_modified (from Step 3 tool call)
        # - checkpoint_validated (from Step 4 git status check)
        assert "test_executed" in types, "test_executed not found"
        assert "error_encountered" in types, "error_encountered not found"
        assert "recovery_attempted" in types, "recovery_attempted not found"
        assert "file_modified" in types, "file_modified not found"
        assert "checkpoint_validated" in types, "checkpoint_validated not found"
        
        # Verify the sequence: recovery_attempted must immediately precede file_modified
        idx_error = types.index("error_encountered")
        idx_rec = types.index("recovery_attempted")
        idx_file = types.index("file_modified")
        assert idx_error < idx_rec < idx_file, "Invalid sequence of error/recovery actions"
        
        print("\nAll Assertions Passed successfully!")

    # Cleanup
    if os.path.exists(mock_transcript_path):
        os.remove(mock_transcript_path)
    if os.path.exists(output_yaml_path):
        os.remove(output_yaml_path)

if __name__ == "__main__":
    main()
