import pytest
import datetime
import pytz
from parser import convert_to_utc

def test_ambiguous_time_raises_error():
    # US/Eastern fall back (ambiguous time)
    dt = datetime.datetime(2024, 11, 3, 1, 30, 0)
    with pytest.raises(pytz.exceptions.AmbiguousTimeError):
        convert_to_utc(dt, 'US/Eastern')

def test_non_existent_time_raises_error():
    # US/Eastern spring forward (non-existent time)
    dt = datetime.datetime(2024, 3, 10, 2, 30, 0)
    with pytest.raises(pytz.exceptions.NonExistentTimeError):
        convert_to_utc(dt, 'US/Eastern')

def test_already_aware_datetime():
    # If already aware, it should convert properly without localizing
    # Let's say it's an aware datetime in UTC
    dt = datetime.datetime(2024, 1, 1, 12, 0, 0, tzinfo=pytz.utc)
    # converting to UTC should give the same time
    result = convert_to_utc(dt, 'US/Eastern')
    assert result == dt
