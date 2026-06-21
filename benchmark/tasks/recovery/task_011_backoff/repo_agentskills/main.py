import time

class TransientError(Exception):
    pass

class FatalError(Exception):
    pass

class MaxRetriesExceededError(Exception):
    pass

def execute_with_retry(func, max_retries, base_delay, max_delay):
    pass
