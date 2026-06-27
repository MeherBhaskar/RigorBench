import time

def fetch_with_recovery(fetch_data, max_retries=3, base_delay=0.1):
    for attempt in range(max_retries + 1):
        try:
            return fetch_data()
        except ConnectionError:
            if attempt == max_retries:
                raise
            time.sleep(base_delay * (2 ** attempt))
