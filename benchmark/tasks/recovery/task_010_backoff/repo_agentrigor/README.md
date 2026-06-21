# Prompt

Implement a decorator `with_recovery(max_retries=3, base_delay=1)` that retries a function if it raises a `ConnectionError`.
The delay between retries should follow exponential backoff: `delay = base_delay * (2 ** attempt)`, where `attempt` starts at 0 for the first retry.
If the function fails after `max_retries` retries (i.e., executed `max_retries + 1` times total), it should re-raise the last `ConnectionError`.
For testing purposes, do not actually `time.sleep()`. Instead, append the delay values to a global list called `sleep_delays` and continue immediately.