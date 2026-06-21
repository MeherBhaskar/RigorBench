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
    pass
