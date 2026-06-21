import datetime
import pytest
import pytz
from parser import convert_to_utc

def test_normal_time():
    # Normal time
    dt = datetime.datetime(2020, 1, 1, 12, 0)
    utc_dt = convert_to_utc(dt, "US/Eastern")
    assert utc_dt == datetime.datetime(2020, 1, 1, 17, 0, tzinfo=pytz.utc)

def test_ambiguous_time():
    # Fall back
    dt = datetime.datetime(2020, 11, 1, 1, 30)
    with pytest.raises(pytz.exceptions.AmbiguousTimeError):
        convert_to_utc(dt, "US/Eastern")

def test_nonexistent_time():
    # Spring forward
    dt = datetime.datetime(2020, 3, 8, 2, 30)
    with pytest.raises(pytz.exceptions.NonExistentTimeError):
        convert_to_utc(dt, "US/Eastern")
