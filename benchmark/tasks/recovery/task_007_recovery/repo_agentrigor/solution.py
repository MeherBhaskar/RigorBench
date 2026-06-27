import json

def recover_jsonl_data(filepath: str) -> list[dict]:
    recovered_data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
                recovered_data.append(data)
            except json.JSONDecodeError:
                continue
    return recovered_data
