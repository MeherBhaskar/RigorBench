import unittest
from main import verify_sequence

class TestVerifySequence(unittest.TestCase):
    def setUp(self):
        self.transitions = {
            'IDLE': {'start': 'RUNNING', 'error': 'ERROR'},
            'RUNNING': {'stop': 'IDLE', 'finish': 'COMPLETED', 'error': 'ERROR'},
            'COMPLETED': {'reset': 'IDLE'},
            'ERROR': {'reset': 'IDLE'}
        }

    def test_valid_sequence(self):
        self.assertTrue(verify_sequence(['start', 'finish'], self.transitions, 'IDLE', {'COMPLETED'}))

    def test_invalid_event(self):
        self.assertFalse(verify_sequence(['start', 'start'], self.transitions, 'IDLE', {'RUNNING', 'IDLE'}))

    def test_invalid_end_state(self):
        self.assertFalse(verify_sequence(['start'], self.transitions, 'IDLE', {'IDLE', 'COMPLETED'}))

    def test_empty_sequence_valid(self):
        self.assertTrue(verify_sequence([], self.transitions, 'IDLE', {'IDLE'}))

    def test_empty_sequence_invalid(self):
        self.assertFalse(verify_sequence([], self.transitions, 'IDLE', {'RUNNING'}))

    def test_unrecognized_state(self):
        self.assertFalse(verify_sequence(['start', 'unknown_event'], self.transitions, 'IDLE', {'COMPLETED'}))

if __name__ == '__main__':
    unittest.main()
