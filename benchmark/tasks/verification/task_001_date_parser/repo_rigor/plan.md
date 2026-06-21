# Plan
1.  **Analyze the Bug**: The current implementation of `convert_to_utc` uses `pytz` and calls `tz.localize(local_dt)`. While this is better than `local_dt.replace(tzinfo=tz)`, it does not handle ambiguous times (during DST fallback) or non-existent times (during DST spring forward) cleanly if `is_dst` is not specified, or it fails if `local_dt` is already timezone-aware. Another possibility is that we should just use Python 3.9+ `zoneinfo` instead of `pytz`, which behaves properly with `replace(tzinfo=...)`.
2.  **Write Tests**: Write tests for edge cases:
    *   Spring forward (non-existent time): standard behavior is to raise or handle.
    *   Fall back (ambiguous time): standard behavior is to raise or handle.
    *   Already timezone-aware datetime: it should gracefully convert without raising a `ValueError`.
3.  **Fix Code**: Update `convert_to_utc` to correctly handle the conversion. I will test using `zoneinfo` or proper `pytz` usage.
4.  **Verify**: Run the tests using `pytest` to verify the bug is fixed and edge cases pass.
