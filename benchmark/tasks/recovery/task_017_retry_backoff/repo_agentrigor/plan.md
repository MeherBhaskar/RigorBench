# Plan for `fetch_with_recovery`

1.  **Understand the Goal**: Implement a function `fetch_with_recovery` that attempts to call a function `fetch_data`. If it raises a `ConnectionError`, it waits and retries using exponential backoff: `base_delay * (2 ** attempt)`.
2.  **Algorithm**:
    *   Loop `attempt` from 0 to `max_retries` inclusive (so `max_retries + 1` iterations).
    *   Inside the loop, `try` to execute `return fetch_data()`.
    *   `except ConnectionError`:
        *   If `attempt == max_retries`, `raise` the exception to let it propagate.
        *   Otherwise, wait for `base_delay * (2 ** attempt)` seconds using `time.sleep()`.
3.  **Implementation**:
    *   Update `main.py` with the loop logic.
4.  **Testing**:
    *   Run `pytest test_main.py` to verify the logic against the existing test suite.
    *   The tests verify success on the first try, success after retries (with correct sleep durations), and failure after max retries.
