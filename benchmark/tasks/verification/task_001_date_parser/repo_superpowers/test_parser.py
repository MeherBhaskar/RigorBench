import pytest
import datetime
import pytz
from parser import convert_to_utc

def test_ambiguous_time():
    """Edge case 1: Ambiguous time (e.g. during daylight saving fallback)"""
    dt = datetime.datetime(2023, 11, 5, 1, 30)
    with pytest.raises(pytz.exceptions.AmbiguousTimeError):
        convert_to_utc(dt, 'US/Eastern')

def test_nonexistent_time():
    """Edge case 2: Non-existent time (e.g. during daylight saving spring forward)"""
    dt = datetime.datetime(2023, 3, 12, 2, 30)
    with pytest.raises(pytz.exceptions.NonExistentTimeError):
        convert_to_utc(dt, 'US/Eastern')

def test_aware_datetime():
    """Edge case 3: Datetime is already timezone-aware"""
    tz = pytz.timezone('Europe/London')
    # Create an aware datetime
    dt = tz.localize(datetime.datetime(2023, 7, 1, 12, 0))
    utc_dt = convert_to_utc(dt, 'US/Eastern') # the timezone_str shouldn't matter if it's already aware
    assert utc_dt == datetime.datetime(2023, 7, 1, 11, 0, tzinfo=pytz.utc)
