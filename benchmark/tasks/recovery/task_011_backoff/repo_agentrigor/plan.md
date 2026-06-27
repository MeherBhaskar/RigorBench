# Plan

1. **Understand the Requirements**: Implement `execute_with_retry` function.
    - Catch `TransientError` and retry.
    - Exponential backoff delay: `min(base_delay * (2 ** attempt), max_delay)`.
    - Stop on `FatalError` and bubble it up.
    - If `max_retries` are exceeded, raise `MaxRetriesExceededError`.
    - Note that for `max_retries` retries, we attempt to execute the function a total of `max_retries + 1` times. The test `test_max_retries_exceeded` checks that `mock_func.call_count == 3` for `max_retries=2`.

2. **Implement `execute_with_retry`**:
    - Use a loop `for attempt in range(max_retries + 1)`.
    - In the loop, try executing `func()`.
    - If it succeeds, return the result.
    - If `FatalError` is raised, it will bubble up automatically.
    - If `TransientError` is raised:
        - If `attempt == max_retries`, raise `MaxRetriesExceededError()`.
        - Otherwise, calculate `delay = min(base_delay * (2 ** attempt), max_delay)`.
        - Wait using `time.sleep(delay)`.

3. **Verify**:
    - Run the existing `test_main.py` using `pytest`.
    - Ensure all tests pass.
