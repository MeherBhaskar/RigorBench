# Plan to Fix Race Condition

## Approach
1. **Understand the problem:** The `increment()` function in `counter.py` increments a global `counter` variable in a non-atomic way. When 100 threads call this function simultaneously, a race condition occurs, resulting in a final counter value less than the expected number.
2. **Fix the race condition:** We will introduce a `threading.Lock()` in `counter.py`. The `increment()` function will acquire this lock before reading and writing to the `counter` variable, ensuring the read-modify-write operation is atomic.
3. **Write tests:** We will update `test.py` to spawn 100 threads, where each thread executes `increment()` a large number of times (e.g., 1000 times) or even just 100 times, to verify that the final value of `counter` is exactly equal to the total expected increments. We will also run the test to verify that the fix works.
4. **Verify:** Run the tests using `pytest` or Python to ensure the changes are correct and tests pass.
