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
    retries = 0
    wait_time = 1
    while True:
        try:
            return mock_api_call(url)
        except (NetworkError, RateLimitError):
            if retries >= max_retries:
                raise MaxRetriesExceededError()
            time.sleep(wait_time)
            wait_time *= 2
            retries += 1
