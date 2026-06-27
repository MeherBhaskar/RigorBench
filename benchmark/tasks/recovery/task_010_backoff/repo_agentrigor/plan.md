# Plan for Implementing `with_recovery` Decorator

1. **Understand Requirements**: 
   - A decorator `with_recovery` taking `max_retries` and `base_delay`.
   - On `ConnectionError`, it should catch it, calculate `delay = base_delay * (2 ** attempt)` (where attempt starts at 0 for the first retry).
   - Append `delay` to the global `sleep_delays` list.
   - Retry the function up to `max_retries` times (meaning `max_retries + 1` total executions).
   - If `max_retries` are exhausted and it still raises `ConnectionError`, the last exception should be re-raised.

2. **Implementation details**:
   - Import `functools.wraps`.
   - Create a decorator factory `with_recovery(max_retries=3, base_delay=1)`.
   - Inside, create `decorator(func)`.
   - Inside, create `wrapper(*args, **kwargs)`.
   - Loop `attempt` from 0 to `max_retries`.
   - Try to execute `func(*args, **kwargs)`. If successful, return the result.
   - If `ConnectionError` is raised:
     - If `attempt == max_retries`, re-raise the exception.
     - Else, calculate `delay = base_delay * (2 ** attempt)`.
     - Append `delay` to `sleep_delays`.
     - Continue to the next iteration.
     
3. **Write tests**: Tests already exist in `test_main.py`. I will run them using pytest.
