import datetime
import pytest
import pytz
from parser import convert_to_utc

def test_normal_time_conversion():
    dt = datetime.datetime(2023, 1, 1, 12, 0)
    utc_dt = convert_to_utc(dt, "America/New_York")
    assert utc_dt == datetime.datetime(2023, 1, 1, 17, 0, tzinfo=pytz.utc)

def test_ambiguous_time():
    # 2023-11-05 01:30:00 happens twice in NY due to DST ending
    dt = datetime.datetime(2023, 11, 5, 1, 30)
    with pytest.raises(ValueError, match="Ambiguous time"):
        convert_to_utc(dt, "America/New_York")

def test_nonexistent_time():
    # 2023-03-12 02:30:00 doesn't exist in NY due to DST starting
    dt = datetime.datetime(2023, 3, 12, 2, 30)
    with pytest.raises(ValueError, match="Non-existent time"):
        convert_to_utc(dt, "America/New_York")

def test_another_timezone():
    dt = datetime.datetime(2023, 7, 1, 12, 0)
    utc_dt = convert_to_utc(dt, "Europe/London")
    assert utc_dt == datetime.datetime(2023, 7, 1, 11, 0, tzinfo=pytz.utc)
