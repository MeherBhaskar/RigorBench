import json

def parse_logs(log_file_content: str):
    if not log_file_content.strip():
        return ([], 0)
    lines = log_file_content.strip().split('\n')
    parsed = []
    corrupted_count = 0
    for line in lines:
        if line.strip():
            try:
                parsed.append(json.loads(line))
            except json.JSONDecodeError:
                corrupted_count += 1
    return (parsed, corrupted_count)
