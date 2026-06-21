# Plan to Add Redis Caching

## 1. Setup and Dependencies
- Install the `redis` Python package.
- If necessary, install `pytest` and `fakeredis` for testing, though we can also just use `unittest.mock`.

## 2. Update `api.py`
- Import the `redis` module.
- Initialize a `Redis` client (e.g., pointing to `localhost:6379`). Allow injecting a mock client for tests, or just mock `redis.Redis`.
- Modify `get_data(user_id)` to first check the cache using a key like `user_data:{user_id}`.
- If data is in cache, return the cached data.
- If data is not in cache, perform the DB query (sleep 2 seconds), get the data, save it to the Redis cache, and then return it.
- Ensure the cached data is properly serialized/deserialized (e.g., using `json`).

## 3. Update `test.py`
- Write tests to verify the caching behavior.
- Test 1: Verify that a cache miss hits the "DB" (takes ~2 seconds) and populates the cache.
- Test 2: Verify that a cache hit returns the data quickly (skips the "DB" sleep).
- The tests should use `unittest.mock` to mock the `redis_client` or mock the `time.sleep` to assert that it is/isn't called, or simply mock the `redis` module completely. Mocking `redis` is probably safer since we don't know if a real Redis server is running.

## 4. Execution
- We will perform the changes atomically.
- Run tests to ensure everything works correctly.
