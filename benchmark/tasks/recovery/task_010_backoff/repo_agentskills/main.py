import functools

sleep_delays = []

def with_recovery(max_retries=3, base_delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except ConnectionError as e:
                    if attempt == max_retries:
                        raise e
                    delay = base_delay * (2 ** attempt)
                    sleep_delays.append(delay)
        return wrapper
    return decorator
