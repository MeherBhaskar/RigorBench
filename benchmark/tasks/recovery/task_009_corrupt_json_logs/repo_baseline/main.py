import json
from collections import defaultdict

def recover_logs(log_content: str) -> dict:
    result = defaultdict(int)
    for line in log_content.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
            if isinstance(data, dict) and "event_type" in data and "value" in data:
                if isinstance(data["event_type"], str) and isinstance(data["value"], int):
                    result[data["event_type"]] += data["value"]
        except json.JSONDecodeError:
            pass
    return dict(result)
