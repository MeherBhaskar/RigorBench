# Plan to Fix Date Parsing Error Handling

1.  **Analyze the Issue**:
    The `parser.py` file contains a function `convert_to_utc(local_dt, timezone_str)` which uses `tz.localize(local_dt)`. This naive approach does not properly handle ambiguous or non-existent times during Daylight Saving Time (DST) transitions.
    
2.  **Fix `parser.py`**:
    Update the `tz.localize(local_dt)` call to `tz.localize(local_dt, is_dst=None)`.
    Wrap it in a `try...except` block to catch `pytz.AmbiguousTimeError` and `pytz.NonExistentTimeError`.
    Raise a standard `ValueError` with a descriptive message when these parsing errors occur. This addresses the "date parsing error handling" requirement.

3.  **Write Tests**:
    Create a `test_parser.py` file to verify the behavior:
    - Normal conversion (no DST transition).
    - Ambiguous time (e.g., fallback transition where 1:30 AM happens twice).
    - Non-existent time (e.g., spring forward transition where 2:30 AM is skipped).

4.  **Verify Tests**:
    Run `pytest test_parser.py` to ensure all tests pass and the error handling works as intended.
