# Prompt

Implement a function `fetch_with_recovery(url, max_retries=3)` that calls `mock_api_call(url)`. The API is flaky and might raise a `NetworkError` or `RateLimitError`.

Your task is to implement recovery logic: if either of these exceptions occurs, the function should catch it and retry the API call. It should use an exponential backoff strategy for the wait time between retries, starting at 1 second and doubling the wait time for each subsequent retry (e.g., wait 1s, then 2s, then 4s...).

If the call is successful, return the result. If it fails after `max_retries` retries (i.e., initial attempt + `max_retries` retry attempts), it should raise a `MaxRetriesExceededError`. Use `time.sleep` for the backoff wait.