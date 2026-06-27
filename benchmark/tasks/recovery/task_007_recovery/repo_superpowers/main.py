import json

def recover_jsonl_data(filepath: str) -> list[dict]:
    valid_objects = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                obj = json.loads(line)
                valid_objects.append(obj)
            except json.JSONDecodeError:
                pass
    return valid_objects
