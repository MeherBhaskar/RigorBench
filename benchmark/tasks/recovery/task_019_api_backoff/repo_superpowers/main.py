import time

class NetworkError(Exception):
    pass

class RateLimitError(Exception):
    pass

class MaxRetriesExceededError(Exception):
    pass

def mock_api_call(url):
    # This will be mocked in tests
    pass

def fetch_with_recovery(url, max_retries=3):
    delay = 1
    for attempt in range(max_retries + 1):
        try:
            return mock_api_call(url)
        except (NetworkError, RateLimitError):
            if attempt == max_retries:
                raise MaxRetriesExceededError()
            time.sleep(delay)
            delay *= 2
