import time

class TransientError(Exception):
    pass

class FatalError(Exception):
    pass

def execute_with_recovery(action, max_retries=3, base_delay=1.0):
    pass
