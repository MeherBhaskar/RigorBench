import unittest
from main import recover_logs

class TestRecovery(unittest.TestCase):
    def test_recover_logs(self):
        logs = """{"event_type": "click", "value": 5}
{event_type: click, value: 10} 
{"event_type": "view", "value": 2}
{"event_type": "click", "value": 
{"event_type": "purchase", "value": 100}
not a json
{"event_type": "view", "value": 3}"""
        expected = {"click": 5, "view": 5, "purchase": 100}
        self.assertEqual(recover_logs(logs), expected)

    def test_empty(self):
        self.assertEqual(recover_logs(""), {})

    def test_all_corrupted(self):
        logs = """{
}
{"a": 1
not json"""
        self.assertEqual(recover_logs(logs), {})

    def test_invalid_types(self):
        logs = """{"event_type": 123, "value": 5}
{"event_type": "click", "value": "5"}
{"event_type": "click", "value": true}
{"event_type": "view", "value": 2.5}"""
        self.assertEqual(recover_logs(logs), {})

if __name__ == '__main__':
    unittest.main()
