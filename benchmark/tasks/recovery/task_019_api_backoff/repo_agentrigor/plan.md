# Plan to implement fetch_with_recovery

1.  **Function Signature**: `def fetch_with_recovery(url, max_retries=3):`
2.  **State Initialization**:
    *   Initialize `wait_time = 1`.
3.  **Loop**: Use a `for attempt in range(max_retries + 1):` loop.
4.  **Try Block**:
    *   Call `mock_api_call(url)`.
    *   If successful, return the result.
5.  **Except Block**: Catch `NetworkError` and `RateLimitError`.
    *   If caught, check if `attempt == max_retries`.
    *   If yes, `raise MaxRetriesExceededError()`.
    *   Otherwise, sleep for `wait_time` (`time.sleep(wait_time)`).
    *   Update `wait_time *= 2`.
6.  **Implementation**: Replace the body of `fetch_with_recovery` in `main.py` with this logic.
7.  **Testing**: Run `pytest test_main.py` to ensure all tests pass.
