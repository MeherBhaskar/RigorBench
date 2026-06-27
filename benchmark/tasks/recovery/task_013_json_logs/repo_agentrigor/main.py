from typing import List, Tuple, Dict, Any
import json

def recover_log_data(log_content: str) -> Tuple[List[Dict[str, Any]], int]:
    valid_data = []
    corrupted_count = 0
    
    if not log_content:
        return valid_data, corrupted_count
        
    for line in log_content.split('\n'):
        if not line.strip():
            continue
            
        try:
            parsed = json.loads(line)
            if isinstance(parsed, dict):
                valid_data.append(parsed)
            else:
                corrupted_count += 1
        except json.JSONDecodeError:
            corrupted_count += 1
            
    return valid_data, corrupted_count
