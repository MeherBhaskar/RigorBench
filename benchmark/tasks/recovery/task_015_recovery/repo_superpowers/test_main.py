import unittest
from main import recover_state

class TestRecovery(unittest.TestCase):
    def test_basic_recovery(self):
        snapshot = {"a": 1, "b": 2}
        logs = [
            {"tx_id": 1, "type": "START"},
            {"tx_id": 1, "type": "SET", "key": "a", "value": 10},
            {"tx_id": 1, "type": "COMMIT"}
        ]
        self.assertEqual(recover_state(snapshot, logs), {"a": 10, "b": 2})

    def test_aborted_transaction(self):
        snapshot = {"a": 1}
        logs = [
            {"tx_id": 1, "type": "START"},
            {"tx_id": 1, "type": "SET", "key": "a", "value": 10},
            {"tx_id": 1, "type": "ABORT"}
        ]
        self.assertEqual(recover_state(snapshot, logs), {"a": 1})

    def test_incomplete_transaction(self):
        snapshot = {"a": 1}
        logs = [
            {"tx_id": 1, "type": "START"},
            {"tx_id": 1, "type": "SET", "key": "a", "value": 10}
        ]
        self.assertEqual(recover_state(snapshot, logs), {"a": 1})

    def test_interleaved_transactions(self):
        snapshot = {"x": 0, "y": 0}
        logs = [
            {"tx_id": 1, "type": "START"},
            {"tx_id": 2, "type": "START"},
            {"tx_id": 1, "type": "SET", "key": "x", "value": 1},
            {"tx_id": 2, "type": "SET", "key": "x", "value": 2},
            {"tx_id": 2, "type": "SET", "key": "y", "value": 2},
            {"tx_id": 1, "type": "COMMIT"},
            {"tx_id": 2, "type": "ABORT"}
        ]
        self.assertEqual(recover_state(snapshot, logs), {"x": 1, "y": 0})
        
    def test_multiple_commits(self):
        snapshot = {}
        logs = [
            {"tx_id": 1, "type": "START"},
            {"tx_id": 2, "type": "START"},
            {"tx_id": 1, "type": "SET", "key": "x", "value": 10},
            {"tx_id": 1, "type": "COMMIT"},
            {"tx_id": 2, "type": "SET", "key": "x", "value": 20},
            {"tx_id": 2, "type": "COMMIT"}
        ]
        self.assertEqual(recover_state(snapshot, logs), {"x": 20})

if __name__ == '__main__':
    unittest.main()
