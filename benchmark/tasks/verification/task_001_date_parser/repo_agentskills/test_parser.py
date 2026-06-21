import pytest
import datetime
from parser import convert_to_utc

def test_ambiguous_time_fold_0():
    """
    Edge case 1: Ambiguous time (Fall back) - First occurrence.
    In America/New_York, 2023-11-05 02:00:00 falls back to 01:00:00.
    Thus, 01:30:00 happens twice. fold=0 represents the first occurrence (EDT, UTC-4).
    """
    dt = datetime.datetime(2023, 11, 5, 1, 30, 0, fold=0)
    utc_dt = convert_to_utc(dt, 'America/New_York')
    assert utc_dt == datetime.datetime(2023, 11, 5, 5, 30, 0, tzinfo=datetime.timezone.utc)

def test_ambiguous_time_fold_1():
    """
    Edge case 2: Ambiguous time (Fall back) - Second occurrence.
    fold=1 represents the second occurrence (EST, UTC-5).
    """
    dt = datetime.datetime(2023, 11, 5, 1, 30, 0, fold=1)
    utc_dt = convert_to_utc(dt, 'America/New_York')
    assert utc_dt == datetime.datetime(2023, 11, 5, 6, 30, 0, tzinfo=datetime.timezone.utc)

def test_nonexistent_time():
    """
    Edge case 3: Non-existent time (Spring forward gap).
    In America/New_York, 2023-03-12 02:00:00 springs forward to 03:00:00.
    Thus, 02:30:00 does not exist. zoneinfo resolves this by returning 07:30 UTC
    (effectively applying the EST UTC-5 offset).
    """
    dt = datetime.datetime(2023, 3, 12, 2, 30, 0)
    utc_dt = convert_to_utc(dt, 'America/New_York')
    assert utc_dt == datetime.datetime(2023, 3, 12, 7, 30, 0, tzinfo=datetime.timezone.utc)

def test_already_aware_datetime():
    """
    Edge case 4: The input datetime is already timezone-aware.
    It should correctly resolve to UTC without crashing.
    """
    from zoneinfo import ZoneInfo
    tz_la = ZoneInfo('America/Los_Angeles')
    dt_aware = datetime.datetime(2023, 1, 1, 12, 0, 0, tzinfo=tz_la) # 12 PM PT = 20:00 UTC
    utc_dt = convert_to_utc(dt_aware, 'America/New_York') # Target timezone string might just be ignored or convert cleanly
    assert utc_dt == datetime.datetime(2023, 1, 1, 20, 0, 0, tzinfo=datetime.timezone.utc)
