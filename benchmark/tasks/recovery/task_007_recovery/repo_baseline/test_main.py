import os
import tempfile
from main import recover_jsonl_data

def test_recover_jsonl_data():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write('{"id": 1, "name": "Alice"}\n')
        f.write('CORRUPTED LINE 1\n')
        f.write('{"id": 2, "name": "Bob"}\n')
        f.write('{"id": 3, "missing_quotes": true\n')
        f.write('{"id": 4, "name": "Charlie"}\n')
        filepath = f.name
    
    try:
        recovered = recover_jsonl_data(filepath)
        assert len(recovered) == 3
        assert recovered[0] == {"id": 1, "name": "Alice"}
        assert recovered[1] == {"id": 2, "name": "Bob"}
        assert recovered[2] == {"id": 4, "name": "Charlie"}
    finally:
        os.remove(filepath)
