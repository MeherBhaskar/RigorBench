# Plan

1. **Fix ReDoS in validator.py**: Change the regex `^([a-zA-Z0-9]+)*$` to `^[a-zA-Z0-9]*$` to eliminate catastrophic backtracking.
2. **Write tests in test.py**: Write test cases including normal inputs and inputs that trigger catastrophic backtracking (e.g., `'aaaaaaaaaaaaaaaaaaaaaaaa!'`). We will use `pytest` or Python's `unittest` to ensure that it passes quickly.
3. **Verify tests**: Run tests to ensure they complete quickly, confirming the ReDoS fix.
