# Prompt

Implement a `fetch_with_recovery` function that takes a `fetch_data` callable, a `max_retries` integer (default 3), and a `base_delay` float (default 0.1).
The `fetch_data` callable might raise a `ConnectionError`.

Your function should attempt to call `fetch_data()`. If it raises a `ConnectionError`, it should recover by waiting for `base_delay * (2 ** attempt)` seconds (where attempt starts at 0 for the first retry, 1 for the second, etc.) and then try again.

If the call succeeds, it should return the result.
If it fails after `max_retries` retries (i.e., a total of `max_retries + 1` attempts), it should let the `ConnectionError` propagate.

Use the `time.sleep` function for waiting.