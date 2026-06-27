import json

def recover_logs(log_content: str) -> dict:
    result = {}
    if not log_content:
        return result
        
    for line in log_content.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
            if isinstance(data, dict):
                event_type = data.get("event_type")
                value = data.get("value")
                
                if type(event_type) is str and type(value) is int:
                    result[event_type] = result.get(event_type, 0) + value
        except (json.JSONDecodeError, TypeError):
            continue
            
    return result
