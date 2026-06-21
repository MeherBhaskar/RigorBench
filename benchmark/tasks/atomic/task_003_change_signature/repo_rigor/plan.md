# Plan to update `log` signature

1. **Update Signature**: In `logger.py`, modify `def log(msg):` to `def log(msg, level):` to add a required argument.
2. **Fix Usages**: 
   - In `app.py`, update `log('started')` to `log('started', 'INFO')`.
   - In `worker.py`, update `log('working')` to `log('working', 'INFO')`.
3. **Write Tests**: In `test.py`, add a test that calls `log` with both arguments and ensure it doesn't throw an error.
4. **Verify**: Run `pytest test.py` or `python test.py` to ensure the tests pass and no issues remain.
