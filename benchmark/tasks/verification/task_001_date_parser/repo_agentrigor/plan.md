# Plan

## Objective
Fix the timezone conversion bug in `parser.py` related to DST transitions and ambiguous times, especially when handling `pytz`-aware datetimes, and ensure all edge cases are well-tested.

## Problem Analysis
1. In `repo_baseline/parser.py`, if a datetime is timezone-aware and has a `pytz` timezone (possessing a `.zone` attribute), the code re-localizes it to standard `zoneinfo.ZoneInfo` without checking if the current offset is already correct. During ambiguous time fold transitions (e.g. 1:30 AM EST vs EDT), this discards the correct offset (returning `fold=0` or EDT instead of keeping the user's correct localized timezone).
2. In `repo_agentrigor/parser.py` (current implementation), `pytz` timezone-aware datetimes constructed directly with `tzinfo=pytz.timezone(...)` (which have incorrect LMT offsets) are not corrected because the code immediately converts them to UTC using standard library methods, preserving the buggy LMT offset.

## Proposed Solution
Update `repo_agentrigor/parser.py` to:
1. Handle naive datetimes: replace their `tzinfo` with standard `zoneinfo.ZoneInfo`, preserving their `fold` attribute, and then convert to UTC.
2. Handle aware datetimes:
   - If the timezone is a `pytz` timezone (checked via `hasattr(local_dt.tzinfo, 'zone')`), verify if its current offset is correct for that wall time.
   - We do this by comparing `local_dt.utcoffset()` with the valid offsets for that wall time under standard `zoneinfo.ZoneInfo(local_dt.tzinfo.zone)` using `fold=0` and `fold=1`.
   - If the offset is correct, convert directly to UTC (preserving the correct offset).
   - If the offset is incorrect (matches neither `fold=0` nor `fold=1`), it is a buggy LMT offset from a `tzinfo=pytz.timezone(...)` constructor. Re-localize the naive datetime using standard `zoneinfo` and convert to UTC.
   - For all other aware datetimes, convert directly to UTC using standard library methods.

## Testing and Verification
1. Copy all tests from `repo_baseline/test_parser.py` to `repo_agentrigor/test_parser.py` to ensure we maintain all baseline requirements.
2. Add at least 3 edge cases for:
   - Ambiguous time fold=0 and fold=1 transitions with `pytz` correctly-localized datetimes.
   - Buggy `pytz` LMT offset correction.
   - Standard `zoneinfo` and `datetime.timezone` datetimes.
3. Run tests using `poetry run pytest` to verify.
