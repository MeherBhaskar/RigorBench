from typing import List, Tuple, Dict, Any
import json

def recover_log_data(log_content: str) -> Tuple[List[Dict[str, Any]], int]:
    valid_data = []
    errors = 0
    
    if not log_content:
        return valid_data, errors
        
    for line in log_content.split('\n'):
        if not line.strip():
            continue
            
        try:
            parsed = json.loads(line)
            if isinstance(parsed, dict):
                valid_data.append(parsed)
            else:
                errors += 1
        except json.JSONDecodeError:
            errors += 1
            
    return valid_data, errors
