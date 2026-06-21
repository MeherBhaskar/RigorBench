# Prompt

Implement a function `execute_with_recovery` that takes a callable `action`, a `max_retries` integer (default 3), and a `base_delay` float (default 1.0).

The function should attempt to call `action()`. If `action()` raises a `TransientError`, it should catch it and wait `base_delay * (2 ** attempt)` seconds (where `attempt` starts at 0 for the first retry) before trying again.

If it succeeds, return the result.
If it exhausts all retries and still fails with a `TransientError`, it should re-raise the final `TransientError`.
If it raises a `FatalError`, it should NOT retry and should immediately re-raise the `FatalError`.
Wait should be implemented using `time.sleep`.