import json

def recover_logs(log_content: str) -> dict:
    result = {}
    for line in log_content.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
            if isinstance(data, dict):
                event_type = data.get("event_type")
                value = data.get("value")
                if isinstance(event_type, str) and isinstance(value, int) and not isinstance(value, bool):
                    result[event_type] = result.get(event_type, 0) + value
        except json.JSONDecodeError:
            pass
    return result
