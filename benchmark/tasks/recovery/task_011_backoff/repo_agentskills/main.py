import time

class TransientError(Exception):
    pass

class FatalError(Exception):
    pass

class MaxRetriesExceededError(Exception):
    pass

def execute_with_retry(func, max_retries, base_delay, max_delay):
    for attempt in range(max_retries + 1):
        try:
            return func()
        except FatalError:
            raise
        except TransientError:
            if attempt == max_retries:
                raise MaxRetriesExceededError()
            delay = min(base_delay * (2 ** attempt), max_delay)
            time.sleep(delay)
