import json

def recover_jsonl_data(filepath: str) -> list[dict]:
    recovered = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                if isinstance(obj, dict):
                    recovered.append(obj)
            except json.JSONDecodeError:
                continue
    return recovered
