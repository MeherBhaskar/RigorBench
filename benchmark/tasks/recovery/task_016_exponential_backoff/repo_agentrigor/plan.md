# Plan for Implementing Exponential Backoff

1. **Analyze Requirements:**
   - Implement `execute_with_recovery(action, max_retries=3, base_delay=1.0)`.
   - Action is a callable.
   - If `action()` raises `TransientError`, wait `base_delay * (2 ** attempt)` seconds (attempt starts at 0).
   - If it succeeds, return the result.
   - If all retries exhausted, re-raise final `TransientError`.
   - If `action()` raises `FatalError`, do not retry, re-raise immediately.
   - Wait using `time.sleep`.

2. **Examine Existing Code:**
   - Look at `main.py` and `test_main.py` for pre-defined classes (e.g., `TransientError`, `FatalError`).

3. **Implementation Details:**
   - Iterate from `attempt = 0` to `max_retries`. (So, total `max_retries + 1` executions: 1 initial + `max_retries` retries).
   - In a try block, execute `action()`.
   - If successful, return the result.
   - Catch `TransientError`. If `attempt < max_retries`, do `time.sleep(base_delay * (2 ** attempt))`.
   - If `attempt == max_retries`, we are out of retries, so `raise` the `TransientError`.
   - `FatalError` is not caught, so it will naturally propagate.

4. **Testing:**
   - Run the provided tests (`pytest test_main.py`).

5. **Atomic Transitions:**
   - Apply the changes to `main.py` in one go.
