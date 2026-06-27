import unittest
import os
import tempfile
from solution import recover_jsonl_data

class TestRecoverJsonlData(unittest.TestCase):
    def test_recover_jsonl_data(self):
        content = """{"name": "Alice", "age": 30}
invalid json line
{"name": "Bob", "age": 25}
{"broken": "json"
{"name": "Charlie", "age": 35}"""

        with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as f:
            f.write(content)
            temp_path = f.name

        try:
            result = recover_jsonl_data(temp_path)
            expected = [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
                {"name": "Charlie", "age": 35}
            ]
            self.assertEqual(result, expected)
        finally:
            os.remove(temp_path)

if __name__ == '__main__':
    unittest.main()
