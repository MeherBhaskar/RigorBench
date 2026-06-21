import pytest
import datetime
import pytz
from parser import convert_to_utc

def test_convert_valid():
    dt = datetime.datetime(2023, 1, 1, 12, 0)
    utc_dt = convert_to_utc(dt, "America/New_York")
    assert utc_dt == datetime.datetime(2023, 1, 1, 17, 0, tzinfo=pytz.utc)

def test_invalid_timezone():
    dt = datetime.datetime(2023, 1, 1, 12, 0)
    with pytest.raises(ValueError):
        convert_to_utc(dt, "Invalid/Timezone")

def test_ambiguous_time():
    dt = datetime.datetime(2023, 11, 5, 1, 30) # DST transition in NY
    with pytest.raises(ValueError):
        convert_to_utc(dt, "America/New_York")

def test_nonexistent_time():
    dt = datetime.datetime(2023, 3, 12, 2, 30) # Spring forward gap in NY
    with pytest.raises(ValueError):
        convert_to_utc(dt, "America/New_York")
