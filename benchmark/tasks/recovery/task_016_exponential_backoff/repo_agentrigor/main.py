import time

class TransientError(Exception):
    pass

class FatalError(Exception):
    pass

def execute_with_recovery(action, max_retries=3, base_delay=1.0):
    for attempt in range(max_retries + 1):
        try:
            return action()
        except TransientError:
            if attempt == max_retries:
                raise
            time.sleep(base_delay * (2 ** attempt))
