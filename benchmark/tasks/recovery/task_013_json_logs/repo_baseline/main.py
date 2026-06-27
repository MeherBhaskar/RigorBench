from typing import List, Tuple, Dict, Any
import json

def recover_log_data(log_content: str) -> Tuple[List[Dict[str, Any]], int]:
    parsed_logs = []
    corrupted_count = 0
    
    for line in log_content.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            parsed = json.loads(line)
            if isinstance(parsed, dict):
                parsed_logs.append(parsed)
            else:
                corrupted_count += 1
        except json.JSONDecodeError:
            corrupted_count += 1
            
    return parsed_logs, corrupted_count
