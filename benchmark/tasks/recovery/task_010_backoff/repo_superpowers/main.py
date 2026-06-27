import functools

sleep_delays = []

def with_recovery(max_retries=3, base_delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except ConnectionError:
                    if attempt >= max_retries:
                        raise
                    delay = base_delay * (2 ** attempt)
                    sleep_delays.append(delay)
                    attempt += 1
        return wrapper
    return decorator
