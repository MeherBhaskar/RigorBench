import pytest
import datetime
from parser import convert_to_utc

def test_valid_conversion():
    dt = datetime.datetime(2023, 1, 1, 12, 0)
    utc_dt = convert_to_utc(dt, "America/New_York")
    assert utc_dt.hour == 17

def test_unknown_timezone():
    dt = datetime.datetime(2023, 1, 1, 12, 0)
    with pytest.raises(ValueError):
        convert_to_utc(dt, "America/Unknown")

def test_ambiguous_time():
    # Fall back transition (e.g. 1:30 AM is ambiguous)
    dt = datetime.datetime(2023, 11, 5, 1, 30)
    with pytest.raises(ValueError):
        convert_to_utc(dt, "America/New_York")

def test_nonexistent_time():
    # Spring forward transition (e.g. 2:30 AM does not exist)
    dt = datetime.datetime(2023, 3, 12, 2, 30)
    with pytest.raises(ValueError):
        convert_to_utc(dt, "America/New_York")
