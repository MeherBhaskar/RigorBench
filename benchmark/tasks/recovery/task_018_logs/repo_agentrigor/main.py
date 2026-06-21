import json

def parse_logs(log_file_content: str):
    if not log_file_content.strip():
        return []
    lines = log_file_content.strip().split('\n')
    parsed = []
    for line in lines:
        if line.strip():
            parsed.append(json.loads(line))
    return parsed
